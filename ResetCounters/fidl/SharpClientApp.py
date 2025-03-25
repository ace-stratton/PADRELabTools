# ********************************************************************************************
# * @file SharpClientApp.py
# * @brief MAC FP client Python implementation generator
# ********************************************************************************************
# * @version           interface Sharp v0.4
# *
# * @copyright         (C) Copyright EnduroSat
# *
# *                    Contents and presentations are protected world-wide.
# *                    Any kind of using, copying etc. is prohibited without prior permission.
# *                    All rights - incl. industrial property rights - are reserved.
# *
# *-------------------------------------------------------------------------------------------
# * GENERATOR: org.endurosat.generators.macchiato.binders.Gen_Py v1.11
# *-------------------------------------------------------------------------------------------
# * !!! Please note that this code is fully GENERATED and shall not be manually modified as
# * all changes will be overwritten !!!
# ********************************************************************************************

from .SerDesHelpers import SerDesHelpers

class FP_API_SHARP:
    def __init__(self, rawSerDesSupport : bool = False):
        self.const_SHARP_PROTOCOL_ID = 105
        self.rawSerDesSupport = rawSerDesSupport
        self.versionMajor=0
        self.versionMinor=4


        #
        # Response parsers map
        #
        self.responseParsersDict = {}
        self.responseParsersDict[9] = self.resp_getRawSharpHK
        self.responseParsersDict[1] = self.resp_getHealthInfo
        self.responseParsersDict[2] = self.resp_getSHIPInfo
        self.responseParsersDict[3] = self.resp_setDetectorPower
        self.responseParsersDict[4] = self.resp_setSharpTime
        self.responseParsersDict[5] = self.resp_setSharpDate
        self.responseParsersDict[6] = self.resp_getSharpTimeDate
        self.responseParsersDict[7] = self.resp_getSharpMode
        self.responseParsersDict[8] = self.resp_setSharpMode

    class enum_DetectorStatus:
        DETECTORSTATUS_ON = 0
        DETECTORSTATUS_OFF = 1
        DETECTORSTATUS_ERROR = 2
    
        ValuesDict = {
            DETECTORSTATUS_ON : 'DETECTORSTATUS_ON', 
            DETECTORSTATUS_OFF : 'DETECTORSTATUS_OFF', 
            DETECTORSTATUS_ERROR : 'DETECTORSTATUS_ERROR'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.enum_DetectorStatus()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_SHARP.enum_DetectorStatus.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_SHARP.enum_DetectorStatus.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_DetectorPower:
        DETECTORPOWER_ON = 0
        DETECTORPOWER_OFF = 1
    
        ValuesDict = {
            DETECTORPOWER_ON : 'DETECTORPOWER_ON', 
            DETECTORPOWER_OFF : 'DETECTORPOWER_OFF'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.enum_DetectorPower()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_SHARP.enum_DetectorPower.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_SHARP.enum_DetectorPower.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_sErrorCodeSharp:
        def __init__(self, uint8__errorCode = 0):
            self.uint8__errorCode = uint8__errorCode
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__errorCode)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_sErrorCodeSharp()
    
            currentPos = pos
            
            (resultInstance.uint8__errorCode, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_sdate:
        def __init__(self, uint16__year = 0, uint8__mon = 0, uint8__day = 0):
            self.uint16__year = uint16__year
            self.uint8__mon = uint8__mon
            self.uint8__day = uint8__day
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__year)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__mon)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__day)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_sdate()
    
            currentPos = pos
            
            (resultInstance.uint16__year, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__mon, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__day, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 4
    
    class struct_stime:
        def __init__(self, uint8__hour = 0, uint8__min = 0, uint8__sec = 0, uint16__ms = 0, uint16__us = 0):
            self.uint8__hour = uint8__hour
            self.uint8__min = uint8__min
            self.uint8__sec = uint8__sec
            self.uint16__ms = uint16__ms
            self.uint16__us = uint16__us
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__hour)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__min)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__sec)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__ms)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__us)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_stime()
    
            currentPos = pos
            
            (resultInstance.uint8__hour, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__min, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__sec, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__ms, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__us, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 7
    
    class struct_sfaultstateSharp:
        def __init__(self, bool__faultflag = False, uint8__faultcount = 0):
            self.bool__faultflag = bool__faultflag
            self.uint8__faultcount = uint8__faultcount
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__faultflag)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__faultcount)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_sfaultstateSharp()
    
            currentPos = pos
            
            (resultInstance.bool__faultflag, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__faultcount, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 2
    
    class struct_sDetectorTemps:
        def __init__(self, uint32__temp1 = 0, uint32__temp2 = 0, uint32__temp3 = 0, uint32__temp4 = 0, uint32__temp5 = 0, uint32__temp6 = 0, uint32__temp7 = 0, uint32__temp8 = 0):
            self.uint32__temp1 = uint32__temp1
            self.uint32__temp2 = uint32__temp2
            self.uint32__temp3 = uint32__temp3
            self.uint32__temp4 = uint32__temp4
            self.uint32__temp5 = uint32__temp5
            self.uint32__temp6 = uint32__temp6
            self.uint32__temp7 = uint32__temp7
            self.uint32__temp8 = uint32__temp8
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__temp1)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__temp2)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__temp3)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__temp4)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__temp5)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__temp6)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__temp7)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__temp8)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_sDetectorTemps()
    
            currentPos = pos
            
            (resultInstance.uint32__temp1, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__temp2, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__temp3, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__temp4, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__temp5, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__temp6, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__temp7, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__temp8, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 32
    
    class struct_sDetectorVoltages:
        def __init__(self, uint32__volt1 = 0, uint32__volt2 = 0, uint32__volt3 = 0, uint32__volt4 = 0, uint32__volt5 = 0, uint32__volt6 = 0, uint32__volt7 = 0, uint32__volt8 = 0):
            self.uint32__volt1 = uint32__volt1
            self.uint32__volt2 = uint32__volt2
            self.uint32__volt3 = uint32__volt3
            self.uint32__volt4 = uint32__volt4
            self.uint32__volt5 = uint32__volt5
            self.uint32__volt6 = uint32__volt6
            self.uint32__volt7 = uint32__volt7
            self.uint32__volt8 = uint32__volt8
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__volt1)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__volt2)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__volt3)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__volt4)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__volt5)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__volt6)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__volt7)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__volt8)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_sDetectorVoltages()
    
            currentPos = pos
            
            (resultInstance.uint32__volt1, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__volt2, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__volt3, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__volt4, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__volt5, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__volt6, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__volt7, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__volt8, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 32
    
    class struct_sDetectorStatus:
        def __init__(self, e__DetectorStatus__status1 = 0, e__DetectorStatus__status2 = 0, e__DetectorStatus__status3 = 0, e__DetectorStatus__status4 = 0, e__DetectorStatus__status5 = 0, e__DetectorStatus__status6 = 0, e__DetectorStatus__status7 = 0, e__DetectorStatus__status8 = 0):
            self.e__DetectorStatus__status1 = e__DetectorStatus__status1
            self.e__DetectorStatus__status2 = e__DetectorStatus__status2
            self.e__DetectorStatus__status3 = e__DetectorStatus__status3
            self.e__DetectorStatus__status4 = e__DetectorStatus__status4
            self.e__DetectorStatus__status5 = e__DetectorStatus__status5
            self.e__DetectorStatus__status6 = e__DetectorStatus__status6
            self.e__DetectorStatus__status7 = e__DetectorStatus__status7
            self.e__DetectorStatus__status8 = e__DetectorStatus__status8
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_SHARP.enum_DetectorStatus(self.e__DetectorStatus__status1).serialize()
            
            result += FP_API_SHARP.enum_DetectorStatus(self.e__DetectorStatus__status2).serialize()
            
            result += FP_API_SHARP.enum_DetectorStatus(self.e__DetectorStatus__status3).serialize()
            
            result += FP_API_SHARP.enum_DetectorStatus(self.e__DetectorStatus__status4).serialize()
            
            result += FP_API_SHARP.enum_DetectorStatus(self.e__DetectorStatus__status5).serialize()
            
            result += FP_API_SHARP.enum_DetectorStatus(self.e__DetectorStatus__status6).serialize()
            
            result += FP_API_SHARP.enum_DetectorStatus(self.e__DetectorStatus__status7).serialize()
            
            result += FP_API_SHARP.enum_DetectorStatus(self.e__DetectorStatus__status8).serialize()
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_sDetectorStatus()
    
            currentPos = pos
            
            (resultInstance.e__DetectorStatus__status1, bytesProcessed) = FP_API_SHARP.enum_DetectorStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__DetectorStatus__status2, bytesProcessed) = FP_API_SHARP.enum_DetectorStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__DetectorStatus__status3, bytesProcessed) = FP_API_SHARP.enum_DetectorStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__DetectorStatus__status4, bytesProcessed) = FP_API_SHARP.enum_DetectorStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__DetectorStatus__status5, bytesProcessed) = FP_API_SHARP.enum_DetectorStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__DetectorStatus__status6, bytesProcessed) = FP_API_SHARP.enum_DetectorStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__DetectorStatus__status7, bytesProcessed) = FP_API_SHARP.enum_DetectorStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__DetectorStatus__status8, bytesProcessed) = FP_API_SHARP.enum_DetectorStatus.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 8
    
    class struct_sSHIPVersion:
        def __init__(self, uint16__firmwareMajor = 0, uint16__firmwareMinor = 0, uint16__softwareMajor = 0, uint16__softwareMinor = 0):
            self.uint16__firmwareMajor = uint16__firmwareMajor
            self.uint16__firmwareMinor = uint16__firmwareMinor
            self.uint16__softwareMajor = uint16__softwareMajor
            self.uint16__softwareMinor = uint16__softwareMinor
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__firmwareMajor)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__firmwareMinor)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__softwareMajor)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__softwareMinor)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_sSHIPVersion()
    
            currentPos = pos
            
            (resultInstance.uint16__firmwareMajor, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__firmwareMinor, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__softwareMajor, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__softwareMinor, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 8
    
    class struct_sFPGAVersion:
        def __init__(self, uint16__fpgafirmwareMajor = 0, uint16__fpgafirmwareMinor = 0):
            self.uint16__fpgafirmwareMajor = uint16__fpgafirmwareMajor
            self.uint16__fpgafirmwareMinor = uint16__fpgafirmwareMinor
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__fpgafirmwareMajor)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__fpgafirmwareMinor)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_sFPGAVersion()
    
            currentPos = pos
            
            (resultInstance.uint16__fpgafirmwareMajor, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__fpgafirmwareMinor, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 4
    
    class struct_sSHIPStorage:
        def __init__(self, uint32__usedShipSpace = 0, uint32__freeShipSpace = 0):
            self.uint32__usedShipSpace = uint32__usedShipSpace
            self.uint32__freeShipSpace = uint32__freeShipSpace
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__usedShipSpace)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__freeShipSpace)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_sSHIPStorage()
    
            currentPos = pos
            
            (resultInstance.uint32__usedShipSpace, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__freeShipSpace, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 8
    
    class struct_sSHIPPower:
        def __init__(self, uint32__voltageShip = 0, uint32__currentShip = 0):
            self.uint32__voltageShip = uint32__voltageShip
            self.uint32__currentShip = uint32__currentShip
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__voltageShip)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__currentShip)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_sSHIPPower()
    
            currentPos = pos
            
            (resultInstance.uint32__voltageShip, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__currentShip, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 8
    
    class enum_eCommandExecutionReturn:
        ECOMMANDEXECUTIONRETURN_SUCCESS = 0
        ECOMMANDEXECUTIONRETURN_FAIL = 1
    
        ValuesDict = {
            ECOMMANDEXECUTIONRETURN_SUCCESS : 'ECOMMANDEXECUTIONRETURN_SUCCESS', 
            ECOMMANDEXECUTIONRETURN_FAIL : 'ECOMMANDEXECUTIONRETURN_FAIL'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.enum_eCommandExecutionReturn()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_SHARP.enum_eCommandExecutionReturn.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_SHARP.enum_eCommandExecutionReturn.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_eSHARPModes:
        ESHARPMODES_SHARP_IDLE_MODE = 0
        ESHARPMODES_SHARP_LOW_POWER_MODE = 1
        ESHARPMODES_SHARP_ENGINEERING_MODE = 2
        ESHARPMODES_SHARP_NOMINAL_SCIENCE_MODE = 3
        ESHARPMODES_SHARP_FAST_READOUT_SCIENCE_MODE = 4
        ESHARPMODES_SHARP_SAFE_MODE = 5
        ESHARPMODES_SHARP_STATE_MACHINE_OFF = 6
        ESHARPMODES_SHARP_STATE_MACHINE_ON = 7
    
        ValuesDict = {
            ESHARPMODES_SHARP_IDLE_MODE : 'ESHARPMODES_SHARP_IDLE_MODE', 
            ESHARPMODES_SHARP_LOW_POWER_MODE : 'ESHARPMODES_SHARP_LOW_POWER_MODE', 
            ESHARPMODES_SHARP_ENGINEERING_MODE : 'ESHARPMODES_SHARP_ENGINEERING_MODE', 
            ESHARPMODES_SHARP_NOMINAL_SCIENCE_MODE : 'ESHARPMODES_SHARP_NOMINAL_SCIENCE_MODE', 
            ESHARPMODES_SHARP_FAST_READOUT_SCIENCE_MODE : 'ESHARPMODES_SHARP_FAST_READOUT_SCIENCE_MODE', 
            ESHARPMODES_SHARP_SAFE_MODE : 'ESHARPMODES_SHARP_SAFE_MODE', 
            ESHARPMODES_SHARP_STATE_MACHINE_OFF : 'ESHARPMODES_SHARP_STATE_MACHINE_OFF', 
            ESHARPMODES_SHARP_STATE_MACHINE_ON : 'ESHARPMODES_SHARP_STATE_MACHINE_ON'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.enum_eSHARPModes()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_SHARP.enum_eSHARPModes.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_SHARP.enum_eSHARPModes.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_eTelemetryStatus:
        ETELEMETRYSTATUS_GOOD = 0
        ETELEMETRYSTATUS_OLD = 1
    
        ValuesDict = {
            ETELEMETRYSTATUS_GOOD : 'ETELEMETRYSTATUS_GOOD', 
            ETELEMETRYSTATUS_OLD : 'ETELEMETRYSTATUS_OLD'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.enum_eTelemetryStatus()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_SHARP.enum_eTelemetryStatus.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_SHARP.enum_eTelemetryStatus.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_sRawTelemetry:
        def __init__(self, uint16__apID = 0, uint16__sequenceCount = 0, uint16__packetNumBytes = 0, uint32__timeTelemetryRaw = 0, a__uint8__32__dataArray = []):
            self.uint16__apID = uint16__apID
            self.uint16__sequenceCount = uint16__sequenceCount
            self.uint16__packetNumBytes = uint16__packetNumBytes
            self.uint32__timeTelemetryRaw = uint32__timeTelemetryRaw
            self.a__uint8__32__dataArray = a__uint8__32__dataArray
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__apID)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__sequenceCount)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__packetNumBytes)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__timeTelemetryRaw)
            actualLen = len(self.a__uint8__32__dataArray)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__32__dataArray, 32)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_SHARP.struct_sRawTelemetry()
    
            currentPos = pos
            
            (resultInstance.uint16__apID, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__sequenceCount, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__packetNumBytes, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__timeTelemetryRaw, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__32__dataArray, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 32)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 42
    

    ############################################################################################################
    """
    Request function for FIDL method: getRawSharpHK
        - function ID: 00000009
        - description: Pulls the raw telemetry from SHARP
    """
    def req_getRawSharpHK(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_SHARP_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000009
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000009, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getRawSharpHK
        - function ID: 00000009
        - description: Pulls the raw telemetry from SHARP
    """
    def resp_getRawSharpHK(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_SHARP_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000009):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_SHARP.enum_eTelemetryStatus.deserialize(data, currentPos)
        responseInstance["e__eTelemetryStatus__telemetryStatus"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sRawTelemetry.deserialize(data, currentPos)
        responseInstance["s__rawTelemetry"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getHealthInfo
        - function ID: 00000001
        - description: Pulls health info of SHARP Instrument
    """
    def req_getHealthInfo(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_SHARP_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000001
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000001, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getHealthInfo
        - function ID: 00000001
        - description: Pulls health info of SHARP Instrument
    """
    def resp_getHealthInfo(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_SHARP_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000001):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_SHARP.struct_sdate.deserialize(data, currentPos)
        responseInstance["s__date"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_stime.deserialize(data, currentPos)
        responseInstance["s__time"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sfaultstateSharp.deserialize(data, currentPos)
        responseInstance["s__faults"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sDetectorTemps.deserialize(data, currentPos)
        responseInstance["s__temperatures"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sDetectorVoltages.deserialize(data, currentPos)
        responseInstance["s__voltages"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sDetectorStatus.deserialize(data, currentPos)
        responseInstance["s__detectorStatus"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getSHIPInfo
        - function ID: 00000002
        - description: Pulls SHIP Info
    """
    def req_getSHIPInfo(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_SHARP_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000002
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000002, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getSHIPInfo
        - function ID: 00000002
        - description: Pulls SHIP Info
    """
    def resp_getSHIPInfo(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_SHARP_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000002):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_SHARP.struct_sSHIPVersion.deserialize(data, currentPos)
        responseInstance["s__versioning"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sFPGAVersion.deserialize(data, currentPos)
        responseInstance["s__fpga_versioning"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sSHIPStorage.deserialize(data, currentPos)
        responseInstance["s__shipStorage"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sSHIPPower.deserialize(data, currentPos)
        responseInstance["s__shipPower"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setDetectorPower
        - function ID: 00000003
        - description: Turns on and off individual detectors
    """
    def req_setDetectorPower(self, uint32__detectorID, e__DetectorPower__onOff):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_SHARP_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000003
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint32", uint32__detectorID)
        requestBytes += FP_API_SHARP.enum_DetectorPower(e__DetectorPower__onOff).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000003, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setDetectorPower
        - function ID: 00000003
        - description: Turns on and off individual detectors
    """
    def resp_setDetectorPower(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_SHARP_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000003):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_SHARP.enum_DetectorPower.deserialize(data, currentPos)
        responseInstance["e__DetectorPower__opResult"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sErrorCodeSharp.deserialize(data, currentPos)
        responseInstance["s__ErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sDetectorStatus.deserialize(data, currentPos)
        responseInstance["s__detectorStatus"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setSharpTime
        - function ID: 00000004
        - description: Sets SHARP time using GNSS or Manual
    """
    def req_setSharpTime(self, bool__GNSS, s__time):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_SHARP_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000004
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", bool__GNSS)
        requestBytes += s__time.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000004, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setSharpTime
        - function ID: 00000004
        - description: Sets SHARP time using GNSS or Manual
    """
    def resp_setSharpTime(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_SHARP_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000004):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_SHARP.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__executionSuccess"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sErrorCodeSharp.deserialize(data, currentPos)
        responseInstance["s__ErrorCode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setSharpDate
        - function ID: 00000005
        - description: Sets SHARP date using GNSS or manual
    """
    def req_setSharpDate(self, bool__GNSS, s__date):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_SHARP_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000005
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", bool__GNSS)
        requestBytes += s__date.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000005, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setSharpDate
        - function ID: 00000005
        - description: Sets SHARP date using GNSS or manual
    """
    def resp_setSharpDate(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_SHARP_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000005):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_SHARP.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__executionSuccess"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sErrorCodeSharp.deserialize(data, currentPos)
        responseInstance["s__ErrorCode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getSharpTimeDate
        - function ID: 00000006
        - description: Gets current date and time of SHARP
    """
    def req_getSharpTimeDate(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_SHARP_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000006
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000006, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getSharpTimeDate
        - function ID: 00000006
        - description: Gets current date and time of SHARP
    """
    def resp_getSharpTimeDate(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_SHARP_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000006):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_SHARP.struct_stime.deserialize(data, currentPos)
        responseInstance["s__time"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sdate.deserialize(data, currentPos)
        responseInstance["s__date"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getSharpMode
        - function ID: 00000007
        - description: Gets current mode of SHARP
    """
    def req_getSharpMode(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_SHARP_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000007
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000007, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getSharpMode
        - function ID: 00000007
        - description: Gets current mode of SHARP
    """
    def resp_getSharpMode(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_SHARP_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000007):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_SHARP.enum_eSHARPModes.deserialize(data, currentPos)
        responseInstance["e__eSHARPModes__mode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setSharpMode
        - function ID: 00000008
        - description: Sets current mode of SHARP
    """
    def req_setSharpMode(self, e__eSHARPModes__mode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_SHARP_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000008
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_SHARP.enum_eSHARPModes(e__eSHARPModes__mode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000008, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setSharpMode
        - function ID: 00000008
        - description: Sets current mode of SHARP
    """
    def resp_setSharpMode(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_SHARP_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000008):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_SHARP.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.struct_sErrorCodeSharp.deserialize(data, currentPos)
        responseInstance["s__ErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_SHARP.enum_eSHARPModes.deserialize(data, currentPos)
        responseInstance["e__eSHARPModes__mode"] = field
        currentPos += bytesProcessed
    
        return responseInstance


    ############################################################################################################
    """
    Deserializes the provided bytearray and returns a dictionary of parsed values for the response;
    functionId parameter shall be supplied if the class is used in rawSerDesSupport mode, otherwise
    it is extracted from the FP header
    """
    def resp_parse(self, respBytes, functionId : int = 0):
        if not self.rawSerDesSupport:
            # try to parse FunctionProtocol header
            (fpHeaderInstance, bytesProcessed) = SerDesHelpers.struct_FPHeader.deserialize(respBytes, 0)
            funcId = fpHeaderInstance.u32FuncId

            if fpHeaderInstance.u16ProtoId != self.const_SHARP_PROTOCOL_ID:
                raise Exception("Unsupported protocol ID", fpHeaderInstance.u16ProtoId)
        else:
            funcId = functionId

        if funcId in self.responseParsersDict:
            respParserFunc = self.responseParsersDict[funcId]
            return respParserFunc(respBytes) if respParserFunc is not None else None
        else:
            raise Exception('Unsupported function id', hex(funcId))
    ############################################################################################################
    """
    Returns the Protocol version as a string vM.m
    """
    def get_version(self):
        return f'v{self.versionMajor}.{self.versionMinor}'
    ############################################################################################################

