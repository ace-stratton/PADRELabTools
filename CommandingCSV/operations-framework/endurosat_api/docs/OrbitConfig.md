# OrbitConfig

Orbit configuration for the simulation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **list[int]** | Time and date of start simulation. Format: [Y, M, D, H, M, S] | [optional] 
**tp** | **int** | Time since last perigee passage [s] | [optional] 
**sma** | **int** | Satellite altitude [km] | [optional] 
**eccentricity** | **float** | Eccentricity | [optional] 
**inclination** | **float** | Inclination [deg] | [optional] 
**aop** | **float** | Argument of Periapsis [deg] | [optional] 
**raan** | **float** | Right ascension of a.n. [deg]. (Either choose RAAN or LTAN input, if use one, set the other to null) | [optional] 
**ltan** | **float** | Float (e.g. 13.5 &#x3D; 13:30). (Either choose RAAN or LTAN input, if use one, set the other to null) | [optional] 
**separation_angle** | **float** | True anomaly difference between two satellites if intersat pointing [deg] | [optional] 
**altitude_difference** | **float** | Altitude difference between the two sats, negative difference means satellite 2 is lower [km] | [optional] 
**position_error_rtn** | **list[int]** | Position knowledge accuracy [Rmean, Rsigma, Tmean, Tsigma, Nmean, Nsigma] Radial Tangent Normal [14, 95, 1, 547, 4, 153] [m] | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


