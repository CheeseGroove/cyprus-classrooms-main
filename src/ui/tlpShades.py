'''

Shades Control Page

'''
# Python imports

# Extron Library imports
from extronlib.system import MESet, Wait
from extronlib.ui import Button, Label, Level, Knob

# Project imports
from modules.helper.ModuleSupport import eventEx
from devices import devTP, devLights, devTV, devShades
import variables as var
import CommonFunctions as cm


Shades25 = Button(devTP, 101)
Shades50 = Button(devTP, 102)
Shades75 = Button(devTP, 103)
ShadesUp = Button(devTP, 104)
ShadesDown = Button(devTP, 105)
ShadesStop = Button(devTP, 106)

ShadesPresetGroup = MESet([Shades25, Shades50, Shades75, ShadesUp, ShadesDown, ShadesStop])

@eventEx(ShadesPresetGroup.Objects, 'Pressed')
def ShadesPresetGroupObjectsPressed(button:Button, state:str):
        print(button.Name, state)
        ShadesPresetGroup.SetCurrent(button)



#print('CALLED SHADES')