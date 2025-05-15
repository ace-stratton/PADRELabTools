#!/usr/bin/env python3
"""
Script to detect and merge mapping entries when actual file sizes deviate
significantly from expected sizes, then write an updated mapping CSV.
"""

# === Configuration ===
FOLDER_PATH = "file-SHARP_Polarization_050325"        # Folder containing the .bin files
MAPPING_CSV = "FilenameDirectory_2505011816_Gen_20250503_202719.csv"  # Original mapping CSV
THRESHOLD   = 7000                       # Bytes: threshold for detecting merges
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
                'sz': int(size_str)
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
            return [os.path.getsize(path), base_edit]
    print(f"Warning: no .bin found for mapping '{new_name}'")
    return None

def choose_number(a, b):
    if a > 0 and b > 0:
        return min(a, b)
    elif a > 0:
        return a
    elif b > 0:
        return b
    else:
        choice = min(abs(a), abs(b))
        if choice == abs(a):
             return a
        else:
             return b
     

mappings = load_mappings(MAPPING_CSV)
new_mappings = []

file_count = sum(1 for f in os.listdir(FOLDER_PATH) if os.path.isfile(os.path.join(FOLDER_PATH, f)))

i_name = 0
i_sz = 0
i_idx = 0

for i in mappings:
    og_sz = mappings[i_sz]['sz']
    og_idx = mappings[i_idx]['new']
    [bin_sz, bin_name] = get_actual_size(FOLDER_PATH, og_idx)
     
    sz_diff = abs(og_sz-bin_sz)

    if sz_diff > THRESHOLD:
        sz_og_prev_combined = (mappings[i_sz-1]['sz']) + og_sz
        sz_og_next_combined = (mappings[i_sz+1]['sz']) + og_sz
        [prev_sz, prev_name] = get_actual_size(FOLDER_PATH, (mappings[i_idx-1]['new']))
        prev_comb_diff = prev_sz - sz_og_prev_combined  
        next_comb_diff = bin_sz - sz_og_next_combined
        chosen_number = choose_number(prev_comb_diff, next_comb_diff)

        if chosen_number == prev_comb_diff:
             replacement_name = mappings[i_name-1]['orig']+"_Merged_"+mappings[i_name]['orig'] #The files need to merge backwards
             replacement_size = sz_og_prev_combined
             new_mappings[-1]['orig'] = replacement_name
             new_mappings[-1]['sz'] = replacement_size
             i_name += 1
             i_sz += 1
             print('yay')
        elif chosen_number == next_comb_diff:
             replacement_name = mappings[i_name]['orig'] + "_Merged_" + mappings[i_name+1]['orig']
             replacement_size = sz_og_next_combined
             new_mappings.append({
                'orig': replacement_name,
                'new': bin_name,
                'timestamp': mappings[i_name]['timestamp'],
                'sz': replacement_size
            })
             i_name += 2
             i_idx += 1
             i_sz += 2


    else:

        new_mappings.append({
                'orig': mappings[i_name]['orig'],
                'new': bin_name,
                'timestamp': mappings[i_name]['timestamp'],
                'sz': og_sz
            })
        i_name += 1
        i_sz += 1
        i_idx += 1
    if i_idx == file_count:
         break

output_csv = "Edited_" + MAPPING_CSV
with open(output_csv, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';', lineterminator="\n")
    for m in new_mappings:
        writer.writerow([m['orig'], m['new'], m['timestamp'], str(m['sz'])])
# printing new mappings to csv 

check_index = 0
for m in new_mappings:
    [bin_sz, bin_name] = get_actual_size(FOLDER_PATH, new_mappings[check_index]['new'])
    if abs(bin_sz - m['sz']) > THRESHOLD:
         Exception('The files did not map properly')
    
    check_index += 1
     
print(f'All files mapped correctly and are saved in {output_csv}')