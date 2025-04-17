# === Configuration (edit these for your environment) ===
RESPONSE_FILE = "SXBAND.txt"           # Text file containing responseData or full JSON
UPLOAD_CSV    = "fileUpload.csv"        # Existing upload CSV
OUTPUT_CSV    = "fileUpload_filtered.csv" # Filtered output CSV
# =====================================================

import re
import json
import csv


def extract_names(response_data_str):
    """
    Extract all filenames from response_data_str using pattern 'Name: <filename>'.
    Returns a list of filenames.
    """
    return re.findall(r"Name: ([^\s]+)", response_data_str)


def decode_data_field(data_list):
    """
    Convert a list of ASCII code strings (or ints) to an ASCII string,
    trimming trailing null characters.
    """
    bytes_list = [int(x) for x in data_list]
    while bytes_list and bytes_list[-1] == 0:
        bytes_list.pop()
    return bytes(bytes_list).decode('ascii')


def filter_upload_csv(upload_csv, output_csv, names_to_remove):
    """
    Read upload_csv, remove rows whose Data field decodes to a name in names_to_remove,
    and write the rest to output_csv.
    """
    with open(upload_csv, newline='') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';', lineterminator="\n")
        for row in reader:
            try:
                cmd_dict = json.loads(row[3])
                cmd_dict2 = cmd_dict.get('cmdData')
                data_list = cmd_dict2.get('Data')
                filename = decode_data_field(data_list)
            except Exception:
                # Keep row if JSON parse fails
                writer.writerow(row)
                continue

            if filename in names_to_remove:
                print(f"Removing entry for {filename}")
            else:
                writer.writerow(row)


def main():
    # Read response data from file
    with open(RESPONSE_FILE, 'r') as f:
        data = f.read()
    # Attempt to parse JSON
    try:
        obj = json.loads(data)
        resp = obj.get('responseData', data)
    except json.JSONDecodeError:
        resp = data

    names = extract_names(resp)
    print(f"Found {len(names)} names to remove: {names}")

    filter_upload_csv(UPLOAD_CSV, OUTPUT_CSV, set(names))
    print(f"Filtered CSV written to {OUTPUT_CSV}")

if __name__ == '__main__':
    main()
