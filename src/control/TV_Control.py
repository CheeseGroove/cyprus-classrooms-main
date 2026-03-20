# Python imports

# Extron Library imports
from extronlib.system import MESet, Wait
from extronlib.ui import Button, Label, Level, Knob, Slider

# Project imports
from modules.helper.ModuleSupport import eventEx
from devices import devTP, devTV, GVEServer
import ui.tlpAV as tlpAV
import CommonFunctions as cf
import variables as var



#TV Power Control
@eventEx(tlpAV.mePower.Objects, 'Pressed')
def PowerButtonEvent(button: Button, state: str):
    if   button == tlpAV.btnON:
            tlpAV.mePower.SetCurrent(tlpAV.btnON)
            devTV.Set('Power', 'On')
            GVEServer.SendStatus(cf.gveDispID, 'Power', 'On')
    elif button == tlpAV.btnOFF:
            tlpAV.mePower.SetCurrent(tlpAV.btnOFF)
            devTV.Set('Power', 'Off')
            GVEServer.SendStatus(cf.gveDispID, 'Power', 'Off')


#TV Source Select
@eventEx(tlpAV.meSourceGroup.Objects, 'Pressed')
def mainSourceButtonEvent(button: Button, state: str):
    if   button == tlpAV.btnHDMI1:
            tlpAV.meSourceGroup.SetCurrent(tlpAV.btnHDMI1)
            devTV.Set('Input', 'HDMI 1')
            GVEServer.SendStatus(cf.gveDispID, 'Source', 'HDMI 1')
    elif button == tlpAV.btnHDMI2:
            tlpAV.meSourceGroup.SetCurrent(tlpAV.btnHDMI2)
            devTV.Set('Input', 'HDMI 2')
            GVEServer.SendStatus(cf.gveDispID, 'Source', 'HDMI 2')
    elif button == tlpAV.btnCastVid:
            tlpAV.meSourceGroup.SetCurrent(tlpAV.btnCastVid)
            devTV.Set('Input', 'Embd Player')
            GVEServer.SendStatus(cf.gveDispID, 'Source', 'Embd Player')




#TV Volume Controls

@eventEx(tlpAV.volTV, ['Changed','Pressed','Released'])
def tlpvolTVChanged(slider: Slider, state, value):
        print(slider.Name, state, value)
        slider.SetFill(value)
        devTV.Set('Volume', value)


@eventEx(tlpAV.btnTVMute, 'Pressed') #Toggle Mute
def muteTVAudio(button: Button, state: str):
    if   button.State == 1:
            button.SetState(0)
            devTV.Set('AudioMute', 'Off')
    else:
            button.SetState(1)
            devTV.Set('AudioMute', 'On')




#print('TV Control Running')