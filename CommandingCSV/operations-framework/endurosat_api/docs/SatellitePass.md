# SatellitePass


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID | [optional] 
**file_upload_start** | **int** | Start time of multipart upload in progress | [optional] 
**has_file** | **bool** | Specifies if this resource has an uploaded payload file | [optional] 
**status** | **str** | Status of the Satellite Pass - SCHEDULED | IN_PROGRESS | FINISHED_SUCCESSFULLY | FINISHED_WITH_ERRORS | CANCELED | 
**satellite** | **str** | ID of the Satellite for this Pass | 
**ground_station** | **str** | ID of the Ground Station above which the satellite will pass | 
**aos** | **int** | Aquisition of Signal Time for the Satellite Pass | 
**los** | **int** | Loss of Signal Time for the Satellite Pass | 
**max_elevation** | **float** | Max Elevation in degrees of the Satellite Pass | 
**tle1** | **str** | TLE Line 1 | [optional] 
**tle2** | **str** | TLE Line 2 | [optional] 
**extra_attributes** | **object** | Configuration of the action | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


