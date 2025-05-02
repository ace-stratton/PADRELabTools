# === Configuration (edit these for your environment) ===
FOLDER_PATH = "file-MeDDEA_DITL_050125"      # Folder containing the .bin files
MAPPING_CSV  = "Edited_FilenameDirectory_2505011816_Gen_20250502_095314.csv"  # Semicolon‑delimited mapping CSV
# =====================================================

import os
import csv


def truncate_and_rename(folder_path, mapping_csv):
    
    with open(mapping_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
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
            
            
            base_edit = base[:idx] + "-" + base[idx:]
            # base_edit = base[:idx] + base[idx:]
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
