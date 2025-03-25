# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 06:49:09 2024

@author: Ace Stratton

This file will handle all OBC test interactions
"""

import sys, os, time
current_dir = os.getcwd()
fidl_path = os.path.abspath(os.path.join(current_dir, "..", "fidl"))
sys.path.insert(0, fidl_path)
from OBCClientApp import FP_API_OBC
from ModuleIdClientApp import FP_API_MODULEID
from timeClientApp import FP_API_TIME
from gnssClientApp import FP_API_GNSS
from FileManagerClientApp import FP_API_FILEMANAGER
import Interface



api = FP_API_OBC()
moduleMac = 51


def getUptime():
	
	payloadBytes = api.req_get_uptime()
	DictOut = Interface.getReturn(payloadBytes, moduleMac, api)
	out = DictOut["uint32__uptime"]
	#print(out)
	
	return(out)


def getVersion():
	
	api = FP_API_MODULEID()
	payloadBytes = api.req_getModuleVersionInfo()
	Result = Interface.getReturn(payloadBytes, moduleMac, api)
	output = vars(Result['s__settings'])
	Result2 = output['s__fwVersion']
	value = vars(Result2)
	Major = value['uint16__Major']
	Minor = value['uint16__Minor']
	Patch = value['uint16__Patch']
	out = [Major, Minor, Patch]
	#print(out)
	
	return(out)

def getTime():
	api = FP_API_TIME()
	payloadBytes = api.req_get_time()
	Result = Interface.getReturn(payloadBytes, moduleMac, api)
	output = vars(Result['s__time'])
	Hour = output['uint8__hour']
	Min = output['uint8__min']
	Sec = output['uint8__sec']
	out = [Hour, Min, Sec] 
	#print(output)
	
	return(out)

def getDate():
	
	api = FP_API_TIME()
	payloadBytes = api.req_get_date()
	Result = Interface.getReturn(payloadBytes, moduleMac, api)
	output = vars(Result['s__date'])
	Day = output['uint8__day']
	Month = output['uint8__mon']
	Year = output['uint16__year']
	out = [Day, Month, Year]
	
	return(out)
  
def getGNSSPower():
    
    api = FP_API_GNSS()
    payloadBytes = api.req_get_power()
    Result = Interface.getReturn(payloadBytes, moduleMac, api)
    PwrStat = vars(Result['e__Power__pwr_status'])
    OpStat = vars(Result['e__Operation__op_status'])
    PwrStat1 = PwrStat['value']
    OpStat1 = OpStat['value']
    
    if PwrStat1 == 1:
      PwrResult = 'OK'
    else:
      PwrResult = 'BAD'
      
    if OpStat1 == 1:
      OpResult = 'ON'
    else:
      OpResult = 'OFF'
      
    return([PwrResult, OpResult])
  
def getSDCard():
    
    api = FP_API_FILEMANAGER()
    payloadBytes = api.req_get_sd_card_status()
    Result = Interface.getReturn(payloadBytes, moduleMac, api)
    SDCardVal = vars(Result['e__SDCardStatus__status'])
    SDCardVal = SDCardVal['value']
    modedict = vars(api.enum_SDCardStatus)
    SDRet = modedict["ValuesDict"][SDCardVal]
    SDRet = SDRet[13:]
    return(SDRet)
  
def clearErrorCounters():
    api = FP_API_OBC()  
  
    
    ResetID_val = getattr(api.enum_ResetCntrId, 'RESETCNTRID_ALL')
    payloadBytes = api.req_clear_reset_counter(ResetID_val)
    Interface.getReturn(payloadBytes, moduleMac, api, 1)
  

def getErrorCounters():
     api = FP_API_OBC()
     payloadBytes = api.req_get_reset_counters()
     Result = Interface.getReturn(payloadBytes, moduleMac, api)
     ParsedResult = vars(Result['s__status'])
     values_list = list(ParsedResult.values())
     return(values_list)
	
	
	