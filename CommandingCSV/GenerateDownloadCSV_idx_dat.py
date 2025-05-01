import os
import csv
import subprocess
import math
from datetime import datetime, timedelta

# -----------------------------------------------------------------------------
# User Input:
#   DateTimePull    - Central time (format "YYMMDDHHMM")
#   DurationMinutes - Window (in minutes) around DateTimePull to include files.
# -----------------------------------------------------------------------------
DateTimePull = "250423233"  # e.g. "YYMMDDHHMM" (change as needed)
DurationMinutes = 60*200    # ± minutes window (adjust as needed)

# Convert the input string to a datetime object.
try:
    dt_pull = datetime.strptime(DateTimePull, "%y%m%d%H%M")
except ValueError:
    raise ValueError("DateTimePull must be in the format YYMMDDHHMM")

# ----------------------------
# Read in DirList.txt (assumed to be in the same directory as the script)
# ----------------------------
with open("DirList.txt", "r") as file:
    # Read all lines and skip the header
    lines = file.readlines()[1:]

# This list will store tuples: (original_filename (upper-case), file_dt)
matching_entries = []

# -----------------------------------------------------------------------------
# Process each line from DirList.txt, filter for files starting with
# "padreMD" or "padreSP" and ending with ".idx", and matching the time window.
# -----------------------------------------------------------------------------
for line in lines:
    line = line.strip()
    if not line:
        continue

    # First column is the file path (e.g., "/sd/padreMDA0_250401212029.idx")
    parts = line.split(",")
    file_path = parts[0]
    file_size = int(parts[1])  # Not used in this script, but can be useful for debugging
    # Get the base file name (e.g., "padreMDA0_250401212029.idx")
    base_name = os.path.basename(file_path)
    lower_name = base_name.lower()

    # Check: filename starts with "padreMD" or "padreSP" AND if file size is >= 500"
    # if (lower_name.startswith("padremd") or lower_name.startswith("padresp")) and file_size >= 500:
    # if (lower_name.startswith("padremd")) and file_size >= 500:
    if (lower_name.startswith("padresp")) and file_size >= 500:
    # if (lower_name.startswith("padremd") or lower_name.startswith("padresp")):
        # Expected filename format: padre####_YYMMDDHHMMSS.idx
        underscore_index = base_name.find("_")
        dot_index = base_name.find(".", underscore_index)
        fileType = base_name[dot_index+1:]
        if underscore_index != -1 and dot_index != -1:
            # Extract the timestamp portion (between '_' and '.')
            time_str = base_name[underscore_index + 1:dot_index]
            # Ensure we have enough characters (at least for YYMMDDHHMM)
            if len(time_str) >= 10:
                try:
                    # Parse the file's timestamp (expects full seconds, i.e. YYMMDDHHMMSS)
                    file_dt = datetime.strptime(time_str, "%y%m%d%H%M%S")
                except ValueError:
                    continue  # Skip files that do not have the expected time string format

                # Check if the file's timestamp is within ±DurationMinutes of the input time.
                if abs(file_dt - dt_pull) <= timedelta(minutes=DurationMinutes) and '_' not in fileType :
                # if abs(file_dt - dt_pull) <= timedelta(minutes=DurationMinutes):
                    # Store the upper-case version of the base file name and its datetime.
                    matching_entries.append((base_name.upper(), file_dt, fileType, file_size))

# -----------------------------------------------------------------------------
# Assign new file names sequentially: file-0, file-1, ...
# Build a list of dictionaries with keys: "old", "new", "timestamp"
# -----------------------------------------------------------------------------
file_mappings = []
for i, (orig_name, file_dt, fileType, file_size) in enumerate(matching_entries):
    new_name = f"file{i}.{fileType}"
    file_mappings.append({"old": orig_name, "new": new_name, "timestamp": file_dt, "filesize": file_size})

# -----------------------------------------------------------------------------
# Step 1: Write the lookup CSV with original and new file names plus timestamp.
# The file is named "FilenameDirectory_[entered date]_Gen_[currentDateTime].csv"
# -----------------------------------------------------------------------------
gen_time_str = datetime.now().strftime("%Y%m%d_%H%M%S")
lookup_csv_filename = f"FilenameDirectory_{DateTimePull}_Gen_{gen_time_str}.csv"

with open(lookup_csv_filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";", lineterminator="\n")
    # Optionally, you may include a header row:
    # writer.writerow(["Old Filename", "New Filename", "Extracted Timestamp"])
    for mapping in file_mappings:
        # Format timestamp in a readable format (e.g., "YYYY-MM-DD HH:MM:SS")
        ts_formatted = mapping["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([mapping["old"], mapping["new"], ts_formatted, mapping["filesize"]])

# -----------------------------------------------------------------------------
# Step 2: Write the rename_files.csv.
# Each row is as follows:
# Rename;padre-padre-filemanager-fidl;padre-obc;{"oldPath": "[OG filename]", "newFileName": "[new file name]"};;100;
# -----------------------------------------------------------------------------
with open("rename_files.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";", lineterminator="\n")
    for mapping in file_mappings:
        row = ["Rename", 
               "padre-padre-filemanager-fidl", 
               "padre-obc", 
               f'{{"oldPath": "{mapping['old']}", "newPath": "{mapping['new']}"}}', 
               "", 
               "100", 
               ""]
        writer.writerow(row)

    # # Now add an extra row for "schedule_03.bin":
    # schedule_bin = "schedule_03.bin"
    # json_part = (f'{{"oldPath": "UP_00225.upl", "newPath": "{schedule_bin}"}}')
    # row = ["Rename", 
    #            "padre-padre-filemanager-fidl", 
    #            "padre-obc", 
    #            json_part, 
    #            "", 
    #            "100", 
    #            ""]
    # writer.writerow(row)

# -----------------------------------------------------------------------------
# Step 3: Write the obc_download_Sci_Files_.csv using the new file names.
# Each row is as follows:
# Download [new file name];padre-file-manager-commands;padre-obc;
# {"type": "obcDownload", "fileName": "[new file name]", "offset": 0,"volId":0};;150;
# -----------------------------------------------------------------------------
with open("obc_download_Sci_Files.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";", lineterminator="\n")
    for mapping in file_mappings:
        fileNAME = mapping["new"]
        json_part = f'{{"type": "obcDownload", "fileName": "{fileNAME}", "offset": 0,"volId":0}}'
        row = [f"Download {mapping['new']}", 
               "padre-file-manager-commands", 
               "padre-obc", 
               json_part, 
               "", 
               "150",
                 ""]
        writer.writerow(row)

# -----------------------------------------------------------------------------
# Helper function to convert a string to its decimal ASCII values and append a trailing 0.
# Returns a list of string representations of the decimals.
# -----------------------------------------------------------------------------
def convert_string_to_decimal_list(s):
    dec_list = [str(ord(ch)) for ch in s]  # Convert each character to its ASCII code as string.
    dec_list.append("0")
    return dec_list

# -----------------------------------------------------------------------------
# Step 4: Write the fileUpload.csv.
# For each new file mapping, create a row like:
# SXBand_GwSendCmd;padre-padre-filemanager-fidl;padre-obc;
# {"Identifier": "8217", "Cmd": {"value": 96}, "Type": {"value": 87}, 
#  "Data": [<decimal list>], "DataLen": "<length>"};;100;
# Then add an extra row to upload "schedule_03.bin" in a similar format.
# -----------------------------------------------------------------------------
with open("schedule_04.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    # # Write a row for each file mapping:
    # for mapping in file_mappings:
    #     new_name = mapping["new"]
    #     dec_list = convert_string_to_decimal_list(new_name)
    #     data_str = "[" + ",".join(dec_list) + "]"
    #     data_len = len(dec_list)
    #     json_part = (f'{{"cmdData": {{"Identifier": "8217", "Cmd": {{"value": 96}}, "Type": {{"value": 87}}, '
    #                  f'"Data": {data_str}, "DataLen": "{data_len}"}}}}')
    #     row = ["SXBand_GwSendCmd", "padre-padre-obc-cp-gw-fidl", "padre-obc", json_part, "", "15", ""]
    #     writer.writerow(row)
    
    # # Now add an extra row for "schedule_03.bin":
    # schedule_bin = "schedule_03.bin"
    # dec_list = convert_string_to_decimal_list(schedule_bin)
    # data_str = "[" + ",".join(dec_list) + "]"
    # data_len = len(dec_list)
    # json_part = (f'{{"cmdData": {{"Identifier": "8217", "Cmd": {{"value": 96}}, "Type": {{"value": 87}}, '
    #              f'"Data": {data_str}, "DataLen": "{data_len}"}}}}')
    # row = ["SXBand_GwSendCmd", "padre-padre-obc-cp-gw-fidl", "padre-obc", json_part, "", "100", ""]
    # writer.writerow(row)

    csvfile.write("cmd,type,data\n")
    # f.write("0x09,R,\n")
    # f.write("0x09,W,000503030107000000010000020000000202070700050000\n")
    # f.write("0x30,W,\n")
    for mapping in file_mappings:
        # Writes: 0x70,W,"file-0"
        csvfile.write(f'0x60,W,"{mapping["new"]}"\n')
    csvfile.write("0x31,W,\n")

command = [
    "python", "sxband_cmd_list_create.py",
    "--input-file", "schedule_04.csv",
    "--output-file", "schedule_04.bin",
    "-sfn", "schedule_04.sfn",
    "--device-id", "8729"
]

try:
    subprocess.run(command, check=True)
    print("External script sxband_cmd_list_create.py executed successfully.")
except subprocess.CalledProcessError as e:
    print("Error running sxband_cmd_list_create.py:", e)
# -----------------------------------------------------------------------------
# Step 5: Write the schedule_03.csv.
# Format:
# Header row:          cmd,type,data
# Fixed rows:
#   0x09,R,
#   0x09,W,000503030107000000010000020000000202070700050000
#   0x30,W,
# Then for each new file (each unique new file name from file_mappings),
#   add a row: 0x70,W,"<new file name>"
# Finally, add a fixed last row: 0x31,W,
# -----------------------------------------------------------------------------
with open("schedule_03.csv", "w", newline="") as f:
    f.write("cmd,type,data\n")
    # f.write("0x09,R,\n")
    # f.write("0x09,W,000503030107000000010000020000000202070700050000\n")
    # f.write("0x30,W,\n")
    counter = 0
    for mapping in file_mappings:
        # Writes: 0x70,W,"file-0"
        f.write(f'0x70,W,"{mapping["new"]}"\n')
        # numSpaces = mapping["filesize"] // 1000000
        # numSpaces = math.ceil(numSpaces)
        numSpaces = 5
        for i in range(numSpaces):
            f.write(f'0x70,W,""\n')
        counter += 1
        if counter == 100:
            break
        
    f.write("0x31,W,\n")

# -----------------------------------------------------------------------------
# Final Step: Call the external script sxband_cmd_list_create.py
#
# This script is called from the command line with arguments:
#   --input-file schedule_03.csv
#   --output-file schedule_03.bin
#   --sfn schedule_03.sfn
#   --device-id 8217
#
# Adjust the command below as needed (for instance the python executable or path).
# -----------------------------------------------------------------------------
command = [
    "python", "sxband_cmd_list_create.py",
    "--input-file", "schedule_03.csv",
    "--output-file", "schedule_03.bin",
    "-sfn", "schedule_03.sfn",
    "--device-id", "8729"
]

try:
    subprocess.run(command, check=True)
    print("External script sxband_cmd_list_create.py executed successfully.")
except subprocess.CalledProcessError as e:
    print("Error running sxband_cmd_list_create.py:", e)

print(f"Generated files:\n  {lookup_csv_filename}\n  rename_files.csv\n  obc_download_Sci_Files.csv\n  fileUpload.csv\n  schedule_03.csv\n  schedule_04.csv\n  schedule_03.bin\n  schedule_04.bin")

# -----------------------------------------------------------------------------
# Additional Step: Create a swapped rename CSV.
# This CSV will be formatted as:
# Rename;padre-padre-filemanager-fidl;padre-obc;{"oldPath": "[new file name]", "newFileName": "[OG filename]"};;100;
# -----------------------------------------------------------------------------
with open("rename_files_swapped.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";", lineterminator="\n")
    for mapping in file_mappings:
        # Swap the identifiers: use the new file name as oldPath and the original filename as newFileName.
        json_part = f'{{"oldPath": "{mapping["new"]}", "newPath": "{mapping["old"]}"}}'
        row = ["Rename", "padre-padre-filemanager-fidl", "padre-obc", json_part, "", "100", ""]
        writer.writerow(row)

print("  rename_files_swapped.csv")

# -----------------------------------------------------------------------------
# Additional Step 2: Create a delete files csv.
# This CSV will be formatted as:
# Delete;padre-padre-filemanager-fidl;padre-obc;{"Path": "[new file name]"};;100;
# -----------------------------------------------------------------------------

with open("delete_files.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";", lineterminator="\n")
    for mapping in file_mappings:
        row = ["Delete", 
               "padre-padre-filemanager-fidl", 
               "padre-obc", 
               f'{{"Path": "{mapping['new']}"}}', 
               "", 
               "50", 
               ""]
        writer.writerow(row)

print("  delete_files.csv") 
# -----------------------------------------------------------------------------