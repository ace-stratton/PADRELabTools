# ********************************************************************************************
# * @file obcClientApp.py
# * @brief MAC FP client Python implementation generator
# ********************************************************************************************
# * @version           interface obc v4.1
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

class FP_API_OBC:
    def __init__(self, rawSerDesSupport : bool = False):
        self.const_OBC_PROTOCOL_ID = 14
        self.rawSerDesSupport = rawSerDesSupport
        self.versionMajor=4
        self.versionMinor=1


        #
        # Response parsers map
        #
        self.responseParsersDict = {}
        self.responseParsersDict[14] = self.resp_get_all_gpo_values
        self.responseParsersDict[15] = self.resp_set_all_gpo_values
        self.responseParsersDict[18] = self.resp_get_i2c_pull_ups_state
        self.responseParsersDict[19] = self.resp_set_i2c_pull_ups_state
        self.responseParsersDict[24] = self.resp_get_uptime
        self.responseParsersDict[42] = self.resp_get_reset_counters
        self.responseParsersDict[43] = self.resp_clear_reset_counter
        self.responseParsersDict[54] = self.resp_trigger_reset_in_mode
        self.responseParsersDict[64] = self.resp_set_device_mac_address
        self.responseParsersDict[65] = self.resp_get_device_mac_address

    class enum_StandardResult:
        STANDARDRESULT_SUCCESS = 0
        STANDARDRESULT_ERROR = 1
        STANDARDRESULT_INVALID_ARGS = 2
        STANDARDRESULT_NOT_SUPPORTED = 3
    
        ValuesDict = {
            STANDARDRESULT_SUCCESS : 'STANDARDRESULT_SUCCESS', 
            STANDARDRESULT_ERROR : 'STANDARDRESULT_ERROR', 
            STANDARDRESULT_INVALID_ARGS : 'STANDARDRESULT_INVALID_ARGS', 
            STANDARDRESULT_NOT_SUPPORTED : 'STANDARDRESULT_NOT_SUPPORTED'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_OBC.enum_StandardResult()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_OBC.enum_StandardResult.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_OBC.enum_StandardResult.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class enum_ApplicationMode:
        APPLICATIONMODE_APPLICATION = 0
        APPLICATIONMODE_BOOTLOADER = 1
    
        ValuesDict = {
            APPLICATIONMODE_APPLICATION : 'APPLICATIONMODE_APPLICATION', 
            APPLICATIONMODE_BOOTLOADER : 'APPLICATIONMODE_BOOTLOADER'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_OBC.enum_ApplicationMode()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_OBC.enum_ApplicationMode.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_OBC.enum_ApplicationMode.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_GpoGetPortsType:
        def __init__(self, bool__gpo_port_nvm = False, bool__gpo_port_active = False):
            self.bool__gpo_port_nvm = bool__gpo_port_nvm
            self.bool__gpo_port_active = bool__gpo_port_active
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__gpo_port_nvm)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__gpo_port_active)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_OBC.struct_GpoGetPortsType()
    
            currentPos = pos
            
            (resultInstance.bool__gpo_port_nvm, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__gpo_port_active, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 2
    
    class enum_GpoSetTypes:
        GPOSETTYPES_DONT_TOUCH = 0
        GPOSETTYPES_SET = 1
        GPOSETTYPES_RESET = 2
    
        ValuesDict = {
            GPOSETTYPES_DONT_TOUCH : 'GPOSETTYPES_DONT_TOUCH', 
            GPOSETTYPES_SET : 'GPOSETTYPES_SET', 
            GPOSETTYPES_RESET : 'GPOSETTYPES_RESET'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_OBC.enum_GpoSetTypes()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_OBC.enum_GpoSetTypes.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_OBC.enum_GpoSetTypes.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    
    class struct_GpoSetPortsType:
        def __init__(self, e__GpoSetTypes__gpo_port_nvm = 0, e__GpoSetTypes__gpo_port_active = 0):
            self.e__GpoSetTypes__gpo_port_nvm = e__GpoSetTypes__gpo_port_nvm
            self.e__GpoSetTypes__gpo_port_active = e__GpoSetTypes__gpo_port_active
    
        def serialize(self):
            result = bytearray()
    
            
            result += FP_API_OBC.enum_GpoSetTypes(self.e__GpoSetTypes__gpo_port_nvm).serialize()
            
            result += FP_API_OBC.enum_GpoSetTypes(self.e__GpoSetTypes__gpo_port_active).serialize()
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_OBC.struct_GpoSetPortsType()
    
            currentPos = pos
            
            (resultInstance.e__GpoSetTypes__gpo_port_nvm, bytesProcessed) = FP_API_OBC.enum_GpoSetTypes.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.e__GpoSetTypes__gpo_port_active, bytesProcessed) = FP_API_OBC.enum_GpoSetTypes.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 2
    
    class struct_GpoPortsGetStruct:
        def __init__(self, s__gpo_1 = None, s__gpo_2 = None, s__gpo_3 = None, s__gpo_5 = None, s__gpo_4_6 = None, s__gpo_7 = None, s__gpo_8 = None):
            self.s__gpo_1 = s__gpo_1
            self.s__gpo_2 = s__gpo_2
            self.s__gpo_3 = s__gpo_3
            self.s__gpo_5 = s__gpo_5
            self.s__gpo_4_6 = s__gpo_4_6
            self.s__gpo_7 = s__gpo_7
            self.s__gpo_8 = s__gpo_8
    
        def serialize(self):
            result = bytearray()
    
            
            result += self.s__gpo_1.serialize()
            
            result += self.s__gpo_2.serialize()
            
            result += self.s__gpo_3.serialize()
            
            result += self.s__gpo_5.serialize()
            
            result += self.s__gpo_4_6.serialize()
            
            result += self.s__gpo_7.serialize()
            
            result += self.s__gpo_8.serialize()
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_OBC.struct_GpoPortsGetStruct()
    
            currentPos = pos
            
            (resultInstance.s__gpo_1, bytesProcessed) = FP_API_OBC.struct_GpoGetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_2, bytesProcessed) = FP_API_OBC.struct_GpoGetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_3, bytesProcessed) = FP_API_OBC.struct_GpoGetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_5, bytesProcessed) = FP_API_OBC.struct_GpoGetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_4_6, bytesProcessed) = FP_API_OBC.struct_GpoGetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_7, bytesProcessed) = FP_API_OBC.struct_GpoGetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_8, bytesProcessed) = FP_API_OBC.struct_GpoGetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 14
    
    class struct_GpoPortsSetStruct:
        def __init__(self, s__gpo_1 = None, s__gpo_2 = None, s__gpo_3 = None, s__gpo_5 = None, s__gpo_4_6 = None, s__gpo_7 = None, s__gpo_8 = None):
            self.s__gpo_1 = s__gpo_1
            self.s__gpo_2 = s__gpo_2
            self.s__gpo_3 = s__gpo_3
            self.s__gpo_5 = s__gpo_5
            self.s__gpo_4_6 = s__gpo_4_6
            self.s__gpo_7 = s__gpo_7
            self.s__gpo_8 = s__gpo_8
    
        def serialize(self):
            result = bytearray()
    
            
            result += self.s__gpo_1.serialize()
            
            result += self.s__gpo_2.serialize()
            
            result += self.s__gpo_3.serialize()
            
            result += self.s__gpo_5.serialize()
            
            result += self.s__gpo_4_6.serialize()
            
            result += self.s__gpo_7.serialize()
            
            result += self.s__gpo_8.serialize()
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_OBC.struct_GpoPortsSetStruct()
    
            currentPos = pos
            
            (resultInstance.s__gpo_1, bytesProcessed) = FP_API_OBC.struct_GpoSetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_2, bytesProcessed) = FP_API_OBC.struct_GpoSetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_3, bytesProcessed) = FP_API_OBC.struct_GpoSetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_5, bytesProcessed) = FP_API_OBC.struct_GpoSetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_4_6, bytesProcessed) = FP_API_OBC.struct_GpoSetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_7, bytesProcessed) = FP_API_OBC.struct_GpoSetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.s__gpo_8, bytesProcessed) = FP_API_OBC.struct_GpoSetPortsType.deserialize(data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 14
    
    class struct_I2CPullUpsState:
        def __init__(self, bool__system_bus_4K7 = False, bool__system_bus_10K = False, bool__payload_bus_4K7 = False, bool__payload_bus_10K = False):
            self.bool__system_bus_4K7 = bool__system_bus_4K7
            self.bool__system_bus_10K = bool__system_bus_10K
            self.bool__payload_bus_4K7 = bool__payload_bus_4K7
            self.bool__payload_bus_10K = bool__payload_bus_10K
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__system_bus_4K7)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__system_bus_10K)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__payload_bus_4K7)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.bool__payload_bus_10K)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_OBC.struct_I2CPullUpsState()
    
            currentPos = pos
            
            (resultInstance.bool__system_bus_4K7, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__system_bus_10K, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__payload_bus_4K7, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.bool__payload_bus_10K, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 4
    
    class struct_ResetCountersInfo:
        def __init__(self, uint32__wwd = 0, uint32__iwd = 0, uint32__lpr = 0, uint32__por = 0, uint32__rst_pin = 0, uint32__bor = 0, uint32__hard_fault = 0, uint32__mem_fault = 0, uint32__bus_fault = 0, uint32__usage_fault = 0):
            self.uint32__wwd = uint32__wwd
            self.uint32__iwd = uint32__iwd
            self.uint32__lpr = uint32__lpr
            self.uint32__por = uint32__por
            self.uint32__rst_pin = uint32__rst_pin
            self.uint32__bor = uint32__bor
            self.uint32__hard_fault = uint32__hard_fault
            self.uint32__mem_fault = uint32__mem_fault
            self.uint32__bus_fault = uint32__bus_fault
            self.uint32__usage_fault = uint32__usage_fault
    
        def serialize(self):
            result = bytearray()
    
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__wwd)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__iwd)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__lpr)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__por)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__rst_pin)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__bor)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__hard_fault)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__mem_fault)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__bus_fault)
            
            result += SerDesHelpers.serdesType_basic.serialize("uint32", self.uint32__usage_fault)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_OBC.struct_ResetCountersInfo()
    
            currentPos = pos
            
            (resultInstance.uint32__wwd, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__iwd, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__lpr, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__por, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__rst_pin, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__bor, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__hard_fault, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__mem_fault, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__bus_fault, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
            
            (resultInstance.uint32__usage_fault, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
            currentPos += bytesProcessed
            
    
            # tuple[1] shall contain the total number of bytes processed by the function
            return (resultInstance, currentPos - pos)
    
        @staticmethod
        def getSize():
            return 40
    
    class enum_ResetCntrId:
        RESETCNTRID_WWD = 0
        RESETCNTRID_IWD = 1
        RESETCNTRID_LPR = 2
        RESETCNTRID_POR = 3
        RESETCNTRID_RST_PIN = 4
        RESETCNTRID_BOR = 5
        RESETCNTRID_HARD_FAULT = 6
        RESETCNTRID_MEM_FAULT = 7
        RESETCNTRID_BUS_FAULT = 8
        RESETCNTRID_USAGE_FAULT = 9
        RESETCNTRID_ALL = 10
    
        ValuesDict = {
            RESETCNTRID_WWD : 'RESETCNTRID_WWD', 
            RESETCNTRID_IWD : 'RESETCNTRID_IWD', 
            RESETCNTRID_LPR : 'RESETCNTRID_LPR', 
            RESETCNTRID_POR : 'RESETCNTRID_POR', 
            RESETCNTRID_RST_PIN : 'RESETCNTRID_RST_PIN', 
            RESETCNTRID_BOR : 'RESETCNTRID_BOR', 
            RESETCNTRID_HARD_FAULT : 'RESETCNTRID_HARD_FAULT', 
            RESETCNTRID_MEM_FAULT : 'RESETCNTRID_MEM_FAULT', 
            RESETCNTRID_BUS_FAULT : 'RESETCNTRID_BUS_FAULT', 
            RESETCNTRID_USAGE_FAULT : 'RESETCNTRID_USAGE_FAULT', 
            RESETCNTRID_ALL : 'RESETCNTRID_ALL'
        }
    
        def __init__(self, value = 0):
            self.value = value
    
        def serialize(self):
            result = bytearray()
    
            result += SerDesHelpers.serdesType_basic.serialize("uint8", self.value)
    
            return result
    
        @staticmethod
        def deserialize(data, pos):
            resultInstance = FP_API_OBC.enum_ResetCntrId()
    
            (resultInstance.value, bytesProcessed) = SerDesHelpers.serdesType_basic.deserialize("uint8", data, pos)
    
            return (resultInstance, bytesProcessed)
    
        def getSymbolicName(self):
            return FP_API_OBC.enum_ResetCntrId.ValuesDict[self.value]
    
        @staticmethod
        def getValueBySymbolicName(literalName):
            for key, value in FP_API_OBC.enum_ResetCntrId.ValuesDict.items():
                if literalName == value:
                    return key
    
        @staticmethod
        def getSize():
            return 1
    

    ############################################################################################################
    """
    Request function for FIDL method: get_all_gpo_values
        - function ID: 0000000E
        - description: Provides all OBC general purpose outputs 1-8
    """
    def req_get_all_gpo_values(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_OBC_PROTOCOL_ID
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
    Response function for FIDL method: get_all_gpo_values
        - function ID: 0000000E
        - description: Provides all OBC general purpose outputs 1-8
    """
    def resp_get_all_gpo_values(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_OBC_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000E):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_OBC.struct_GpoPortsGetStruct.deserialize(data, currentPos)
        responseInstance["s__gpo"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_OBC.enum_StandardResult.deserialize(data, currentPos)
        responseInstance["e__StandardResult__result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: set_all_gpo_values
        - function ID: 0000000F
        - description: Sets all GPOs both active and nvm persistant
    """
    def req_set_all_gpo_values(self, s__gpo):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_OBC_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000000F
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__gpo.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000000F, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: set_all_gpo_values
        - function ID: 0000000F
        - description: Sets all GPOs both active and nvm persistant
    """
    def resp_set_all_gpo_values(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_OBC_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000000F):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_OBC.enum_StandardResult.deserialize(data, currentPos)
        responseInstance["e__StandardResult__result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: get_i2c_pull_ups_state
        - function ID: 00000012
        - description: Obtains information on state of the I2C Pull-Up resistors for system and
                              customer payload buses
    """
    def req_get_i2c_pull_ups_state(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_OBC_PROTOCOL_ID
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
    Response function for FIDL method: get_i2c_pull_ups_state
        - function ID: 00000012
        - description: Obtains information on state of the I2C Pull-Up resistors for system and
                              customer payload buses
    """
    def resp_get_i2c_pull_ups_state(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_OBC_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000012):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_OBC.struct_I2CPullUpsState.deserialize(data, currentPos)
        responseInstance["s__nvm_pull_ups_state"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_OBC.struct_I2CPullUpsState.deserialize(data, currentPos)
        responseInstance["s__io_pull_ups_state"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: set_i2c_pull_ups_state
        - function ID: 00000013
        - description: Reconfigures the state of the I2C Pull-Up resistors for system and
                              customer payload buses
    """
    def req_set_i2c_pull_ups_state(self, s__pull_up_state):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_OBC_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000013
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += s__pull_up_state.serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000013, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: set_i2c_pull_ups_state
        - function ID: 00000013
        - description: Reconfigures the state of the I2C Pull-Up resistors for system and
                              customer payload buses
    """
    def resp_set_i2c_pull_ups_state(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_OBC_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000013):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_OBC.struct_I2CPullUpsState.deserialize(data, currentPos)
        responseInstance["s__pull_ups_io_state"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: get_uptime
        - function ID: 00000018
        - description: Obtains the up time of the OBC since last reset.
    """
    def req_get_uptime(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_OBC_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000018
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000018, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: get_uptime
        - function ID: 00000018
        - description: Obtains the up time of the OBC since last reset.
    """
    def resp_get_uptime(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_OBC_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000018):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint32", data, currentPos)
        responseInstance["uint32__uptime"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: get_reset_counters
        - function ID: 0000002A
        - description: Obtains the current values of the MCU reset counters
    """
    def req_get_reset_counters(self):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_OBC_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000002A
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000002A, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: get_reset_counters
        - function ID: 0000002A
        - description: Obtains the current values of the MCU reset counters
    """
    def resp_get_reset_counters(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_OBC_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000002A):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_OBC.struct_ResetCountersInfo.deserialize(data, currentPos)
        responseInstance["s__status"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: clear_reset_counter
        - function ID: 0000002B
        - description: Clears a given MCU reset counter
    """
    def req_clear_reset_counter(self, e__ResetCntrId__id):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_OBC_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x0000002B
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_OBC.enum_ResetCntrId(e__ResetCntrId__id).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x0000002B, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: clear_reset_counter
        - function ID: 0000002B
        - description: Clears a given MCU reset counter
    """
    def resp_clear_reset_counter(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_OBC_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x0000002B):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_OBC.enum_StandardResult.deserialize(data, currentPos)
        responseInstance["e__StandardResult__op_result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: trigger_reset_in_mode
        - function ID: 00000036
        - description: Triggers a reset of the OBC starting with the specified APP mode
    """
    def req_trigger_reset_in_mode(self, e__ApplicationMode__start_mode):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_OBC_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000036
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += FP_API_OBC.enum_ApplicationMode(e__ApplicationMode__start_mode).serialize()
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000036, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: trigger_reset_in_mode
        - function ID: 00000036
        - description: Triggers a reset of the OBC starting with the specified APP mode
    """
    def resp_trigger_reset_in_mode(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_OBC_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000036):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_OBC.enum_StandardResult.deserialize(data, currentPos)
        responseInstance["e__StandardResult__op_result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: set_device_mac_address
        - function ID: 00000040
        - description: Update the MAC addres in the mac address book of the OBC NVM.
    """
    def req_set_device_mac_address(self, uint8__new_mac_address, uint8__device_id):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_OBC_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000040
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__new_mac_address)
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__device_id)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000040, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: set_device_mac_address
        - function ID: 00000040
        - description: Update the MAC addres in the mac address book of the OBC NVM.
    """
    def resp_set_device_mac_address(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_OBC_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000040):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = FP_API_OBC.enum_StandardResult.deserialize(data, currentPos)
        responseInstance["e__StandardResult__op_result"] = field
        currentPos += bytesProcessed
    
        return responseInstance

    ############################################################################################################
    """
    Request function for FIDL method: get_device_mac_address
        - function ID: 00000041
        - description: Read the MAC addres in the mac address book of the OBC NVM.
    """
    def req_get_device_mac_address(self, uint8__device_id):
        requestBytes = bytearray()
    
        if not self.rawSerDesSupport:
            fpHeaderInstance = SerDesHelpers.struct_FPHeader()
    
            fpHeaderInstance.u16ProtoId = self.const_OBC_PROTOCOL_ID
            fpHeaderInstance.u32FuncId = 0x00000041
            fpHeaderInstance.u16seqId = 0
            fpHeaderInstance.u8ErrCode = 0
    
            requestBytes += fpHeaderInstance.serialize()
    
        requestBytes += SerDesHelpers.serdesType_basic.serialize("uint8", uint8__device_id)
    
        if not self.rawSerDesSupport:
            return requestBytes
        else:
            return (0x00000041, requestBytes)

    ############################################################################################################
    """
    Response function for FIDL method: get_device_mac_address
        - function ID: 00000041
        - description: Read the MAC addres in the mac address book of the OBC NVM.
    """
    def resp_get_device_mac_address(self, data):
        # (key, value) = (output arg name, output arg data)
        responseInstance = {}
    
        if not self.rawSerDesSupport:
            fpHeaderInstance, headerBytesProcessed = SerDesHelpers.struct_FPHeader.deserialize(data, 0)
    
            if (fpHeaderInstance.u16ProtoId != self.const_OBC_PROTOCOL_ID) or (fpHeaderInstance.u32FuncId != 0x00000041):
               raise Exception("Protocol ID and/or Function ID do not match to the called response method!")
    
            currentPos = headerBytesProcessed
        else:
            currentPos = 0
    
    
        field, bytesProcessed = SerDesHelpers.serdesType_basic.deserialize("uint8", data, currentPos)
        responseInstance["uint8__mac_address"] = field
        currentPos += bytesProcessed
    
        field, bytesProcessed = FP_API_OBC.enum_StandardResult.deserialize(data, currentPos)
        responseInstance["e__StandardResult__op_result"] = field
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

            if fpHeaderInstance.u16ProtoId != self.const_OBC_PROTOCOL_ID:
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

