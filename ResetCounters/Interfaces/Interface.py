# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 06:57:15 2024

@author: Ace Stratton 

This is intended to get payload bytes as needed
"""
import threading, sys, os, time
current_dir = os.getcwd()
fidl_path = os.path.abspath(os.path.join(current_dir, "..", "fidl"))
sys.path.insert(0, fidl_path)

main_path = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, main_path)
from pygs import pygs, consts, go, gs
pygs.Verbose(enable=False)


with open("setCOM.txt", "r", encoding="utf-8") as file:
  comFileRead = file.read()
  print(comFileRead)
  
COM = comFileRead


def getReturn(payloadBytes, moduleMac, api, Set=None):
    
    payload=go.Slice_byte(bytes(payloadBytes))
    resultBytes = go.Slice_byte()

    gs1 = gs.NewGS(
        gs.WithFile("./config.yml"),
            gs.WithMacGWConn(macProtoId=consts.MacProtoId_FP),
        gs.WithCommSerial(COM, 115200, "1s"),
    )
    


    conn : gs.Conn
    conn = gs1.Dial("/esmdg/esmgw/{}/esfp".format(moduleMac))

    # Handle Ctrl+C
    #signal.signal(signal.SIGINT, lambda sig, frame: (conn.Cancel()))
    global errorFlag
    errorFlag = 0
    def start():
        # Read and write as well as dial can throw
        #print("PyGS writing data")
        totalTimeout = 2
        startTime = time.time()
        while time.time() - startTime < totalTimeout:
          try: 
      
            conn.Write(payload)
    
            #print("PyGS reading result")
            conn.Read(resultBytes)
            
            return resultBytes
            break
          except RuntimeError as e:
            if "no read progress timeout" in str(e):
                # This might indicate a short read timeout within the native code itself
                # or partial data. We'll keep looping until our total_timeout expires
                pass
            else:
                # Another error that's not just "would block" or "no data" 
                # so raise it
                raise
          time.sleep(0.1)
        global errorFlag
        errorFlag = 1
        
          
        
        
        
            
    
    t = threading.Thread(target=start)
    if errorFlag == 0:
      t.start()
      t.join()
  
      conn.Close()
    elif errorFlag == 1:
      conn.Close()
    
    
    if Set == None and errorFlag == 0:
    
        Result = api.resp_parse(bytes(resultBytes))
        #Value = vars(Result[variable])
        #parsedResult = api.enum_SGPO_SetError(Result['e__SGPO_SetError__Err'])
        #outInt = Value['value']
        #output = api.enum_SGPO_SetError.ValuesDict.get(outInt)
        
        
        # Assume response_obj is the object you want to inspect
    
        
    
        #print(resultBytes)
        
        
        
        
        return(Result)
      
    else:
      return()

