#!/usr/bin/env python3
"""
Script to detect and merge mapping entries when actual file sizes deviate
significantly from expected sizes, then write an updated mapping CSV.
"""

# === Configuration ===
FOLDER_PATH = "file-MeDDEA_DITL_050125"        # Folder containing the .bin files
MAPPING_CSV = "FilenameDirectory_2505011816_Gen_20250502_095314.csv"  # Original mapping CSV
THRESHOLD   = 1500                       # Bytes: threshold for detecting merges
# =====================

import os
import csv


def load_mappings(mapping_csv):
    """Load mapping CSV into a list of dicts."""
    mappings = []
    with open(mapping_csv, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            orig, new, timestamp, size_str = row
            mappings.append({
                'orig': orig,
                'new': new,
                'timestamp': timestamp,
                'expected_size': int(size_str)
            })
    return mappings


def get_actual_size(folder_path, new_name):
    """Return actual size of the .bin file for a mapping, considering both hyphenated and non-hyphenated forms."""
    base, _ = os.path.splitext(new_name)
    for i, ch in enumerate(base):
                if ch.isdigit():
                    idx = i
                    break
            
            
    base_edit = base[:idx] + "-" + base[idx:]
    candidates = [f"{base}.bin", f"{base_edit}.bin"]
    for fn in candidates:
        path = os.path.join(folder_path, fn)
        if os.path.exists(path):
            return os.path.getsize(path)
    print(f"Warning: no .bin found for mapping '{new_name}'")
    return None


def merge_mappings(folder_path, mappings):
    """
    Detect and merge adjacent mapping entries when the actual file size
    equals (within threshold) the sum of two expected sizes.
    """
    i = 0  # start merge loop
    merges = 0
        # NOTE: removed precomputed actuals list to avoid index misalignment
    while i < len(mappings) - 1:
        
        expected = mappings[i+merges]['expected_size']
        actual = get_actual_size(folder_path, mappings[i]['new'])  # CHANGED: compute actual size on the fly
        if actual is None:
            i += 1
            continue

        # If deviation beyond threshold, check merge with next entry
        if (actual - expected) > THRESHOLD:
            expected2 = mappings[i + 1]['expected_size']
            if abs(actual - (expected + expected2)) <= THRESHOLD:
                # Perform merge of i and i+1
                merges = +1
                merged_orig = f"{mappings[i]['orig']}_merged_{mappings[i+1]['orig']}"
                mappings[i] = {
                    'orig': merged_orig,
                    'new': mappings[i]['new'],
                    'timestamp': mappings[i]['timestamp'],
                    'expected_size': expected + expected2
                }
                del mappings[i + 1]
                # Do not increment i to allow cascading merges
                
            
        i += 1
    return mappings



def reindex_mappings(mappings):
    """Reassign sequential new filenames file-0, file-1, ..."""
    for idx, m in enumerate(mappings):
        m['new'] = f"file-{idx}"
    return mappings


def write_mappings(mappings, output_csv):
    """Write the updated mapping list back to a CSV."""
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';', lineterminator="\n")
        for m in mappings:
            writer.writerow([m['orig'], m['new'], m['timestamp'], str(m['expected_size'])])


def main():
    base = os.path.basename(MAPPING_CSV)
    out_csv = os.path.join(os.path.dirname(MAPPING_CSV), f"edited_{base}")

    mappings = load_mappings(MAPPING_CSV)
    merged   = merge_mappings(FOLDER_PATH, mappings)
    reindexed= reindex_mappings(merged)
    write_mappings(reindexed, out_csv)

    print(f"Edited mapping CSV written to: {out_csv}")


if __name__ == "__main__":
    main()
