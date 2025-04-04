import os
import shutil
import uuid

from endurosat_api import api_client
from endurosat_api.api.authentication_api import AuthenticationApi
from endurosat_api.api.ground_stations_api import GroundStationsApi
from endurosat_api.api.payload_slots_api import PayloadSlotsApi
from endurosat_api.api.satellite_pass_predictions_api import SatellitePassPredictionsApi
from endurosat_api.api.satellite_subsystems_api import SatelliteSubsystemsApi
from endurosat_api.api.satellite_telemetry_api import SatelliteTelemetryApi
from endurosat_api.api.satellite_telecommands_api import SatelliteTelecommandsApi
from endurosat_api.api.mission_databases_api import MissionDatabasesApi
from endurosat_api.api.satellite_passes_api import SatellitePassesApi
from endurosat_api.api.payload_files_api import PayloadFilesApi
from endurosat_api.api.satellites_api import SatellitesApi
from endurosat_api.api.user_data_api import UserDataApi
from endurosat_api.models.telecommand import Telecommand
from endurosat_api.models.telemetry_entry import TelemetryEntry
from endurosat_api.models.satellite_pass import SatellitePass
from endurosat_api.models.telecommand_ground_execution_rules import (
    TelecommandGroundExecutionRules,
)
from endurosat_api.models.execution_rule import ExecutionRule

from cfg.access_cfg import API_CLIENT_ID, API_PASSWORD, API_USERNAME
from cfg.gen_cfg import GEN_LINE
from cfg.defaults_cfg import FAKE_PASS_ID, SAT_ID, SUFFIX

import sys
import csv
import json

import sys
import argparse
import textwrap
import subprocess

from datetime import datetime
import time
import logging

DEFAULT_PASS_DURATION = 15
DEAFULT_PRIORITY = 699


class API:
    def __init__(self, api_client_id, api_user_name, api_password):
        self.auth_api = AuthenticationApi()
        auth_response = self.auth_api.authenticate(
            client_id=api_client_id,
            grant_type="password",
            username=api_user_name,
            password=api_password,
        )
        if auth_response is None:
            raise Exception("Authentication failed")
        self.api_client = api_client.ApiClient()
        self.api_client.configuration.access_token = auth_response.access_token
        self.tlmApi = SatelliteTelemetryApi(self.api_client)
        self.tcApi = SatelliteTelecommandsApi(self.api_client)
        self.passApi = SatellitePassesApi(self.api_client)
        self.satApi = SatellitesApi(self.api_client)

    def clr_cmds(self, sat_id):
        logging.info(f"Deleting commands for satellite {sat_id}")
        answer = input("Are you sure? [y/yes]: ")
        if answer.lower() not in ["y", "yes"]:
            logging.warn("Command cancelled!")
            return
        allTelecommands = self.tcApi.get_filtered_telecommands(
            satellite_id=sat_id, page_size_limit=1000, status="SCHEDULED"
        )
        logging.info("DELETING {} COMMANDS: ".format(len(allTelecommands.items)))
        for tc in allTelecommands.items:
            print(tc.id)
            self.tcApi.delete_telecommand_by_id(tc.id)
        logging.info("DONE")

    def create_fake_pass(self, pass_id, pass_duration):
        if pass_id is None:
            logging.warning("Provide pass_id")
            return
        try:
            sat_pass: SatellitePass = self.passApi.get_satellite_pass_by_id(pass_id)
        except Exception as e:
            print(e)
            raise Exception("Could not find the pass with ID " + pass_id)

        # In milliseconds
        sat_pass.aos = int(
            (time.mktime(datetime.now().timetuple()) * 1000) + (30 * 1000)
        )
        pass_duration_ms = pass_duration * 60 * 1000

        sat_pass.los = sat_pass.aos + pass_duration_ms
        sat_pass.status = "SCHEDULED"
        self.passApi.update_satellite_pass_by_id(sat_pass.id, sat_pass)
        logging.info(
            "Faked pass {} from {} to {} for satellite {}".format(
                pass_id,
                datetime.fromtimestamp(sat_pass.aos / 1e3).strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                datetime.fromtimestamp(sat_pass.los / 1e3).strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                sat_pass.satellite,
            )
        )

    def create_command(
        self,
        name: str,
        priority: int,
        sat_id: str,
        mdb: str,
        subsystem: str,
        data: json = None,
        payload_file_path: str = None,
        maxRetry=1,
        requested_pass=None,
    ):
        tc = Telecommand(
            name=name,
            satellite=sat_id,
            mission_database=mdb,
            priority=priority,
            satellite_subsystem=subsystem,
            status="SCHEDULED",
            has_payload_file=True if payload_file_path else False,
            expect_telemetry_response=True,
            max_tries=maxRetry,
            continue_on_fail=True,
            data=data,
        )
        if requested_pass is not None:
            tc.requested_satellite_pass = requested_pass
        else:
            execution_rule = ExecutionRule(execution_rule_type="FIRST_OPPORTUNITY")
            rule = TelecommandGroundExecutionRules(rules=[execution_rule])
            tc.execution_rules = rule
        if payload_file_path is None:
            return self.tcApi.create_telecommand(tc)
        file_to_upl_path = payload_file_path
        # script folder
        if os.path.isdir(payload_file_path):
            script_bundle_dir = "temp_files/script_bundle"
            if os.path.exists(script_bundle_dir):
                shutil.rmtree(script_bundle_dir)
            os.mkdir(script_bundle_dir)
            shutil.copyfile("operations.py", script_bundle_dir + "/operations.py")
            shutil.copytree(payload_file_path, script_bundle_dir + "/script")
            shutil.make_archive("temp_files/payload", "zip", script_bundle_dir)
            file_to_upl_path = "temp_files/payload.zip"

        serialized_tc = json.dumps(self.tcApi.api_client.sanitize_for_serialization(tc))
        return self.tcApi.create_telecommand_with_payload(
            file_to_upl_path, serialized_tc
        )

    def check_cmd_result(self, id):
        """
        input:
            id - command id

        return: dict of type {'status': String, 'data': dict}
        """
        tc = self.tcApi.get_telecommand_by_id(id)
        status = False
        telemetry = None
        if tc.status == "SUCCESSFUL" or tc.status == "FAILED":
            if tc.telemetry_response is not None:
                telemetry = self.tlmApi.get_telemetry_entry_by_id(
                    telemetry_entry_id=tc.telemetry_response
                )
                if telemetry.data is not None:
                    status = True
        return {"status": status, "data": telemetry.data if status is True else {}}


class TEST:
    def __init__(self, fname=None):
        self.csv = fname

    def open_csv_file(self):
        if self.csv is None:
            raise Exception("No file provided to class method")
        return open(self.csv, newline="")

    def close_csv_file(self, fHandle):
        fHandle.close()

    def execute_test(
        self,
        api_inst: API,
        sat_id,
        suffix,
        priority,
        requested_pass_id=None,
        add_delay=False,
    ):
        handle = self.open_csv_file()
        csv_handle = csv.reader(handle, delimiter=";")
        commands_dict = {}
        if requested_pass_id is not None:
            requested_pass: SatellitePass = api_inst.passApi.get_satellite_pass_by_id(
                requested_pass_id
            )
            if requested_pass is None:
                raise Exception("Could not find pass with id " + requested_pass_id)
            if requested_pass.status == "IN_PROGRESS":
                add_delay = True
                logging.info(
                    f"Found pass ongoing {requested_pass.aos}, so adding a delay between commands"
                )
        for row in csv_handle:
            row = self.append_csv_entry(row, suffix)
            logging.info(
                "Creating command for satellite: {}{} with name: {} and priority {}".format(
                    sat_id, suffix, row[0], priority
                )
            )
            command_id = api_inst.create_command(
                name=row[0],
                priority=priority,
                sat_id=sat_id + suffix,
                mdb=row[1],
                subsystem=row[2],
                data=json.loads(row[3]) if row[3] else None,
                payload_file_path=row[4] if row[4] else None,
                maxRetry=row[5],
                requested_pass=requested_pass_id,
            )
            logging.info(
                "--------------------------------------------------------------------"
            )
            logging.info("Created command with id: {}".format(command_id))
            commands_dict[command_id] = row[0]
            priority -= 10
            if add_delay:
                logging.info(
                    "Live pass, sleeping for 4s to allow for rawData to be filled in..."
                )
                time.sleep(4)
        self.close_csv_file(handle)
        return commands_dict

    def append_csv_entry(self, csv_row, suffix):
        if csv_row[1] is not None and len(csv_row[1]) > 0:
            csv_row[1] += suffix
        if csv_row[2] is not None and len(csv_row[2]) > 0:
            csv_row[2] += suffix
        return csv_row


def gen_api():
    try:
        # Execute the command and wait for the subprocess to terminate
        # STDERR is redirected to STDOUT
        phandle = subprocess.Popen(
            GEN_LINE, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        # Read the stdout/sterr buffers and retcode
        output, _ = phandle.communicate(timeout=60)
        retcode = phandle.poll()
    except subprocess.TimeoutExpired:
        # Kill the running process
        if phandle is not None:
            phandle.kill()
        raise Exception(f"Timeout {60}s expired: {GEN_LINE}")
    except Exception as e:
        print(e)
        raise Exception(f"Could not execute command: {GEN_LINE}")

    if retcode:
        print("Returned exit code {}: {}\n".format(retcode, GEN_LINE))
    else:
        print("Executed successfully: {}\n".format(GEN_LINE))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """\
           Mission operations utility
++++++++++++++++++++++++++++++++++++++++++++++
                          _________________
                         /      /  /      /
                        /______/__/______/
                              |   | |
                              | + | |
                              |___|/



            \-/
          ___|______
         /___|_____/|
         |▀▀▀▀▀▀▀▀▀||
         | ▀  ▀  ▀ ||
         |▄▄▄▄▄▄▄▄▄|/
++++++++++++++++++++++++++++++++++++++++++++++
The main purpose of this utility program is to facilitate the commissioning procedure. It makes use of CSV files that
describe the commands as per the DGS expectations. Commands are uploaded to the DGS for execution at FIRST_OPPORTUNITY or
        at a given pass if specified with the -rp flag.

Other functionalities:
    1. The utility can generated the latest version of the DGS client
    2. The utility can generate a fake pass

Configuration:
    1. gen_cfg.py - holds the DGS client generation line
    2. access_cfg.py - it contains the credentials for the access
    2. defaults.py - it contains the default sat ID, suffix and fake pass ID

CSV file format:
    1. Column 0 - Command name as per the fidl description
    2. Column 1 - FIDL name as uploaded for the current platform
    3. Column 2 - Subsystem name in the mission database
    4. Column 3 - Parameters field as a JSON
    5. Column 4 - Payload file path on local machine. If path is a folder, the folder will be zipped
    6. Column 5 - Retry count
"""
        ),
    )
    parser.add_argument(
        "-g",
        "--gen",
        action="store_true",
        help="Generate the latest version of the DGS client",
    )
    parser.add_argument(
        "-fp",
        "--fake-pass",
        nargs="?",
        const=FAKE_PASS_ID,
        help="Call the fake pass utility. If a value is provided, it will be used as the ID of the pass to fake. If not provided, the ID from the defaults_cfg files will be used.",
    )
    parser.add_argument(
        "-pd",
        "--pass-duration",
        type=int,
        default=DEFAULT_PASS_DURATION,
        help="Duration of the fake pass in minutes. Defaults to "
        + str(DEFAULT_PASS_DURATION),
    )
    parser.add_argument(
        "-sat",
        "--sat",
        help="ID of the context satellite. If not provided, the default ID from the defaults_cfg files will be used.",
    )
    parser.add_argument(
        "-suff",
        "--suff",
        help="Suffix of the context satellite. If not provided, the default suffix from the defaults_cfg files will be used.",
    )
    parser.add_argument(
        "-prio",
        "--priority",
        default=DEAFULT_PRIORITY,
        type=int,
        help="Priority of the first command in the schedule sequence. Defaults to "
        + str(DEAFULT_PRIORITY),
    )
    parser.add_argument(
        "-d",
        "--delete",
        action="store_true",
        help="Delete all commands for the configured satellite",
    )
    parser.add_argument(
        "-s", "--schedule", help="Schedules the commands in the specified CSV file"
    )
    parser.add_argument(
        "-rp",
        "--requested-pass",
        help="Requested pass ID. Commands will be assigned for execution on this pass instead of using FIRST_OPPORTUNITY rule",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Request verbose output"
    )
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    api_inst = API(
        api_client_id=API_CLIENT_ID,
        api_user_name=API_USERNAME,
        api_password=API_PASSWORD,
    )
    # Configure logger
    rootLogger = logging.getLogger()
    fh = logging.FileHandler("mo_util.log", mode="w")
    lf = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
    fh.setFormatter(lf)
    ch = logging.StreamHandler()
    ch.setFormatter(lf)
    if args.verbose:
        fh.setLevel(logging.DEBUG)
        ch.setLevel(logging.DEBUG)
        rootLogger.setLevel(logging.DEBUG)
    else:
        fh.setLevel(logging.INFO)
        ch.setLevel(logging.INFO)
        rootLogger.setLevel(logging.INFO)
    rootLogger.addHandler(fh)
    rootLogger.addHandler(ch)
    logging.info(f"Starting utility with arguments: {args}")

    sat_id = SAT_ID
    suffix = SUFFIX

    if args.sat:
        sat_id = args.sat
    if args.suff is not None:
        suffix = args.suff

    if args.delete:
        api_inst.clr_cmds(sat_id + suffix)
    if args.gen:
        gen_api()
    if args.fake_pass:
        api_inst.create_fake_pass(args.fake_pass, args.pass_duration)
    if args.schedule:
        test_inst = TEST(args.schedule)
        test_inst.execute_test(
            api_inst, sat_id, suffix, args.priority, args.requested_pass
        )
    exit(0)
