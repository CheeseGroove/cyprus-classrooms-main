# Python imports

# Extron Library imports
from extronlib.system import MESet, Wait
from extronlib.ui import Button, Label, Level, Knob

# Project imports
from modules.helper.ModuleSupport import eventEx
from devices import devTP, devShades
import ui.tlpShades as tlp
import variables as var


Shades_dict ={tlp.Shades25: '25',
              tlp.Shades50: '50',
              tlp.Shades75: '75',
              tlp.ShadesUp: 'Open',
              tlp.ShadesDown: 'Close',
              tlp.ShadesStop: 'Stop'
              }


@eventEx(tlp.ShadesPresetGroup.Objects, 'Pressed')
def ShadeControlButtonPressed(button, state):
    devShades.Set('ShadeControl', Shades_dict[button], {'Shade Group': '1'})