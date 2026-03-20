'''

Keypad Lock

'''
# Python imports

# Extron Library imports
from extronlib.system import MESet, Wait
from extronlib.ui import Button, Label, Level, Knob

# Project imports
from modules.helper.ModuleSupport import eventEx
from devices import devTP, devTV, devIPCP
import modules.helper.Keypad_Lock as KeypadLock
import variables as var
import CommonFunctions as cf


PanelLockPasscodes = ['7167', '6461']
SettingsPasscodes = ['7167', '0428', '6461']


btnKeypadEnter = Button(devTP, 9014)
btnKeypadExit = Button(devTP, 9015)
Keypad = KeypadLock.KeypadControl(devIPCP, devTP)


WhichKeypad = [1]


@eventEx(btnKeypadEnter, ['Pressed', 'Released'])
def btnKeypadEnterPressed(button:Button, state:str):
    cf.BtnFB_MomentaryType(button,state)
    print(WhichKeypad[0])
    if WhichKeypad[0] == 1:
        if Keypad.AcceptandClear() == True:
            @Wait(1)
            def WaitClose():
                print('KP1 Accept')
                devTP.HideAllPopups()
                devTP.ShowPopup('Technician Popup')
    if WhichKeypad[0] == 2:
        if Keypad.AcceptandClear() == True:
            @Wait(1)
            def WaitClose():
                print('KP2 Accept')
                devTP.HideAllPopups()
                devTP.ShowPopup('Technician Popup')
    


@eventEx(btnKeypadExit, 'Pressed')
def btnKeypadExitPressed(button:Button, state:str):
    print(button.Name, state)
    devTP.HidePopup('Keypad')
    Keypad.ClearKeypad()

