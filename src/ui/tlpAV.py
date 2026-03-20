'''

Display Page

'''
# Python imports

# Extron Library imports
from extronlib.system import MESet, Wait
from extronlib.ui import Button, Label, Level, Knob, Slider

# Project imports
from modules.helper.ModuleSupport import eventEx
from devices import devTP, devTV




#TV Volume Fader

volTV           = Slider(devTP, 61)
btnTVMute       = Button(devTP, 62)
volTV.SetRange(0,80, 5)



        


#      TV Power Buttons
btnON   = Button(devTP, 51)
btnOFF  = Button(devTP, 52)
mePower = MESet([btnON, btnOFF,])

@eventEx(mePower.Objects, 'Pressed')
def mainSourceButtonEvent(button: Button, state: str):
    print(button.Name, state)
    mePower.SetCurrent(button)

        

#       Source Select Buttons

btnHDMI1        = Button(devTP, 53)
btnHDMI2        = Button(devTP, 54)
btnCastVid      = Button(devTP, 55)
meSourceGroup   = MESet([btnHDMI1, btnHDMI2, btnCastVid])

@eventEx(meSourceGroup.Objects, 'Pressed')
def mainSourceButtonEvent(button: Button, state: str):
    print(button.Name, state)
    meSourceGroup.SetCurrent(button)



#print('CALLED AV')