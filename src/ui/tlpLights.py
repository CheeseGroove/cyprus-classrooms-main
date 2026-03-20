'''

Lighting Control Pages

'''
# Python imports

# Extron Library imports
from extronlib.system import MESet, Wait
from extronlib.ui import Button, Label, Level, Knob

# Project imports
from modules.helper.ModuleSupport import eventEx
from devices import devTP, devTV

import variables as var
import CommonFunctions as cf


#Preset Press

btnLights100        = Button(devTP, 201)
btnLights75         = Button(devTP, 202)
btnLights50         = Button(devTP, 203)
btnLights25         = Button(devTP, 204)
btnLightsPresent    = Button(devTP, 205)
btnLightsOff        = Button(devTP, 206)
LightPresetGroup    = MESet([btnLights100, btnLights75, btnLights50, btnLights25, btnLightsPresent, btnLightsOff,])


@eventEx(LightPresetGroup.Objects, 'Pressed')
def btnLightPresetsEvent(button: Button, state: str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(button)




#Front/Rear Zone Controls

btnLightsFrontUp    = Button(devTP, 207, repeatTime= 0.3)
btnLightsFrontDown  = Button(devTP, 208, repeatTime= 0.3)
btnLightsFrontOff   = Button(devTP, 209)
btnLightsRearUp     = Button(devTP, 210, repeatTime= 0.3)
btnLightsRearDown   = Button(devTP, 211, repeatTime= 0.3)
btnLightsRearOff    = Button(devTP, 212)



@eventEx(btnLightsFrontUp, ['Pressed', 'Released'])
def btnLightsFrontUpPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    btnLightsFrontOff.SetState(0)
    cf.BtnFB_MomentaryType(button,state)

@eventEx(btnLightsFrontDown, ['Pressed', 'Released'])
def btnLightsFrontDownPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    btnLightsFrontOff.SetState(0)
    cf.BtnFB_MomentaryType(button,state)
    
@eventEx(btnLightsFrontOff, ['Pressed', 'Released'])
def btnLightsFrontOffPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    btnLightsFrontOff.SetState(1)


@eventEx(btnLightsRearUp, ['Pressed', 'Released'])
def btnLightsRearUpPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    btnLightsRearOff.SetState(0)
    cf.BtnFB_MomentaryType(button,state)

@eventEx(btnLightsRearDown, ['Pressed', 'Released'])
def btnLightsRearDownPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    btnLightsRearOff.SetState(0)
    cf.BtnFB_MomentaryType(button,state)

@eventEx(btnLightsRearOff, ['Pressed', 'Released'])
def btnLightsRearOffPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    cf.BtnFB_MomentaryType(button,state)
    btnLightsRearOff.SetState(1)


#Ind Zone Controls

btnLightsZ1On        = Button(devTP, 221)
btnLightsZ1Off       = Button(devTP, 222)
btnLightsZ2On        = Button(devTP, 223)
btnLightsZ2Off       = Button(devTP, 224)
btnLightsZ3On        = Button(devTP, 225)
btnLightsZ3Off       = Button(devTP, 226)
btnLightsZ4On        = Button(devTP, 227)
btnLightsZ4Off       = Button(devTP, 228)

@eventEx(btnLightsZ1On, ['Pressed', 'Released'])
def btnLightsZ1OnPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    cf.BtnFB_MomentaryType(button,state)

@eventEx(btnLightsZ1Off, ['Pressed', 'Released'])
def btnLightsZ1OffPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    cf.BtnFB_MomentaryType(button,state)

@eventEx(btnLightsZ2On, ['Pressed', 'Released'])
def btnLightsZ2OnPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    cf.BtnFB_MomentaryType(button,state)

@eventEx(btnLightsZ2Off, ['Pressed', 'Released'])
def btnLightsZ2OffPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    cf.BtnFB_MomentaryType(button,state)

@eventEx(btnLightsZ3On, ['Pressed', 'Released'])
def btnLightsZ3OnPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    cf.BtnFB_MomentaryType(button,state)

@eventEx(btnLightsZ3Off, ['Pressed', 'Released'])
def btnLightsZ3OffPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    cf.BtnFB_MomentaryType(button,state)

@eventEx(btnLightsZ4On, ['Pressed', 'Released'])
def btnLightsZ4OnPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    cf.BtnFB_MomentaryType(button,state)

@eventEx(btnLightsZ4Off, ['Pressed', 'Released'])
def btnLightsZ4OffPressed(button:Button, state:str):
    print(button.Name, state)
    LightPresetGroup.SetCurrent(None)
    cf.BtnFB_MomentaryType(button,state)


#Enable/Disable Rear Zone Buttons

btnRearZoneEnable      = Button(devTP, 260)
lblFrontLights         = Label(devTP, 904)
lblRearLights          = Label(devTP, 905)

@eventEx(btnRearZoneEnable, 'Pressed')
def btnRearZoneEnablePressed(button:Button, state:str):
    print(button.Name, state)
    if button.State == 1:        
        cf.rmData['Settings']['RearZoneEnable'] = 0

    elif button.State == 0:
        cf.rmData['Settings']['RearZoneEnable'] = 1

    RearZoneEnable()
    cf.SaveFile(cf.rmData, cf.IPCPHostName +'_RoomData.json')



#Zone Select

btnLightsZ1Front       = Button(devTP, 251)
btnLightsZ2Front       = Button(devTP, 252)
btnLightsZ3Front       = Button(devTP, 253)
btnLightsZ4Front       = Button(devTP, 254)
btnLightsZ1Rear        = Button(devTP, 261)
btnLightsZ2Rear        = Button(devTP, 262)
btnLightsZ3Rear        = Button(devTP, 263)
btnLightsZ4Rear        = Button(devTP, 264)

Zone1Loc = MESet([btnLightsZ1Front, btnLightsZ1Rear])
Zone2Loc = MESet([btnLightsZ2Front, btnLightsZ2Rear])
Zone3Loc = MESet([btnLightsZ3Front, btnLightsZ3Rear])
Zone4Loc = MESet([btnLightsZ4Front, btnLightsZ4Rear])

@eventEx(Zone1Loc.Objects, 'Pressed')
def Zone1LocObjectsPressed(button:Button, state:str):
    print(button.Name, state)
    Zone1Loc.SetCurrent(button)
    if button == btnLightsZ1Front:
        cf.rmData['Settings']['Zone 1'] = 'Front'
    elif button == btnLightsZ1Rear:
        cf.rmData['Settings']['Zone 1'] = 'Rear'
    cf.SaveFile(cf.rmData, cf.IPCPHostName +'_RoomData.json')
        

@eventEx(Zone2Loc.Objects, 'Pressed')
def Zone2LocObjectsPressed(button:Button, state:str):
    print(button.Name, state)
    Zone2Loc.SetCurrent(button)
    if button == btnLightsZ2Front:
        cf.rmData['Settings']['Zone 2'] = 'Front'
    elif button == btnLightsZ2Rear:
        cf.rmData['Settings']['Zone 2'] = 'Rear'
    cf.SaveFile(cf.rmData, cf.IPCPHostName +'_RoomData.json')

@eventEx(Zone3Loc.Objects, 'Pressed')
def Zone3LocObjectsPressed(button:Button, state:str):
    print(button.Name, state)
    Zone3Loc.SetCurrent(button)
    if button == btnLightsZ3Front:
        cf.rmData['Settings']['Zone 3'] = 'Front'
    elif button == btnLightsZ3Rear:
        cf.rmData['Settings']['Zone 3'] = 'Rear'
    cf.SaveFile(cf.rmData, cf.IPCPHostName +'_RoomData.json')
    
@eventEx(Zone4Loc.Objects, 'Pressed')
def Zone4LocObjectsPressed(button:Button, state:str):
    print(button.Name, state)
    Zone4Loc.SetCurrent(button)
    if button == btnLightsZ4Front:
        cf.rmData['Settings']['Zone 4'] = 'Front'
    elif button == btnLightsZ4Rear:
        cf.rmData['Settings']['Zone 4'] = 'Rear'
    cf.SaveFile(cf.rmData, cf.IPCPHostName +'_RoomData.json')


## Set button States based off of Room Data json


if cf.rmData['Settings']['Zone 1'] == 'Front':
    Zone1Loc.SetCurrent(btnLightsZ1Front)
elif cf.rmData['Settings']['Zone 1'] == 'Rear':
    Zone1Loc.SetCurrent(btnLightsZ1Rear)

if cf.rmData['Settings']['Zone 2'] == 'Front':
    Zone2Loc.SetCurrent(btnLightsZ2Front)
elif cf.rmData['Settings']['Zone 2'] == 'Rear':
    Zone2Loc.SetCurrent(btnLightsZ2Rear)

if cf.rmData['Settings']['Zone 3'] == 'Front':
    Zone3Loc.SetCurrent(btnLightsZ3Front)
elif cf.rmData['Settings']['Zone 3'] == 'Rear':
    Zone3Loc.SetCurrent(btnLightsZ3Rear)

if cf.rmData['Settings']['Zone 4'] == 'Front':
    Zone4Loc.SetCurrent(btnLightsZ4Front)
elif cf.rmData['Settings']['Zone 4'] == 'Rear':
    Zone4Loc.SetCurrent(btnLightsZ4Rear)


def RearZoneEnable():
    if cf.rmData['Settings']['RearZoneEnable'] == 1:
        btnRearZoneEnable.SetState(1)
        btnRearZoneEnable.SetText('Rear Zone\nEnabled')
        btnLightsRearUp.SetVisible(1)
        btnLightsRearDown.SetVisible(1)
        btnLightsRearOff.SetVisible(1)
        lblRearLights.SetVisible(1)
        lblFrontLights.SetText('Front Lights')
        btnLightsPresent.SetVisible(1)
    elif cf.rmData['Settings']['RearZoneEnable'] == 0:
        btnRearZoneEnable.SetState(0)
        btnRearZoneEnable.SetText('Rear Zone\nDisabled')
        btnLightsRearUp.SetVisible(0)
        btnLightsRearDown.SetVisible(0)
        btnLightsRearOff.SetVisible(0)
        lblRearLights.SetVisible(0)
        btnLightsPresent.SetVisible(0)
        lblFrontLights.SetText('Lights')

RearZoneEnable()

#print('CALLED LIGHTS')