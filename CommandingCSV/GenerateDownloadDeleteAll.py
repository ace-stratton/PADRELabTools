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
DateTimePull = "2504181852"  # e.g. "YYMMDDHHMM" (change as needed)
DurationMinutes = 60*200        # ± minutes window (adjust as needed)

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
    # if (lower_name.startswith("padresp")) and file_size >= 500:
    if (lower_name.startswith("padremd") or lower_name.startswith("padresp")):
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
lookup_csv_filename = f"FilenameDirectory_DeleteAll_{DateTimePull}_Gen_{gen_time_str}.csv"

with open(lookup_csv_filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";", lineterminator="\n")
    # Optionally, you may include a header row:
    # writer.writerow(["Old Filename", "New Filename", "Extracted Timestamp"])
    for mapping in file_mappings:
        # Format timestamp in a readable format (e.g., "YYYY-MM-DD HH:MM:SS")
        ts_formatted = mapping["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([mapping["old"], mapping["new"], ts_formatted, mapping["filesize"]])



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

print("Delete files CSV 'delete_files.csv' generated.") 
# -----------------------------------------------------------------------------