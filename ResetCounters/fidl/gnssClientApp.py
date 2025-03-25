# ********************************************************************************************
# * @file gnssClientApp.py
# * @brief MAC FP client Python implementation generator
# ********************************************************************************************
# * @version           interface gnss v1.2
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

class FP_API_GNSS:
    def __init__(self, rawSerDesSupport : bool = False):
        self.const_GNSS_PROTOCOL_ID = 23
        self.rawSerDesSupport = rawSerDesSupport
        self.versionMajor=1
        self.versionMinor=2


        #
        # Response parsers map
        #
        self.responseParsersDict = {}
        self.responseParsersDict[1] = self.resp_set_power
        self.responseParsersDict[2] = self.resp_get_power
        self.responseParsersDict[3] = self.resp_request_command_execution
        self.responseParsersDict[4] = self.resp_get_command_execution_status
        self.responseParsersDict[5] = self.resp_set_gnss_uart_baudrate
        self.responseParsersDict[6] = self.resp_get_gnss_uart_baudrate

    class enum_Operation:
        OPERATION_ERROR = 0
        OPERATION_OK = 1
    
        ValuesDict = {
            OPERATION_ERROR : 'OPERATION_ERROR', 
            OPERATION_OK : 'OPERATION_OK'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_GNSS.enum_Operation()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_GNSS.enum_Operation.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_GNSS.enum_Operation.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_Power:
        POWER_OFF = 0
        POWER_ON = 1
    
        ValuesDict = {
            POWER_OFF : 'POWER_OFF', 
            POWER_ON : 'POWER_ON'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_GNSS.enum_Power()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_GNSS.enum_Power.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_GNSS.enum_Power.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_CommandStatus:
        COMMANDSTATUS_OK = 0
        COMMANDSTATUS_ERROR = 1
        COMMANDSTATUS_QUEUE_FULL = 2
        COMMANDSTATUS_WRONG_PARAMS = 3
        COMMANDSTATUS_PROCESSING = 4
        COMMANDSTATUS_PENDING = 5
        COMMANDSTATUS_NOT_FOUND = 6
        COMMANDSTATUS_TIMED_OUT = 7
        COMMANDSTATUS_MUTEX_FAIL = 8
    
        ValuesDict = {
            COMMANDSTATUS_OK : 'COMMANDSTATUS_OK', 
            COMMANDSTATUS_ERROR : 'COMMANDSTATUS_ERROR', 
            COMMANDSTATUS_QUEUE_FULL : 'COMMANDSTATUS_QUEUE_FULL', 
            COMMANDSTATUS_WRONG_PARAMS : 'COMMANDSTATUS_WRONG_PARAMS', 
            COMMANDSTATUS_PROCESSING : 'COMMANDSTATUS_PROCESSING', 
            COMMANDSTATUS_PENDING : 'COMMANDSTATUS_PENDING', 
            COMMANDSTATUS_NOT_FOUND : 'COMMANDSTATUS_NOT_FOUND', 
            COMMANDSTATUS_TIMED_OUT : 'COMMANDSTATUS_TIMED_OUT', 
            COMMANDSTATUS_MUTEX_FAIL : 'COMMANDSTATUS_MUTEX_FAIL'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_GNSS.enum_CommandStatus()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_GNSS.enum_CommandStatus.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_GNSS.enum_CommandStatus.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_TimeStruct:
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
            resultInstance = FP_API_GNSS.struct_TimeStruct()
    
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
    
    class enum_BaudRate:
        BAUDRATE_BAUD_9600_BPS = 0
        BAUDRATE_BAUD_19200_BPS = 1
        BAUDRATE_BAUD_38400_BPS = 2
        BAUDRATE_BAUD_57600_BPS = 3
        BAUDRATE_BAUD_115200_BPS = 4
        BAUDRATE_BAUD_230400_BPS = 5
        BAUDRATE_BAUD_460800_BPS = 6
    
        ValuesDict = {
            BAUDRATE_BAUD_9600_BPS : 'BAUDRATE_BAUD_9600_BPS', 
            BAUDRATE_BAUD_19200_BPS : 'BAUDRATE_BAUD_19200_BPS', 
            BAUDRATE_BAUD_38400_BPS : 'BAUDRATE_BAUD_38400_BPS', 
            BAUDRATE_BAUD_57600_BPS : 'BAUDRATE_BAUD_57600_BPS', 
            BAUDRATE_BAUD_115200_BPS : 'BAUDRATE_BAUD_115200_BPS', 
            BAUDRATE_BAUD_230400_BPS : 'BAUDRATE_BAUD_230400_BPS', 
            BAUDRATE_BAUD_460800_BPS : 'BAUDRATE_BAUD_460800_BPS'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_GNSS.enum_BaudRate()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_GNSS.enum_BaudRate.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_GNSS.enum_BaudRate.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    

    ############################################################################################################
    """
    Request function for FIDL method: set_power
        - function ID: 00000001
        - description: set gnss power (on/off)
    """
    def req_set_power(self, e__Power__pwr_status):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_GNSS_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000001
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_GNSS.enum_Power(e__Power__pwr_status).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000001, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: set_power
        - function ID: 00000001
        - description: set gnss power (on/off)
    """
    def resp_set_power(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_GNSS_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000001):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_GNSS.enum_Operation.deserialize(data, currentPos)
        responseInstance["e__Operation__op_status"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: get_power
        - function ID: 00000002
        - description: get gnss power status (on/off)
    """
    def req_get_power(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_GNSS_PROTOCOL_ID
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
    Response function for FIDL method: get_power
        - function ID: 00000002
        - description: get gnss power status (on/off)
    """
    def resp_get_power(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_GNSS_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000002):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_GNSS.enum_Power.deserialize(data, currentPos)
        responseInstance["e__Power__pwr_status"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_GNSS.enum_Operation.deserialize(data, currentPos)
        responseInstance["e__Operation__op_status"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: request_command_execution
        - function ID: 00000003
        - description: execute gnss command
    """
    def req_request_command_execution(self, string__cmd, uint32__timeout_ms):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_GNSS_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000003
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        actualLen = len(string__cmd)
    
        if (actualLen > 240):
            raise Exception("The maximum expected size for array argument string__cmd is 240 bytes but " + str(actualLen) + " bytes were provided.")
        requestBytes += SerDesHelpers.serdesType_basic.serialize('uint8', actualLen) + SerDesHelpers.serdesType_string.serialize(string__cmd, 240)
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint32", uint32__timeout_ms)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000003, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: request_command_execution
        - function ID: 00000003
        - description: execute gnss command
    """
    def resp_request_command_execution(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_GNSS_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000003):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["uint8__cmd_id"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_GNSS.enum_CommandStatus.deserialize(data, currentPos)
        responseInstance["e__CommandStatus__command_status"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: get_command_execution_status
        - function ID: 00000004
        - description: get gnss command status, based on command id
    """
    def req_get_command_execution_status(self, uint8__cmd_id):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_GNSS_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000004
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__cmd_id)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000004, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: get_command_execution_status
        - function ID: 00000004
        - description: get gnss command status, based on command id
    """
    def resp_get_command_execution_status(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_GNSS_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000004):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_GNSS.enum_CommandStatus.deserialize(data, currentPos)
        responseInstance["e__CommandStatus__command_status"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__duration_ms"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_GNSS.struct_TimeStruct.deserialize(data, currentPos)
        responseInstance["s__requested_time"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_GNSS.struct_TimeStruct.deserialize(data, currentPos)
        responseInstance["s__time_started"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: set_gnss_uart_baudrate
        - function ID: 00000005
        - description: Set gnss uart baud rate. This method overwrites the currently
                              saved baud rate in the NVM. Then, it attempts to re-initialize
                              the UART peripheral with the new desired baud rate.
    """
    def req_set_gnss_uart_baudrate(self, e__BaudRate__baud_rate):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_GNSS_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000005
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_GNSS.enum_BaudRate(e__BaudRate__baud_rate).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000005, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: set_gnss_uart_baudrate
        - function ID: 00000005
        - description: Set gnss uart baud rate. This method overwrites the currently
                              saved baud rate in the NVM. Then, it attempts to re-initialize
                              the UART peripheral with the new desired baud rate.
    """
    def resp_set_gnss_uart_baudrate(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_GNSS_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000005):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_GNSS.enum_Operation.deserialize(data, currentPos)
        responseInstance["e__Operation__op_status"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: get_gnss_uart_baudrate
        - function ID: 00000006
        - description: get gnss uart baud rate
    """
    def req_get_gnss_uart_baudrate(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_GNSS_PROTOCOL_ID
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
    Response function for FIDL method: get_gnss_uart_baudrate
        - function ID: 00000006
        - description: get gnss uart baud rate
    """
    def resp_get_gnss_uart_baudrate(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_GNSS_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000006):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_GNSS.enum_BaudRate.deserialize(data, currentPos)
        responseInstance["e__BaudRate__gnss_uart_baudrate_nvm"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_GNSS.enum_BaudRate.deserialize(data, currentPos)
        responseInstance["e__BaudRate__gnss_uart_baudrate_current"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_GNSS.enum_Operation.deserialize(data, currentPos)
        responseInstance["e__Operation__op_status"] = field
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

            if fpHeaderInstance.u16ProtoId != self.const_GNSS_PROTOCOL_ID:
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

