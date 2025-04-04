import os
import csv
from datetime import datetime, timedelta

# ----------------------------
# User Input: DateTimePull (format "YYMMDDHHMM")
# ----------------------------
DateTimePull = "2504031904"  # change this string as needed

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

# List to hold matching file names (in uppercase)
selected_files = []

# ----------------------------
# Process each line in the file
# ----------------------------
for line in lines:
    line = line.strip()
    if not line:
        continue

    # The first column is the file path (e.g., "/sd/padreMDA0_250401212029.dat")
    parts = line.split(",")
    file_path = parts[0]

    # Get the base file name (e.g., "padreMDA0_250401212029.dat")
    base_name = os.path.basename(file_path)
    lower_name = base_name.lower()

    # Check if the file name starts with "padreMD" or "padreSP"
    if lower_name.startswith("padremd") or lower_name.startswith("padresp"):
        # Extract the timestamp part from the file name.
        # Expected format: padre####_YYMMDDHHMMSS.xxx
        underscore_index = base_name.find("_")
        dot_index = base_name.find(".", underscore_index)
        if underscore_index != -1 and dot_index != -1:
            # Extract the time portion between the underscore and the dot.
            time_str = base_name[underscore_index + 1:dot_index]
            # Ensure we have at least 10 characters (the input covers YYMMDDHHMM).
            if len(time_str) >= 10:
                try:
                    # Parse the file's timestamp (which includes seconds)
                    file_dt = datetime.strptime(time_str, "%y%m%d%H%M%S")
                except ValueError:
                    # Skip files that don't follow the expected time format
                    continue

                # Check if the file's timestamp is within +/- 10 minutes of dt_pull.
                if abs(file_dt - dt_pull) <= timedelta(minutes=10):
                    # Convert the file name (base_name) to upper case and store it.
                    selected_files.append(base_name.upper())

# ----------------------------
# Write the output CSV
# ----------------------------
output_filename = "obc_download_Sci_Files_.csv"
with open(output_filename, "w", newline="") as csvfile:
    # Create a CSV writer that uses semicolons as delimiters.
    writer = csv.writer(csvfile, delimiter=";")
    for fname in selected_files:
        # Construct the row using the provided template,
        # replacing DIRLIST.TXT with the current file name.
        row = [
            f"Download {fname}",
            "padre-file-manager-commands",
            "padre-obc",
            f'{{"type": "obcDownload", "fileName": "{fname}", "offset": 0,"volId":0}}',
            "",
            "150",
            ""
        ]
        writer.writerow(row)

print(f"CSV file '{output_filename}' has been generated with {len(selected_files)} matching file(s).")
