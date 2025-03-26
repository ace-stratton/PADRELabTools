import csv
from datetime import datetime
import os, sys


current_dir = os.getcwd()
fidl_path = os.path.abspath(os.path.join(current_dir, ".", "fidl"))
sys.path.insert(0, fidl_path)

interfaces_path = os.path.abspath(os.path.join(current_dir, ".", "Interfaces"))
sys.path.insert(0, interfaces_path)

import getResetCounters

def main():
    filename = "rst_counters_flight.csv"


    headers = [
        "Datetime",
        "EDC_RST_TOTAL",
        "EDC_RST_BROWNOUT",
        "EDC_RST_RSTIFG",
        "EDC_RST_PMMSWBOR",
        "EDC_RST_LPM_X_5_WAKE",
        "EDC_RST_SECURITY_VIOLATION",
        "EDC_RST_RES1",
        "EDC_RST_SVSHIFG",
        "EDC_RST_RES2",
        "EDC_RST_RES3",
        "EDC_RST_PMMSWPOR",
        "EDC_RST_WDTIFG",
        "EDC_RST_WDTPW",
        "EDC_RST_FRCTLPW",
        "EDC_RST_FRAM_BIT_ERR",
        "EDC_RST_PER_FETCH",
        "EDC_RST_PMMPW",
        "EDC_RST_MPUPW",
        "EDC_RST_CSPW",
        "EDC_RST_MPUSEGIPIFG",
        "EDC_RST_MPUSEGIIFG",
        "EDC_RST_MPUSEG1IFG",
        "EDC_RST_MPUSEG2IFG",
        "EDC_RST_MPUSEG3IFG",
        "EDC_CONOPS_ENTER_IN_PANEL_COUNTER",
        "EDC_CONOPS_ENTER_IN_HIB_COUNTER"
    ]
    

    
    # Get current date/time and RST counters
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    rst_values = getResetCounters.getResetCounters()
    
    # Check if the file exists
    file_exists = os.path.exists(filename)
    
    # Open the CSV file in append mode
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # If the file doesn't exist, write the headers first
        if not file_exists:
            writer.writerow(headers)
        
        # Write the new row (datetime + counters)
        writer.writerow([now] + rst_values)
    
    # Print out the date/time, RST total, and done message
    print(f"{now} - RST Total: {rst_values[0]}, done!")

if __name__ == "__main__":
    main()
