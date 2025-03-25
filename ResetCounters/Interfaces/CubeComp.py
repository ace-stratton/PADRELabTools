# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 17:16:56 2025

@author: user
"""


import sys, os
current_dir = os.getcwd()
fidl_path = os.path.abspath(os.path.join(current_dir, "..", "fidl"))
sys.path.insert(0, fidl_path)
from CubeADCS_Gen2_CubeComputerControlProgram8ClientApp import FP_API_CUBEADCS_GEN2_CUBECOMPUTERCONTROLPROGRAM8
from CubeADCS_Gen2_CommonFramework1ClientApp import FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1

interfaces_path = os.path.abspath(os.path.join(current_dir, "..", ))
print(interfaces_path)
sys.path.insert(0, interfaces_path)
from pygs import pygs, go, gs, consts
import signal, threading


with open("setCOM.txt", "r", encoding="utf-8") as file:
  comFileRead = file.read()
  print(comFileRead)
  
COM = comFileRead






# Enabling verbose to see all of the logs that are usually native to the Go Comms core
pygs.Verbose(enable=False)



def getPPSFlag():
  
  api = FP_API_CUBEADCS_GEN2_CUBECOMPUTERCONTROLPROGRAM8()
  payloadBytes = api.req_getTlmGnssRaw(0)
  resp = cubeInterface(payloadBytes, api)
  parsed = vars(resp['s__returnVal'])
  RetVal = parsed["bool__GnssPPSDetected"]
  if RetVal == 1:
    RetVal = 'TRUE'
  else:
    RetVal = 0
  return(RetVal)

def getRuntime():
  api = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1()
  payloadBytes = api.req_getIdentification(0)
  resp = cubeInterface(payloadBytes, api)
  parsed = vars(resp['s__returnVal'])
  RetVal = parsed["uint16__RuntimeSeconds"]
  return(RetVal)

def getTemp():
  api = FP_API_CUBEADCS_GEN2_CUBECOMPUTERCONTROLPROGRAM8()
  payloadBytes = api.req_getTlmCubeComputerHealth(0)
  resp = cubeInterface(payloadBytes, api)
  parsed = vars(resp['s__returnVal'])
  RetVal = parsed['double__McuTemp']
  return(RetVal)

def cubeInterface(payloadBytes, api):
  moduleMac = 51
  satId = 2
  cmdType = 2000  

  
  # Module mac, Satellite ID, CmdType and the payload are pretty much the only parameters that differ
  # for the different EnduroSat modules (on this level, that is)
  payloadBytes.insert(0, len(payloadBytes)) 
  
  payload=go.Slice_byte(bytes(payloadBytes))
  resultBytes = go.Slice_byte()
  
  # We'll reuse the GSSD config.yml which has everything needed already configured.
  #
  # Since we want to communicate a CP command through a Mac Dongle connection we
  # set the MacGWConn, TPConn and CPConn options.
  #
  # And since the config.yml for the GSSD by default is configured for working with a GS UHF underneath
  # we'll have to reconfigure the comm serial device it talks to.
  # gs1 = gs.NewGS(
  # 	gs.WithFile("./config.yml"),
  #     	gs.WithMacGWConn(macProtoId=consts.MacProtoId_TP),
  # 	gs.WithCommSerial(COM, 115200, "1s"),
  # 	gs.WithTPConn(tpProtoId=consts.TPProtoId_CP, packetId=13, hostContext=13),
  # 	gs.WithCPConn(cmdId=13, cmdType=cmdType, cpTripType=consts.CPTripType_ImmediateRes),
  # )
  gs1 = gs.NewGS( 
    gs.WithFile("./config.yml"), 
        gs.WithMacGWConn(macProtoId=consts.MacProtoId_TP), 
    gs.WithCommSerial(COM, 115200, "1s"), 
    gs.WithTPConn(tpProtoId=consts.TPProtoId_CP, packetId=12361, hostContext=12361), 
    gs.WithCPConn(cmdId=12361, cmdType=cmdType, cpTripType=consts.CPTripType_ImmediateRes), 
  )
  
  conn : gs.Conn
  conn = gs1.Dial("/esmdg/esmgw/{}/estp/2:{}:{}/escp".format(moduleMac, satId, moduleMac))
  
  # Handle Ctrl+C
  #signal.signal(signal.SIGINT, lambda sig, frame: (conn.Cancel()))
  
  def start():
  	#print("PyGS writing data")
  	conn.Write(payload)
  
  	#print("PyGS reading result")
  	conn.Read(resultBytes)
  
  t = threading.Thread(target=start, daemon=True)
  t.start()
  t.join()
  
  conn.Close()
  
  return(api.resp_parse(bytes(resultBytes)))

