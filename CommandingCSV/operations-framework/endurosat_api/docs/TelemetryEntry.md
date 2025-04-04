# TelemetryEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID | [optional] 
**file_upload_start** | **int** | Start time of multipart upload in progress | [optional] 
**has_file** | **bool** | Specifies if this resource has an uploaded payload file | [optional] 
**name** | **str** | Human friendly name of the Telemetry Entry | [optional] 
**mission_database** | **str** | ID of the Mission Database where this type of telemetry entry is defined | [optional] 
**raw_data** | **str** | Base64 encoded value of the Telemetry Entry&#39;s raw byte stream if hasPayloadFile is false | [optional] 
**data** | **object** | Decoded (from the raw data) telemetry data represented as JSON String if hasPayloadFile is false | [optional] 
**received_at_timestamp** | **int** | Time at which the Telemetry Entry was received on the Ground Station | 
**satellite_pass** | **str** | ID of Satellite Pass during which the Telemetry Entry was recorded | 
**satellite** | **str** | ID of the Satellite from which the Telemetry Entry was recorded | 
**satellite_subsystem** | **str** | ID of the Satellite Subsystem from which the Telemetry Entry was recorded | [optional] 
**has_payload_file** | **bool** | Specifies if the telemetry value is a separate file (available for download from fileUrl) or contains the TM value in the same object | [optional] 
**telecommand_request** | **str** | Specifies the telecommand request to which the current telemetry entry is a response. Will be empty if the telemetry entry is not a response to a telecommand | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


