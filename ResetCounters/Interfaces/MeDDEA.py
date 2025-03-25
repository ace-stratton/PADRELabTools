# -*- coding: utf-8 -*-chrome://vivaldi-webui/startpage?section=Speed-dials&background-color=#110d0b
"""
Created on Wed Mar 12 14:51:41 2025

@author: Ace
"""

import sys, os
current_dir = os.getcwd()
fidl_path = os.path.abspath(os.path.join(current_dir, "..", "fidl"))
sys.path.insert(0, fidl_path)
from MeddeaClientApp import FP_API_MEDDEA
import Interface



api = FP_API_MEDDEA()
moduleMac = 51


def getHouseKeeping():
    payloadBytes = api.req_houseKeepingMEDDEA()
    Response = Interface.getReturn(payloadBytes, moduleMac, api)
    ParsedResult = vars(Response['s__HouseKeepingReturn'])
    values_list = list(ParsedResult.values())
    
    for x, val in Calibration.items():
      original = values_list[x]
      newVal = Translate(original, x)
      values_list[x] =float(newVal)
    return(values_list)
  
import numpy as np



Calibration = {
    #fp_temp
    3: [
        -7.09802295e-13,
         7.66830550e-08,
        -3.75100311e-03,
         4.76443005e+01
    ],
    #dib_temp
    4: [
        -2.30984324147617e-12,
         2.19923164121208e-07,
        -8.0360785693563e-03,
         1.38564006682943e+02
    ],
    #hvps_temp
    5: [
        -2.09989019049292e-12,
         1.99856414598901e-07,
        -7.3346158267138e-03,
         1.03967411298627e+02
    ],
    #hvps_vsense
    6: [
        -0.0101,
         1.291
    ],
    #hvps_csense
    7: [
         1.6914e-04,
        -4.1556e-03
    ],
    #"csense_15v"
    8: [
        -0.010776,
         446.17
    ],
    #"csense_33vd"
    9: [
        -0.010776,
         446.17
    ],
    #"csense_33va"
    10: [
        -0.010776,
         446.17
    ],
    #"heater_pwm_duty_cycle"
    14: [
         0.0016,
         0
    ]
}


def Translate(x, name):

    constants = Calibration.get(name, None)

    p = np.poly1d(constants)

    return(p(x))

