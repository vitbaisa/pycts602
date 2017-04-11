registers = [
  {
    'name': 'Nilan_Bus_Version',
    'address': '000',
    'scale': '',
    'unit': '',
    'description': 'Protocol version number',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_App_VersionMajor',
    'address': '001',
    'scale': '',
    'unit': 'text',
    'description': 'Software version - major (2 character ascii text)',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_App_VersionMinor',
    'address': '002',
    'scale': '',
    'unit': 'text',
    'description': 'Software version - minor (2 character ascii text)',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_App_VersionRelease',
    'address': '003',
    'scale': '',
    'unit': 'text',
    'description': 'Software version - release (2 character ascii text)',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_UserFunc',
    'address': '100',
    'scale': '',
    'unit': '',
    'description': 'User function',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_AirFilter',
    'address': '101',
    'scale': '',
    'unit': '',
    'description': 'Air filter alarm',
    'devices': 'VPM-Comfort-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_DoorOpen',
    'address': '102',
    'scale': '',
    'unit': '',
    'description': 'Door contact ',
    'devices': 'VPM-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_Smoke',
    'address': '103',
    'scale': '',
    'unit': '',
    'description': 'Fire/Smoke alarm',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_MotorThermo',
    'address': '104',
    'scale': '',
    'unit': '',
    'description': 'Motor thermo fuse ',
    'devices': 'VPM-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_Frost_Overht',
    'address': '105',
    'scale': '',
    'unit': '',
    'description': 'Heating surface frost / overheat',
    'devices': 'VPL-VPM-Compact-Comfort-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_AirFlow',
    'address': '106',
    'scale': '',
    'unit': '',
    'description': 'Airflow monitor (guard)',
    'devices': 'VPL-VPM-Compact-Comfort-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_P_HI',
    'address': '107',
    'scale': '',
    'unit': '',
    'description': 'High pressure switch',
    'devices': 'All Plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_P_LO',
    'address': '108',
    'scale': '',
    'unit': '',
    'description': 'Low pressure switch',
    'devices': 'Not in use',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_Boil',
    'address': '109',
    'scale': '',
    'unit': '',
    'description': 'Hot water boiling',
    'devices': 'VGU-VP-Compact',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_3WayPos',
    'address': '110',
    'scale': '',
    'unit': '',
    'description': 'Hot water 3-way valve position',
    'devices': 'Not in use',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_DefrostHG',
    'address': '111',
    'scale': '',
    'unit': '',
    'description': 'Hotgas defrost type selection',
    'devices': 'Not in use',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_Defrost',
    'address': '112',
    'scale': '',
    'unit': '',
    'description': 'Defrost thermostat',
    'devices': 'VPL-VPM-VGU-VP-Compact',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_UserFunc_2',
    'address': '113',
    'scale': '',
    'unit': '',
    'description': 'User function 2',
    'devices': 'VPL-VGU-VP-Compact-Comfort',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T0_Controller',
    'address': '200',
    'scale': '100',
    'unit': '°C',
    'description': 'Controller board temperature',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T1_Intake',
    'address': '201',
    'scale': '100',
    'unit': '°C',
    'description': 'Fresh air intake temperature',
    'devices': 'VPL-VPM-VGU-VP-Compact',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T2_Inlet',
    'address': '202',
    'scale': '100',
    'unit': '°C',
    'description': 'Inlet temperature (before heater)',
    'devices': 'VPL-VPM-VP-Compact-Comfort-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T3_Exhaust',
    'address': '203',
    'scale': '100',
    'unit': '°C',
    'description': 'Room exhaust temperature',
    'devices': 'Comfort-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T4_Outlet',
    'address': '204',
    'scale': '100',
    'unit': '°C',
    'description': 'Outlet temperature',
    'devices': 'Compact-Comfort-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T5_Cond',
    'address': '205',
    'scale': '100',
    'unit': '°C',
    'description': 'Condenser temperature',
    'devices': 'VPL-VPM-VP-Compact',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T6_Evap',
    'address': '206',
    'scale': '100',
    'unit': '°C',
    'description': 'Evaporator temperature',
    'devices': 'VPL-VPM-VGU-VP-Compact',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T7_Inlet',
    'address': '207',
    'scale': '100',
    'unit': '°C',
    'description': 'Inlet temperature (after heater)',
    'devices': 'VPL-VPM-VP-Compact-Comfort-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T8_Outdoor',
    'address': '208',
    'scale': '100',
    'unit': '°C',
    'description': 'Outdoor temperature',
    'devices': 'Comfort-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T9_Heater',
    'address': '209',
    'scale': '100',
    'unit': '°C',
    'description': 'Heating surface temperature',
    'devices': 'VPL-VPM-Comfort-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T10_Extem',
    'address': '210',
    'scale': '100',
    'unit': '°C',
    'description': 'External room temperature',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T11_Top',
    'address': '211',
    'scale': '100',
    'unit': '°C',
    'description': 'Hot water top temperature',
    'devices': 'VGU-VP-Compact',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T12_Bottom',
    'address': '212',
    'scale': '100',
    'unit': '°C',
    'description': 'Hot water bottom temperature',
    'devices': 'VGU-VP-Compact',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T13_Retum',
    'address': '213',
    'scale': '100',
    'unit': '°C',
    'description': 'EK return temperature',
    'devices': 'VGU-VP',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T14_Supply',
    'address': '214',
    'scale': '100',
    'unit': '°C',
    'description': 'EK supply temperature',
    'devices': 'VGU-VP',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T15_Room',
    'address': '215',
    'scale': '100',
    'unit': '°C',
    'description': 'User panel room temperature',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_T16',
    'address': '216',
    'scale': '100',
    'unit': '°C',
    'description': 'AUX temperature (sacrificial anode)',
    'devices': 'VGU-VP-Compact',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_RH',
    'address': '221',
    'scale': '100',
    'unit': '%',
    'description': 'Humidity',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Input_0O2',
    'address': '222',
    'scale': '',
    'unit': 'ppm',
    'description': 'Carbon dioxide',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Alarm_Status',
    'address': '400',
    'scale': '',
    'unit': '',
    'description': 'Alarm state bit mask',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Alarm_List_1_ID',
    'address': '401',
    'scale': '',
    'unit': '',
    'description': 'Alarm 1 - Code',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Alarm_List_1_Date',
    'address': '402',
    'scale': '',
    'unit': '',
    'description': 'Alarm 1 - Date',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Alarm_List_1_Time',
    'address': '403',
    'scale': '',
    'unit': '',
    'description': 'Alarm 1 - Time',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Alarm_List_2_ID',
    'address': '404',
    'scale': '',
    'unit': '',
    'description': 'Alarm 2 - Code',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Alarm_List_2_Date',
    'address': '405',
    'scale': '',
    'unit': '',
    'description': 'Alarm 2 - Date',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Alarm_List_2_Time',
    'address': '406',
    'scale': '',
    'unit': '',
    'description': 'Alarm 2 - Time',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Alarm_List_3_ID',
    'address': '407',
    'scale': '',
    'unit': '',
    'description': 'Alarm 3 - Code',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Alarm_List_3_Date',
    'address': '408',
    'scale': '',
    'unit': '',
    'description': 'Alarm 3 - Date',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Alarm_List_3_Time',
    'address': '409',
    'scale': '',
    'unit': '',
    'description': 'Alarm 3 - Time',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Control_RunAct',
    'address': '1000',
    'scale': '',
    'unit': '',
    'description': 'Actual on/off state',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Control_ModeAct',
    'address': '1001',
    'scale': '',
    'unit': '',
    'description': 'Actual operation mode',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Control_State',
    'address': '1002',
    'scale': '',
    'unit': '',
    'description': 'Actual control state',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Control_SeclnState',
    'address': '1003',
    'scale': '',
    'unit': 'Sec',
    'description': 'Actual time in state',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_AirTemp_IsSummer',
    'address': '1200',
    'scale': '',
    'unit': '',
    'description': 'Summer state',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_AirTemp_Tempinlet',
    'address': '1201',
    'scale': '100',
    'unit': '°C',
    'description': 'Inlet temperature request (T7 setpoint)',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_AirTemp_TempCont',
    'address': '1202',
    'scale': '100',
    'unit': '°C',
    'description': 'Actual value for controlled temperature',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_AirTemp_TempRoom',
    'address': '1203',
    'scale': '100',
    'unit': '°C',
    'description': 'Actual room temperature (T15 or T10)',
    'devices': 'All',
    'type': 'Input'
  },
  {
    'name': 'Nilan_AirTemp_EffPct',
    'address': '1204',
    'scale': '100',
    'unit': '%',
    'description': 'Passive heat exchanger efficiency',
    'devices': 'Compact-Comfort-Comforti',
    'type': 'Input'
  },
  {
    'name': 'Nilan_AirTemp_CapSet',
    'address': '1205',
    'scale': '100',
    'unit': '%',
    'description': 'Requested capacity',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_AirTemp_CapAct',
    'address': '1206',
    'scale': '100',
    'unit': '%',
    'description': 'Actual capacity',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_LED_1',
    'address': '2000',
    'scale': '',
    'unit': '',
    'description': 'User panel indicator light',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_LED_2',
    'address': '2001',
    'scale': '',
    'unit': '',
    'description': '',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_Text_1_2',
    'address': '2002',
    'scale': '',
    'unit': 'ascii',
    'description': 'Text line 1 character 1-2',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_Text_3_4',
    'address': '2003',
    'scale': '',
    'unit': 'ascii',
    'description': '',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_Text_5_6',
    'address': '2004',
    'scale': '',
    'unit': 'ascii',
    'description': '',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_Text_7_8',
    'address': '2005',
    'scale': '',
    'unit': 'ascii',
    'description': '',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_Attr_1_8',
    'address': '2006',
    'scale': '',
    'unit': '',
    'description': 'Text line 1 flags',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_Text_9_10',
    'address': '2007',
    'scale': '',
    'unit': 'ascii',
    'description': 'ext line 2 character 9-10',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_Text_11_12',
    'address': '2008',
    'scale': '',
    'unit': 'ascii',
    'description': '',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_Text_13_14',
    'address': '2009',
    'scale': '',
    'unit': 'ascii',
    'description': '',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_Text_15_16',
    'address': '2010',
    'scale': '',
    'unit': 'ascii',
    'description': '',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Display_Attr_9_16',
    'address': '2011',
    'scale': '',
    'unit': '',
    'description': 'Text line 2 flags',
    'devices': 'All plants',
    'type': 'Input'
  },
  {
    'name': 'Nilan_Bus_Address',
    'address': '0',
    'scale': '',
    'unit': '',
    'description': 'Protocol node address (default = 30)',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_AirFlap',
    'address': '100',
    'scale': '',
    'unit': '',
    'description': 'Air flap',
    'devices': 'VPL-VPM-VGU-VP-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_SmokeFlap',
    'address': '101',
    'scale': '',
    'unit': '',
    'description': 'Fire/Smoke flap',
    'devices': 'VPM-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_BypassOpen',
    'address': '102',
    'scale': '',
    'unit': '',
    'description': 'Bypass flap open',
    'devices': 'Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_BypassClose',
    'address': '103',
    'scale': '',
    'unit': '',
    'description': 'Bypass flap close',
    'devices': 'Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_AirCircPump',
    'address': '104',
    'scale': '',
    'unit': '',
    'description': 'Air heat circulation pump',
    'devices': 'VPM-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_AirHeatAllo',
    'address': '105',
    'scale': '',
    'unit': '',
    'description': 'Air heating selected',
    'devices': 'VPL-VPM-Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_AirHeat_1',
    'address': '106',
    'scale': '',
    'unit': '',
    'description': 'Air heater relays',
    'devices': 'VPM-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_AirHeat_2',
    'address': '107',
    'scale': '',
    'unit': '',
    'description': 'Air heater relays',
    'devices': 'VPM-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_AirHeat_3',
    'address': '108',
    'scale': '',
    'unit': '',
    'description': 'Air heater relays',
    'devices': 'VPM-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_Compressor',
    'address': '109',
    'scale': '',
    'unit': '',
    'description': 'Compressor',
    'devices': 'VPL-VPM-VGU-VP-Compact',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_Compressor2',
    'address': '110',
    'scale': '',
    'unit': '',
    'description': 'Compressor 2',
    'devices': 'Not in use',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_4WayCool',
    'address': '111',
    'scale': '',
    'unit': '',
    'description': '4-way valve',
    'devices': 'VPL-VPM-VGU-Compact',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_HotgasHeat',
    'address': '112',
    'scale': '',
    'unit': '',
    'description': 'Hotgas valve - heat',
    'devices': 'VPM',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_HotgasCool',
    'address': '113',
    'scale': '',
    'unit': '',
    'description': 'Hotgas valve - cool',
    'devices': 'VPM',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_CondOpen',
    'address': '114',
    'scale': '',
    'unit': '',
    'description': 'Air condenser active',
    'devices': 'Compact',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_CondClose',
    'address': '115',
    'scale': '',
    'unit': '',
    'description': 'Air condenser inactive',
    'devices': 'Compact',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_WaterHeat',
    'address': '116',
    'scale': '',
    'unit': '',
    'description': 'Hot water heater',
    'devices': 'VGU-VP-Compact',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_3WayValve',
    'address': '117',
    'scale': '',
    'unit': '',
    'description': 'Hot water 3-way valve',
    'devices': 'Not in use',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_CenCircPump',
    'address': '118',
    'scale': '',
    'unit': '',
    'description': 'EK circulation pump',
    'devices': 'VGU-VP',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_CenHeat_1',
    'address': '119',
    'scale': '',
    'unit': '',
    'description': 'EK heater relays',
    'devices': 'VGU-VP',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_CenHeat_2',
    'address': '120',
    'scale': '',
    'unit': '',
    'description': 'EK heater relays',
    'devices': 'VGU-VP',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_CenHeat_3',
    'address': '121',
    'scale': '',
    'unit': '',
    'description': 'EK heater relays',
    'devices': 'VGU-VP',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_CenHeatExt',
    'address': '122',
    'scale': '',
    'unit': '',
    'description': 'External radiator heat',
    'devices': 'VPL-VP-Compact-Comfort',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_UserFunc',
    'address': '123',
    'scale': '',
    'unit': '',
    'description': 'User function active',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_UserFunc_2',
    'address': '124',
    'scale': '',
    'unit': '',
    'description': 'User function active',
    'devices': 'VPL-VGU-VP-Compact-Comfort',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_Defrosting',
    'address': '125',
    'scale': '',
    'unit': '',
    'description': 'Defrost function active',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_ExhaustSpeed',
    'address': '200',
    'scale': '100',
    'unit': '%',
    'description': 'Exhaust fan speed',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_InletSpeed',
    'address': '201',
    'scale': '100',
    'unit': '%',
    'description': 'Inlet fan speed',
    'devices': 'VPL-VPM-VP-Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_AirHeatCap',
    'address': '202',
    'scale': '100',
    'unit': '%',
    'description': 'Air heater capacity',
    'devices': 'VPL-VPM-Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_CenHeatCap',
    'address': '203',
    'scale': '100',
    'unit': '%',
    'description': 'Central heater capacity',
    'devices': 'VGU-VP',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_CprCap',
    'address': '204',
    'scale': '100',
    'unit': '%',
    'description': 'Compresor capacity',
    'devices': 'VPL-VPM-VGU-VP-Compact',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Output_EarthSpeed',
    'address': '205',
    'scale': '100',
    'unit': '%',
    'description': 'Earth tube air intake fan speed',
    'devices': 'VPcCoB',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Time_Second',
    'address': '300',
    'scale': '',
    'unit': 'ss',
    'description': 'Second',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Time_Minute',
    'address': '301',
    'scale': '',
    'unit': 'nn',
    'description': 'Minute',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Time_Hour',
    'address': '302',
    'scale': '',
    'unit': 'hh',
    'description': 'Hour',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Time_Day',
    'address': '303',
    'scale': '',
    'unit': 'dd',
    'description': 'Day',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Time_Month',
    'address': '304',
    'scale': '',
    'unit': 'mm',
    'description': 'Month',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Time_Year',
    'address': '305',
    'scale': '',
    'unit': 'yyyy',
    'description': 'Year',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Alarm_Reset',
    'address': '400',
    'scale': '',
    'unit': '',
    'description': 'Clear one specific alarm code or all',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_Select',
    'address': '500',
    'scale': '',
    'unit': '',
    'description': 'Week program nb. select',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_UserFuncAct',
    'address': '600',
    'scale': '',
    'unit': '',
    'description': 'User function active (See UserFuncSet)',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_UserFuncSet',
    'address': '601',
    'scale': '',
    'unit': '',
    'description': 'User function select',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_UserTimeSet',
    'address': '602',
    'scale': '',
    'unit': '',
    'description': 'Min User function period',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_UserVentSet',
    'address': '603',
    'scale': '',
    'unit': '',
    'description': 'Step User function ventilation',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_UserTempSet',
    'address': '604',
    'scale': '',
    'unit': '°C',
    'description': 'User function temperature (Extend function only)',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_UserOffsSet',
    'address': '605',
    'scale': '',
    'unit': '°C',
    'description': 'User function temperature(Offset function only)',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_User2FuncAct',
    'address': '610',
    'scale': '',
    'unit': '',
    'description': 'User function active (See UserFuncSet2)',
    'devices': 'VPL-VGU-VP-Compact-Comfort',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_User2FuncSet',
    'address': '611',
    'scale': '',
    'unit': '',
    'description': 'User function select',
    'devices': 'VPL-VGU-VP-Compact-Comfort',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_User2TimeSet',
    'address': '612',
    'scale': '',
    'unit': '',
    'description': 'Min User function period',
    'devices': 'VPL-VGU-VP-Compact-Comfort',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_User2VentSet',
    'address': '613',
    'scale': '',
    'unit': '',
    'description': 'Step User function ventilation',
    'devices': 'VPL-VGU-VP-Compact-Comfort',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_User2TempSet',
    'address': '614',
    'scale': '',
    'unit': '°C',
    'description': 'User function temperature (Extend function only)',
    'devices': 'VPL-VGU-VP-Compact-Comfort',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Program_User2OffsSet',
    'address': '615',
    'scale': '',
    'unit': '°C',
    'description': 'User function temperature(Offset function only)',
    'devices': 'VPL-VGU-VP-Compact-Comfort',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Control_Type',
    'address': '1000',
    'scale': '',
    'unit': '',
    'description': 'Machine type select',
    'devices': 'Do not use',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Control_RunSet',
    'address': '1001',
    'scale': '',
    'unit': '',
    'description': 'User on / off select',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Control_ModeSet',
    'address': '1002',
    'scale': '',
    'unit': '',
    'description': 'User operation mode select',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Control_VentSet',
    'address': '1003',
    'scale': '',
    'unit': 'Step',
    'description': 'User ventilation step select',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Control_TempSet',
    'address': '1004',
    'scale': '100',
    'unit': '°C',
    'description': 'User temperature setpoint',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Control_ServiceMode',
    'address': '1005',
    'scale': '',
    'unit': '',
    'description': 'Service mode select',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Control_ServicePct',
    'address': '1006',
    'scale': '100',
    'unit': '%',
    'description': 'Service mode capacity',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Control_Preset',
    'address': '1007',
    'scale': '',
    'unit': '',
    'description': 'Request preset to factory',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirFlow_AirExchMode',
    'address': '1100',
    'scale': '',
    'unit': '',
    'description': 'Air exchange mode',
    'devices': 'VPL-VPM-VGU-VP-',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirFlow_CoolVent',
    'address': '1101',
    'scale': '',
    'unit': 'Step',
    'description': 'Cooling high ventilation step',
    'devices': 'VPL-VPM-VP-Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirTemp_CoolSet',
    'address': '1200',
    'scale': '',
    'unit': '°C',
    'description': 'Cooling temperature setpoint select',
    'devices': 'VPL-VPM-VP-Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirTemp_TempMinSum',
    'address': '1201',
    'scale': '100',
    'unit': '°C',
    'description': 'Inlet temp. min. summer',
    'devices': 'VPL-VPM-VP-Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirTemp_TempMinWin',
    'address': '1202',
    'scale': '100',
    'unit': '°C',
    'description': 'Inlet temp. min. winter',
    'devices': 'VPL-VPM-VP-Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirTemp_TempMax',
    'address': '1203',
    'scale': '100',
    'unit': '°C',
    'description': 'Inlet temp. max. summer',
    'devices': 'VPL-VPM-VP-Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirTemp_TempMaxWin',
    'address': '1204',
    'scale': '100',
    'unit': '°C',
    'description': 'Inlet temp. max. winter',
    'devices': 'VPL-VPM-VP-Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirTemp_TempSummer',
    'address': '1205',
    'scale': '100',
    'unit': '°C',
    'description': 'Summer/winter limit',
    'devices': 'VPL-VPM-VP-Compact-Comfort-Comforti',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_HotWater_TempSet_T11',
    'address': '1700',
    'scale': '',
    'unit': '°C',
    'description': 'Top temperature setpoint',
    'devices': 'VGU-VP-Compact',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_HotWater_TempSet_T12',
    'address': '1701',
    'scale': '',
    'unit': '°C',
    'description': 'Bottom temperature setpoint',
    'devices': 'VGU-VP-Compact',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_CentralHeat_HeatExtern',
    'address': '1800',
    'scale': '',
    'unit': '°C',
    'description': 'External heating offset from room temperature setpoint',
    'devices': 'VPL-VP-Compact-VPcCoB-',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirQual_RH_VentLo',
    'address': '1910',
    'scale': '',
    'unit': 'Step',
    'description': 'Humidity low winter step select',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirQual_RH_VentHi',
    'address': '1911',
    'scale': '',
    'unit': 'Step',
    'description': 'Humidity high step select',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirQual_RH_LimLo',
    'address': '1912',
    'scale': '100',
    'unit': '%',
    'description': 'Humidity limit for low ventilation',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirQual_RH_TimeOut',
    'address': '1913',
    'scale': '',
    'unit': 'min',
    'description': 'Humidity max. time on high ventilation',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirQual_CO2_VentHi',
    'address': '1920',
    'scale': '',
    'unit': 'Step',
    'description': 'CO2 high step select',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirQual_CO2_LimLo',
    'address': '1921',
    'scale': '',
    'unit': 'ppm',
    'description': 'CO2 limit for normal ventilation',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_AirQual_0O2_LimHi',
    'address': '1922',
    'scale': '',
    'unit': 'ppm',
    'description': 'CO2 limit for high ventilation',
    'devices': 'All plants',
    'type': 'Holding'
  },
  {
    'name': 'Nilan_Display_KeyCode',
    'address': '2000',
    'scale': '',
    'unit': '',
    'description': 'User panel keypress',
    'devices': 'All plants',
    'type': 'Holding'
  }
]
