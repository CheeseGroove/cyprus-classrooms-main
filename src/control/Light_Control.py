# Python imports

# Extron Library imports
from extronlib.system import MESet, Wait
from extronlib.ui import Button, Label, Level, Knob

# Project imports
from modules.helper.ModuleSupport import eventEx
from devices import devTP, devLights
import ui.tlpLights as tlp
import CommonFunctions as cf
import variables as var


#Local Variables
Delimiter = '\x0D'
FadeTime = 1



#Preset Recall

@eventEx(tlp.LightPresetGroup.Objects, 'Pressed')
def tlpbtnLightPresetsEvent(button: Button, state: str):
    if button == tlp.btnLightsOff:
        devLights.Set('SceneRecall', 5, {'Area': cf.LightArea, 'Fade': FadeTime})
        tlp.btnLightsFrontOff.SetState(1)
        tlp.btnLightsRearOff.SetState(1)
        return
    
    elif button == tlp.btnLightsPresent: #Set Lights based on if zones are in front or rear
        if cf.rmData['Settings']['Zone 1'] == 'Rear':
            devLights.Set('ChannelLevel', 25, {'Channel': 1, 'Area': cf.LightArea, 'Fade': FadeTime})
        if cf.rmData['Settings']['Zone 2'] == 'Rear':
            devLights.Set('ChannelLevel', 25, {'Channel': 2, 'Area': cf.LightArea, 'Fade': FadeTime})
        if cf.rmData['Settings']['Zone 3'] == 'Rear':
            devLights.Set('ChannelLevel', 25, {'Channel': 3, 'Area': cf.LightArea, 'Fade': FadeTime})
        if cf.rmData['Settings']['Zone 4'] == 'Rear':
            devLights.Set('ChannelLevel', 25, {'Channel': 4, 'Area': cf.LightArea, 'Fade': FadeTime})

        if cf.rmData['Settings']['Zone 1'] == 'Front':
            devLights.Set('ChannelLevel', 0, {'Channel': 1, 'Area': cf.LightArea, 'Fade': FadeTime})
        if cf.rmData['Settings']['Zone 2'] == 'Front':
            devLights.Set('ChannelLevel', 0, {'Channel': 2, 'Area': cf.LightArea, 'Fade': FadeTime})
        if cf.rmData['Settings']['Zone 3'] == 'Front':
            devLights.Set('ChannelLevel', 0, {'Channel': 3, 'Area': cf.LightArea, 'Fade': FadeTime})
        if cf.rmData['Settings']['Zone 4'] == 'Front':
            devLights.Set('ChannelLevel', 0, {'Channel': 4, 'Area': cf.LightArea, 'Fade': FadeTime})
        tlp.btnLightsFrontOff.SetState(0)
        tlp.btnLightsRearOff.SetState(0)
        return
    
    
    try:
        Scene = int(tlp.LightPresetGroup.Objects.index(tlp.LightPresetGroup.GetCurrent())+1)
        #print(Scene)
    except ValueError as err:
        print(err, 'Setting Scene to a null string')
        Scene = ''
    
    if Scene != '' and cf.LightArea != '' and FadeTime != '':
        devLights.Set('SceneRecall', Scene, {'Area': cf.LightArea, 'Fade': FadeTime})
        tlp.btnLightsFrontOff.SetState(0)
        tlp.btnLightsRearOff.SetState(0)

   


# Front and Rear Light Zone Controls. Zone assignments can be adjusted on advanced page




@eventEx(tlp.btnLightsFrontUp, ['Pressed', 'Repeated'])
def tlpbtnLightsFrontUpEvent(button :Button, state :str):
    if cf.rmData['Settings']['Zone 1'] == 'Front':
        devLights.Set('RaiseChannelLevel', None, {'Channel': 1, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 2'] == 'Front':
        devLights.Set('RaiseChannelLevel', None, {'Channel': 2, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 3'] == 'Front':
        devLights.Set('RaiseChannelLevel', None, {'Channel': 3, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 4'] == 'Front':
        devLights.Set('RaiseChannelLevel', None, {'Channel': 4, 'Area': cf.LightArea})        

@eventEx(tlp.btnLightsFrontDown, ['Pressed', 'Repeated'])
def tlpbtnLightsFrontDownEvent(button :Button, state :str):
    if cf.rmData['Settings']['Zone 1'] == 'Front':
        devLights.Set('LowerChannelLevel', None, {'Channel': 1, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 2'] == 'Front':
        devLights.Set('LowerChannelLevel', None, {'Channel': 2, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 3'] == 'Front':
        devLights.Set('LowerChannelLevel', None, {'Channel': 3, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 4'] == 'Front':
        devLights.Set('LowerChannelLevel', None, {'Channel': 4, 'Area': cf.LightArea})


@eventEx(tlp.btnLightsFrontOff, 'Pressed')
def tlpbtnLightsFrontOffEvent(button :Button, state :str):
    if cf.rmData['Settings']['Zone 1'] == 'Front':
        devLights.Set('ChannelLevel', 0, {'Channel': 1, 'Area': cf.LightArea, 'Fade': FadeTime})
    if cf.rmData['Settings']['Zone 2'] == 'Front':
        devLights.Set('ChannelLevel', 0, {'Channel': 2, 'Area': cf.LightArea, 'Fade': FadeTime})
    if cf.rmData['Settings']['Zone 3'] == 'Front':
        devLights.Set('ChannelLevel', 0, {'Channel': 3, 'Area': cf.LightArea, 'Fade': FadeTime})
    if cf.rmData['Settings']['Zone 4'] == 'Front':
        devLights.Set('ChannelLevel', 0, {'Channel': 4, 'Area': cf.LightArea, 'Fade': FadeTime})
    

@eventEx(tlp.btnLightsRearUp, ['Pressed', 'Repeated'])
def tlpbtnLightsRearUpEvent(button :Button, state :str):
    if cf.rmData['Settings']['Zone 1'] == 'Rear':
        devLights.Set('RaiseChannelLevel', None, {'Channel': 1, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 2'] == 'Rear':
        devLights.Set('RaiseChannelLevel', None, {'Channel': 2, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 3'] == 'Rear':
        devLights.Set('RaiseChannelLevel', None, {'Channel': 3, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 4'] == 'Rear':
        devLights.Set('RaiseChannelLevel', None, {'Channel': 4, 'Area': cf.LightArea})

@eventEx(tlp.btnLightsRearDown, ['Pressed', 'Repeated'])
def tlpbtnLightsRearDownEvent(button :Button, state :str):
    if cf.rmData['Settings']['Zone 1'] == 'Rear':
        devLights.Set('LowerChannelLevel', None, {'Channel': 1, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 2'] == 'Rear':
        devLights.Set('LowerChannelLevel', None, {'Channel': 2, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 3'] == 'Rear':
        devLights.Set('LowerChannelLevel', None, {'Channel': 3, 'Area': cf.LightArea})
    if cf.rmData['Settings']['Zone 4'] == 'Rear':
        devLights.Set('LowerChannelLevel', None, {'Channel': 4, 'Area': cf.LightArea})

@eventEx(tlp.btnLightsRearOff, 'Pressed')
def tlpbtnLightsRearOffEvent(button :Button, state :str):
    if cf.rmData['Settings']['Zone 1'] == 'Rear':
        devLights.Set('ChannelLevel', 0, {'Channel': 1, 'Area': cf.LightArea, 'Fade': FadeTime})
    if cf.rmData['Settings']['Zone 2'] == 'Rear':
        devLights.Set('ChannelLevel', 0, {'Channel': 2, 'Area': cf.LightArea, 'Fade': FadeTime})
    if cf.rmData['Settings']['Zone 3'] == 'Rear':
        devLights.Set('ChannelLevel', 0, {'Channel': 3, 'Area': cf.LightArea, 'Fade': FadeTime})
    if cf.rmData['Settings']['Zone 4'] == 'Rear':
        devLights.Set('ChannelLevel', 0, {'Channel': 4, 'Area': cf.LightArea, 'Fade': FadeTime})




#Advanced Page Zone Assignment




@eventEx(tlp.btnLightsZ1Front, 'Pressed')
def tlpbtnLightsZ1FrontPressed(button :Button, state :str):
    cf.rmData['Settings']['Zone 1'] = 'Front'

@eventEx(tlp.btnLightsZ2Front, 'Pressed')
def tlpbtnLightsZ2FrontPressed(button :Button, state :str):
    cf.rmData['Settings']['Zone 2'] = 'Front'

@eventEx(tlp.btnLightsZ3Front, 'Pressed')
def tlpbtnLightsZ3FrontPressed(button :Button, state :str):
    cf.rmData['Settings']['Zone 3'] = 'Front'
    

@eventEx(tlp.btnLightsZ4Front, 'Pressed')
def tlpbtnLightsZ4FrontPressed(button :Button, state :str):
    cf.rmData['Settings']['Zone 4'] = 'Front'
    




@eventEx(tlp.btnLightsZ1Rear, 'Pressed')
def tlpbtnLightsZ1RearPressed(button :Button, state :str):
    cf.rmData['Settings']['Zone 1'] = 'Rear'

@eventEx(tlp.btnLightsZ2Rear, 'Pressed')
def tlpbtnLightsZ2RearPressed(button :Button, state :str):
    cf.rmData['Settings']['Zone 2'] = 'Rear'

@eventEx(tlp.btnLightsZ3Rear, 'Pressed')
def tlpbtnLightsZ3RearPressed(button :Button, state :str):
    cf.rmData['Settings']['Zone 3'] = 'Rear'
    
@eventEx(tlp.btnLightsZ4Rear, 'Pressed')
def tlpbtnLightsZ4RearPressed(button :Button, state :str):
    cf.rmData['Settings']['Zone 4'] = 'Rear'




#Advanced Page Individual Zone Control

@eventEx(tlp.btnLightsZ1On, 'Pressed')
def tlpbtnLightsZ1OnPressed(button :Button, state :str):
        devLights.Set('ChannelLevel', 100, {'Channel': 1, 'Area': cf.LightArea, 'Fade': FadeTime})
   

@eventEx(tlp.btnLightsZ1Off, 'Pressed')
def tlpbtnLightsZ1OffPressed(button :Button, state :str):
        devLights.Set('ChannelLevel', 0, {'Channel': 1, 'Area': cf.LightArea, 'Fade': FadeTime})
   
   

@eventEx(tlp.btnLightsZ2On, 'Pressed')
def tlpbtnLightsZ2OnPressed(button :Button, state :str):
        devLights.Set('ChannelLevel', 100, {'Channel': 2, 'Area': cf.LightArea, 'Fade': FadeTime})
   
   

@eventEx(tlp.btnLightsZ2Off, 'Pressed')
def tlpbtnLightsZ2OffPressed(button :Button, state :str):
        devLights.Set('ChannelLevel', 0, {'Channel': 2, 'Area': cf.LightArea, 'Fade': FadeTime})
   
   

@eventEx(tlp.btnLightsZ3On, 'Pressed')
def tlpbtnLightsZ3OnPressed(button :Button, state :str):
        devLights.Set('ChannelLevel', 100, {'Channel': 3, 'Area': cf.LightArea, 'Fade': FadeTime})
   
   

@eventEx(tlp.btnLightsZ3Off, 'Pressed')
def tlpbtnLightsZ3OffPressed(button :Button, state :str):
        devLights.Set('ChannelLevel', 0, {'Channel': 3, 'Area': cf.LightArea, 'Fade': FadeTime})
   
   

@eventEx(tlp.btnLightsZ4On, 'Pressed')
def tlpbtnLightsZ4OnPressed(button :Button, state :str):
        devLights.Set('ChannelLevel', 100, {'Channel': 4, 'Area': cf.LightArea, 'Fade': FadeTime})
   
   

@eventEx(tlp.btnLightsZ4Off, 'Pressed')
def tlpbtnLightsZ4OffPressed(button :Button, state :str):
        devLights.Set('ChannelLevel', 0, {'Channel': 4, 'Area': cf.LightArea, 'Fade': FadeTime})


#print('Light Control Running')