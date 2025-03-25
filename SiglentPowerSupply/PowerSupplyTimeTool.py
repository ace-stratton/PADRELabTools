import csv
from datetime import datetime, timedelta
import os

def process_csv(file_path):
    # Load CSV
    with open(file_path, newline='') as csvfile:
        reader = list(csv.reader(csvfile))
    
    # Extract end datetime from row 9 (index 8)
    base_raw = reader[8][0]  # e.g., "{Date : 2025-03-22 14:25:32}"
    base_str = base_raw.split(":", 1)[1].strip(" }")
    end_datetime = datetime.strptime(base_str, "%Y-%m-%d %H:%M:%S")

    # Get the last seconds value (from the first column, last row)
    try:
        last_seconds = float(reader[-1][0])
    except ValueError:
        raise ValueError("Last value in first column is not a valid float.")

    # Compute start time
    start_datetime = end_datetime - timedelta(seconds=last_seconds)

    # Update rows with absolute datetimes
    for i in range(11, len(reader)):
        try:
            seconds = float(reader[i][0])
            new_datetime = start_datetime + timedelta(seconds=seconds)
            reader[i][0] = new_datetime.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            # Skip rows that don’t contain valid float seconds
            pass

    # Save new file
    output_filename = os.path.splitext(file_path)[0] + "_withDatetime.csv"
    with open(output_filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(reader)

    print(f"Processed file saved as: {output_filename}")

def detect_power_transitions(file_path):
    with open(file_path, newline='') as csvfile:
        reader = list(csv.reader(csvfile))

    # Find first valid datetime to use in the filename
    first_datetime_str = None
    for row in reader[11:]:
        try:
            first_datetime_str = row[0]
            first_datetime = datetime.strptime(first_datetime_str, "%Y-%m-%d %H:%M:%S")
            break
        except (ValueError, IndexError):
            continue  # Skip malformed rows

    if not first_datetime_str:
        raise ValueError("No valid datetime found in the first column starting at row 12.")

    # Prepare output filename
    dt_str_for_filename = first_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    output_filename = f"PowerBehaviorReport_{dt_str_for_filename}.txt"

    # Initialize report content
    report_lines = []
    previous_on = False

    for row in reader[11:]:
        try:
            time_str = row[0]
            current = float(row[2])
            time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

            is_on = current > 0.002

            if is_on and not previous_on:
                msg = f"The spacecraft turned on at {time_obj}"
                print(msg)
                report_lines.append(msg)
            elif not is_on and previous_on:
                msg = f"The spacecraft turned off at {time_obj}"
                print(msg)
                report_lines.append(msg)

            previous_on = is_on

        except (ValueError, IndexError):
            continue  # Skip malformed rows

    # Write report to file
    with open(output_filename, "w") as report_file:
        for line in report_lines:
            report_file.write(line + "\n")

    print(f"\nReport saved as: {output_filename}")

detect_power_transitions("rollerswitch_withDatetime.csv")
