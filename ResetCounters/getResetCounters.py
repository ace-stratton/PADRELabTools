import sys, os
current_dir = os.getcwd()
fidl_path = os.path.abspath(os.path.join(current_dir, "fidl"))
sys.path.insert(0, fidl_path)

interface_path = os.path.abspath(os.path.join(current_dir, "Interfaces"))
print(interface_path)
sys.path.insert(0, fidl_path)
from EPSII_BP_1ClientApp import FP_API_EPSII_BP_1
import Interface


api = FP_API_EPSII_BP_1()
moduleMac = 102

def getResetCounters():
    payloadBytes = api.req_GetMainAppErrCounters()
    out1 = Interface.getReturn(payloadBytes, moduleMac, api)
    ParsedResult = vars(out1['s__errorCounters'])
    values_list = list(ParsedResult.values())
    errors1 = values_list[40:64]
    
    
    # payloadBytes = api.req_GetMainAppErrCounters2()
    # out1 = Interface.getReturn(payloadBytes, moduleMac, api)
    # ParsedResult = vars(out1['s__errorCounters2'])
    # errors2 = list(ParsedResult.values())

    # errors1.extend(errors2)
   
    return errors1