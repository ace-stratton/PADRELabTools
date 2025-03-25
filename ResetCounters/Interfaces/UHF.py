# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 15:22:42 2025

@author: Ace

Module to run UHF commanding
"""

import sys, os
current_dir = os.getcwd()
fidl_path = os.path.abspath(os.path.join(current_dir, "..", "fidl"))
sys.path.insert(0, fidl_path)
from UHFClientApp import FP_API_UHF
import Interface


api = FP_API_UHF()
moduleMac = 17


def getUptime():
  payloadBytes = api.req_ReadUpTime()
  Result = Interface.getReturn(payloadBytes, moduleMac, api)
  parsed = vars(Result['s__UpTime'])
  result = parsed['uint32__u32UpTime']
  return result