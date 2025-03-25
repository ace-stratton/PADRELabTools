# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 2024

@author: Ace Stratton

This file will handle all BP Interactions
"""

import sys, os
current_dir = os.getcwd()
fidl_path = os.path.abspath(os.path.join(current_dir, ".", "fidl"))
sys.path.insert(0, fidl_path)
from EPSII_BP_1ClientApp import FP_API_EPSII_BP_1
import Interface

api = FP_API_EPSII_BP_1()
moduleMac = 102

def getDeviceInfo(inquiry):
    payloadBytes = api.req_GetDeviceInfo()
    out1 = Interface.getReturn(payloadBytes, moduleMac, api)
    #print(out1)
    if out1 == None:
      return(None)
    
    
    if inquiry == 'modType':
      length = out1['uint8__string__ModuleTypeSize']
      modType1 = out1['string__ModuleType']
      modTypeReturn = modType1[0:length]
      return(modTypeReturn)
    
    if inquiry == 'fwType':
      length = out1['uint8__string__FWTypeSize']
      fwType = out1['string__FWType']
      fwTypeRet = fwType[0:length]
      return(fwTypeRet)
    
    if inquiry == 'serial':
      length = out1['uint8__string__DeviceSerialNumberSize']
      serial = out1['string__DeviceSerialNumber']
      serialRet = serial[0:length]
      return(serialRet)
    
def getBatteryInfo(inquiry):
    payloadBytes = api.req_GetBatteryInfo()
    out1 = Interface.getReturn(payloadBytes, moduleMac, api)
    #print(out1)
    if out1 == None:
      return(None)
    voltageRet = out1['int64__BattVoltage']
    modeOut = vars(out1['e__BP_Mode_Type__bp_mode'])
    modeValue = modeOut['value']
    modedict = vars(api.enum_BP_Mode_Type)
    modeRet = modedict["ValuesDict"][modeValue]
    modeRet1 = modeRet[13:]
    currentRet = out1['int64__BattCurrent']  
    tempRet = out1['int64__BattTemperature']
    tempRet1 = tempRet/1000 
    
    if inquiry == 'mode':
      
      return(modeRet1)
    
    if inquiry == 'battV':
      
      return(voltageRet)
    
    if inquiry == 'battI':
      
      return(currentRet)
    
    if inquiry == 'battT':
      
      return(tempRet1)
    if inquiry == 'All':
      
      
      return(modeRet1, voltageRet, currentRet, tempRet1)
    
def getCPURunTime():
  payloadBytes = api.req_GetDeviceHealthInfo()
  out1 = Interface.getReturn(payloadBytes, moduleMac, api)
  if out1 == None:
    return(None)
  CPURunTime = out1['int32__ActiveCPU_RunningTime']
  return CPURunTime