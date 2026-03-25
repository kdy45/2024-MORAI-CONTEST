
"use strict";

let MultiEgoSetting = require('./MultiEgoSetting.js');
let PREvent = require('./PREvent.js');
let SyncModeSetGear = require('./SyncModeSetGear.js');
let SyncModeRemoveObject = require('./SyncModeRemoveObject.js');
let SensorPosControl = require('./SensorPosControl.js');
let FaultStatusInfo = require('./FaultStatusInfo.js');
let IntersectionControl = require('./IntersectionControl.js');
let MoraiTLInfo = require('./MoraiTLInfo.js');
let GPSMessage = require('./GPSMessage.js');
let ObjectStatusListExtended = require('./ObjectStatusListExtended.js');
let WaitForTickResponse = require('./WaitForTickResponse.js');
let NpcGhostCmd = require('./NpcGhostCmd.js');
let IntersectionStatus = require('./IntersectionStatus.js');
let SyncModeCmd = require('./SyncModeCmd.js');
let MoraiSimProcStatus = require('./MoraiSimProcStatus.js');
let WoowaDillyStatus = require('./WoowaDillyStatus.js');
let IntscnTL = require('./IntscnTL.js');
let FaultStatusInfo_Sensor = require('./FaultStatusInfo_Sensor.js');
let FaultInjection_Response = require('./FaultInjection_Response.js');
let GhostMessage = require('./GhostMessage.js');
let DillyCmd = require('./DillyCmd.js');
let MapSpec = require('./MapSpec.js');
let SyncModeCmdResponse = require('./SyncModeCmdResponse.js');
let SyncModeInfo = require('./SyncModeInfo.js');
let MultiPlayEventResponse = require('./MultiPlayEventResponse.js');
let VehicleCollision = require('./VehicleCollision.js');
let FaultStatusInfo_Overall = require('./FaultStatusInfo_Overall.js');
let SaveSensorData = require('./SaveSensorData.js');
let SkateboardCtrlCmd = require('./SkateboardCtrlCmd.js');
let SVADC = require('./SVADC.js');
let GetTrafficLightStatus = require('./GetTrafficLightStatus.js');
let NpcGhostInfo = require('./NpcGhostInfo.js');
let SyncModeScenarioLoad = require('./SyncModeScenarioLoad.js');
let DillyCmdResponse = require('./DillyCmdResponse.js');
let SkidSteer6wUGVCtrlCmd = require('./SkidSteer6wUGVCtrlCmd.js');
let ObjectStatusExtended = require('./ObjectStatusExtended.js');
let PRStatus = require('./PRStatus.js');
let VehicleCollisionData = require('./VehicleCollisionData.js');
let ObjectStatus = require('./ObjectStatus.js');
let FaultInjection_Controller = require('./FaultInjection_Controller.js');
let SkateboardStatus = require('./SkateboardStatus.js');
let MultiPlayEventRequest = require('./MultiPlayEventRequest.js');
let MoraiSrvResponse = require('./MoraiSrvResponse.js');
let MoraiTLIndex = require('./MoraiTLIndex.js');
let ReplayInfo = require('./ReplayInfo.js');
let CtrlCmd = require('./CtrlCmd.js');
let FaultInjection_Tire = require('./FaultInjection_Tire.js');
let EgoDdVehicleStatus = require('./EgoDdVehicleStatus.js');
let SyncModeCtrlCmd = require('./SyncModeCtrlCmd.js');
let VehicleSpecIndex = require('./VehicleSpecIndex.js');
let ObjectStatusList = require('./ObjectStatusList.js');
let RadarDetection = require('./RadarDetection.js');
let Lamps = require('./Lamps.js');
let EgoVehicleStatusExtended = require('./EgoVehicleStatusExtended.js');
let TrafficLight = require('./TrafficLight.js');
let FaultInjection_Sensor = require('./FaultInjection_Sensor.js');
let PRCtrlCmd = require('./PRCtrlCmd.js');
let ERP42Info = require('./ERP42Info.js');
let ScenarioLoad = require('./ScenarioLoad.js');
let EgoVehicleStatus = require('./EgoVehicleStatus.js');
let SyncModeResultResponse = require('./SyncModeResultResponse.js');
let VehicleSpec = require('./VehicleSpec.js');
let WaitForTick = require('./WaitForTick.js');
let DdCtrlCmd = require('./DdCtrlCmd.js');
let RadarDetections = require('./RadarDetections.js');
let SkidSteer6wUGVStatus = require('./SkidSteer6wUGVStatus.js');
let SyncModeAddObject = require('./SyncModeAddObject.js');
let CollisionData = require('./CollisionData.js');
let SetTrafficLight = require('./SetTrafficLight.js');
let FaultStatusInfo_Vehicle = require('./FaultStatusInfo_Vehicle.js');
let EventInfo = require('./EventInfo.js');
let MapSpecIndex = require('./MapSpecIndex.js');
let MoraiSimProcHandle = require('./MoraiSimProcHandle.js');

module.exports = {
  MultiEgoSetting: MultiEgoSetting,
  PREvent: PREvent,
  SyncModeSetGear: SyncModeSetGear,
  SyncModeRemoveObject: SyncModeRemoveObject,
  SensorPosControl: SensorPosControl,
  FaultStatusInfo: FaultStatusInfo,
  IntersectionControl: IntersectionControl,
  MoraiTLInfo: MoraiTLInfo,
  GPSMessage: GPSMessage,
  ObjectStatusListExtended: ObjectStatusListExtended,
  WaitForTickResponse: WaitForTickResponse,
  NpcGhostCmd: NpcGhostCmd,
  IntersectionStatus: IntersectionStatus,
  SyncModeCmd: SyncModeCmd,
  MoraiSimProcStatus: MoraiSimProcStatus,
  WoowaDillyStatus: WoowaDillyStatus,
  IntscnTL: IntscnTL,
  FaultStatusInfo_Sensor: FaultStatusInfo_Sensor,
  FaultInjection_Response: FaultInjection_Response,
  GhostMessage: GhostMessage,
  DillyCmd: DillyCmd,
  MapSpec: MapSpec,
  SyncModeCmdResponse: SyncModeCmdResponse,
  SyncModeInfo: SyncModeInfo,
  MultiPlayEventResponse: MultiPlayEventResponse,
  VehicleCollision: VehicleCollision,
  FaultStatusInfo_Overall: FaultStatusInfo_Overall,
  SaveSensorData: SaveSensorData,
  SkateboardCtrlCmd: SkateboardCtrlCmd,
  SVADC: SVADC,
  GetTrafficLightStatus: GetTrafficLightStatus,
  NpcGhostInfo: NpcGhostInfo,
  SyncModeScenarioLoad: SyncModeScenarioLoad,
  DillyCmdResponse: DillyCmdResponse,
  SkidSteer6wUGVCtrlCmd: SkidSteer6wUGVCtrlCmd,
  ObjectStatusExtended: ObjectStatusExtended,
  PRStatus: PRStatus,
  VehicleCollisionData: VehicleCollisionData,
  ObjectStatus: ObjectStatus,
  FaultInjection_Controller: FaultInjection_Controller,
  SkateboardStatus: SkateboardStatus,
  MultiPlayEventRequest: MultiPlayEventRequest,
  MoraiSrvResponse: MoraiSrvResponse,
  MoraiTLIndex: MoraiTLIndex,
  ReplayInfo: ReplayInfo,
  CtrlCmd: CtrlCmd,
  FaultInjection_Tire: FaultInjection_Tire,
  EgoDdVehicleStatus: EgoDdVehicleStatus,
  SyncModeCtrlCmd: SyncModeCtrlCmd,
  VehicleSpecIndex: VehicleSpecIndex,
  ObjectStatusList: ObjectStatusList,
  RadarDetection: RadarDetection,
  Lamps: Lamps,
  EgoVehicleStatusExtended: EgoVehicleStatusExtended,
  TrafficLight: TrafficLight,
  FaultInjection_Sensor: FaultInjection_Sensor,
  PRCtrlCmd: PRCtrlCmd,
  ERP42Info: ERP42Info,
  ScenarioLoad: ScenarioLoad,
  EgoVehicleStatus: EgoVehicleStatus,
  SyncModeResultResponse: SyncModeResultResponse,
  VehicleSpec: VehicleSpec,
  WaitForTick: WaitForTick,
  DdCtrlCmd: DdCtrlCmd,
  RadarDetections: RadarDetections,
  SkidSteer6wUGVStatus: SkidSteer6wUGVStatus,
  SyncModeAddObject: SyncModeAddObject,
  CollisionData: CollisionData,
  SetTrafficLight: SetTrafficLight,
  FaultStatusInfo_Vehicle: FaultStatusInfo_Vehicle,
  EventInfo: EventInfo,
  MapSpecIndex: MapSpecIndex,
  MoraiSimProcHandle: MoraiSimProcHandle,
};
