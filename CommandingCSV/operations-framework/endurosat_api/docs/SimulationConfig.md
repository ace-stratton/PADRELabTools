# SimulationConfig

Configuration for the simulation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sim_mode** | **str** | 1: ADCS, 2: STMA] (adcs only, OBC state machine) | 
**initial_mode** | **str** | Initial operational mode, can only be &#39;safe&#39; or &#39;idle&#39;. Only relevant for simmode 2. | [optional] 
**number_of_orbits** | **int** | Maximum number of orbits, should be bigger or equal to the commanded time of the operational modes in OBC yaml [if not only adcs sim] | [optional] 
**time_step** | **int** | [s] subsystems loop period | [optional] 
**max_integration_time_step** | **int** | [s] maximum integration timestep | [optional] 
**start_with_tumbling** | **bool** | if True, no torques will be acting on the satellite (this setting is mainly for verification tests) | [optional] 
**initial_rate** | **list[float]** | [deg/s] Initial rate in the body frame wrt ECI if starting with tumbling if startWithTumbling set to true. | [optional] 
**no_torques** | **bool** | If true, no torques will be acting on the satellite | [optional] 
**no_disturb_torques** | **bool** | If true, there will be no disturbance torques simulated | [optional] 
**rw_imbalance_model** | **str** | Reaction wheel imbalance model [&#39;ADVANCED&#39;, &#39;SIMPLE&#39;, &#39;NOT&#39;] | [optional] 
**stop_on_rw_saturation** | **bool** | End the simulation if RWs are saturated; else, continue | [optional] 
**include_sensor_views** | **bool** | If True, the orientation of the sensors in the satellite will matter wrt sun earth blocking | [optional] 
**include_est_ctrl_compatibility** | **bool** | If True, the Opsim will check the compatibility between control and estimation modes and transitions. if false, everything is allowed | [optional] 
**nadir_mode_in_eclipse** | **bool** | Switch to nadir mode during eclipse, when sun-pointing and not SimMode ADCS | [optional] 
**mode_transition_threshold** | **float** | [deg] when pointing error over sample period lower than this threshold after a mode transition, new mode is active and transition is completed | [optional] 
**mode_transition_samples** | **int** | number of samples for the above threshold (modeTransitionThreshold) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


