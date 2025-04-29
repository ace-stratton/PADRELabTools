# === Configuration (edit these for your environment) ===
FOLDER_PATH = "file-0-42-1704252033"      # Folder containing the .bin files
MAPPING_CSV  = "FilenameDirectory_2504180042_Gen_20250417_201022.csv"  # Semicolon‑delimited mapping CSV
# =====================================================

import os
import csv


def truncate_and_rename(folder_path, mapping_csv):
    counter = 0
    with open(mapping_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            
            
            orig_name, new_name, _, size_str = row
            desired_size = int(size_str)
            
            # Determine the .bin filename by replacing extension with .bin
            base, _ = os.path.splitext(new_name)
            # find where digits start
            for i, ch in enumerate(base):
                if ch.isdigit():
                    idx = i
                    break
            
            if base[idx:] in ['9', '10', '16', '33', '31']:
                print(f'Skipping {base_edit} as it is a known issue')
                counter += 1
                continue
            base_edit = base[:idx] + "-" + base[idx:]
            
            bin_filename = f"{base_edit}.bin"
            bin_path = os.path.join(folder_path, bin_filename)
            
            if not os.path.exists(bin_path):
                print(f"Warning: {bin_filename} not found in {folder_path}")
                continue
            
            # Truncate the file to the desired size
            with open(bin_path, 'rb+') as f:
                f.truncate(desired_size)
            
            # Rename the truncated file to the original filename
            new_path = os.path.join(folder_path, orig_name)
            os.rename(bin_path, new_path)
            print(f"Truncated and renamed {bin_filename} -> {orig_name}")


def main():
    truncate_and_rename(FOLDER_PATH, MAPPING_CSV)


if __name__ == "__main__":
    main()
