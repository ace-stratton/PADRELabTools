# ********************************************************************************************
# * @file UHFClientApp.py
# * @brief MAC FP client Python implementation generator
# ********************************************************************************************
# * @version           interface UHF v0.5
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

class FP_API_UHF:
    def __init__(self, rawSerDesSupport : bool = False):
        self.const_UHF_PROTOCOL_ID = 5
        self.rawSerDesSupport = rawSerDesSupport
        self.versionMajor=0
        self.versionMinor=5


        #
        # Response parsers map
        #
        self.responseParsersDict = {}
        self.responseParsersDict[1] = self.resp_WriteSCW
        self.responseParsersDict[2] = self.resp_ReadSCW
        self.responseParsersDict[3] = self.resp_WriteRfConfig
        self.responseParsersDict[4] = self.resp_ReadRfConfig
        self.responseParsersDict[5] = self.resp_ReadUpTime
        self.responseParsersDict[6] = self.resp_ReadNumberOfTxPackets
        self.responseParsersDict[7] = self.resp_ReadNumberOfRxPackets
        self.responseParsersDict[8] = self.resp_ReadNumberOfRxPacketsCRCErr
        self.responseParsersDict[9] = self.resp_WriteBeaconMessageTxPeriodCfg
        self.responseParsersDict[10] = self.resp_ReadBeaconMessageTxPeriodCfg
        self.responseParsersDict[11] = self.resp_WriteBeaconMessageBetweeenTxPeriodConfig
        self.responseParsersDict[12] = self.resp_ReadBeaconMessageBetweeenTxPeriodConfig
        self.responseParsersDict[13] = self.resp_RestoreDefaultConfig
        self.responseParsersDict[14] = self.resp_ResetCounters
        self.responseParsersDict[16] = self.resp_WriteAntenna
        self.responseParsersDict[17] = self.resp_ReadAntenna
        self.responseParsersDict[18] = self.resp_EnterLPM
        self.responseParsersDict[19] = self.resp_ReadLPM
        self.responseParsersDict[20] = self.resp_WriteDestCallSign
        self.responseParsersDict[21] = self.resp_ReadDestCallSign
        self.responseParsersDict[22] = self.resp_WriteSrcCallSign
        self.responseParsersDict[23] = self.resp_ReadSRCCallSign
        self.responseParsersDict[24] = self.resp_WriteMorseCallSign
        self.responseParsersDict[25] = self.resp_ReadMorseCallSign
        self.responseParsersDict[26] = self.resp_WriteMIDIAudioBeacon
        self.responseParsersDict[27] = self.resp_ReadMIDIAudioBeacon
        self.responseParsersDict[28] = self.resp_ReadSWVersion
        self.responseParsersDict[29] = self.resp_ReadPayloadSize
        self.responseParsersDict[30] = self.resp_WriteBeaconMessageContentCfg
        self.responseParsersDict[31] = self.resp_ReadBeaconMessageContentCfg
        self.responseParsersDict[32] = self.resp_WriteDeviceAddrConfig
        self.responseParsersDict[33] = self.resp_WriteFRAM
        self.responseParsersDict[34] = self.resp_ReadFRAM
        self.responseParsersDict[35] = self.resp_WriteTransProperty
        self.responseParsersDict[36] = self.resp_ReadTransProperty
        self.responseParsersDict[37] = self.resp_ReadTemp
        self.responseParsersDict[38] = self.resp_ReadRSSI
        self.responseParsersDict[39] = self.resp_WriteRadioRawData
        self.responseParsersDict[40] = self.resp_Ping
        self.responseParsersDict[41] = self.resp_ExBeaconSetSend
        self.responseParsersDict[42] = self.resp_WriteI2cConfig
        self.responseParsersDict[43] = self.resp_ReadI2cConfig
        self.responseParsersDict[44] = self.resp_WriteAntennaCfg
        self.responseParsersDict[45] = self.resp_ReadAntennaCfg
        self.responseParsersDict[46] = self.resp_WriteEpsCfg
        self.responseParsersDict[47] = self.resp_ReadEpsCfg
        self.responseParsersDict[48] = self.resp_WriteEpsConOpsCfg
        self.responseParsersDict[49] = self.resp_ReadEpsConOpsCfg
        self.responseParsersDict[50] = self.resp_WriteRs485Config
        self.responseParsersDict[51] = self.resp_ReadRs485Config
        self.responseParsersDict[52] = self.resp_WriteOBCConfig
        self.responseParsersDict[53] = self.resp_ReadOBCConfig
        self.responseParsersDict[54] = self.resp_WriteSatConfig
        self.responseParsersDict[55] = self.resp_ReadSatConfig
        self.responseParsersDict[56] = self.resp_ReadEpsCfgOut
        self.responseParsersDict[57] = self.resp_WriteEpsCfgOut
        self.responseParsersDict[58] = self.resp_Write2UAntennaCfg
        self.responseParsersDict[59] = self.resp_Read2UAntennaCfg
        self.responseParsersDict[60] = self.resp_WriteAutomatedBeaconCfg
        self.responseParsersDict[61] = self.resp_ReadAutomatedBeaconCfg
        self.responseParsersDict[62] = self.resp_WriteOutputPowerCfg
        self.responseParsersDict[63] = self.resp_ReadOutputPowerCfg
        self.responseParsersDict[64] = self.resp_ReadCounters
        self.responseParsersDict[65] = self.resp_WriteCipherKeySlot
        self.responseParsersDict[66] = self.resp_ReadCipherKeySlotStatus
        self.responseParsersDict[67] = self.resp_EraseCipherKeySlot
        self.responseParsersDict[68] = self.resp_AntennaDirectRelease

    class enum_eESSA_UhfStatus:
        EESSA_UHFSTATUS_OK = 0
        EESSA_UHFSTATUS_ERROR = 1
        EESSA_UHFSTATUS_ERROR_BAD_DATA = 2
        EESSA_UHFSTATUS_ERROR_NOT_IMPLEMENTED = 3
        EESSA_UHFSTATUS_ERROR_I2C_NACK = 4
        EESSA_UHFSTATUS_UHF_ERR_BUSY = 5
    
        ValuesDict = {
            EESSA_UHFSTATUS_OK : 'EESSA_UHFSTATUS_OK', 
            EESSA_UHFSTATUS_ERROR : 'EESSA_UHFSTATUS_ERROR', 
            EESSA_UHFSTATUS_ERROR_BAD_DATA : 'EESSA_UHFSTATUS_ERROR_BAD_DATA', 
            EESSA_UHFSTATUS_ERROR_NOT_IMPLEMENTED : 'EESSA_UHFSTATUS_ERROR_NOT_IMPLEMENTED', 
            EESSA_UHFSTATUS_ERROR_I2C_NACK : 'EESSA_UHFSTATUS_ERROR_I2C_NACK', 
            EESSA_UHFSTATUS_UHF_ERR_BUSY : 'EESSA_UHFSTATUS_UHF_ERR_BUSY'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.enum_eESSA_UhfStatus()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_UHF.enum_eESSA_UhfStatus.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_UHF.enum_eESSA_UhfStatus.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_eESSA_UhfSCipherKeySlotStatus:
        EESSA_UHFSCIPHERKEYSLOTSTATUS_SUCCESS = 0
        EESSA_UHFSCIPHERKEYSLOTSTATUS_EMPTY = 1
        EESSA_UHFSCIPHERKEYSLOTSTATUS_OCCUPIED = 2
        EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_OUT_OF_RANGE = 3
        EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_IO = 4
        EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_OCCUPIED = 5
        EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_EMPTY = 6
        EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_KEYSIZE = 7
        EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_NOMASTER = 8
        EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_KEYNOTMATCH = 9
        EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR = 10
    
        ValuesDict = {
            EESSA_UHFSCIPHERKEYSLOTSTATUS_SUCCESS : 'EESSA_UHFSCIPHERKEYSLOTSTATUS_SUCCESS', 
            EESSA_UHFSCIPHERKEYSLOTSTATUS_EMPTY : 'EESSA_UHFSCIPHERKEYSLOTSTATUS_EMPTY', 
            EESSA_UHFSCIPHERKEYSLOTSTATUS_OCCUPIED : 'EESSA_UHFSCIPHERKEYSLOTSTATUS_OCCUPIED', 
            EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_OUT_OF_RANGE : 'EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_OUT_OF_RANGE', 
            EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_IO : 'EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_IO', 
            EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_OCCUPIED : 'EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_OCCUPIED', 
            EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_EMPTY : 'EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_EMPTY', 
            EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_KEYSIZE : 'EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_KEYSIZE', 
            EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_NOMASTER : 'EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_NOMASTER', 
            EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_KEYNOTMATCH : 'EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR_KEYNOTMATCH', 
            EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR : 'EESSA_UHFSCIPHERKEYSLOTSTATUS_ERR'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.enum_eESSA_UhfSCipherKeySlotStatus()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_UHF.enum_eESSA_UhfSCipherKeySlotStatus.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_UHF.enum_eESSA_UhfSCipherKeySlotStatus.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_eAntennaReleaseType:
        EANTENNARELEASETYPE_OFF = 0
        EANTENNARELEASETYPE_A = 1
        EANTENNARELEASETYPE_B = 2
        EANTENNARELEASETYPE_AB = 3
    
        ValuesDict = {
            EANTENNARELEASETYPE_OFF : 'EANTENNARELEASETYPE_OFF', 
            EANTENNARELEASETYPE_A : 'EANTENNARELEASETYPE_A', 
            EANTENNARELEASETYPE_B : 'EANTENNARELEASETYPE_B', 
            EANTENNARELEASETYPE_AB : 'EANTENNARELEASETYPE_AB'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.enum_eAntennaReleaseType()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_UHF.enum_eAntennaReleaseType.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_UHF.enum_eAntennaReleaseType.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_StatusControlWord:
        def __init__(self, uint16__SCWBitField = 0):
            self.uint16__SCWBitField = uint16__SCWBitField
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__SCWBitField)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_StatusControlWord()
    
            currentPos = pos
            
            (resultInstance.uint16__SCWBitField, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 2
    
    class struct_sUpTime:
        def __init__(self, uint32__u32UpTime = 0):
            self.uint32__u32UpTime = uint32__u32UpTime
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__u32UpTime)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sUpTime()
    
            currentPos = pos
            
            (resultInstance.uint32__u32UpTime, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 4
    
    class struct_sRFConfig:
        def __init__(self, uint8__RxIntPar = 0, a__uint8__3__RxFractional = [], uint8__TxIntPar = 0, a__uint8__3__TxFractional = [], uint8__Validity = 0):
            self.uint8__RxIntPar = uint8__RxIntPar
            self.a__uint8__3__RxFractional = a__uint8__3__RxFractional
            self.uint8__TxIntPar = uint8__TxIntPar
            self.a__uint8__3__TxFractional = a__uint8__3__TxFractional
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__RxIntPar)
            actualLen = len(self.a__uint8__3__RxFractional)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__3__RxFractional, 3)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__TxIntPar)
            actualLen = len(self.a__uint8__3__TxFractional)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__3__TxFractional, 3)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sRFConfig()
    
            currentPos = pos
            
            (resultInstance.uint8__RxIntPar, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__3__RxFractional, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 3)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__TxIntPar, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__3__TxFractional, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 3)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 9
    
    class struct_sBeaconMessageTxPeriodCfg:
        def __init__(self, uint16__Period = 0, uint8__Validity = 0):
            self.uint16__Period = uint16__Period
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__Period)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sBeaconMessageTxPeriodCfg()
    
            currentPos = pos
            
            (resultInstance.uint16__Period, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 3
    
    class struct_sAntennaReleaseCfg:
        def __init__(self, uint8__Enable = 0, uint8__Time = 0, uint8__Validity = 0):
            self.uint8__Enable = uint8__Enable
            self.uint8__Time = uint8__Time
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Enable)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Time)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sAntennaReleaseCfg()
    
            currentPos = pos
            
            (resultInstance.uint8__Enable, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Time, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 3
    
    class struct_sBeaconMessageBetweenTxPeriodCfg:
        def __init__(self, uint16__Period = 0, uint8__Validity = 0):
            self.uint16__Period = uint16__Period
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__Period)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sBeaconMessageBetweenTxPeriodCfg()
    
            currentPos = pos
            
            (resultInstance.uint16__Period, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 3
    
    class struct_sAntennaDirectRelease:
        def __init__(self, e__eAntennaReleaseType__eReleaseType = 0, uint8__OnTime = 0, uint8__Validity = 0):
            self.e__eAntennaReleaseType__eReleaseType = e__eAntennaReleaseType__eReleaseType
            self.uint8__OnTime = uint8__OnTime
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_UHF.enum_eAntennaReleaseType(self.e__eAntennaReleaseType__eReleaseType).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__OnTime)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sAntennaDirectRelease()
    
            currentPos = pos
            
            (resultInstance.e__eAntennaReleaseType__eReleaseType, bytesProcessed) = FP_API_UHF.enum_eAntennaReleaseType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__OnTime, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 3
    
    class struct_sAntennaData:
        def __init__(self, uint32__Data = 0, uint8__Validity = 0):
            self.uint32__Data = uint32__Data
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__Data)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sAntennaData()
    
            currentPos = pos
            
            (resultInstance.uint32__Data, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 5
    
    class struct_sCallSign:
        def __init__(self, a__uint8__6__Signature = [], uint8__u8Validity = 0):
            self.a__uint8__6__Signature = a__uint8__6__Signature
            self.uint8__u8Validity = uint8__u8Validity
    
        def serialize(self):
            result = bytearray()
    
            actualLen = len(self.a__uint8__6__Signature)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__6__Signature, 6)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__u8Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sCallSign()
    
            currentPos = pos
            
            (resultInstance.a__uint8__6__Signature, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 6)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__u8Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 7
    
    class struct_sMorseCallSign:
        def __init__(self, uint8__Size = 0, a__uint8__37__Signature = [], uint8__Validity = 0):
            self.uint8__Size = uint8__Size
            self.a__uint8__37__Signature = a__uint8__37__Signature
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Size)
            actualLen = len(self.a__uint8__37__Signature)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__37__Signature, 37)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sMorseCallSign()
    
            currentPos = pos
            
            (resultInstance.uint8__Size, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__37__Signature, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 37)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 39
    
    class struct_sMidiAudioBeacon:
        def __init__(self, uint8__Size = 0, a__uint16__37__Midi = [], uint8__Validity = 0):
            self.uint8__Size = uint8__Size
            self.a__uint16__37__Midi = a__uint16__37__Midi
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Size)
            actualLen = len(self.a__uint16__37__Midi)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint16", self.a__uint16__37__Midi, 37)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sMidiAudioBeacon()
    
            currentPos = pos
            
            (resultInstance.uint8__Size, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint16__37__Midi, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint16", data, currentPos, 37)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 76
    
    class struct_sSwVersionBuild:
        def __init__(self, uint8__Version = 0, uint8__Increment = 0, a__uint8__25__DateTimeAsciiZ = [], uint8__Validity = 0):
            self.uint8__Version = uint8__Version
            self.uint8__Increment = uint8__Increment
            self.a__uint8__25__DateTimeAsciiZ = a__uint8__25__DateTimeAsciiZ
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Version)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Increment)
            actualLen = len(self.a__uint8__25__DateTimeAsciiZ)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__25__DateTimeAsciiZ, 25)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sSwVersionBuild()
    
            currentPos = pos
            
            (resultInstance.uint8__Version, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Increment, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__25__DateTimeAsciiZ, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 25)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 28
    
    class struct_sBeaconMessageContentCfg:
        def __init__(self, uint8__Size = 0, a__uint8__98__Message = [], uint8__Validity = 0):
            self.uint8__Size = uint8__Size
            self.a__uint8__98__Message = a__uint8__98__Message
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Size)
            actualLen = len(self.a__uint8__98__Message)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__98__Message, 98)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sBeaconMessageContentCfg()
    
            currentPos = pos
            
            (resultInstance.uint8__Size, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__98__Message, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 98)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 100
    
    class struct_sAddrCfg:
        def __init__(self, uint8__Addr = 0, uint8__Validity = 0):
            self.uint8__Addr = uint8__Addr
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Addr)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sAddrCfg()
    
            currentPos = pos
            
            (resultInstance.uint8__Addr, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 2
    
    class struct_sFramData:
        def __init__(self, uint32__Addr = 0, a__uint8__16__Data = [], uint8__Validity = 0):
            self.uint32__Addr = uint32__Addr
            self.a__uint8__16__Data = a__uint8__16__Data
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__Addr)
            actualLen = len(self.a__uint8__16__Data)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__16__Data, 16)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sFramData()
    
            currentPos = pos
            
            (resultInstance.uint32__Addr, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__16__Data, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 16)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 21
    
    class struct_sReadTransceiverProperty:
        def __init__(self, uint8__Group = 0, uint8__Offset = 0, uint8__Size = 0):
            self.uint8__Group = uint8__Group
            self.uint8__Offset = uint8__Offset
            self.uint8__Size = uint8__Size
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Group)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Offset)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Size)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sReadTransceiverProperty()
    
            currentPos = pos
            
            (resultInstance.uint8__Group, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Offset, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Size, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 3
    
    class struct_sTransceiverProperty:
        def __init__(self, uint8__Group = 0, uint8__Offset = 0, uint8__Size = 0, a__uint8__16__Data = [], uint8__Validity = 0):
            self.uint8__Group = uint8__Group
            self.uint8__Offset = uint8__Offset
            self.uint8__Size = uint8__Size
            self.a__uint8__16__Data = a__uint8__16__Data
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Group)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Offset)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Size)
            actualLen = len(self.a__uint8__16__Data)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__16__Data, 16)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sTransceiverProperty()
    
            currentPos = pos
            
            (resultInstance.uint8__Group, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Offset, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Size, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__16__Data, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 16)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 20
    
    class struct_sSi4463ModemStatus:
        def __init__(self, uint8__MODEM_PEND = 0, uint8__MODEM_STATUS = 0, uint8__CURR_RSSI = 0, uint8__LATCH_RSSI = 0, uint8__ANT1_RSSI = 0, uint8__ANT2_RSSI = 0, uint16__AFC_FREQ_OFFSET = 0):
            self.uint8__MODEM_PEND = uint8__MODEM_PEND
            self.uint8__MODEM_STATUS = uint8__MODEM_STATUS
            self.uint8__CURR_RSSI = uint8__CURR_RSSI
            self.uint8__LATCH_RSSI = uint8__LATCH_RSSI
            self.uint8__ANT1_RSSI = uint8__ANT1_RSSI
            self.uint8__ANT2_RSSI = uint8__ANT2_RSSI
            self.uint16__AFC_FREQ_OFFSET = uint16__AFC_FREQ_OFFSET
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__MODEM_PEND)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__MODEM_STATUS)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__CURR_RSSI)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__LATCH_RSSI)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__ANT1_RSSI)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__ANT2_RSSI)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__AFC_FREQ_OFFSET)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sSi4463ModemStatus()
    
            currentPos = pos
            
            (resultInstance.uint8__MODEM_PEND, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__MODEM_STATUS, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__CURR_RSSI, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__LATCH_RSSI, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__ANT1_RSSI, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__ANT2_RSSI, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__AFC_FREQ_OFFSET, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 8
    
    class struct_sRadioRawData:
        def __init__(self, uint8__Size = 0, a__uint8__128__Data = []):
            self.uint8__Size = uint8__Size
            self.a__uint8__128__Data = a__uint8__128__Data
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Size)
            actualLen = len(self.a__uint8__128__Data)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__128__Data, 128)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sRadioRawData()
    
            currentPos = pos
            
            (resultInstance.uint8__Size, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__128__Data, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 128)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 129
    
    class struct_sPing:
        def __init__(self, uint8__Size = 0, a__uint8__16__Data = []):
            self.uint8__Size = uint8__Size
            self.a__uint8__16__Data = a__uint8__16__Data
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Size)
            actualLen = len(self.a__uint8__16__Data)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__16__Data, 16)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sPing()
    
            currentPos = pos
            
            (resultInstance.uint8__Size, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__16__Data, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 16)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 17
    
    class struct_sExBeacon:
        def __init__(self, uint8__Size = 0, a__uint8__73__Data = []):
            self.uint8__Size = uint8__Size
            self.a__uint8__73__Data = a__uint8__73__Data
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Size)
            actualLen = len(self.a__uint8__73__Data)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__73__Data, 73)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sExBeacon()
    
            currentPos = pos
            
            (resultInstance.uint8__Size, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__73__Data, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 73)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 74
    
    class struct_sI2cCfg:
        def __init__(self, uint8__Addr = 0, uint8__PullUp4_7K = 0, uint8__PullUp10K = 0, uint8__Validity = 0):
            self.uint8__Addr = uint8__Addr
            self.uint8__PullUp4_7K = uint8__PullUp4_7K
            self.uint8__PullUp10K = uint8__PullUp10K
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Addr)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__PullUp4_7K)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__PullUp10K)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sI2cCfg()
    
            currentPos = pos
            
            (resultInstance.uint8__Addr, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__PullUp4_7K, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__PullUp10K, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 4
    
    class struct_sAntennaCfg:
        def __init__(self, uint8__I2cAddr = 0, uint8__AntennaReleaseCheckEnable = 0, uint8__AntennaReleaseCheckTime = 0, uint8__Validity = 0):
            self.uint8__I2cAddr = uint8__I2cAddr
            self.uint8__AntennaReleaseCheckEnable = uint8__AntennaReleaseCheckEnable
            self.uint8__AntennaReleaseCheckTime = uint8__AntennaReleaseCheckTime
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__I2cAddr)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__AntennaReleaseCheckEnable)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__AntennaReleaseCheckTime)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sAntennaCfg()
    
            currentPos = pos
            
            (resultInstance.uint8__I2cAddr, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__AntennaReleaseCheckEnable, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__AntennaReleaseCheckTime, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 4
    
    class struct_sEpsCfg:
        def __init__(self, uint8__Addr = 0, uint8__u8Variant = 0, uint32__u32RequestTimeMs = 0, uint8__Validity = 0):
            self.uint8__Addr = uint8__Addr
            self.uint8__u8Variant = uint8__u8Variant
            self.uint32__u32RequestTimeMs = uint32__u32RequestTimeMs
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Addr)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__u8Variant)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__u32RequestTimeMs)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sEpsCfg()
    
            currentPos = pos
            
            (resultInstance.uint8__Addr, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__u8Variant, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__u32RequestTimeMs, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 7
    
    class struct_sEpsConOpsCfg:
        def __init__(self, uint16__v_low = 0, uint16__i_low = 0, uint16__v_high = 0, uint16__i_high = 0, uint16__v_ideal_low = 0, uint16__v_ideal_high = 0, uint8__Validity = 0):
            self.uint16__v_low = uint16__v_low
            self.uint16__i_low = uint16__i_low
            self.uint16__v_high = uint16__v_high
            self.uint16__i_high = uint16__i_high
            self.uint16__v_ideal_low = uint16__v_ideal_low
            self.uint16__v_ideal_high = uint16__v_ideal_high
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__v_low)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__i_low)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__v_high)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__i_high)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__v_ideal_low)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__v_ideal_high)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sEpsConOpsCfg()
    
            currentPos = pos
            
            (resultInstance.uint16__v_low, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__i_low, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__v_high, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__i_high, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__v_ideal_low, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__v_ideal_high, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 13
    
    class struct_sRS485Cfg:
        def __init__(self, uint8__Termination = 0, uint8__Validity = 0):
            self.uint8__Termination = uint8__Termination
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Termination)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sRS485Cfg()
    
            currentPos = pos
            
            (resultInstance.uint8__Termination, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 2
    
    class struct_sObcCfg:
        def __init__(self, uint8__Addr1 = 0, uint8__Variant1 = 0, uint8__EPSOut1 = 0, uint8__Addr2 = 0, uint8__Variant2 = 0, uint8__EPSOut2 = 0, uint16__PingTimeoutS = 0, uint8__RstRetry = 0, uint8__PingPeriod = 0, uint8__Validity = 0):
            self.uint8__Addr1 = uint8__Addr1
            self.uint8__Variant1 = uint8__Variant1
            self.uint8__EPSOut1 = uint8__EPSOut1
            self.uint8__Addr2 = uint8__Addr2
            self.uint8__Variant2 = uint8__Variant2
            self.uint8__EPSOut2 = uint8__EPSOut2
            self.uint16__PingTimeoutS = uint16__PingTimeoutS
            self.uint8__RstRetry = uint8__RstRetry
            self.uint8__PingPeriod = uint8__PingPeriod
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Addr1)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Variant1)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__EPSOut1)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Addr2)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Variant2)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__EPSOut2)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__PingTimeoutS)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__RstRetry)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__PingPeriod)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sObcCfg()
    
            currentPos = pos
            
            (resultInstance.uint8__Addr1, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Variant1, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__EPSOut1, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Addr2, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Variant2, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__EPSOut2, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__PingTimeoutS, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__RstRetry, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__PingPeriod, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 11
    
    class struct_sSatCfg:
        def __init__(self, uint64__SatID = 0, uint8__Validity = 0):
            self.uint64__SatID = uint64__SatID
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint64", self.uint64__SatID)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sSatCfg()
    
            currentPos = pos
            
            (resultInstance.uint64__SatID, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint64", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 9
    
    class struct_sEpsOutCfg:
        def __init__(self, uint8__output_normal = 0, uint8__mask_normal = 0, uint8__output_phoenix = 0, uint8__mask_phoenix = 0, uint8__Validity = 0):
            self.uint8__output_normal = uint8__output_normal
            self.uint8__mask_normal = uint8__mask_normal
            self.uint8__output_phoenix = uint8__output_phoenix
            self.uint8__mask_phoenix = uint8__mask_phoenix
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__output_normal)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__mask_normal)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__output_phoenix)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__mask_phoenix)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sEpsOutCfg()
    
            currentPos = pos
            
            (resultInstance.uint8__output_normal, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__mask_normal, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__output_phoenix, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__mask_phoenix, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 5
    
    class enum_Ant2U_Alg_State:
        ANT2U_ALG_STATE_IDLE = 0
        ANT2U_ALG_STATE_GPO_REQ = 1
        ANT2U_ALG_STATE_GPO1 = 2
        ANT2U_ALG_STATE_GPO2 = 3
        ANT2U_ALG_STATE_GPO3 = 4
        ANT2U_ALG_STATE_MCU_REQ = 5
        ANT2U_ALG_STATE_MCU1 = 6
        ANT2U_ALG_STATE_MCU2 = 7
        ANT2U_ALG_STATE_GET_STAT = 8
        ANT2U_ALG_STATE_WAIT_RESP = 9
        ANT2U_ALG_STATE_TIMEOUT = 10
        ANT2U_ALG_STATE_END = 11
    
        ValuesDict = {
            ANT2U_ALG_STATE_IDLE : 'ANT2U_ALG_STATE_IDLE', 
            ANT2U_ALG_STATE_GPO_REQ : 'ANT2U_ALG_STATE_GPO_REQ', 
            ANT2U_ALG_STATE_GPO1 : 'ANT2U_ALG_STATE_GPO1', 
            ANT2U_ALG_STATE_GPO2 : 'ANT2U_ALG_STATE_GPO2', 
            ANT2U_ALG_STATE_GPO3 : 'ANT2U_ALG_STATE_GPO3', 
            ANT2U_ALG_STATE_MCU_REQ : 'ANT2U_ALG_STATE_MCU_REQ', 
            ANT2U_ALG_STATE_MCU1 : 'ANT2U_ALG_STATE_MCU1', 
            ANT2U_ALG_STATE_MCU2 : 'ANT2U_ALG_STATE_MCU2', 
            ANT2U_ALG_STATE_GET_STAT : 'ANT2U_ALG_STATE_GET_STAT', 
            ANT2U_ALG_STATE_WAIT_RESP : 'ANT2U_ALG_STATE_WAIT_RESP', 
            ANT2U_ALG_STATE_TIMEOUT : 'ANT2U_ALG_STATE_TIMEOUT', 
            ANT2U_ALG_STATE_END : 'ANT2U_ALG_STATE_END'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.enum_Ant2U_Alg_State()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_UHF.enum_Ant2U_Alg_State.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_UHF.enum_Ant2U_Alg_State.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_Ant2U_deployment:
        ANT2U_DEPLOYMENT_ENABLED = 90
        ANT2U_DEPLOYMENT_DISABLED = 0
    
        ValuesDict = {
            ANT2U_DEPLOYMENT_ENABLED : 'ANT2U_DEPLOYMENT_ENABLED', 
            ANT2U_DEPLOYMENT_DISABLED : 'ANT2U_DEPLOYMENT_DISABLED'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.enum_Ant2U_deployment()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_UHF.enum_Ant2U_deployment.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_UHF.enum_Ant2U_deployment.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_s2UAntennaCfg:
        def __init__(self, e__Ant2U_deployment__Enable = 0, uint8__MACAddr = 0, uint8__Robust = 0, uint8__AlgCheckDelay = 0, uint16__AlgTimeout = 0, uint16__RemainingBootCount = 0, e__Ant2U_Alg_State__State = 0, uint8__Validity = 0):
            self.e__Ant2U_deployment__Enable = e__Ant2U_deployment__Enable
            self.uint8__MACAddr = uint8__MACAddr
            self.uint8__Robust = uint8__Robust
            self.uint8__AlgCheckDelay = uint8__AlgCheckDelay
            self.uint16__AlgTimeout = uint16__AlgTimeout
            self.uint16__RemainingBootCount = uint16__RemainingBootCount
            self.e__Ant2U_Alg_State__State = e__Ant2U_Alg_State__State
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_UHF.enum_Ant2U_deployment(self.e__Ant2U_deployment__Enable).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__MACAddr)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Robust)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__AlgCheckDelay)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__AlgTimeout)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__RemainingBootCount)
            
            result += FP_API_UHF.enum_Ant2U_Alg_State(self.e__Ant2U_Alg_State__State).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_s2UAntennaCfg()
    
            currentPos = pos
            
            (resultInstance.e__Ant2U_deployment__Enable, bytesProcessed) = FP_API_UHF.enum_Ant2U_deployment.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__MACAddr, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Robust, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__AlgCheckDelay, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__AlgTimeout, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__RemainingBootCount, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__Ant2U_Alg_State__State, bytesProcessed) = FP_API_UHF.enum_Ant2U_Alg_State.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 10
    
    class struct_sAutomatedBeaconCfg:
        def __init__(self, uint64__EnPhoenix = 0, uint64__EnNormal = 0, uint8__Validity = 0):
            self.uint64__EnPhoenix = uint64__EnPhoenix
            self.uint64__EnNormal = uint64__EnNormal
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint64", self.uint64__EnPhoenix)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint64", self.uint64__EnNormal)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sAutomatedBeaconCfg()
    
            currentPos = pos
            
            (resultInstance.uint64__EnPhoenix, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint64", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint64__EnNormal, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint64", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 17
    
    class struct_sOutputPowerCfg:
        def __init__(self, uint8__Value = 0, uint32__Reserved = 0, uint8__Validity = 0):
            self.uint8__Value = uint8__Value
            self.uint32__Reserved = uint32__Reserved
            self.uint8__Validity = uint8__Validity
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Value)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__Reserved)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Validity)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sOutputPowerCfg()
    
            currentPos = pos
            
            (resultInstance.uint8__Value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__Reserved, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Validity, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 6
    
    class struct_sCounters:
        def __init__(self, uint32__POR = 0, uint32__MAC_Collisions = 0, uint32__MAC_fails = 0, uint32__GS_Handshakes = 0, uint32__NvMWriteFails = 0, uint32__NvMReadFails = 0, uint32__NvMDefaultEntry = 0, uint32__IntFRAM_corruptions = 0, uint32__ExtFRAM_corruptions = 0, uint32__ExtFRAM_gone = 0):
            self.uint32__POR = uint32__POR
            self.uint32__MAC_Collisions = uint32__MAC_Collisions
            self.uint32__MAC_fails = uint32__MAC_fails
            self.uint32__GS_Handshakes = uint32__GS_Handshakes
            self.uint32__NvMWriteFails = uint32__NvMWriteFails
            self.uint32__NvMReadFails = uint32__NvMReadFails
            self.uint32__NvMDefaultEntry = uint32__NvMDefaultEntry
            self.uint32__IntFRAM_corruptions = uint32__IntFRAM_corruptions
            self.uint32__ExtFRAM_corruptions = uint32__ExtFRAM_corruptions
            self.uint32__ExtFRAM_gone = uint32__ExtFRAM_gone
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__POR)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__MAC_Collisions)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__MAC_fails)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__GS_Handshakes)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__NvMWriteFails)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__NvMReadFails)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__NvMDefaultEntry)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__IntFRAM_corruptions)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__ExtFRAM_corruptions)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__ExtFRAM_gone)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sCounters()
    
            currentPos = pos
            
            (resultInstance.uint32__POR, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__MAC_Collisions, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__MAC_fails, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__GS_Handshakes, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__NvMWriteFails, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__NvMReadFails, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__NvMDefaultEntry, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__IntFRAM_corruptions, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__ExtFRAM_corruptions, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__ExtFRAM_gone, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 40
    
    class enum_KeyServiceID:
        KEYSERVICEID_MKEY = 0
        KEYSERVICEID_UNUSED = 1
        KEYSERVICEID_AIRMAC = 2
        KEYSERVICEID_AX25 = 3
    
        ValuesDict = {
            KEYSERVICEID_MKEY : 'KEYSERVICEID_MKEY', 
            KEYSERVICEID_UNUSED : 'KEYSERVICEID_UNUSED', 
            KEYSERVICEID_AIRMAC : 'KEYSERVICEID_AIRMAC', 
            KEYSERVICEID_AX25 : 'KEYSERVICEID_AX25'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.enum_KeyServiceID()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_UHF.enum_KeyServiceID.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_UHF.enum_KeyServiceID.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_sCipherKeySlot:
        def __init__(self, e__KeyServiceID__ServiceID = 0, uint8__SlotID = 0, a__uint8__32__Data = [], uint8__Size = 0):
            self.e__KeyServiceID__ServiceID = e__KeyServiceID__ServiceID
            self.uint8__SlotID = uint8__SlotID
            self.a__uint8__32__Data = a__uint8__32__Data
            self.uint8__Size = uint8__Size
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_UHF.enum_KeyServiceID(self.e__KeyServiceID__ServiceID).serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__SlotID)
            actualLen = len(self.a__uint8__32__Data)
            
            result += SerDesHelpers.serdesType_basicArray.serialize("uint8", self.a__uint8__32__Data, 32)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.uint8__Size)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_UHF.struct_sCipherKeySlot()
    
            currentPos = pos
            
            (resultInstance.e__KeyServiceID__ServiceID, bytesProcessed) = FP_API_UHF.enum_KeyServiceID.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__SlotID, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.a__uint8__32__Data, bytesProcessed) = SerDesHelpers.serdesType_basicArray.deserialize("uint8", data, currentPos, 32)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint8__Size, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 35
    

    ############################################################################################################
    """
    Request function for FIDL method: WriteSCW
        - function ID: 00000001
        - description: Write Status control word
    """
    def req_WriteSCW(self, s__Scw):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000001
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Scw.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000001, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteSCW
        - function ID: 00000001
        - description: Write Status control word
    """
    def resp_WriteSCW(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000001):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadSCW
        - function ID: 00000002
        - description: Read Status control word
    """
    def req_ReadSCW(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
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
    Response function for FIDL method: ReadSCW
        - function ID: 00000002
        - description: Read Status control word
    """
    def resp_ReadSCW(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000002):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_StatusControlWord.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteRfConfig
        - function ID: 00000003
        - description: Write RF Config
    """
    def req_WriteRfConfig(self, s__RfConfig):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000003
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__RfConfig.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000003, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteRfConfig
        - function ID: 00000003
        - description: Write RF Config
    """
    def resp_WriteRfConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000003):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadRfConfig
        - function ID: 00000004
        - description: Read RF Config
    """
    def req_ReadRfConfig(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000004
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000004, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadRfConfig
        - function ID: 00000004
        - description: Read RF Config
    """
    def resp_ReadRfConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000004):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sRFConfig.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadUpTime
        - function ID: 00000005
        - description: Read Uptime
    """
    def req_ReadUpTime(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
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
    Response function for FIDL method: ReadUpTime
        - function ID: 00000005
        - description: Read Uptime
    """
    def resp_ReadUpTime(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000005):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sUpTime.deserialize(data, currentPos)
        responseInstance["s__UpTime"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadNumberOfTxPackets
        - function ID: 00000006
        - description: Read Number Of Tx Packets
    """
    def req_ReadNumberOfTxPackets(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
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
    Response function for FIDL method: ReadNumberOfTxPackets
        - function ID: 00000006
        - description: Read Number Of Tx Packets
    """
    def resp_ReadNumberOfTxPackets(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000006):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__Packets"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadNumberOfRxPackets
        - function ID: 00000007
        - description: Read Number Of Rx Packets
    """
    def req_ReadNumberOfRxPackets(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
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
    Response function for FIDL method: ReadNumberOfRxPackets
        - function ID: 00000007
        - description: Read Number Of Rx Packets
    """
    def resp_ReadNumberOfRxPackets(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000007):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__Packets"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadNumberOfRxPacketsCRCErr
        - function ID: 00000008
        - description: Read Number Of Rx Packets with CRC Error
    """
    def req_ReadNumberOfRxPacketsCRCErr(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000008
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000008, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadNumberOfRxPacketsCRCErr
        - function ID: 00000008
        - description: Read Number Of Rx Packets with CRC Error
    """
    def resp_ReadNumberOfRxPacketsCRCErr(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000008):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__Packets"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteBeaconMessageTxPeriodCfg
        - function ID: 00000009
        - description: Write Beacon Message Tx Period Configuration
    """
    def req_WriteBeaconMessageTxPeriodCfg(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000009
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000009, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteBeaconMessageTxPeriodCfg
        - function ID: 00000009
        - description: Write Beacon Message Tx Period Configuration
    """
    def resp_WriteBeaconMessageTxPeriodCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000009):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadBeaconMessageTxPeriodCfg
        - function ID: 0000000A
        - description: Read Beacon Message Tx Period Configuration
    """
    def req_ReadBeaconMessageTxPeriodCfg(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000A
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000A, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadBeaconMessageTxPeriodCfg
        - function ID: 0000000A
        - description: Read Beacon Message Tx Period Configuration
    """
    def resp_ReadBeaconMessageTxPeriodCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000A):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sBeaconMessageTxPeriodCfg.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteBeaconMessageBetweeenTxPeriodConfig
        - function ID: 0000000B
        - description: Write Beacon Message Between Tx Period Config
    """
    def req_WriteBeaconMessageBetweeenTxPeriodConfig(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000B
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000B, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteBeaconMessageBetweeenTxPeriodConfig
        - function ID: 0000000B
        - description: Write Beacon Message Between Tx Period Config
    """
    def resp_WriteBeaconMessageBetweeenTxPeriodConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000B):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadBeaconMessageBetweeenTxPeriodConfig
        - function ID: 0000000C
        - description: Read Beacon Message Between Tx Period Config
    """
    def req_ReadBeaconMessageBetweeenTxPeriodConfig(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000C
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000C, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadBeaconMessageBetweeenTxPeriodConfig
        - function ID: 0000000C
        - description: Read Beacon Message Between Tx Period Config
    """
    def resp_ReadBeaconMessageBetweeenTxPeriodConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000C):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sBeaconMessageBetweenTxPeriodCfg.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: RestoreDefaultConfig
        - function ID: 0000000D
        - description: Restore Default Config
    """
    def req_RestoreDefaultConfig(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000D
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000D, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: RestoreDefaultConfig
        - function ID: 0000000D
        - description: Restore Default Config
    """
    def resp_RestoreDefaultConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000D):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ResetCounters
        - function ID: 0000000E
        - description: Reset the error counters
    """
    def req_ResetCounters(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000E
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000E, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ResetCounters
        - function ID: 0000000E
        - description: Reset the error counters
    """
    def resp_ResetCounters(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000E):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteAntenna
        - function ID: 00000010
        - description: Write Antenna
    """
    def req_WriteAntenna(self, uint8__Algorithm):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000010
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__Algorithm)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000010, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteAntenna
        - function ID: 00000010
        - description: Write Antenna
    """
    def resp_WriteAntenna(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000010):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadAntenna
        - function ID: 00000011
        - description: Read Antenna
    """
    def req_ReadAntenna(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
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
    Response function for FIDL method: ReadAntenna
        - function ID: 00000011
        - description: Read Antenna
    """
    def resp_ReadAntenna(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000011):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sAntennaData.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: EnterLPM
        - function ID: 00000012
        - description: Enter Low Power Mode
    """
    def req_EnterLPM(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000012
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000012, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: EnterLPM
        - function ID: 00000012
        - description: Enter Low Power Mode
    """
    def resp_EnterLPM(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000012):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadLPM
        - function ID: 00000013
        - description: Read Low Power Mode
    """
    def req_ReadLPM(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
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
    Response function for FIDL method: ReadLPM
        - function ID: 00000013
        - description: Read Low Power Mode
    """
    def resp_ReadLPM(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000013):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["uint8__Mode"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteDestCallSign
        - function ID: 00000014
        - description: Write Destination Call Sign
    """
    def req_WriteDestCallSign(self, s__CallSign):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000014
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__CallSign.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000014, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteDestCallSign
        - function ID: 00000014
        - description: Write Destination Call Sign
    """
    def resp_WriteDestCallSign(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000014):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadDestCallSign
        - function ID: 00000015
        - description: Read Destination Call Sign
    """
    def req_ReadDestCallSign(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000015
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000015, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadDestCallSign
        - function ID: 00000015
        - description: Read Destination Call Sign
    """
    def resp_ReadDestCallSign(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000015):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sCallSign.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteSrcCallSign
        - function ID: 00000016
        - description: Write Source Call Sign
    """
    def req_WriteSrcCallSign(self, s__CallSign):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000016
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__CallSign.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000016, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteSrcCallSign
        - function ID: 00000016
        - description: Write Source Call Sign
    """
    def resp_WriteSrcCallSign(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000016):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadSRCCallSign
        - function ID: 00000017
        - description: Read Source Call Sign
    """
    def req_ReadSRCCallSign(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000017
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000017, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadSRCCallSign
        - function ID: 00000017
        - description: Read Source Call Sign
    """
    def resp_ReadSRCCallSign(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000017):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sCallSign.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteMorseCallSign
        - function ID: 00000018
        - description: Write Morse Call Sign
    """
    def req_WriteMorseCallSign(self, s__MorseCallSign):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000018
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__MorseCallSign.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000018, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteMorseCallSign
        - function ID: 00000018
        - description: Write Morse Call Sign
    """
    def resp_WriteMorseCallSign(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000018):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadMorseCallSign
        - function ID: 00000019
        - description: Read Morse Call Sign
    """
    def req_ReadMorseCallSign(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000019
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000019, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadMorseCallSign
        - function ID: 00000019
        - description: Read Morse Call Sign
    """
    def resp_ReadMorseCallSign(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000019):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sMorseCallSign.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteMIDIAudioBeacon
        - function ID: 0000001A
        - description: Write MIDI audio Beacon
    """
    def req_WriteMIDIAudioBeacon(self, s__Midi):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000001A
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Midi.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000001A, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteMIDIAudioBeacon
        - function ID: 0000001A
        - description: Write MIDI audio Beacon
    """
    def resp_WriteMIDIAudioBeacon(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000001A):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadMIDIAudioBeacon
        - function ID: 0000001B
        - description: Read MIDI audio Beacon
    """
    def req_ReadMIDIAudioBeacon(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000001B
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000001B, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadMIDIAudioBeacon
        - function ID: 0000001B
        - description: Read MIDI audio Beacon
    """
    def resp_ReadMIDIAudioBeacon(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000001B):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sMidiAudioBeacon.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadSWVersion
        - function ID: 0000001C
        - description: Read SW Version Build
    """
    def req_ReadSWVersion(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000001C
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000001C, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadSWVersion
        - function ID: 0000001C
        - description: Read SW Version Build
    """
    def resp_ReadSWVersion(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000001C):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sSwVersionBuild.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadPayloadSize
        - function ID: 0000001D
        - description: Read Payload Size
    """
    def req_ReadPayloadSize(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000001D
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000001D, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadPayloadSize
        - function ID: 0000001D
        - description: Read Payload Size
    """
    def resp_ReadPayloadSize(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000001D):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
        responseInstance["uint16__PayloadSize"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteBeaconMessageContentCfg
        - function ID: 0000001E
        - description: Write Beacon Message Content Config
    """
    def req_WriteBeaconMessageContentCfg(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000001E
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000001E, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteBeaconMessageContentCfg
        - function ID: 0000001E
        - description: Write Beacon Message Content Config
    """
    def resp_WriteBeaconMessageContentCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000001E):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadBeaconMessageContentCfg
        - function ID: 0000001F
        - description: Read Beacon Message Content Config
    """
    def req_ReadBeaconMessageContentCfg(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000001F
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000001F, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadBeaconMessageContentCfg
        - function ID: 0000001F
        - description: Read Beacon Message Content Config
    """
    def resp_ReadBeaconMessageContentCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000001F):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sBeaconMessageContentCfg.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteDeviceAddrConfig
        - function ID: 00000020
        - description: Write Device Address Config
    """
    def req_WriteDeviceAddrConfig(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000020
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000020, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteDeviceAddrConfig
        - function ID: 00000020
        - description: Write Device Address Config
    """
    def resp_WriteDeviceAddrConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000020):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteFRAM
        - function ID: 00000021
        - description: Write FRAM
    """
    def req_WriteFRAM(self, s__FramWriteReq):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000021
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__FramWriteReq.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000021, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteFRAM
        - function ID: 00000021
        - description: Write FRAM
    """
    def resp_WriteFRAM(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000021):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadFRAM
        - function ID: 00000022
        - description: Read FRAM
    """
    def req_ReadFRAM(self, uint32__Addr):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000022
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint32", uint32__Addr)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000022, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadFRAM
        - function ID: 00000022
        - description: Read FRAM
    """
    def resp_ReadFRAM(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000022):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sFramData.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteTransProperty
        - function ID: 00000023
        - description: Write Transceiver Property
    """
    def req_WriteTransProperty(self, s__Property):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000023
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Property.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000023, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteTransProperty
        - function ID: 00000023
        - description: Write Transceiver Property
    """
    def resp_WriteTransProperty(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000023):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadTransProperty
        - function ID: 00000024
        - description: Read Transceiver Property
    """
    def req_ReadTransProperty(self, s__Property):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000024
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Property.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000024, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadTransProperty
        - function ID: 00000024
        - description: Read Transceiver Property
    """
    def resp_ReadTransProperty(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000024):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sTransceiverProperty.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadTemp
        - function ID: 00000025
        - description: Read Temperature
    """
    def req_ReadTemp(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000025
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000025, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadTemp
        - function ID: 00000025
        - description: Read Temperature
    """
    def resp_ReadTemp(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000025):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("int16", data, currentPos)
        responseInstance["int16__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadRSSI
        - function ID: 00000026
        - description: Read Modem RSSI. Response to GET_MODEM_STATUS (0x22) command according to SI4463 specification.
    """
    def req_ReadRSSI(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000026
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000026, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadRSSI
        - function ID: 00000026
        - description: Read Modem RSSI. Response to GET_MODEM_STATUS (0x22) command according to SI4463 specification.
    """
    def resp_ReadRSSI(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000026):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sSi4463ModemStatus.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteRadioRawData
        - function ID: 00000027
        - description: Write Raw Data to Radio
    """
    def req_WriteRadioRawData(self, s__Data):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000027
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Data.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000027, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteRadioRawData
        - function ID: 00000027
        - description: Write Raw Data to Radio
    """
    def resp_WriteRadioRawData(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000027):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: Ping
        - function ID: 00000028
        - description: Ping
    """
    def req_Ping(self, s__Data):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000028
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Data.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000028, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: Ping
        - function ID: 00000028
        - description: Ping
    """
    def resp_Ping(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000028):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sPing.deserialize(data, currentPos)
        responseInstance["s__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ExBeaconSetSend
        - function ID: 00000029
        - description: Explicit beacon set and send. If there is a key with a service id 3 the beacon message will be encrypted. Encrypted data is limited to 60 bytes. Excess data will be truncated.
    """
    def req_ExBeaconSetSend(self, s__Data):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000029
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Data.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000029, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ExBeaconSetSend
        - function ID: 00000029
        - description: Explicit beacon set and send. If there is a key with a service id 3 the beacon message will be encrypted. Encrypted data is limited to 60 bytes. Excess data will be truncated.
    """
    def resp_ExBeaconSetSend(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000029):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteI2cConfig
        - function ID: 0000002A
        - description: Write i2c configuration
    """
    def req_WriteI2cConfig(self, s__Data):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000002A
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Data.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000002A, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteI2cConfig
        - function ID: 0000002A
        - description: Write i2c configuration
    """
    def resp_WriteI2cConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000002A):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadI2cConfig
        - function ID: 0000002B
        - description: Read i2c configuration
    """
    def req_ReadI2cConfig(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000002B
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000002B, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadI2cConfig
        - function ID: 0000002B
        - description: Read i2c configuration
    """
    def resp_ReadI2cConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000002B):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sI2cCfg.deserialize(data, currentPos)
        responseInstance["s__Data"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteAntennaCfg
        - function ID: 0000002C
        - description: Write antenna configuration
    """
    def req_WriteAntennaCfg(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000002C
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000002C, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteAntennaCfg
        - function ID: 0000002C
        - description: Write antenna configuration
    """
    def resp_WriteAntennaCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000002C):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadAntennaCfg
        - function ID: 0000002D
        - description: Write antenna configuration
    """
    def req_ReadAntennaCfg(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000002D
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000002D, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadAntennaCfg
        - function ID: 0000002D
        - description: Write antenna configuration
    """
    def resp_ReadAntennaCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000002D):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sAntennaCfg.deserialize(data, currentPos)
        responseInstance["s__Cfg"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteEpsCfg
        - function ID: 0000002E
        - description: Write EPS base configuration
    """
    def req_WriteEpsCfg(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000002E
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000002E, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteEpsCfg
        - function ID: 0000002E
        - description: Write EPS base configuration
    """
    def resp_WriteEpsCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000002E):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadEpsCfg
        - function ID: 0000002F
        - description: Write EPS base configuration
    """
    def req_ReadEpsCfg(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000002F
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000002F, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadEpsCfg
        - function ID: 0000002F
        - description: Write EPS base configuration
    """
    def resp_ReadEpsCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000002F):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sEpsCfg.deserialize(data, currentPos)
        responseInstance["s__Cfg"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteEpsConOpsCfg
        - function ID: 00000030
        - description: Write EPS configuration
    """
    def req_WriteEpsConOpsCfg(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000030
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000030, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteEpsConOpsCfg
        - function ID: 00000030
        - description: Write EPS configuration
    """
    def resp_WriteEpsConOpsCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000030):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadEpsConOpsCfg
        - function ID: 00000031
        - description: Read EPS configuration
    """
    def req_ReadEpsConOpsCfg(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000031
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000031, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadEpsConOpsCfg
        - function ID: 00000031
        - description: Read EPS configuration
    """
    def resp_ReadEpsConOpsCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000031):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sEpsConOpsCfg.deserialize(data, currentPos)
        responseInstance["s__Cfg"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteRs485Config
        - function ID: 00000032
        - description: Write RS485 network configuration
    """
    def req_WriteRs485Config(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000032
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000032, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteRs485Config
        - function ID: 00000032
        - description: Write RS485 network configuration
    """
    def resp_WriteRs485Config(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000032):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadRs485Config
        - function ID: 00000033
        - description: Read RS485 network configuration
    """
    def req_ReadRs485Config(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000033
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000033, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadRs485Config
        - function ID: 00000033
        - description: Read RS485 network configuration
    """
    def resp_ReadRs485Config(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000033):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sRS485Cfg.deserialize(data, currentPos)
        responseInstance["s__Cfg"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteOBCConfig
        - function ID: 00000034
        - description: Write OBC configuration
    """
    def req_WriteOBCConfig(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000034
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000034, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteOBCConfig
        - function ID: 00000034
        - description: Write OBC configuration
    """
    def resp_WriteOBCConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000034):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadOBCConfig
        - function ID: 00000035
        - description: Read OBC configuration
    """
    def req_ReadOBCConfig(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000035
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000035, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadOBCConfig
        - function ID: 00000035
        - description: Read OBC configuration
    """
    def resp_ReadOBCConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000035):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sObcCfg.deserialize(data, currentPos)
        responseInstance["s__Cfg"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteSatConfig
        - function ID: 00000036
        - description: Write Sat configuration
    """
    def req_WriteSatConfig(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000036
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000036, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteSatConfig
        - function ID: 00000036
        - description: Write Sat configuration
    """
    def resp_WriteSatConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000036):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadSatConfig
        - function ID: 00000037
        - description: Read Sat configuration
    """
    def req_ReadSatConfig(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000037
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000037, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadSatConfig
        - function ID: 00000037
        - description: Read Sat configuration
    """
    def resp_ReadSatConfig(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000037):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sSatCfg.deserialize(data, currentPos)
        responseInstance["s__Cfg"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadEpsCfgOut
        - function ID: 00000038
        - description: Read EPS output configuration
    """
    def req_ReadEpsCfgOut(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000038
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000038, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadEpsCfgOut
        - function ID: 00000038
        - description: Read EPS output configuration
    """
    def resp_ReadEpsCfgOut(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000038):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sEpsOutCfg.deserialize(data, currentPos)
        responseInstance["s__Cfg"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteEpsCfgOut
        - function ID: 00000039
        - description: Write EPS output configuration
    """
    def req_WriteEpsCfgOut(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000039
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000039, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteEpsCfgOut
        - function ID: 00000039
        - description: Write EPS output configuration
    """
    def resp_WriteEpsCfgOut(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000039):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: Write2UAntennaCfg
        - function ID: 0000003A
        - description: Write 2U antenna configuration
    """
    def req_Write2UAntennaCfg(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000003A
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000003A, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: Write2UAntennaCfg
        - function ID: 0000003A
        - description: Write 2U antenna configuration
    """
    def resp_Write2UAntennaCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000003A):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: Read2UAntennaCfg
        - function ID: 0000003B
        - description: Read 2U antenna configuration
    """
    def req_Read2UAntennaCfg(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000003B
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000003B, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: Read2UAntennaCfg
        - function ID: 0000003B
        - description: Read 2U antenna configuration
    """
    def resp_Read2UAntennaCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000003B):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_s2UAntennaCfg.deserialize(data, currentPos)
        responseInstance["s__Cfg"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteAutomatedBeaconCfg
        - function ID: 0000003C
        - description: Write automated beacons configuration
    """
    def req_WriteAutomatedBeaconCfg(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000003C
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000003C, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteAutomatedBeaconCfg
        - function ID: 0000003C
        - description: Write automated beacons configuration
    """
    def resp_WriteAutomatedBeaconCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000003C):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadAutomatedBeaconCfg
        - function ID: 0000003D
        - description: Read automated beacons configuration
    """
    def req_ReadAutomatedBeaconCfg(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000003D
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000003D, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadAutomatedBeaconCfg
        - function ID: 0000003D
        - description: Read automated beacons configuration
    """
    def resp_ReadAutomatedBeaconCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000003D):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sAutomatedBeaconCfg.deserialize(data, currentPos)
        responseInstance["s__Cfg"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteOutputPowerCfg
        - function ID: 0000003E
        - description: Write output power configuration
    """
    def req_WriteOutputPowerCfg(self, s__Cfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000003E
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__Cfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000003E, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteOutputPowerCfg
        - function ID: 0000003E
        - description: Write output power configuration
    """
    def resp_WriteOutputPowerCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000003E):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadOutputPowerCfg
        - function ID: 0000003F
        - description: Read output power configuration
    """
    def req_ReadOutputPowerCfg(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000003F
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000003F, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadOutputPowerCfg
        - function ID: 0000003F
        - description: Read output power configuration
    """
    def resp_ReadOutputPowerCfg(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000003F):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sOutputPowerCfg.deserialize(data, currentPos)
        responseInstance["s__Cfg"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadCounters
        - function ID: 00000040
        - description: Read counters
    """
    def req_ReadCounters(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000040
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000040, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadCounters
        - function ID: 00000040
        - description: Read counters
    """
    def resp_ReadCounters(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000040):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.struct_sCounters.deserialize(data, currentPos)
        responseInstance["s__Cfg"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: WriteCipherKeySlot
        - function ID: 00000041
        - description: Write cipher key slot
    """
    def req_WriteCipherKeySlot(self, s__sKeySlot):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000041
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__sKeySlot.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000041, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: WriteCipherKeySlot
        - function ID: 00000041
        - description: Write cipher key slot
    """
    def resp_WriteCipherKeySlot(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000041):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfSCipherKeySlotStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfSCipherKeySlotStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: ReadCipherKeySlotStatus
        - function ID: 00000042
        - description: Read cipher key slot status
    """
    def req_ReadCipherKeySlotStatus(self, uint8__SlotId):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000042
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__SlotId)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000042, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: ReadCipherKeySlotStatus
        - function ID: 00000042
        - description: Read cipher key slot status
    """
    def resp_ReadCipherKeySlotStatus(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000042):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfSCipherKeySlotStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfSCipherKeySlotStatus__eSlotStatus"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: EraseCipherKeySlot
        - function ID: 00000043
        - description: Erase cipher key slot
    """
    def req_EraseCipherKeySlot(self, s__sKeySlot):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000043
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__sKeySlot.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000043, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: EraseCipherKeySlot
        - function ID: 00000043
        - description: Erase cipher key slot
    """
    def resp_EraseCipherKeySlot(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000043):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfSCipherKeySlotStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfSCipherKeySlotStatus__opResult"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: AntennaDirectRelease
        - function ID: 00000044
        - description: Direct relase of antenna
    """
    def req_AntennaDirectRelease(self, s__sCfg):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_UHF_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000044
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__sCfg.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000044, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: AntennaDirectRelease
        - function ID: 00000044
        - description: Direct relase of antenna
    """
    def resp_AntennaDirectRelease(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000044):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_UHF.enum_eESSA_UhfStatus.deserialize(data, currentPos)
        responseInstance["e__eESSA_UhfStatus__opResult"] = field
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

            if fpHeaderInstance.u16ProtoId != self.const_UHF_PROTOCOL_ID:
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

