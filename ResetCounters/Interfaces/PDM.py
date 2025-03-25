# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 04:17:51 2024

@author: Ace Stratton

This script is intended to handle all the test functions for the performance
tests regarding the Power Distribution Model (PDM)
"""
import sys, os, time
current_dir = os.getcwd()
fidl_path = os.path.abspath(os.path.join(current_dir, ".", "fidl"))
sys.path.insert(0, fidl_path)
from EPSII_PDM_1ClientApp import FP_API_EPSII_PDM_1
import Interface



api = FP_API_EPSII_PDM_1()
moduleMac = 119


def getPDMHealthInfo(inquiry):
    
    payloadBytes = api.req_GetDeviceHealthInfo()
    out1 = Interface.getReturn(payloadBytes, moduleMac, api)
    results = vars(out1["s__GetDeviceHealthInfo"])
    #print(results)
    
    out_time = results["int32__ActiveCPU_RunningTime"]
    temp = results["int32__ActiveCPU_Temperature"]
    if inquiry == "uptime":
        
        return(out_time)
    
    if inquiry == "CPUVoltage":
        out_CPUV = results["int32__ActiveCPU_Voltage"]
        return(out_CPUV)
    if inquiry == "Temperatures":
        out = results["int32__ActiveCPU_Temperature"]
        out2 = results["int32__PCB_Temperature_1"]
        out3 = results["int32__PCB_Temperature_2"]
        output = [out, out2, out3]
        return(output)
    
    if inquiry == 'All':
        return(out_time, temp)
    else:
        
        return(results)
      
def getPDMInfo(inquiry):
    payloadBytes = api.req_GetDeviceInfo()
    out1 = Interface.getReturn(payloadBytes, moduleMac, api)
    #print(out1)
    
    
    if inquiry == 'serial':
        length = out1['uint8__string__DeviceSerialNumberSize']
        results = out1['string__DeviceSerialNumber']
        serial = results[0:length]
        return serial
      
    if inquiry == 'moduleType':
        length = out1['uint8__string__ModuleTypeSize']
        results = out1['string__ModuleType']
        modType = results[0:length]
        return modType
      
    if inquiry == 'fwType':
        length = out1['uint8__string__FWTypeSize']
        results = out1['string__FWType']
        fwType = results[0:length]
        return fwType
      
def getPowerDistInfo(inquiry=None):
  payloadBytes = api.req_GetPowerDistributionInfo()
  out1 = Interface.getReturn(payloadBytes, moduleMac, api)
  out2 = vars(out1['s__PowerDistributionInfo'])
  #print(vars(out2['s__Out_5V_Output1_Sense']))
  
  if inquiry == 'rawBatt':
    batRawParse = vars(out2['s__Out_BatRAW_Output_Sense'])
    battVRaw = batRawParse['int32__U']
    return battVRaw
  elif inquiry == 'All':
    powerReturn = []
    var_list = [
    's__Out_12V_Output_Sense',
    's__Out_5V_Output1_Sense',
    's__Out_5V_Output2_Sense',
    's__Out_3V3_Output1_Sense',
    's__Out_3V3_Output2_Sense'
    ]
   
    for channel in var_list:
      output = vars(out2[channel])
      powerReturn.append(output['int32__U'])
      powerReturn.append(output['int32__I'])
    
    return powerReturn
  
    
    
    
    

