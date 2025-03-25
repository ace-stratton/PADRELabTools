# ********************************************************************************************
# * @file FileManagerClientApp.py
# * @brief MAC FP client Python implementation generator
# ********************************************************************************************
# * @version           interface FileManager v1.2
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

class FP_API_FILEMANAGER:
    def __init__(self, rawSerDesSupport : bool = False):
        self.const_FILEMANAGER_PROTOCOL_ID = 15
        self.rawSerDesSupport = rawSerDesSupport
        self.versionMajor=1
        self.versionMinor=2


        #
        # Response parsers map
        #
        self.responseParsersDict = {}
        self.responseParsersDict[0] = self.resp_fileOpen
        self.responseParsersDict[1] = self.resp_fileClose
        self.responseParsersDict[2] = self.resp_fileRead
        self.responseParsersDict[3] = self.resp_fileWrite
        self.responseParsersDict[15] = self.resp_Rename
        self.responseParsersDict[4] = self.resp_Delete
        self.responseParsersDict[5] = self.resp_fileGetSize
        self.responseParsersDict[6] = self.resp_fileGetCheckSum
        self.responseParsersDict[7] = self.resp_fileGetOpenedHandlesCount
        self.responseParsersDict[8] = self.resp_formatPartition
        self.responseParsersDict[9] = self.resp_fileDumpDirListToFile
        self.responseParsersDict[10] = self.resp_getStatistics
        self.responseParsersDict[11] = self.resp_clearStatistics
        self.responseParsersDict[12] = self.resp_sdReinit
        self.responseParsersDict[13] = self.resp_dirMake
        self.responseParsersDict[14] = self.resp_get_sd_card_status

    class enum_FManOpResult:
        FMANOPRESULT_OK = 0
        FMANOPRESULT_DISK_ERR = 1
        FMANOPRESULT_INT_ERR = 2
        FMANOPRESULT_NOT_READY = 3
        FMANOPRESULT_NO_FILE = 4
        FMANOPRESULT_NO_PATH = 5
        FMANOPRESULT_INVALID_NAME = 6
        FMANOPRESULT_DENIED = 7
        FMANOPRESULT_EXIST = 8
        FMANOPRESULT_INVALID_OBJECT = 9
        FMANOPRESULT_WRITE_PROTECTED = 10
        FMANOPRESULT_INVALID_DRIVE = 11
        FMANOPRESULT_NOT_ENABLED = 12
        FMANOPRESULT_NO_FILESYSTEM = 13
        FMANOPRESULT_MKFS_ABORTED = 14
        FMANOPRESULT_TIMEOUT = 15
        FMANOPRESULT_LOCKED = 16
        FMANOPRESULT_NOT_ENOUGH_CORE = 17
        FMANOPRESULT_TOO_MANY_OPEN_FILES = 18
        FMANOPRESULT_INVALID_PARAMETER = 19
    
        ValuesDict = {
            FMANOPRESULT_OK : 'FMANOPRESULT_OK', 
            FMANOPRESULT_DISK_ERR : 'FMANOPRESULT_DISK_ERR', 
            FMANOPRESULT_INT_ERR : 'FMANOPRESULT_INT_ERR', 
            FMANOPRESULT_NOT_READY : 'FMANOPRESULT_NOT_READY', 
            FMANOPRESULT_NO_FILE : 'FMANOPRESULT_NO_FILE', 
            FMANOPRESULT_NO_PATH : 'FMANOPRESULT_NO_PATH', 
            FMANOPRESULT_INVALID_NAME : 'FMANOPRESULT_INVALID_NAME', 
            FMANOPRESULT_DENIED : 'FMANOPRESULT_DENIED', 
            FMANOPRESULT_EXIST : 'FMANOPRESULT_EXIST', 
            FMANOPRESULT_INVALID_OBJECT : 'FMANOPRESULT_INVALID_OBJECT', 
            FMANOPRESULT_WRITE_PROTECTED : 'FMANOPRESULT_WRITE_PROTECTED', 
            FMANOPRESULT_INVALID_DRIVE : 'FMANOPRESULT_INVALID_DRIVE', 
            FMANOPRESULT_NOT_ENABLED : 'FMANOPRESULT_NOT_ENABLED', 
            FMANOPRESULT_NO_FILESYSTEM : 'FMANOPRESULT_NO_FILESYSTEM', 
            FMANOPRESULT_MKFS_ABORTED : 'FMANOPRESULT_MKFS_ABORTED', 
            FMANOPRESULT_TIMEOUT : 'FMANOPRESULT_TIMEOUT', 
            FMANOPRESULT_LOCKED : 'FMANOPRESULT_LOCKED', 
            FMANOPRESULT_NOT_ENOUGH_CORE : 'FMANOPRESULT_NOT_ENOUGH_CORE', 
            FMANOPRESULT_TOO_MANY_OPEN_FILES : 'FMANOPRESULT_TOO_MANY_OPEN_FILES', 
            FMANOPRESULT_INVALID_PARAMETER : 'FMANOPRESULT_INVALID_PARAMETER'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_FILEMANAGER.enum_FManOpResult()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_FILEMANAGER.enum_FManOpResult.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_FILEMANAGER.enum_FManOpResult.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_FManPartitions:
        FMANPARTITIONS_SD_PARTITION = 0
    
        ValuesDict = {
            FMANPARTITIONS_SD_PARTITION : 'FMANPARTITIONS_SD_PARTITION'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_FILEMANAGER.enum_FManPartitions()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_FILEMANAGER.enum_FManPartitions.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_FILEMANAGER.enum_FManPartitions.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_FManFileModeId:
        FMANFILEMODEID_OPEN_EXISTING = 0
        FMANFILEMODEID_READ = 1
        FMANFILEMODEID_WRITE = 2
        FMANFILEMODEID_CREATE_NEW = 4
        FMANFILEMODEID_CREATE_ALWAYS = 8
        FMANFILEMODEID_OPEN_ALWAYS = 16
        FMANFILEMODEID_OPEN_APPEND = 48
    
        ValuesDict = {
            FMANFILEMODEID_OPEN_EXISTING : 'FMANFILEMODEID_OPEN_EXISTING', 
            FMANFILEMODEID_READ : 'FMANFILEMODEID_READ', 
            FMANFILEMODEID_WRITE : 'FMANFILEMODEID_WRITE', 
            FMANFILEMODEID_CREATE_NEW : 'FMANFILEMODEID_CREATE_NEW', 
            FMANFILEMODEID_CREATE_ALWAYS : 'FMANFILEMODEID_CREATE_ALWAYS', 
            FMANFILEMODEID_OPEN_ALWAYS : 'FMANFILEMODEID_OPEN_ALWAYS', 
            FMANFILEMODEID_OPEN_APPEND : 'FMANFILEMODEID_OPEN_APPEND'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_FILEMANAGER.enum_FManFileModeId()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_FILEMANAGER.enum_FManFileModeId.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_FILEMANAGER.enum_FManFileModeId.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_ErrorCounters:
        def __init__(self, uint16__DISK_ERR = 0, uint16__INT_ERR = 0, uint16__NOT_READY = 0, uint16__NO_FILE = 0, uint16__NO_PATH = 0, uint16__INVALID_NAME = 0, uint16__DENIED = 0, uint16__EXIST = 0, uint16__INVALID_OBJECT = 0, uint16__WRITE_PROTECTED = 0, uint16__INVALID_DRIVE = 0, uint16__NOT_ENABLED = 0, uint16__NO_FILESYSTEM = 0, uint16__MKFS_ABORTED = 0, uint16__TIMEOUT = 0, uint16__LOCKED = 0, uint16__NOT_ENOUGH_CORE = 0, uint16__TOO_MANY_OPEN_FILES = 0, uint16__INVALID_PARAMETER = 0):
            self.uint16__DISK_ERR = uint16__DISK_ERR
            self.uint16__INT_ERR = uint16__INT_ERR
            self.uint16__NOT_READY = uint16__NOT_READY
            self.uint16__NO_FILE = uint16__NO_FILE
            self.uint16__NO_PATH = uint16__NO_PATH
            self.uint16__INVALID_NAME = uint16__INVALID_NAME
            self.uint16__DENIED = uint16__DENIED
            self.uint16__EXIST = uint16__EXIST
            self.uint16__INVALID_OBJECT = uint16__INVALID_OBJECT
            self.uint16__WRITE_PROTECTED = uint16__WRITE_PROTECTED
            self.uint16__INVALID_DRIVE = uint16__INVALID_DRIVE
            self.uint16__NOT_ENABLED = uint16__NOT_ENABLED
            self.uint16__NO_FILESYSTEM = uint16__NO_FILESYSTEM
            self.uint16__MKFS_ABORTED = uint16__MKFS_ABORTED
            self.uint16__TIMEOUT = uint16__TIMEOUT
            self.uint16__LOCKED = uint16__LOCKED
            self.uint16__NOT_ENOUGH_CORE = uint16__NOT_ENOUGH_CORE
            self.uint16__TOO_MANY_OPEN_FILES = uint16__TOO_MANY_OPEN_FILES
            self.uint16__INVALID_PARAMETER = uint16__INVALID_PARAMETER
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__DISK_ERR)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__INT_ERR)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__NOT_READY)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__NO_FILE)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__NO_PATH)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__INVALID_NAME)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__DENIED)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__EXIST)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__INVALID_OBJECT)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__WRITE_PROTECTED)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__INVALID_DRIVE)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__NOT_ENABLED)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__NO_FILESYSTEM)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__MKFS_ABORTED)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__TIMEOUT)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__LOCKED)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__NOT_ENOUGH_CORE)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__TOO_MANY_OPEN_FILES)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint16", self.uint16__INVALID_PARAMETER)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_FILEMANAGER.struct_ErrorCounters()
    
            currentPos = pos
            
            (resultInstance.uint16__DISK_ERR, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__INT_ERR, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__NOT_READY, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__NO_FILE, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__NO_PATH, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__INVALID_NAME, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__DENIED, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__EXIST, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__INVALID_OBJECT, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__WRITE_PROTECTED, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__INVALID_DRIVE, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__NOT_ENABLED, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__NO_FILESYSTEM, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__MKFS_ABORTED, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__TIMEOUT, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__LOCKED, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__NOT_ENOUGH_CORE, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__TOO_MANY_OPEN_FILES, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint16__INVALID_PARAMETER, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 38
    
    class struct_Statistics:
        def __init__(self, s__errCounters = None, int16__nestCount = 0, int16__maxNestCount = 0):
            self.s__errCounters = s__errCounters
            self.int16__nestCount = int16__nestCount
            self.int16__maxNestCount = int16__maxNestCount
    
        def serialize(self):
            result = bytearray()
    
            
            result += self.s__errCounters.serialize()
            
            result += SerDesHelpers.serdesType_basic.serialize("int16", self.int16__nestCount)
            
            result += SerDesHelpers.serdesType_basic.serialize("int16", self.int16__maxNestCount)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_FILEMANAGER.struct_Statistics()
    
            currentPos = pos
            
            (resultInstance.s__errCounters, bytesProcessed) = FP_API_FILEMANAGER.struct_ErrorCounters.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int16__nestCount, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int16", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.int16__maxNestCount, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("int16", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 42
    
    class enum_SDCardStatus:
        SDCARDSTATUS_READY = 0
        SDCARDSTATUS_NOT_INIT = 1
        SDCARDSTATUS_EJECTED = 2
        SDCARDSTATUS_ERROR = 3
    
        ValuesDict = {
            SDCARDSTATUS_READY : 'SDCARDSTATUS_READY', 
            SDCARDSTATUS_NOT_INIT : 'SDCARDSTATUS_NOT_INIT', 
            SDCARDSTATUS_EJECTED : 'SDCARDSTATUS_EJECTED', 
            SDCARDSTATUS_ERROR : 'SDCARDSTATUS_ERROR'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_FILEMANAGER.enum_SDCardStatus()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_FILEMANAGER.enum_SDCardStatus.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_FILEMANAGER.enum_SDCardStatus.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    

    ############################################################################################################
    """
    Request function for FIDL method: fileOpen
        - function ID: 00000000
        - description: Opens a file in a specified mode and provides a handle for use with other FileManager methods, e.g. fileRead, fileWrite, etc.
    """
    def req_fileOpen(self, string__filePath, uint8__mode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000000
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        actualLen = len(string__filePath)
    
        if (actualLen > 47):
            raise Exception("The maximum expected size for array argument string__filePath is 47 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basic.serialize('uint8', actualLen) + SerDesHelpers.serdesType_string.serialize(string__filePath, 47)
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__mode)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000000, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: fileOpen
        - function ID: 00000000
        - description: Opens a file in a specified mode and provides a handle for use with other FileManager methods, e.g. fileRead, fileWrite, etc.
    """
    def resp_fileOpen(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000000):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["t__uint32__handle"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_FManOpResult.deserialize(data, currentPos)
        responseInstance["e__FManOpResult__res"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: fileClose
        - function ID: 00000001
        - description: Closes an opened file and invalidates its handle.
    """
    def req_fileClose(self, t__uint32__handle):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000001
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint32", t__uint32__handle)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000001, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: fileClose
        - function ID: 00000001
        - description: Closes an opened file and invalidates its handle.
    """
    def resp_fileClose(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000001):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_FManOpResult.deserialize(data, currentPos)
        responseInstance["e__FManOpResult__res"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: fileRead
        - function ID: 00000002
        - description: Reads a block of bytes from an opened file. The file handle for this method shall be obtained via
                              fileOpen() method and the file mode shall support reading.
    """
    def req_fileRead(self, t__uint32__handle, uint32__pos, uint32__bytesToRead):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000002
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint32", t__uint32__handle)
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint32", uint32__pos)
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint32", uint32__bytesToRead)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000002, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: fileRead
        - function ID: 00000002
        - description: Reads a block of bytes from an opened file. The file handle for this method shall be obtained via
                              fileOpen() method and the file mode shall support reading.
    """
    def resp_fileRead(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000002):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["uint8__bytebuffer__dataSize"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basicArray.deserialize('uint8', data, currentPos, 230)
        responseInstance["bytebuffer__data"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__bytesRead"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_FManOpResult.deserialize(data, currentPos)
        responseInstance["e__FManOpResult__res"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: fileWrite
        - function ID: 00000003
        - description: Writes a block of bytes to an opened file. The file handle for this method shall be obtained via fileOpen() method and the file mode shall support writing.
    """
    def req_fileWrite(self, t__uint32__handle, uint32__pos, bytebuffer__data):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000003
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint32", t__uint32__handle)
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint32", uint32__pos)
        actualLen = len(bytebuffer__data)
    
        if (actualLen > 230):
            raise Exception("The maximum expected size for array argument bytebuffer__data is 230 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basic.serialize('uint8', actualLen) + SerDesHelpers.serdesType_basicArray.serialize('uint8', bytebuffer__data, 230)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000003, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: fileWrite
        - function ID: 00000003
        - description: Writes a block of bytes to an opened file. The file handle for this method shall be obtained via fileOpen() method and the file mode shall support writing.
    """
    def resp_fileWrite(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000003):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__bytesWritten"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_FManOpResult.deserialize(data, currentPos)
        responseInstance["e__FManOpResult__res"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: Rename
        - function ID: 0000000F
        - description: Renames a specified directory or file
    """
    def req_Rename(self, string__oldPath, string__newPath):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000F
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        actualLen = len(string__oldPath)
    
        if (actualLen > 47):
            raise Exception("The maximum expected size for array argument string__oldPath is 47 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basic.serialize('uint8', actualLen) + SerDesHelpers.serdesType_string.serialize(string__oldPath, 47)
        actualLen = len(string__newPath)
    
        if (actualLen > 47):
            raise Exception("The maximum expected size for array argument string__newPath is 47 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basic.serialize('uint8', actualLen) + SerDesHelpers.serdesType_string.serialize(string__newPath, 47)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000F, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: Rename
        - function ID: 0000000F
        - description: Renames a specified directory or file
    """
    def resp_Rename(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000F):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_FManOpResult.deserialize(data, currentPos)
        responseInstance["e__FManOpResult__res"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: Delete
        - function ID: 00000004
        - description: Deletes a specified file or directory
    """
    def req_Delete(self, string__Path):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000004
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        actualLen = len(string__Path)
    
        if (actualLen > 47):
            raise Exception("The maximum expected size for array argument string__Path is 47 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basic.serialize('uint8', actualLen) + SerDesHelpers.serdesType_string.serialize(string__Path, 47)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000004, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: Delete
        - function ID: 00000004
        - description: Deletes a specified file or directory
    """
    def resp_Delete(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000004):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_FManOpResult.deserialize(data, currentPos)
        responseInstance["e__FManOpResult__res"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: fileGetSize
        - function ID: 00000005
        - description: Returns the size of a specified file in bytes
    """
    def req_fileGetSize(self, string__filePath):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000005
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        actualLen = len(string__filePath)
    
        if (actualLen > 47):
            raise Exception("The maximum expected size for array argument string__filePath is 47 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basic.serialize('uint8', actualLen) + SerDesHelpers.serdesType_string.serialize(string__filePath, 47)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000005, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: fileGetSize
        - function ID: 00000005
        - description: Returns the size of a specified file in bytes
    """
    def resp_fileGetSize(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000005):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__fSize"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_FManOpResult.deserialize(data, currentPos)
        responseInstance["e__FManOpResult__res"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: fileGetCheckSum
        - function ID: 00000006
        - description: Returns a simple mod 2^32 check sum of a specified file
    """
    def req_fileGetCheckSum(self, string__filePath):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000006
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        actualLen = len(string__filePath)
    
        if (actualLen > 47):
            raise Exception("The maximum expected size for array argument string__filePath is 47 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basic.serialize('uint8', actualLen) + SerDesHelpers.serdesType_string.serialize(string__filePath, 47)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000006, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: fileGetCheckSum
        - function ID: 00000006
        - description: Returns a simple mod 2^32 check sum of a specified file
    """
    def resp_fileGetCheckSum(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000006):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__cs"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_FManOpResult.deserialize(data, currentPos)
        responseInstance["e__FManOpResult__res"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: fileGetOpenedHandlesCount
        - function ID: 00000007
        - description: Returns the number of currently opened file handles.
    """
    def req_fileGetOpenedHandlesCount(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
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
    Response function for FIDL method: fileGetOpenedHandlesCount
        - function ID: 00000007
        - description: Returns the number of currently opened file handles.
    """
    def resp_fileGetOpenedHandlesCount(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000007):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__handlesCount"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: formatPartition
        - function ID: 00000008
        - description: The operation is used to format a storage volume given its unique identifier in the system.
                              For a list of identifiers valid for a particular device, refer to the device specification.
    """
    def req_formatPartition(self, e__FManPartitions__PartitionId):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000008
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_FILEMANAGER.enum_FManPartitions(e__FManPartitions__PartitionId).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000008, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: formatPartition
        - function ID: 00000008
        - description: The operation is used to format a storage volume given its unique identifier in the system.
                              For a list of identifiers valid for a particular device, refer to the device specification.
    """
    def resp_formatPartition(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000008):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_FManOpResult.deserialize(data, currentPos)
        responseInstance["e__FManOpResult__res"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: fileDumpDirListToFile
        - function ID: 00000009
        - description: Dumps a file listing using a specified wildcard pattern to an ASCII file with a user-defined name.
    """
    def req_fileDumpDirListToFile(self, string__filePath, string__pattern):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000009
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        actualLen = len(string__filePath)
    
        if (actualLen > 47):
            raise Exception("The maximum expected size for array argument string__filePath is 47 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basic.serialize('uint8', actualLen) + SerDesHelpers.serdesType_string.serialize(string__filePath, 47)
        actualLen = len(string__pattern)
    
        if (actualLen > 47):
            raise Exception("The maximum expected size for array argument string__pattern is 47 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basic.serialize('uint8', actualLen) + SerDesHelpers.serdesType_string.serialize(string__pattern, 47)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000009, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: fileDumpDirListToFile
        - function ID: 00000009
        - description: Dumps a file listing using a specified wildcard pattern to an ASCII file with a user-defined name.
    """
    def resp_fileDumpDirListToFile(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000009):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_FManOpResult.deserialize(data, currentPos)
        responseInstance["e__FManOpResult__res"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: getStatistics
        - function ID: 0000000A
        - description: The function provides a set of statistic counters providing more insight on the type of errors occurred during file operation.
    """
    def req_getStatistics(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
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
    Response function for FIDL method: getStatistics
        - function ID: 0000000A
        - description: The function provides a set of statistic counters providing more insight on the type of errors occurred during file operation.
    """
    def resp_getStatistics(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000A):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_FILEMANAGER.struct_Statistics.deserialize(data, currentPos)
        responseInstance["s__stats"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: clearStatistics
        - function ID: 0000000B
        - description: The function clears all accummulated statistics related to file operations. The statistics is only kept in RAM until the next CPU reset, so
                              this function clears the RAM content of the statistic counters.
    """
    def req_clearStatistics(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000B
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000B, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: clearStatistics
        - function ID: 0000000B
        - description: The function clears all accummulated statistics related to file operations. The statistics is only kept in RAM until the next CPU reset, so
                              this function clears the RAM content of the statistic counters.
    """
    def resp_clearStatistics(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000B):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: sdReinit
        - function ID: 0000000C
        - description: The function executes a manual reinit of the SD card.
    """
    def req_sdReinit(self, bool__synchronousCall):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000C
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", bool__synchronousCall)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000C, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: sdReinit
        - function ID: 0000000C
        - description: The function executes a manual reinit of the SD card.
    """
    def resp_sdReinit(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000C):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["bool__status"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: dirMake
        - function ID: 0000000D
        - description: Creates a new directory. Absolute path is required.
    """
    def req_dirMake(self, string__dirName):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000D
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        actualLen = len(string__dirName)
    
        if (actualLen > 47):
            raise Exception("The maximum expected size for array argument string__dirName is 47 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basic.serialize('uint8', actualLen) + SerDesHelpers.serdesType_string.serialize(string__dirName, 47)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000D, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: dirMake
        - function ID: 0000000D
        - description: Creates a new directory. Absolute path is required.
    """
    def resp_dirMake(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000D):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_FManOpResult.deserialize(data, currentPos)
        responseInstance["e__FManOpResult__res"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: get_sd_card_status
        - function ID: 0000000E
        - description: Return true if the SD card is ready, false if the sd card is not.
    """
    def req_get_sd_card_status(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_FILEMANAGER_PROTOCOL_ID
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
    Response function for FIDL method: get_sd_card_status
        - function ID: 0000000E
        - description: Return true if the SD card is ready, false if the sd card is not.
    """
    def resp_get_sd_card_status(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000E):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_FILEMANAGER.enum_SDCardStatus.deserialize(data, currentPos)
        responseInstance["e__SDCardStatus__status"] = field
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

            if fpHeaderInstance.u16ProtoId != self.const_FILEMANAGER_PROTOCOL_ID:
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

