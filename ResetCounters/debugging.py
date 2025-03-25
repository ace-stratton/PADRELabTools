# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 17:22:35 2025

@author: user
"""

import os, sys
from datetime import datetime

current_dir = os.getcwd()
fidl_path = os.path.abspath(os.path.join(current_dir, ".", "fidl"))
sys.path.insert(0, fidl_path)

interfaces_path = os.path.abspath(os.path.join(current_dir, ".", "Interfaces"))
sys.path.insert(0, interfaces_path)

import getResetCounters

print(getResetCounters.getResetCounters())
