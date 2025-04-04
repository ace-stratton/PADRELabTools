# GroundStation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object ID | [optional] 
**longitude** | **float** | Ground Station Geographic Longitude | [optional] 
**latitude** | **float** | Ground Station Geographic Latitude | [optional] 
**elevation** | **float** | Ground Station Geographic Elevation | [optional] 
**antennas** | [**dict(str, TypedDescriptor)**](TypedDescriptor.md) | Antenna Descriptions as supported by EnduroSat | [optional] 
**channels** | [**list[CommunicationChannel]**](CommunicationChannel.md) | Communication Channel Descriptions as supported by EnduroSat | [optional] 
**supported_protocols** | **list[str]** | Communication Channel Protocols as supported by EnduroSat | [optional] 
**protocols** | [**dict(str, CommunicationProtocol)**](CommunicationProtocol.md) | Communication Channel Protocols as supported by EnduroSat | [optional] 
**sockets** | [**dict(str, TypedDescriptor)**](TypedDescriptor.md) | Represent the endpoints of Streams as supported by EnduroSat | [optional] 
**satellite_streams** | **dict(str, dict(str, StreamDescriptor))** | Describes streams between satellites and the ground station | [optional] 
**user_streams** | [**dict(str, UserStreamDescriptor)**](UserStreamDescriptor.md) | Describes streams between the ground station and the Cloud layer | [optional] 
**hardware** | [**dict(str, TypedDescriptor)**](TypedDescriptor.md) | Describes the available hardware on the radio layer | [optional] 
**additional_properties** | **dict(str, str)** | Additional Properties for the configuration of the Ground Station | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


