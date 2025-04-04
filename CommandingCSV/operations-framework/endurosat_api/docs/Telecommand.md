# Telecommand

The result data set, contained in the current page

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID | [optional] 
**file_upload_start** | **int** | Start time of multipart upload in progress | [optional] 
**has_file** | **bool** | Specifies if this resource has an uploaded payload file | [optional] 
**mission_database** | **str** | ID of the Mission Database where this type of telecommand is defined | [optional] 
**name** | **str** | Human friendly name of the Satellite Telecommand | 
**raw_data** | **str** | Base64 encoded value of the Telecommand&#39;s raw byte stream | [optional] 
**data** | **object** | A JSON String representation of the telecommand before binary encoding | [optional] 
**priority** | **int** | Command priority | [optional] 
**satellite** | **str** | ID of the Satellite for which the Telecommand is issued. | 
**satellite_subsystem** | **str** | ID of the Satellite Subsystem for which the Telecommand is issued. | [optional] 
**requested_satellite_pass** | **str** | ID of the Satellite Pass for which the Telecommand is scheduled. If null - Telecommand will be executed when possible | [optional] 
**executed_satellite_pass** | **str** | ID of the Satellite Pass during which the Telecommand was sent. | [optional] 
**status** | **str** | Current status of the Telecommand | [optional] 
**has_payload_file** | **bool** | Specifies if the telecommand has a payload file  | [optional] 
**expect_telemetry_response** | **bool** | Specifies if a response is expected for this telecommand as a separate telemetry value | [optional] 
**telemetry_response** | **str** | Specifies the telemetry entry that contains the response of this telecommand. Will be empty if expectTelemetryResponse is false or if expectTelemetryResponse is true but the response has not arrived yet | [optional] 
**max_tries** | **int** | Specifies the maximum number of execution attempts for the command before it is considered as failed. | [optional] 
**continue_on_fail** | **bool** | Specifies whether command execution should continue if thic command fails. | [optional] 
**execution_rules** | [**TelecommandGroundExecutionRules**](TelecommandGroundExecutionRules.md) |  | [optional] 
**satellite_execution_rule** | [**TelecommandSatelliteExecutionRule**](TelecommandSatelliteExecutionRule.md) |  | [optional] 
**executed_at_timestamp** | **int** | Time at which the Telecommand was executed by the Ground Station | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


