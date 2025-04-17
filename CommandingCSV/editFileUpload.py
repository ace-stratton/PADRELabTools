# === Configuration (edit these for your environment) ===
RESPONSE_JSON = {
	"responseData": "Page 0, Found files = 75 rn00 Name: file0.dat  [Size: 3558]rn01 Name: Index_Log.bin  [Size: 4]rn02 Name: Error_Log.bin  [Size: 2336]rn03 Name: file1.idx  [Size: 545]rn04 Name: file2.dat  [Size: 24648]rn05 Name: file3.idx_  [Size: 423905]rn06 Name: file4.dat  [Size: 5243579]rn07 Name: file19.idx  [Size: 86273]rn08 Name: file20.idx_  [Size: 8129]rn09 Name: file21.idx  [Size: 3425]rn10 Name: file22.dat  [Size: 5250024]rn11 Name: file25.idx  [Size: 36001]rn12 Name: file26.dat_  [Size: 4733823]rn13 Name: file27.idx  [Size: 3425]rn14 Name: file28.dat_  [Size: 640848]rn15 Name: file29.dat  [Size: 958272]rn16 Name: file40.dat_  [Size: 342238]rn17 Name: file41.idx_  [Size: 20289]rn18 Name: file42.dat_  [Size: 4864975]rn19 Name: file43.idx_  [Size: 1489]rn20 Name: file44.dat_  [Size: 3216532]rn21 Name: file45.idx  [Size: 3425]rn22 Name: file46.dat  [Size: 5250024]rn23 Name: file51.idx  [Size: 71969]rn24 Name: file52.dat  [Size: 5243064]rn25 Name: file80.dat  [Size: 587328]rn26 Name: file95.idx  [Size: 71841]rn27 Name: file96.dat  [Size: 5243560]rn28 Name: file99.idx  [Size: 71729]rn29 Name: file100.dat  [Size: 5244024]rn30 Name: file103.idx  [Size: 71697]rn31 Name: file104.dat  [Size: 5243964]rn32 Name: file114.dat  [Size: 78016]rn33 Name: file120.dat  [Size: 5243920]rn34 Name: file123.idx  [Size: 71569]rn35 Name: file8.dat_  [Size: 4199638]rn36 Name: file9.dat_  [Size: 2789238]rn37 Name: file10.dat  [Size: 5250024]rn38 Name: file23.idx  [Size: 3425]rn39 Name: file24.da >>SXBAND.LOGu0000"
}
UPLOAD_CSV = "fileUpload.csv"         # existing upload CSV
OUTPUT_CSV = "fileUpload_filtered.csv"  # filtered output CSV
# =====================================================

import re
import json
import csv


def extract_names(response_data_str):
    # Find all occurrences of Name: <filename>
    return re.findall(r"Name: ([^\s]+)", response_data_str)


def decode_data_field(data_list):
    # Convert list of ASCII code strings to a Python string, strip trailing null
    # Data can be list of ints or strings representing ints
    bytes_list = [int(x) for x in data_list]
    # Remove trailing zero(s)
    while bytes_list and bytes_list[-1] == 0:
        bytes_list.pop()
    return bytes(bytes_list).decode('ascii')


def filter_upload_csv(upload_csv, output_csv, names_to_remove):
    with open(upload_csv, newline='') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';', lineterminator="\n")
        for row in reader:
            # JSON part is in 4th column (index 3)
            try:
                cmd_dict = json.loads(row[3])
                data_list = cmd_dict.get('Data', [])
                filename = decode_data_field(data_list)
            except Exception:
                # If parsing fails, keep the row
                writer.writerow(row)
                continue

            if filename in names_to_remove:
                print(f"Removing entry for {filename}")
            else:
                writer.writerow(row)


def main():
    resp = RESPONSE_JSON.get('responseData', '')
    names = extract_names(resp)
    print(f"Found {len(names)} names to remove: {names}")
    filter_upload_csv(UPLOAD_CSV, OUTPUT_CSV, set(names))
    print(f"Filtered CSV written to {OUTPUT_CSV}")


if __name__ == '__main__':
    main()
