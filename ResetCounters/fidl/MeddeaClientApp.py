# ********************************************************************************************
# * @file MeddeaClientApp.py
# * @brief MAC FP client Python implementation generator
# ********************************************************************************************
# * @version           interface Meddea v1.2
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

from SerDesHelpers import SerDesHelpers

class FP_API_MEDDEA:
    def __init__(self, rawSerDesSupport : bool = False):
        self.const_MEDDEA_PROTOCOL_ID = 106
        self.rawSerDesSupport = rawSerDesSupport
        self.versionMajor=1
        self.versionMinor=2


        #
        # Response parsers map
        #
        self.responseParsersDict = {}
        self.responseParsersDict[1] = self.resp_getMEDDEAMode
        self.responseParsersDict[2] = self.resp_setMEDDEAMode
        self.responseParsersDict[3] = self.resp_registerWriteMEDDEA
        self.responseParsersDict[4] = self.resp_registerReadMEDDEA
        self.responseParsersDict[5] = self.resp_houseKeepingMEDDEA
        self.responseParsersDict[6] = self.resp_sendRawCCSDS_MEDDEA
        self.responseParsersDict[7] = self.resp_setMEDDEAConfigCommands
        self.responseParsersDict[8] = self.resp_getMEDDEAConfigCommands
        self.responseParsersDict[9] = self.resp_clearMEDDEAConfigCommands
        self.responseParsersDict[16] = self.resp_changeMEDDEAConfig
        self.responseParsersDict[17] = self.resp_getMEDDEAConfig
        self.responseParsersDict[18] = self.resp_selectSatelliteModel
        self.responseParsersDict[19] = self.resp_getSatelliteModel

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
            resultInstance = FP_API_MEDDEA.enum_eCommandExecutionReturn()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_MEDDEA.enum_eCommandExecutionReturn.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_MEDDEA.enum_eCommandExecutionReturn.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_eMEDDEAModes:
        EMEDDEAMODES_MEDDEA_OFF_MODE = 0
        EMEDDEAMODES_MEDDEA_SAFE_MODE = 1
        EMEDDEAMODES_MEDDEA_IDLE_MODE = 2
        EMEDDEAMODES_MEDDEA_DEPOLARIZATION_MODE = 3
        EMEDDEAMODES_MEDDEA_SCIENCE_MODE = 4
        EMEDDEAMODES_MEDDEA_SAFE_IN_PROGRESS = 5
        EMEDDEAMODES_MEDDEA_IDLE_IN_PROGRESS = 6
    
        ValuesDict = {
            EMEDDEAMODES_MEDDEA_OFF_MODE : 'EMEDDEAMODES_MEDDEA_OFF_MODE', 
            EMEDDEAMODES_MEDDEA_SAFE_MODE : 'EMEDDEAMODES_MEDDEA_SAFE_MODE', 
            EMEDDEAMODES_MEDDEA_IDLE_MODE : 'EMEDDEAMODES_MEDDEA_IDLE_MODE', 
            EMEDDEAMODES_MEDDEA_DEPOLARIZATION_MODE : 'EMEDDEAMODES_MEDDEA_DEPOLARIZATION_MODE', 
            EMEDDEAMODES_MEDDEA_SCIENCE_MODE : 'EMEDDEAMODES_MEDDEA_SCIENCE_MODE', 
            EMEDDEAMODES_MEDDEA_SAFE_IN_PROGRESS : 'EMEDDEAMODES_MEDDEA_SAFE_IN_PROGRESS', 
            EMEDDEAMODES_MEDDEA_IDLE_IN_PROGRESS : 'EMEDDEAMODES_MEDDEA_IDLE_IN_PROGRESS'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_MEDDEA.enum_eMEDDEAModes()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_MEDDEA.enum_eMEDDEAModes.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_MEDDEA.enum_eMEDDEAModes.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_eMEDDEAConfigurations:
        EMEDDEACONFIGURATIONS_DEFAULT = 0
        EMEDDEACONFIGURATIONS_X_CLASS_FLARE = 1
        EMEDDEACONFIGURATIONS_HIGH_SENSITIVITY = 2
    
        ValuesDict = {
            EMEDDEACONFIGURATIONS_DEFAULT : 'EMEDDEACONFIGURATIONS_DEFAULT', 
            EMEDDEACONFIGURATIONS_X_CLASS_FLARE : 'EMEDDEACONFIGURATIONS_X_CLASS_FLARE', 
            EMEDDEACONFIGURATIONS_HIGH_SENSITIVITY : 'EMEDDEACONFIGURATIONS_HIGH_SENSITIVITY'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_MEDDEA.enum_eMEDDEAConfigurations()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_MEDDEA.enum_eMEDDEAConfigurations.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_MEDDEA.enum_eMEDDEAConfigurations.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_eMEDDEAModels:
        EMEDDEAMODELS_FLIGHT = 0
        EMEDDEAMODELS_FLAT_SAT = 1
    
        ValuesDict = {
            EMEDDEAMODELS_FLIGHT : 'EMEDDEAMODELS_FLIGHT', 
            EMEDDEAMODELS_FLAT_SAT : 'EMEDDEAMODELS_FLAT_SAT'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_MEDDEA.enum_eMEDDEAModels()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_MEDDEA.enum_eMEDDEAModels.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_MEDDEA.enum_eMEDDEAModels.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_sWriteMEDDEA:
        def __init__(self, uint16__regID = 0, uint16__dataBytes = 0):
            self.uint16__regID = uint16__regID
            self.uint16__dataBytes = uint16__dataBytes
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__regID)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__dataBytes)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_MEDDEA.struct_sWriteMEDDEA()
    
            currentPos = pos
            
            (resultInstance.uint16__regID, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__dataBytes, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 4
    
    class struct_sReadResponsePacketMEDDEA:
        def __init__(self, uint16__regID = 0, uint16__dataBytes = 0):
            self.uint16__regID = uint16__regID
            self.uint16__dataBytes = uint16__dataBytes
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__regID)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__dataBytes)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_MEDDEA.struct_sReadResponsePacketMEDDEA()
    
            currentPos = pos
            
            (resultInstance.uint16__regID, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__dataBytes, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 4
    
    class struct_sHKPacketMEDDEA:
        def __init__(self, uint16__SequenceCount = 0, uint16__TimeStamp1 = 0, uint16__TimeStamp2 = 0, uint16__FPTemp = 0, uint16__DIBTemp = 0, uint16__HVTemp = 0, uint16__HVVolts = 0, uint16__HVCurrent = 0, uint16__Amps_1V5 = 0, uint16__Amps_3V3_D = 0, uint16__Amps_3V3_A = 0, uint16__phRate = 0, uint16__goodCmdCount = 0, uint16__errorCount = 0, uint16__heaterPWM = 0, uint16__heaterAccum = 0, uint16__sysError = 0):
            self.uint16__SequenceCount = uint16__SequenceCount
            self.uint16__TimeStamp1 = uint16__TimeStamp1
            self.uint16__TimeStamp2 = uint16__TimeStamp2
            self.uint16__FPTemp = uint16__FPTemp
            self.uint16__DIBTemp = uint16__DIBTemp
            self.uint16__HVTemp = uint16__HVTemp
            self.uint16__HVVolts = uint16__HVVolts
            self.uint16__HVCurrent = uint16__HVCurrent
            self.uint16__Amps_1V5 = uint16__Amps_1V5
            self.uint16__Amps_3V3_D = uint16__Amps_3V3_D
            self.uint16__Amps_3V3_A = uint16__Amps_3V3_A
            self.uint16__phRate = uint16__phRate
            self.uint16__goodCmdCount = uint16__goodCmdCount
            self.uint16__errorCount = uint16__errorCount
            self.uint16__heaterPWM = uint16__heaterPWM
            self.uint16__heaterAccum = uint16__heaterAccum
            self.uint16__sysError = uint16__sysError
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__SequenceCount)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__TimeStamp1)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__TimeStamp2)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__FPTemp)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__DIBTemp)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__HVTemp)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__HVVolts)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__HVCurrent)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__Amps_1V5)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__Amps_3V3_D)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__Amps_3V3_A)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__phRate)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__goodCmdCount)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__errorCount)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__heaterPWM)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__heaterAccum)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__sysError)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_MEDDEA.struct_sHKPacketMEDDEA()
    
            currentPos = pos
            
            (resultInstance.uint16__SequenceCount, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__TimeStamp1, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__TimeStamp2, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__FPTemp, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__DIBTemp, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__HVTemp, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__HVVolts, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__HVCurrent, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__Amps_1V5, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__Amps_3V3_D, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__Amps_3V3_A, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__phRate, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__goodCmdCount, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__errorCount, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__heaterPWM, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__heaterAccum, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__sysError, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 34
    

    ############################################################################################################
    """
    Request function for FIDL method: getMEDDEAMode
        - function ID: 00000001
        - description: Gets current mode of MEDDEA
    """
    def req_getMEDDEAMode(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
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
    Response function for FIDL method: getMEDDEAMode
        - function ID: 00000001
        - description: Gets current mode of MEDDEA
    """
    def resp_getMEDDEAMode(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000001):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eMEDDEAModes.deserialize(data, currentPos)
        responseInstance["e__eMEDDEAModes__currentMode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setMEDDEAMode
        - function ID: 00000002
        - description: Sets current mode of MEDDEA
    """
    def req_setMEDDEAMode(self, e__eMEDDEAModes__setMode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000002
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_MEDDEA.enum_eMEDDEAModes(e__eMEDDEAModes__setMode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000002, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setMEDDEAMode
        - function ID: 00000002
        - description: Sets current mode of MEDDEA
    """
    def resp_setMEDDEAMode(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000002):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eMEDDEAModes.deserialize(data, currentPos)
        responseInstance["e__eMEDDEAModes__currentMode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: registerWriteMEDDEA
        - function ID: 00000003
        - description: Writes to MeDDEA
    """
    def req_registerWriteMEDDEA(self, s__writeData):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000003
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__writeData.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000003, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: registerWriteMEDDEA
        - function ID: 00000003
        - description: Writes to MeDDEA
    """
    def resp_registerWriteMEDDEA(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000003):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: registerReadMEDDEA
        - function ID: 00000004
        - description: Reads from MeDDEA
    """
    def req_registerReadMEDDEA(self, uint16__regID):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000004
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint16", uint16__regID)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000004, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: registerReadMEDDEA
        - function ID: 00000004
        - description: Reads from MeDDEA
    """
    def resp_registerReadMEDDEA(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000004):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_MEDDEA.struct_sReadResponsePacketMEDDEA.deserialize(data, currentPos)
        responseInstance["s__ReadResponse"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: houseKeepingMEDDEA
        - function ID: 00000005
        - description: Displays most recent house keeping information from the data cache
    """
    def req_houseKeepingMEDDEA(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000005
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000005, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: houseKeepingMEDDEA
        - function ID: 00000005
        - description: Displays most recent house keeping information from the data cache
    """
    def resp_houseKeepingMEDDEA(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000005):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_MEDDEA.struct_sHKPacketMEDDEA.deserialize(data, currentPos)
        responseInstance["s__HouseKeepingReturn"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: sendRawCCSDS_MEDDEA
        - function ID: 00000006
        - description: Send raw ccsds packet
    """
    def req_sendRawCCSDS_MEDDEA(self, a__uint16__50__CCSDSData, uint8__CCSDSSize):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000006
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        actualLen = len(a__uint16__50__CCSDSData)
    
        if (actualLen > 50):
            raise Exception("The maximum expected size for array argument a__uint16__50__CCSDSData is 50 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basicArray.serialize("uint16", a__uint16__50__CCSDSData, 50)
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__CCSDSSize)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000006, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: sendRawCCSDS_MEDDEA
        - function ID: 00000006
        - description: Send raw ccsds packet
    """
    def resp_sendRawCCSDS_MEDDEA(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000006):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setMEDDEAConfigCommands
        - function ID: 00000007
        - description: Sets the list of commands for given configuration
    """
    def req_setMEDDEAConfigCommands(self, uint8__configSetASIC, e__eMEDDEAConfigurations__configSetSelection, a__uint16__29__configSetRegAddr, a__uint16__29__configSetDataVal, uint8__configSetSize):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000007
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__configSetASIC)
        requestBytes += FP_API_MEDDEA.enum_eMEDDEAConfigurations(e__eMEDDEAConfigurations__configSetSelection).serialize()
        actualLen = len(a__uint16__29__configSetRegAddr)
    
        if (actualLen > 29):
            raise Exception("The maximum expected size for array argument a__uint16__29__configSetRegAddr is 29 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basicArray.serialize("uint16", a__uint16__29__configSetRegAddr, 29)
        actualLen = len(a__uint16__29__configSetDataVal)
    
        if (actualLen > 29):
            raise Exception("The maximum expected size for array argument a__uint16__29__configSetDataVal is 29 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basicArray.serialize("uint16", a__uint16__29__configSetDataVal, 29)
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__configSetSize)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000007, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setMEDDEAConfigCommands
        - function ID: 00000007
        - description: Sets the list of commands for given configuration
    """
    def resp_setMEDDEAConfigCommands(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000007):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getMEDDEAConfigCommands
        - function ID: 00000008
        - description: Gets the list of commands for given configuration and ASIC
    """
    def req_getMEDDEAConfigCommands(self, uint8__configGetASIC, e__eMEDDEAConfigurations__configGetSelection):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000008
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__configGetASIC)
        requestBytes += FP_API_MEDDEA.enum_eMEDDEAConfigurations(e__eMEDDEAConfigurations__configGetSelection).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000008, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getMEDDEAConfigCommands
        - function ID: 00000008
        - description: Gets the list of commands for given configuration and ASIC
    """
    def resp_getMEDDEAConfigCommands(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000008):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basicArray.deserialize("uint16", data, currentPos, 29)
        responseInstance["a__uint16__29__configGetRegAddr"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basicArray.deserialize("uint16", data, currentPos, 29)
        responseInstance["a__uint16__29__configGetDataVal"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["uint8__configGetSize"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: clearMEDDEAConfigCommands
        - function ID: 00000009
        - description: Clears list of configuration commands back to none
    """
    def req_clearMEDDEAConfigCommands(self, uint8__configClearASIC, e__eMEDDEAConfigurations__configClearSelection):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000009
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__configClearASIC)
        requestBytes += FP_API_MEDDEA.enum_eMEDDEAConfigurations(e__eMEDDEAConfigurations__configClearSelection).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000009, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: clearMEDDEAConfigCommands
        - function ID: 00000009
        - description: Clears list of configuration commands back to none
    """
    def resp_clearMEDDEAConfigCommands(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000009):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: changeMEDDEAConfig
        - function ID: 00000010
        - description: (CAN ONLY BE DONE IN IDLE) Switches the configuration that MeDDEA is using, loads all 4 asics for given configuration
    """
    def req_changeMEDDEAConfig(self, e__eMEDDEAConfigurations__configSelection):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000010
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_MEDDEA.enum_eMEDDEAConfigurations(e__eMEDDEAConfigurations__configSelection).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000010, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: changeMEDDEAConfig
        - function ID: 00000010
        - description: (CAN ONLY BE DONE IN IDLE) Switches the configuration that MeDDEA is using, loads all 4 asics for given configuration
    """
    def resp_changeMEDDEAConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000010):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getMEDDEAConfig
        - function ID: 00000011
        - description: Gets the most recently applied MeDDEA config.
    """
    def req_getMEDDEAConfig(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000011
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000011, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getMEDDEAConfig
        - function ID: 00000011
        - description: Gets the most recently applied MeDDEA config.
    """
    def resp_getMEDDEAConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000011):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eMEDDEAConfigurations.deserialize(data, currentPos)
        responseInstance["e__eMEDDEAConfigurations__configReturn"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: selectSatelliteModel
        - function ID: 00000012
        - description: Sets whether you are operating the FlatSat or the Flight Sat.
    """
    def req_selectSatelliteModel(self, e__eMEDDEAModels__modelSelection):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000012
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_MEDDEA.enum_eMEDDEAModels(e__eMEDDEAModels__modelSelection).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000012, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: selectSatelliteModel
        - function ID: 00000012
        - description: Sets whether you are operating the FlatSat or the Flight Sat.
    """
    def resp_selectSatelliteModel(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000012):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eMEDDEAModels.deserialize(data, currentPos)
        responseInstance["e__eMEDDEAModels__modelReturn"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getSatelliteModel
        - function ID: 00000013
        - description: Gets which model of MeDDEA you are operating the FlatSat or the Flight Sat.
    """
    def req_getSatelliteModel(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_MEDDEA_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000013
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000013, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getSatelliteModel
        - function ID: 00000013
        - description: Gets which model of MeDDEA you are operating the FlatSat or the Flight Sat.
    """
    def resp_getSatelliteModel(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000013):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eCommandExecutionReturn.deserialize(data, currentPos)
        responseInstance["e__eCommandExecutionReturn__opResult"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_MEDDEA.enum_eMEDDEAModels.deserialize(data, currentPos)
        responseInstance["e__eMEDDEAModels__modelReturn"] = field
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

            if fpHeaderInstance.u16ProtoId != self.const_MEDDEA_PROTOCOL_ID:
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

