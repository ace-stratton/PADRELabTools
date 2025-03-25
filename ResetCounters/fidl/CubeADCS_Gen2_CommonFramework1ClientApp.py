# ********************************************************************************************
# * @file CubeADCS_Gen2_CommonFramework1ClientApp.py
# * @brief MAC FP client Python implementation generator
# ********************************************************************************************
# * @version           interface CubeADCS_Gen2_CommonFramework1 v6.0
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

class FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1:
    def __init__(self, rawSerDesSupport : bool = False):
        self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID = 300
        self.rawSerDesSupport = rawSerDesSupport
        self.versionMajor=6
        self.versionMinor=0


        #
        # Response parsers map
        #
        self.responseParsersDict = {}
        self.responseParsersDict[0] = self.resp_setReset
        self.responseParsersDict[1] = self.resp_setUnixTime
        self.responseParsersDict[2] = self.resp_setErrorLogIndex
        self.responseParsersDict[3] = self.resp_setErrorLogEntry
        self.responseParsersDict[4] = self.resp_setErrorLogClear
        self.responseParsersDict[5] = self.resp_setErrorLogSettings
        self.responseParsersDict[6] = self.resp_setConfigPersist
        self.responseParsersDict[7] = self.resp_getIdentification
        self.responseParsersDict[8] = self.resp_getSerialNumber
        self.responseParsersDict[9] = self.resp_getErrorLogIndex
        self.responseParsersDict[10] = self.resp_getErrorLogEntry
        self.responseParsersDict[11] = self.resp_getErrorLogSettings
        self.responseParsersDict[12] = self.resp_getUnixTime
        self.responseParsersDict[13] = self.resp_getConfigPersistDiagnostics
        self.responseParsersDict[14] = self.resp_getCommsStatus
        self.responseParsersDict[15] = self.resp_getVersion
        self.responseParsersDict[16] = self.resp_getBootStatus
        self.responseParsersDict[17] = self.resp_getTelecommandAcknowledge
        self.responseParsersDict[18] = self.resp_getCommonErrorCodes
        self.responseParsersDict[19] = self.resp_getIdentification2

    class enum_CmdTargetNode:
        CMDTARGETNODE_NODEINVALID = 0
        CMDTARGETNODE_NODECOMPUTER = 1
        CMDTARGETNODE_NODESTR0 = 2
        CMDTARGETNODE_NODESTR1 = 3
        CMDTARGETNODE_NODEFSS0 = 4
        CMDTARGETNODE_NODEFSS1 = 5
        CMDTARGETNODE_NODEFSS2 = 6
        CMDTARGETNODE_NODEFSS3 = 7
        CMDTARGETNODE_NODEHSS0 = 8
        CMDTARGETNODE_NODEHSS1 = 9
        CMDTARGETNODE_NODEMAG0 = 10
        CMDTARGETNODE_NODEMAG1 = 11
        CMDTARGETNODE_NODERWL0 = 14
        CMDTARGETNODE_NODERWL1 = 15
        CMDTARGETNODE_NODERWL2 = 16
        CMDTARGETNODE_NODERWL3 = 17
        CMDTARGETNODE_NODERWL4 = 18
    
        ValuesDict = {
            CMDTARGETNODE_NODEINVALID : 'CMDTARGETNODE_NODEINVALID', 
            CMDTARGETNODE_NODECOMPUTER : 'CMDTARGETNODE_NODECOMPUTER', 
            CMDTARGETNODE_NODESTR0 : 'CMDTARGETNODE_NODESTR0', 
            CMDTARGETNODE_NODESTR1 : 'CMDTARGETNODE_NODESTR1', 
            CMDTARGETNODE_NODEFSS0 : 'CMDTARGETNODE_NODEFSS0', 
            CMDTARGETNODE_NODEFSS1 : 'CMDTARGETNODE_NODEFSS1', 
            CMDTARGETNODE_NODEFSS2 : 'CMDTARGETNODE_NODEFSS2', 
            CMDTARGETNODE_NODEFSS3 : 'CMDTARGETNODE_NODEFSS3', 
            CMDTARGETNODE_NODEHSS0 : 'CMDTARGETNODE_NODEHSS0', 
            CMDTARGETNODE_NODEHSS1 : 'CMDTARGETNODE_NODEHSS1', 
            CMDTARGETNODE_NODEMAG0 : 'CMDTARGETNODE_NODEMAG0', 
            CMDTARGETNODE_NODEMAG1 : 'CMDTARGETNODE_NODEMAG1', 
            CMDTARGETNODE_NODERWL0 : 'CMDTARGETNODE_NODERWL0', 
            CMDTARGETNODE_NODERWL1 : 'CMDTARGETNODE_NODERWL1', 
            CMDTARGETNODE_NODERWL2 : 'CMDTARGETNODE_NODERWL2', 
            CMDTARGETNODE_NODERWL3 : 'CMDTARGETNODE_NODERWL3', 
            CMDTARGETNODE_NODERWL4 : 'CMDTARGETNODE_NODERWL4'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFramework1_ErrorLogSearch:
        COMMONFRAMEWORK1_ERRORLOGSEARCH_REFERENCEHEAD = 0
        COMMONFRAMEWORK1_ERRORLOGSEARCH_REFERENCETAIL = 1
    
        ValuesDict = {
            COMMONFRAMEWORK1_ERRORLOGSEARCH_REFERENCEHEAD : 'COMMONFRAMEWORK1_ERRORLOGSEARCH_REFERENCEHEAD', 
            COMMONFRAMEWORK1_ERRORLOGSEARCH_REFERENCETAIL : 'COMMONFRAMEWORK1_ERRORLOGSEARCH_REFERENCETAIL'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ErrorLogSearch()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ErrorLogSearch.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ErrorLogSearch.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFramework1_ActiveState:
        COMMONFRAMEWORK1_ACTIVESTATE_DISABLED = 0
        COMMONFRAMEWORK1_ACTIVESTATE_ENABLED = 1
    
        ValuesDict = {
            COMMONFRAMEWORK1_ACTIVESTATE_DISABLED : 'COMMONFRAMEWORK1_ACTIVESTATE_DISABLED', 
            COMMONFRAMEWORK1_ACTIVESTATE_ENABLED : 'COMMONFRAMEWORK1_ACTIVESTATE_ENABLED'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ActiveState()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ActiveState.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ActiveState.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFramework1_BufferFullAction:
        COMMONFRAMEWORK1_BUFFERFULLACTION_IGNORE = 0
        COMMONFRAMEWORK1_BUFFERFULLACTION_ERASE = 1
    
        ValuesDict = {
            COMMONFRAMEWORK1_BUFFERFULLACTION_IGNORE : 'COMMONFRAMEWORK1_BUFFERFULLACTION_IGNORE', 
            COMMONFRAMEWORK1_BUFFERFULLACTION_ERASE : 'COMMONFRAMEWORK1_BUFFERFULLACTION_ERASE'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BufferFullAction()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BufferFullAction.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BufferFullAction.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFramework1_ResetVal:
        COMMONFRAMEWORK1_RESETVAL_DONOTHING = 0
        COMMONFRAMEWORK1_RESETVAL_SOFT = 55
        COMMONFRAMEWORK1_RESETVAL_HARD = 66
    
        ValuesDict = {
            COMMONFRAMEWORK1_RESETVAL_DONOTHING : 'COMMONFRAMEWORK1_RESETVAL_DONOTHING', 
            COMMONFRAMEWORK1_RESETVAL_SOFT : 'COMMONFRAMEWORK1_RESETVAL_SOFT', 
            COMMONFRAMEWORK1_RESETVAL_HARD : 'COMMONFRAMEWORK1_RESETVAL_HARD'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ResetVal()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ResetVal.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ResetVal.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFramework1_ConfigPersistState:
        COMMONFRAMEWORK1_CONFIGPERSISTSTATE_CONFIGPERSISTIDLE = 0
        COMMONFRAMEWORK1_CONFIGPERSISTSTATE_CONFIGPERSISTBUSY = 1
    
        ValuesDict = {
            COMMONFRAMEWORK1_CONFIGPERSISTSTATE_CONFIGPERSISTIDLE : 'COMMONFRAMEWORK1_CONFIGPERSISTSTATE_CONFIGPERSISTIDLE', 
            COMMONFRAMEWORK1_CONFIGPERSISTSTATE_CONFIGPERSISTBUSY : 'COMMONFRAMEWORK1_CONFIGPERSISTSTATE_CONFIGPERSISTBUSY'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ConfigPersistState()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ConfigPersistState.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ConfigPersistState.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFramework1_ConfigPersistResult:
        COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTNONE = 0
        COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTSUCCESS = 1
        COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTERRORPARAMLOCK = 2
        COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTERRORFLASH = 3
    
        ValuesDict = {
            COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTNONE : 'COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTNONE', 
            COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTSUCCESS : 'COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTSUCCESS', 
            COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTERRORPARAMLOCK : 'COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTERRORPARAMLOCK', 
            COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTERRORFLASH : 'COMMONFRAMEWORK1_CONFIGPERSISTRESULT_CONFIGPERSISTERRORFLASH'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ConfigPersistResult()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ConfigPersistResult.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ConfigPersistResult.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFramework1_GitBranch:
        COMMONFRAMEWORK1_GITBRANCH_MASTER = 0
        COMMONFRAMEWORK1_GITBRANCH_RELEASE = 1
        COMMONFRAMEWORK1_GITBRANCH_OTHER = 2
    
        ValuesDict = {
            COMMONFRAMEWORK1_GITBRANCH_MASTER : 'COMMONFRAMEWORK1_GITBRANCH_MASTER', 
            COMMONFRAMEWORK1_GITBRANCH_RELEASE : 'COMMONFRAMEWORK1_GITBRANCH_RELEASE', 
            COMMONFRAMEWORK1_GITBRANCH_OTHER : 'COMMONFRAMEWORK1_GITBRANCH_OTHER'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_GitBranch()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_GitBranch.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_GitBranch.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFramework1_BootState:
        COMMONFRAMEWORK1_BOOTSTATE_APPLICATIONINIT = 0
        COMMONFRAMEWORK1_BOOTSTATE_PORTVALIDATION = 1
        COMMONFRAMEWORK1_BOOTSTATE_AUTODISCOVER = 2
        COMMONFRAMEWORK1_BOOTSTATE_APPLICATIONRUNNING = 3
        COMMONFRAMEWORK1_BOOTSTATE_ASSERTERROR = 4
    
        ValuesDict = {
            COMMONFRAMEWORK1_BOOTSTATE_APPLICATIONINIT : 'COMMONFRAMEWORK1_BOOTSTATE_APPLICATIONINIT', 
            COMMONFRAMEWORK1_BOOTSTATE_PORTVALIDATION : 'COMMONFRAMEWORK1_BOOTSTATE_PORTVALIDATION', 
            COMMONFRAMEWORK1_BOOTSTATE_AUTODISCOVER : 'COMMONFRAMEWORK1_BOOTSTATE_AUTODISCOVER', 
            COMMONFRAMEWORK1_BOOTSTATE_APPLICATIONRUNNING : 'COMMONFRAMEWORK1_BOOTSTATE_APPLICATIONRUNNING', 
            COMMONFRAMEWORK1_BOOTSTATE_ASSERTERROR : 'COMMONFRAMEWORK1_BOOTSTATE_ASSERTERROR'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BootState()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BootState.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BootState.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFramework1_BootResetReason:
        COMMONFRAMEWORK1_BOOTRESETREASON_RESETUNKNOWN = 0
        COMMONFRAMEWORK1_BOOTRESETREASON_RESETFIREWALL = 1
        COMMONFRAMEWORK1_BOOTRESETREASON_RESETOBL = 2
        COMMONFRAMEWORK1_BOOTRESETREASON_RESETEXTPIN = 3
        COMMONFRAMEWORK1_BOOTRESETREASON_RESETBROWNOUT = 4
        COMMONFRAMEWORK1_BOOTRESETREASON_RESETSOFT = 5
        COMMONFRAMEWORK1_BOOTRESETREASON_RESETWATCHDOG = 6
        COMMONFRAMEWORK1_BOOTRESETREASON_RESETLOWPOWER = 7
        COMMONFRAMEWORK1_BOOTRESETREASON_RESETASSERTERR = 8
    
        ValuesDict = {
            COMMONFRAMEWORK1_BOOTRESETREASON_RESETUNKNOWN : 'COMMONFRAMEWORK1_BOOTRESETREASON_RESETUNKNOWN', 
            COMMONFRAMEWORK1_BOOTRESETREASON_RESETFIREWALL : 'COMMONFRAMEWORK1_BOOTRESETREASON_RESETFIREWALL', 
            COMMONFRAMEWORK1_BOOTRESETREASON_RESETOBL : 'COMMONFRAMEWORK1_BOOTRESETREASON_RESETOBL', 
            COMMONFRAMEWORK1_BOOTRESETREASON_RESETEXTPIN : 'COMMONFRAMEWORK1_BOOTRESETREASON_RESETEXTPIN', 
            COMMONFRAMEWORK1_BOOTRESETREASON_RESETBROWNOUT : 'COMMONFRAMEWORK1_BOOTRESETREASON_RESETBROWNOUT', 
            COMMONFRAMEWORK1_BOOTRESETREASON_RESETSOFT : 'COMMONFRAMEWORK1_BOOTRESETREASON_RESETSOFT', 
            COMMONFRAMEWORK1_BOOTRESETREASON_RESETWATCHDOG : 'COMMONFRAMEWORK1_BOOTRESETREASON_RESETWATCHDOG', 
            COMMONFRAMEWORK1_BOOTRESETREASON_RESETLOWPOWER : 'COMMONFRAMEWORK1_BOOTRESETREASON_RESETLOWPOWER', 
            COMMONFRAMEWORK1_BOOTRESETREASON_RESETASSERTERR : 'COMMONFRAMEWORK1_BOOTRESETREASON_RESETASSERTERR'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BootResetReason()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BootResetReason.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BootResetReason.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFrameworkTypes1_TcTlmError:
        COMMONFRAMEWORKTYPES1_TCTLMERROR_OK = 0
        COMMONFRAMEWORKTYPES1_TCTLMERROR_INVALIDID = 1
        COMMONFRAMEWORKTYPES1_TCTLMERROR_INVALIDLENGTH = 2
        COMMONFRAMEWORKTYPES1_TCTLMERROR_INVALIDPARAM = 3
        COMMONFRAMEWORKTYPES1_TCTLMERROR_CRC = 4
        COMMONFRAMEWORKTYPES1_TCTLMERROR_NOTIMPLEMENTED = 5
        COMMONFRAMEWORKTYPES1_TCTLMERROR_TCTLMBUSY = 6
        COMMONFRAMEWORKTYPES1_TCTLMERROR_SEQUENCE = 7
        COMMONFRAMEWORKTYPES1_TCTLMERROR_INTERNAL = 8
        COMMONFRAMEWORKTYPES1_TCTLMERROR_PASSTIMEOUT = 9
        COMMONFRAMEWORKTYPES1_TCTLMERROR_PASSTARGET = 10
    
        ValuesDict = {
            COMMONFRAMEWORKTYPES1_TCTLMERROR_OK : 'COMMONFRAMEWORKTYPES1_TCTLMERROR_OK', 
            COMMONFRAMEWORKTYPES1_TCTLMERROR_INVALIDID : 'COMMONFRAMEWORKTYPES1_TCTLMERROR_INVALIDID', 
            COMMONFRAMEWORKTYPES1_TCTLMERROR_INVALIDLENGTH : 'COMMONFRAMEWORKTYPES1_TCTLMERROR_INVALIDLENGTH', 
            COMMONFRAMEWORKTYPES1_TCTLMERROR_INVALIDPARAM : 'COMMONFRAMEWORKTYPES1_TCTLMERROR_INVALIDPARAM', 
            COMMONFRAMEWORKTYPES1_TCTLMERROR_CRC : 'COMMONFRAMEWORKTYPES1_TCTLMERROR_CRC', 
            COMMONFRAMEWORKTYPES1_TCTLMERROR_NOTIMPLEMENTED : 'COMMONFRAMEWORKTYPES1_TCTLMERROR_NOTIMPLEMENTED', 
            COMMONFRAMEWORKTYPES1_TCTLMERROR_TCTLMBUSY : 'COMMONFRAMEWORKTYPES1_TCTLMERROR_TCTLMBUSY', 
            COMMONFRAMEWORKTYPES1_TCTLMERROR_SEQUENCE : 'COMMONFRAMEWORKTYPES1_TCTLMERROR_SEQUENCE', 
            COMMONFRAMEWORKTYPES1_TCTLMERROR_INTERNAL : 'COMMONFRAMEWORKTYPES1_TCTLMERROR_INTERNAL', 
            COMMONFRAMEWORKTYPES1_TCTLMERROR_PASSTIMEOUT : 'COMMONFRAMEWORKTYPES1_TCTLMERROR_PASSTIMEOUT', 
            COMMONFRAMEWORKTYPES1_TCTLMERROR_PASSTARGET : 'COMMONFRAMEWORKTYPES1_TCTLMERROR_PASSTARGET'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_TcTlmError()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_TcTlmError.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_TcTlmError.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFrameworkTypes1_NodeTypeLegacy:
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYINVALID = 0
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBECOMPUTER = 1
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBESENSE = 2
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEWHEEL = 3
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEIR = 4
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEMAGDEPLOY = 5
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEMAGCOMPACT = 6
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBESTAR = 7
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEAURIGA = 8
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODE = 9
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODESLT = 10
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODEPST3S = 11
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODENSSRWL = 12
        COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYEXTENDED = 15
    
        ValuesDict = {
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYINVALID : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYINVALID', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBECOMPUTER : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBECOMPUTER', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBESENSE : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBESENSE', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEWHEEL : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEWHEEL', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEIR : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEIR', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEMAGDEPLOY : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEMAGDEPLOY', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEMAGCOMPACT : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEMAGCOMPACT', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBESTAR : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBESTAR', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEAURIGA : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBEAURIGA', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODE : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODE', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODESLT : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODESLT', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODEPST3S : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODEPST3S', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODENSSRWL : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYCUBENODENSSRWL', 
            COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYEXTENDED : 'COMMONFRAMEWORKTYPES1_NODETYPELEGACY_NODETYPELEGACYEXTENDED'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeTypeLegacy()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeTypeLegacy.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeTypeLegacy.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFrameworkTypes1_NodeType:
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPEINVALID = 0
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBECOMPUTER = 1
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBESENSE = 2
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEWHEEL = 3
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEIR = 4
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEMAGDEPLOY = 5
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEMAGCOMPACT = 6
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBESTAR = 7
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEAURIGA = 8
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODE = 9
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODESLT = 10
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEPST3S = 11
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODENSSRWL = 12
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUAD = 16
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUADPST3S = 17
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUADNSSRWL = 18
        COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUADLITEFUFORS = 19
    
        ValuesDict = {
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPEINVALID : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPEINVALID', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBECOMPUTER : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBECOMPUTER', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBESENSE : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBESENSE', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEWHEEL : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEWHEEL', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEIR : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEIR', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEMAGDEPLOY : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEMAGDEPLOY', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEMAGCOMPACT : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEMAGCOMPACT', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBESTAR : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBESTAR', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEAURIGA : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBEAURIGA', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODE : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODE', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODESLT : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODESLT', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEPST3S : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEPST3S', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODENSSRWL : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODENSSRWL', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUAD : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUAD', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUADPST3S : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUADPST3S', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUADNSSRWL : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUADNSSRWL', 
            COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUADLITEFUFORS : 'COMMONFRAMEWORKTYPES1_NODETYPE_NODETYPECUBENODEQUADLITEFUFORS'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeType()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeType.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeType.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFrameworkTypes1_ProgramType:
        COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPEINVALID = 0
        COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPECONTROL = 1
        COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPEBOOTLOADER = 4
        COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPEHEALTHCHECK = 7
    
        ValuesDict = {
            COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPEINVALID : 'COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPEINVALID', 
            COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPECONTROL : 'COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPECONTROL', 
            COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPEBOOTLOADER : 'COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPEBOOTLOADER', 
            COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPEHEALTHCHECK : 'COMMONFRAMEWORKTYPES1_PROGRAMTYPE_PROGRAMTYPEHEALTHCHECK'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_ProgramType()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_ProgramType.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_ProgramType.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommonFrameworkTypes1_SerialSource:
        COMMONFRAMEWORKTYPES1_SERIALSOURCE_SOURCEOTP = 0
        COMMONFRAMEWORKTYPES1_SERIALSOURCE_SOURCECONFIG = 1
    
        ValuesDict = {
            COMMONFRAMEWORKTYPES1_SERIALSOURCE_SOURCEOTP : 'COMMONFRAMEWORKTYPES1_SERIALSOURCE_SOURCEOTP', 
            COMMONFRAMEWORKTYPES1_SERIALSOURCE_SOURCECONFIG : 'COMMONFRAMEWORKTYPES1_SERIALSOURCE_SOURCECONFIG'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_SerialSource()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_SerialSource.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_SerialSource.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_Reset:
        def __init__(self, e__CommonFramework1_ResetVal__ResetType = 0):
            self.e__CommonFramework1_ResetVal__ResetType = e__CommonFramework1_ResetVal__ResetType
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ResetVal(self.e__CommonFramework1_ResetVal__ResetType).serialize()
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_Reset()
    
            currentPos = pos
            
            (resultInstance.e__CommonFramework1_ResetVal__ResetType, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ResetVal.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_UnixTime:
        def __init__(self, uint32__UnixTimeSeconds = 0, uint32__UnixTimeNanoSeconds = 0):
            self.uint32__UnixTimeSeconds = uint32__UnixTimeSeconds
            self.uint32__UnixTimeNanoSeconds = uint32__UnixTimeNanoSeconds
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__UnixTimeSeconds)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__UnixTimeNanoSeconds)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_UnixTime()
    
            currentPos = pos
            
            (resultInstance.uint32__UnixTimeSeconds, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__UnixTimeNanoSeconds, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 8
    
    class struct_ErrorLogIndex:
        def __init__(self, e__CommonFramework1_ErrorLogSearch__ErrorLogIndexReference = 0, uint16__ErrorLogIndexValue = 0, uint16__ErrorLogEntries = 0):
            self.e__CommonFramework1_ErrorLogSearch__ErrorLogIndexReference = e__CommonFramework1_ErrorLogSearch__ErrorLogIndexReference
            self.uint16__ErrorLogIndexValue = uint16__ErrorLogIndexValue
            self.uint16__ErrorLogEntries = uint16__ErrorLogEntries
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ErrorLogSearch(self.e__CommonFramework1_ErrorLogSearch__ErrorLogIndexReference).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__ErrorLogIndexValue)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__ErrorLogEntries)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_ErrorLogIndex()
    
            currentPos = pos
            
            (resultInstance.e__CommonFramework1_ErrorLogSearch__ErrorLogIndexReference, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ErrorLogSearch.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__ErrorLogIndexValue, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__ErrorLogEntries, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 5
    
    class struct_ErrorLogEntry:
        def __init__(self, uint32__ErrorLogEntryTimestamp = 0, uint32__ErrorLogEntryErrorCode = 0):
            self.uint32__ErrorLogEntryTimestamp = uint32__ErrorLogEntryTimestamp
            self.uint32__ErrorLogEntryErrorCode = uint32__ErrorLogEntryErrorCode
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__ErrorLogEntryTimestamp)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__ErrorLogEntryErrorCode)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_ErrorLogEntry()
    
            currentPos = pos
            
            (resultInstance.uint32__ErrorLogEntryTimestamp, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__ErrorLogEntryErrorCode, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 8
    
    class struct_ErrorLogSettings:
        def __init__(self, e__CommonFramework1_ActiveState__ActiveState = 0, e__CommonFramework1_BufferFullAction__BufferFullAction = 0):
            self.e__CommonFramework1_ActiveState__ActiveState = e__CommonFramework1_ActiveState__ActiveState
            self.e__CommonFramework1_BufferFullAction__BufferFullAction = e__CommonFramework1_BufferFullAction__BufferFullAction
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ActiveState(self.e__CommonFramework1_ActiveState__ActiveState).serialize()
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BufferFullAction(self.e__CommonFramework1_BufferFullAction__BufferFullAction).serialize()
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_ErrorLogSettings()
    
            currentPos = pos
            
            (resultInstance.e__CommonFramework1_ActiveState__ActiveState, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ActiveState.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__CommonFramework1_BufferFullAction__BufferFullAction, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BufferFullAction.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 2
    
    class struct_Identification:
        def __init__(self, e__CommonFrameworkTypes1_NodeTypeLegacy__NodeType = 0, e__CommonFrameworkTypes1_ProgramType__ProgramType = 0, uint8__InterfaceVersion = 0, uint8__FirmwareMajorVersion = 0, uint8__FirmwareMinorVersion = 0, uint16__RuntimeSeconds = 0, uint16__RuntimeMilliseconds = 0):
            self.e__CommonFrameworkTypes1_NodeTypeLegacy__NodeType = e__CommonFrameworkTypes1_NodeTypeLegacy__NodeType
            self.e__CommonFrameworkTypes1_ProgramType__ProgramType = e__CommonFrameworkTypes1_ProgramType__ProgramType
            self.uint8__InterfaceVersion = uint8__InterfaceVersion
            self.uint8__FirmwareMajorVersion = uint8__FirmwareMajorVersion
            self.uint8__FirmwareMinorVersion = uint8__FirmwareMinorVersion
            self.uint16__RuntimeSeconds = uint16__RuntimeSeconds
            self.uint16__RuntimeMilliseconds = uint16__RuntimeMilliseconds
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeTypeLegacy(self.e__CommonFrameworkTypes1_NodeTypeLegacy__NodeType).serialize()
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_ProgramType(self.e__CommonFrameworkTypes1_ProgramType__ProgramType).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__InterfaceVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__FirmwareMajorVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__FirmwareMinorVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__RuntimeSeconds)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__RuntimeMilliseconds)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_Identification()
    
            currentPos = pos
            
            (resultInstance.e__CommonFrameworkTypes1_NodeTypeLegacy__NodeType, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeTypeLegacy.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__CommonFrameworkTypes1_ProgramType__ProgramType, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_ProgramType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__InterfaceVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__FirmwareMajorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__FirmwareMinorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__RuntimeSeconds, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__RuntimeMilliseconds, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 9
    
    class struct_SerialNumber:
        def __init__(self, a__uint8__32__OtpSerial = [], a__uint8__32__CfgSerial = [], e__CommonFrameworkTypes1_NodeType__NodeType = 0, uint32__SerialInt = 0, e__CommonFrameworkTypes1_SerialSource__ActiveSerial = 0):
            self.a__uint8__32__OtpSerial = a__uint8__32__OtpSerial
            self.a__uint8__32__CfgSerial = a__uint8__32__CfgSerial
            self.e__CommonFrameworkTypes1_NodeType__NodeType = e__CommonFrameworkTypes1_NodeType__NodeType
            self.uint32__SerialInt = uint32__SerialInt
            self.e__CommonFrameworkTypes1_SerialSource__ActiveSerial = e__CommonFrameworkTypes1_SerialSource__ActiveSerial
    
        def serialize(self):
            result = bytearray()
    
            actualLen = len(self.a__uint8__32__OtpSerial)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__32__OtpSerial, 32)
            actualLen = len(self.a__uint8__32__CfgSerial)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__32__CfgSerial, 32)
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeType(self.e__CommonFrameworkTypes1_NodeType__NodeType).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__SerialInt)
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_SerialSource(self.e__CommonFrameworkTypes1_SerialSource__ActiveSerial).serialize()
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_SerialNumber()
    
            currentPos = pos
            
            (resultInstance.a__uint8__32__OtpSerial, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 32)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__32__CfgSerial, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 32)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__CommonFrameworkTypes1_NodeType__NodeType, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__SerialInt, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__CommonFrameworkTypes1_SerialSource__ActiveSerial, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_SerialSource.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 70
    
    class struct_ConfigPersistDiagnostics:
        def __init__(self, e__CommonFramework1_ConfigPersistState__State = 0, e__CommonFramework1_ConfigPersistResult__LastResult = 0, uint32__Timestamp = 0):
            self.e__CommonFramework1_ConfigPersistState__State = e__CommonFramework1_ConfigPersistState__State
            self.e__CommonFramework1_ConfigPersistResult__LastResult = e__CommonFramework1_ConfigPersistResult__LastResult
            self.uint32__Timestamp = uint32__Timestamp
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ConfigPersistState(self.e__CommonFramework1_ConfigPersistState__State).serialize()
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ConfigPersistResult(self.e__CommonFramework1_ConfigPersistResult__LastResult).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__Timestamp)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_ConfigPersistDiagnostics()
    
            currentPos = pos
            
            (resultInstance.e__CommonFramework1_ConfigPersistState__State, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ConfigPersistState.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__CommonFramework1_ConfigPersistResult__LastResult, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_ConfigPersistResult.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__Timestamp, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 6
    
    class struct_CommsStatus:
        def __init__(self, uint16__uartTcCounter = 0, uint16__uartTlmCounter = 0, uint16__uartSoftwareProtoErrors = 0, uint16__uartHardwareFlagErrors = 0, uint16__uart2TcCounter = 0, uint16__uart2TlmCounter = 0, uint16__uart2SoftwareProtoErrors = 0, uint16__uart2HardwareFlagErrors = 0, uint16__canTcCounter = 0, uint16__canTlmCounter = 0, uint16__canSoftwareProtoErrors = 0, uint16__canHardwareFlagErrors = 0, uint16__i2cTcCounter = 0, uint16__i2cTlmCounter = 0, uint16__i2cSoftwareProtoErrors = 0, uint16__i2cHardwareFlagErrors = 0):
            self.uint16__uartTcCounter = uint16__uartTcCounter
            self.uint16__uartTlmCounter = uint16__uartTlmCounter
            self.uint16__uartSoftwareProtoErrors = uint16__uartSoftwareProtoErrors
            self.uint16__uartHardwareFlagErrors = uint16__uartHardwareFlagErrors
            self.uint16__uart2TcCounter = uint16__uart2TcCounter
            self.uint16__uart2TlmCounter = uint16__uart2TlmCounter
            self.uint16__uart2SoftwareProtoErrors = uint16__uart2SoftwareProtoErrors
            self.uint16__uart2HardwareFlagErrors = uint16__uart2HardwareFlagErrors
            self.uint16__canTcCounter = uint16__canTcCounter
            self.uint16__canTlmCounter = uint16__canTlmCounter
            self.uint16__canSoftwareProtoErrors = uint16__canSoftwareProtoErrors
            self.uint16__canHardwareFlagErrors = uint16__canHardwareFlagErrors
            self.uint16__i2cTcCounter = uint16__i2cTcCounter
            self.uint16__i2cTlmCounter = uint16__i2cTlmCounter
            self.uint16__i2cSoftwareProtoErrors = uint16__i2cSoftwareProtoErrors
            self.uint16__i2cHardwareFlagErrors = uint16__i2cHardwareFlagErrors
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__uartTcCounter)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__uartTlmCounter)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__uartSoftwareProtoErrors)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__uartHardwareFlagErrors)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__uart2TcCounter)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__uart2TlmCounter)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__uart2SoftwareProtoErrors)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__uart2HardwareFlagErrors)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__canTcCounter)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__canTlmCounter)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__canSoftwareProtoErrors)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__canHardwareFlagErrors)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__i2cTcCounter)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__i2cTlmCounter)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__i2cSoftwareProtoErrors)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__i2cHardwareFlagErrors)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_CommsStatus()
    
            currentPos = pos
            
            (resultInstance.uint16__uartTcCounter, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__uartTlmCounter, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__uartSoftwareProtoErrors, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__uartHardwareFlagErrors, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__uart2TcCounter, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__uart2TlmCounter, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__uart2SoftwareProtoErrors, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__uart2HardwareFlagErrors, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__canTcCounter, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__canTlmCounter, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__canSoftwareProtoErrors, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__canHardwareFlagErrors, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__i2cTcCounter, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__i2cTlmCounter, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__i2cSoftwareProtoErrors, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__i2cHardwareFlagErrors, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 32
    
    class struct_Version:
        def __init__(self, uint8__FirmwareMajorVersion = 0, uint8__FirmwareMinorVersion = 0, uint16__FirmwarePatchVersion = 0, uint8__SystemMajorVersion = 0, uint8__SystemMinorVersion = 0, uint16__SystemPatchVersion = 0, e__CommonFramework1_GitBranch__GitBranch = 0, uint32__GitHash = 0, uint32__BuildHash = 0, uint32__BuildTimeSeconds = 0, uint8__HardwareMinorVersion = 0):
            self.uint8__FirmwareMajorVersion = uint8__FirmwareMajorVersion
            self.uint8__FirmwareMinorVersion = uint8__FirmwareMinorVersion
            self.uint16__FirmwarePatchVersion = uint16__FirmwarePatchVersion
            self.uint8__SystemMajorVersion = uint8__SystemMajorVersion
            self.uint8__SystemMinorVersion = uint8__SystemMinorVersion
            self.uint16__SystemPatchVersion = uint16__SystemPatchVersion
            self.e__CommonFramework1_GitBranch__GitBranch = e__CommonFramework1_GitBranch__GitBranch
            self.uint32__GitHash = uint32__GitHash
            self.uint32__BuildHash = uint32__BuildHash
            self.uint32__BuildTimeSeconds = uint32__BuildTimeSeconds
            self.uint8__HardwareMinorVersion = uint8__HardwareMinorVersion
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__FirmwareMajorVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__FirmwareMinorVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__FirmwarePatchVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__SystemMajorVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__SystemMinorVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__SystemPatchVersion)
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_GitBranch(self.e__CommonFramework1_GitBranch__GitBranch).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__GitHash)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__BuildHash)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__BuildTimeSeconds)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__HardwareMinorVersion)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_Version()
    
            currentPos = pos
            
            (resultInstance.uint8__FirmwareMajorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__FirmwareMinorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__FirmwarePatchVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__SystemMajorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__SystemMinorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__SystemPatchVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__CommonFramework1_GitBranch__GitBranch, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_GitBranch.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__GitHash, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__BuildHash, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__BuildTimeSeconds, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__HardwareMinorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 22
    
    class struct_BootStatus:
        def __init__(self, e__CommonFramework1_BootState__State = 0, e__CommonFramework1_BootResetReason__ResetReason = 0, bool__SharedParamsError = False, bool__PortValidationError = False, bool__PortDiscoveryError = False, bool__OtpSerialError = False, bool__CfgSerialError = False, bool__SerialMismatchError = False, bool__ConfigInvalidError = False):
            self.e__CommonFramework1_BootState__State = e__CommonFramework1_BootState__State
            self.e__CommonFramework1_BootResetReason__ResetReason = e__CommonFramework1_BootResetReason__ResetReason
            self.bool__SharedParamsError = bool__SharedParamsError
            self.bool__PortValidationError = bool__PortValidationError
            self.bool__PortDiscoveryError = bool__PortDiscoveryError
            self.bool__OtpSerialError = bool__OtpSerialError
            self.bool__CfgSerialError = bool__CfgSerialError
            self.bool__SerialMismatchError = bool__SerialMismatchError
            self.bool__ConfigInvalidError = bool__ConfigInvalidError
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BootState(self.e__CommonFramework1_BootState__State).serialize()
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BootResetReason(self.e__CommonFramework1_BootResetReason__ResetReason).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__SharedParamsError)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__PortValidationError)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__PortDiscoveryError)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__OtpSerialError)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__CfgSerialError)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__SerialMismatchError)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__ConfigInvalidError)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_BootStatus()
    
            currentPos = pos
            
            (resultInstance.e__CommonFramework1_BootState__State, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BootState.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__CommonFramework1_BootResetReason__ResetReason, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFramework1_BootResetReason.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__SharedParamsError, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__PortValidationError, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__PortDiscoveryError, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__OtpSerialError, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__CfgSerialError, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__SerialMismatchError, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__ConfigInvalidError, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 9
    
    class struct_TelecommandAcknowledge:
        def __init__(self, uint8__Id = 0, e__CommonFrameworkTypes1_TcTlmError__Error = 0, uint8__ErrorIndex = 0, bool__Read = False):
            self.uint8__Id = uint8__Id
            self.e__CommonFrameworkTypes1_TcTlmError__Error = e__CommonFrameworkTypes1_TcTlmError__Error
            self.uint8__ErrorIndex = uint8__ErrorIndex
            self.bool__Read = bool__Read
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Id)
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_TcTlmError(self.e__CommonFrameworkTypes1_TcTlmError__Error).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__ErrorIndex)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__Read)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_TelecommandAcknowledge()
    
            currentPos = pos
            
            (resultInstance.uint8__Id, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__CommonFrameworkTypes1_TcTlmError__Error, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_TcTlmError.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__ErrorIndex, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__Read, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 4
    
    class struct_CommonErrorCodes:
        def __init__(self, uint32__SlaveSvcCan = 0, uint32__SlaveSvcUart = 0, uint32__SlaveSvcI2c = 0, uint32__ErrorLogSvc = 0):
            self.uint32__SlaveSvcCan = uint32__SlaveSvcCan
            self.uint32__SlaveSvcUart = uint32__SlaveSvcUart
            self.uint32__SlaveSvcI2c = uint32__SlaveSvcI2c
            self.uint32__ErrorLogSvc = uint32__ErrorLogSvc
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__SlaveSvcCan)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__SlaveSvcUart)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__SlaveSvcI2c)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__ErrorLogSvc)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_CommonErrorCodes()
    
            currentPos = pos
            
            (resultInstance.uint32__SlaveSvcCan, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__SlaveSvcUart, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__SlaveSvcI2c, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__ErrorLogSvc, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 16
    
    class struct_Identification2:
        def __init__(self, e__CommonFrameworkTypes1_NodeType__NodeType = 0, e__CommonFrameworkTypes1_ProgramType__ProgramType = 0, uint32__SerialInt = 0, uint8__InterfaceVersion = 0, uint8__FirmwareMajorVersion = 0, uint8__FirmwareMinorVersion = 0, uint16__FirmwarePatchVersion = 0, uint8__SystemMajorVersion = 0, uint8__SystemMinorVersion = 0, uint16__SystemPatchVersion = 0, uint8__HardwareMinorVersion = 0, uint16__RuntimeSeconds = 0, uint16__RuntimeMilliseconds = 0):
            self.e__CommonFrameworkTypes1_NodeType__NodeType = e__CommonFrameworkTypes1_NodeType__NodeType
            self.e__CommonFrameworkTypes1_ProgramType__ProgramType = e__CommonFrameworkTypes1_ProgramType__ProgramType
            self.uint32__SerialInt = uint32__SerialInt
            self.uint8__InterfaceVersion = uint8__InterfaceVersion
            self.uint8__FirmwareMajorVersion = uint8__FirmwareMajorVersion
            self.uint8__FirmwareMinorVersion = uint8__FirmwareMinorVersion
            self.uint16__FirmwarePatchVersion = uint16__FirmwarePatchVersion
            self.uint8__SystemMajorVersion = uint8__SystemMajorVersion
            self.uint8__SystemMinorVersion = uint8__SystemMinorVersion
            self.uint16__SystemPatchVersion = uint16__SystemPatchVersion
            self.uint8__HardwareMinorVersion = uint8__HardwareMinorVersion
            self.uint16__RuntimeSeconds = uint16__RuntimeSeconds
            self.uint16__RuntimeMilliseconds = uint16__RuntimeMilliseconds
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeType(self.e__CommonFrameworkTypes1_NodeType__NodeType).serialize()
            
            result += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_ProgramType(self.e__CommonFrameworkTypes1_ProgramType__ProgramType).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__SerialInt)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__InterfaceVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__FirmwareMajorVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__FirmwareMinorVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__FirmwarePatchVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__SystemMajorVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__SystemMinorVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__SystemPatchVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__HardwareMinorVersion)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__RuntimeSeconds)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__RuntimeMilliseconds)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_Identification2()
    
            currentPos = pos
            
            (resultInstance.e__CommonFrameworkTypes1_NodeType__NodeType, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_NodeType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__CommonFrameworkTypes1_ProgramType__ProgramType, bytesProcessed) = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CommonFrameworkTypes1_ProgramType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__SerialInt, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__InterfaceVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__FirmwareMajorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__FirmwareMinorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__FirmwarePatchVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__SystemMajorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__SystemMinorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__SystemPatchVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__HardwareMinorVersion, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__RuntimeSeconds, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__RuntimeMilliseconds, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 20
    

    ############################################################################################################
    """
    Request function for FIDL method: setReset
        - function ID: 00000000
        - description: Perform a soft reset
    """
    def req_setReset(self, e__CmdTargetNode__cmdTargetNode, s__setVal):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000000
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
        requestBytes += s__setVal.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000000, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setReset
        - function ID: 00000000
        - description: Perform a soft reset
    """
    def resp_setReset(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000000):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setUnixTime
        - function ID: 00000001
        - description: Current Unix time
    """
    def req_setUnixTime(self, e__CmdTargetNode__cmdTargetNode, s__setVal):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000001
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
        requestBytes += s__setVal.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000001, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setUnixTime
        - function ID: 00000001
        - description: Current Unix time
    """
    def resp_setUnixTime(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000001):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setErrorLogIndex
        - function ID: 00000002
        - description: Describes the index of the error log that will be read when calling GetErrorLogEntry
    """
    def req_setErrorLogIndex(self, e__CmdTargetNode__cmdTargetNode, s__setVal):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000002
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
        requestBytes += s__setVal.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000002, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setErrorLogIndex
        - function ID: 00000002
        - description: Describes the index of the error log that will be read when calling GetErrorLogEntry
    """
    def resp_setErrorLogIndex(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000002):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setErrorLogEntry
        - function ID: 00000003
        - description: Error Log Entry
    """
    def req_setErrorLogEntry(self, e__CmdTargetNode__cmdTargetNode, s__setVal):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000003
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
        requestBytes += s__setVal.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000003, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setErrorLogEntry
        - function ID: 00000003
        - description: Error Log Entry
    """
    def resp_setErrorLogEntry(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000003):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setErrorLogClear
        - function ID: 00000004
        - description: Clear the Error Log
    """
    def req_setErrorLogClear(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000004
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000004, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setErrorLogClear
        - function ID: 00000004
        - description: Clear the Error Log
    """
    def resp_setErrorLogClear(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000004):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setErrorLogSettings
        - function ID: 00000005
        - description: Error Log Settings
    """
    def req_setErrorLogSettings(self, e__CmdTargetNode__cmdTargetNode, s__setVal):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000005
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
        requestBytes += s__setVal.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000005, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setErrorLogSettings
        - function ID: 00000005
        - description: Error Log Settings
    """
    def resp_setErrorLogSettings(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000005):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: setConfigPersist
        - function ID: 00000006
        - description: Writes volatile config items to flash
    """
    def req_setConfigPersist(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000006
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000006, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: setConfigPersist
        - function ID: 00000006
        - description: Writes volatile config items to flash
    """
    def resp_setConfigPersist(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000006):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getIdentification
        - function ID: 00000007
        - description: Identification information for this node (Legacy definition - use Identification2 instead)
    """
    def req_getIdentification(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000007
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000007, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getIdentification
        - function ID: 00000007
        - description: Identification information for this node (Legacy definition - use Identification2 instead)
    """
    def resp_getIdentification(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000007):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_Identification.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getSerialNumber
        - function ID: 00000008
        - description: Unique serial number of the CubeSpace Component
    """
    def req_getSerialNumber(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000008
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000008, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getSerialNumber
        - function ID: 00000008
        - description: Unique serial number of the CubeSpace Component
    """
    def resp_getSerialNumber(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000008):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_SerialNumber.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getErrorLogIndex
        - function ID: 00000009
        - description: Describes the index of the error log that will be read when calling GetErrorLogEntry
    """
    def req_getErrorLogIndex(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000009
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000009, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getErrorLogIndex
        - function ID: 00000009
        - description: Describes the index of the error log that will be read when calling GetErrorLogEntry
    """
    def resp_getErrorLogIndex(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000009):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_ErrorLogIndex.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getErrorLogEntry
        - function ID: 0000000A
        - description: Error Log Entry
    """
    def req_getErrorLogEntry(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000A
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000A, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getErrorLogEntry
        - function ID: 0000000A
        - description: Error Log Entry
    """
    def resp_getErrorLogEntry(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000A):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_ErrorLogEntry.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getErrorLogSettings
        - function ID: 0000000B
        - description: Error Log Settings
    """
    def req_getErrorLogSettings(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000B
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000B, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getErrorLogSettings
        - function ID: 0000000B
        - description: Error Log Settings
    """
    def resp_getErrorLogSettings(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000B):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_ErrorLogSettings.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getUnixTime
        - function ID: 0000000C
        - description: Current Unix time
    """
    def req_getUnixTime(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000C
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000C, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getUnixTime
        - function ID: 0000000C
        - description: Current Unix time
    """
    def resp_getUnixTime(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000C):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_UnixTime.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getConfigPersistDiagnostics
        - function ID: 0000000D
        - description: Diagnostics data for config persistence
    """
    def req_getConfigPersistDiagnostics(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000D
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000D, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getConfigPersistDiagnostics
        - function ID: 0000000D
        - description: Diagnostics data for config persistence
    """
    def resp_getConfigPersistDiagnostics(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000D):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_ConfigPersistDiagnostics.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getCommsStatus
        - function ID: 0000000E
        - description: Communication Status
    """
    def req_getCommsStatus(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000E
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000E, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getCommsStatus
        - function ID: 0000000E
        - description: Communication Status
    """
    def resp_getCommsStatus(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000E):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_CommsStatus.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getVersion
        - function ID: 0000000F
        - description: Firmware Version
    """
    def req_getVersion(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000F
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000F, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getVersion
        - function ID: 0000000F
        - description: Firmware Version
    """
    def resp_getVersion(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000F):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_Version.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getBootStatus
        - function ID: 00000010
        - description: State information about the device boot process
    """
    def req_getBootStatus(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000010
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000010, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getBootStatus
        - function ID: 00000010
        - description: State information about the device boot process
    """
    def resp_getBootStatus(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000010):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_BootStatus.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getTelecommandAcknowledge
        - function ID: 00000011
        - description: Used with the I2C protocol to receive Telecommand Ack/Nack
    """
    def req_getTelecommandAcknowledge(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000011
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000011, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getTelecommandAcknowledge
        - function ID: 00000011
        - description: Used with the I2C protocol to receive Telecommand Ack/Nack
    """
    def resp_getTelecommandAcknowledge(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000011):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_TelecommandAcknowledge.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getCommonErrorCodes
        - function ID: 00000012
        - description: Error codes common to all applications
    """
    def req_getCommonErrorCodes(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000012
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000012, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getCommonErrorCodes
        - function ID: 00000012
        - description: Error codes common to all applications
    """
    def resp_getCommonErrorCodes(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000012):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_CommonErrorCodes.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getIdentification2
        - function ID: 00000013
        - description: Identification information for this node
    """
    def req_getIdentification2(self, e__CmdTargetNode__cmdTargetNode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000013
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.enum_CmdTargetNode(e__CmdTargetNode__cmdTargetNode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000013, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: getIdentification2
        - function ID: 00000013
        - description: Identification information for this node
    """
    def resp_getIdentification2(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000013):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int32", data, currentPos)
        responseInstance["t__int32__adcsErrorCode"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_CUBEADCS_GEN2_COMMONFRAMEWORK1.struct_Identification2.deserialize(data, currentPos)
        responseInstance["s__returnVal"] = field
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

            if fpHeaderInstance.u16ProtoId != self.const_CUBEADCS_GEN2_COMMONFRAMEWORK1_PROTOCOL_ID:
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

