now new task 

Requirement 

While

- Position lights signal command state is (AUTO OR POSITION LIGHTS OR LOWBEAM)
 
When

- vehicleSpeed is less than clbHeadLampSpeedThresholdSafety AND

Vehicle Power Mode switch from (Traction ON) to (PARK ON OR LIFE ON BOARD ON OR POWER ON)

OR

- Vehicle Power Mode is (PARK ON OR LIFE ON BOARD ON OR POWER ON) and

vehicleSpeed becomes less than clbHeadLampSpeedThresholdSafety(3)


Then,

- component SHALL launch cfgBatterySavePositionLightsTimer and cfgBatterySaveLowBeamTimer2

- after cfgBatterySavePositionLightsTimer duration the component SHALL open the Position lights manager session with Usage ID assigned to POSITIONLIGHTS_USAGES_BATTERY_SAVE and with position lights request equal to OFF.
  
take timer = 5s




enumeration PositionLightsUsages {
    POSITIONLIGHTS_USAGES_NONE = 0
    POSITIONLIGHTS_USAGES_SW_UPDATE = 1
    POSITIONLIGHTS_USAGES_POWER_AUTHORIZER = 2
    POSITIONLIGHTS_USAGES_DIAG_IO_CONTROL = 16
    POSITIONLIGHTS_USAGES_POWERLOCK = 17
    POSITIONLIGHTS_USAGES_BATTERY_SAVE = 18
    POSITIONLIGHTS_USAGES_LOWBEAM = 19
    POSITIONLIGHTS_USAGES_ALS_AUTHORIZATION = 20
    POSITIONLIGHTS_USAGES_DRIVER_MANUAL = 21
    POSITIONLIGHTS_USAGES_ADR = 22
    POSITIONLIGHTS_USAGES_REMOTE_LIGHTING = 23
    POSITIONLIGHTS_USAGES_CAR_FINDER = 24
    POSITIONLIGHTS_USAGES_DEMO_MODE = 25
    POSITIONLIGHTS_USAGES_WG = 26
    POSITIONLIGHTS_USAGES_DRL = 27
}
enumeration VehiclePowerModeType {
    VEHICLEPOWERMODE_LOW_POWER = 0
    VEHICLEPOWERMODE_PARK = 1
    VEHICLEPOWERMODE_SW_UPDATE = 2
    VEHICLEPOWERMODE_LIFE_ON_BOARD = 3
    VEHICLEPOWERMODE_POWER_ON = 4
    VEHICLEPOWERMODE_TRACTION_ON = 5
    VEHICLEPOWERMODE_UNDEFINED = 7
    VEHICLEPOWERMODE_NOT_USED = 6
}
enum PositionLightsCmdState;
 
/*********        PositionLightsCmdState VALUES        *********
Name of the Data : PositionLightsCmdState
Description: 
Type: uint8
POSITION_LIGHTS_CMD_STATE_POSITION_LIGHTS= 0,
POSITION_LIGHTS_CMD_STATE_LOWBEAM= 1,
POSITION_LIGHTS_CMD_STATE_AUTO= 2,
POSITION_LIGHTS_CMD_STATE_UNAVAILABLE= 255,
**************************************************/
enum PositionLightsRequest;
 
/*********        PositionLightsRequest VALUES        *********
Name of the Data : PositionLightsRequest
Description: 
Type: uint8
POSITION_LIGHTS_REQUEST_OFF= 0,
POSITION_LIGHTS_REQUEST_ON= 1,
POSITION_LIGHTS_REQUEST_NO_REQUEST= 2,
POSITION_LIGHTS_REQUEST_UNAVAILABLE= 255,
**************************************************/
 
struct PositionLightsCmdEvent
{
    ValueState positionLightsCmdValueState;
    PositionLightsCmdState cmdState;
};
 
interface parameter Float clbHeadLampSpeedThresholdSafetyItf (init = 3.0)




Need 15 usecase sheets combination of functional and negative for the above requirement 
