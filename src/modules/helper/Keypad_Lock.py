## Begin ControlScript Import --------------------------------------------------
from extronlib import event, Version
from extronlib.device import ProcessorDevice, UIDevice
from extronlib.interface import (EthernetClientInterface, 
    SerialInterface, IRInterface, RelayInterface, 
    ContactInterface, DigitalIOInterface, FlexIOInterface, SWPowerInterface, 
    VolumeInterface)
from extronlib.ui import Button, Knob, Label, Level
from extronlib.system import Clock, MESet, Wait
from modules.helper.ModuleSupport import eventEx



## End ControlScript Import ----------------------------------------------------
##
## Begin User Import -----------------------------------------------------------

## End User Import -------------------------------------------------------------
##
## Begin Device/Processor Definition -------------------------------------------
## End Device/Processor Definition ---------------------------------------------
##
## Begin Device/User Interface Definition --------------------------------------

## End Device/User Interface Definition ----------------------------------------
##
## Begin Communication Interface Definition ------------------------------------

## End Communication Interface Definition --------------------------------------

    ## Event Definitions -----------------------------------------------------------
    
    ## End Events Definitions-------------------------------------------------------
class KeypadControl:
    def __init__(self,dvProcessor, dvTLP):    
        self.dvProcessor = dvProcessor
        self.dvTLP = dvTLP
        self.KeypadButton = []
        self.KeypadLabel = Button(dvTLP, 9013)
        self.KeypadString = ''
        self.AcceptedPasscodes = ['7167','6461']
        self.HidePin = True
            
        KeypadBackspace = Button(self.dvTLP, 9010, repeatTime = 0.3)
        @eventEx(KeypadBackspace, ['Pressed', 'Released', 'Repeated'])
        def BackspacePressed(button :Button, state :str):
            if state == 'Pressed':
                self.KeypadString = self.KeypadString[:-1]
                if self.HidePin == True:
                    self.UpdateLabel("*" * len(self.KeypadString))
                else:
                    self.UpdateLabel(self.KeypadString)
                button.SetState(1)
            elif state == 'Repeated':
                self.KeypadString = self.KeypadString[:-1]
                if self.HidePin == True:
                    self.UpdateLabel("*" * len(self.KeypadString))
                else:
                    self.UpdateLabel(self.KeypadString)
            else:
                button.SetState(0)

        KeypadClear = Button(self.dvTLP, 9011)
        @eventEx(KeypadClear, 'Pressed')
        def ClearPressed(button, state):
            self.KeypadString = ''
            self.UpdateLabel(self.KeypadString)
            
        KeypadShowPin = Button(self.dvTLP, 9012)
        @eventEx(KeypadShowPin, ['Pressed', 'Released'])
        def KeyPadShowPin(button :Button, state :str):
            if state == 'Pressed':
                self.UpdateLabel(self.KeypadString)
            elif state == 'Released':
                self.UpdateLabel("*" * len(self.KeypadString))



        #Mass Definition of Keypad Buttons
        
        for Button_IDs in range(9000, 9010):
            self.KeypadButton.append(Button(self.dvTLP, Button_IDs, repeatTime = 0.3))
                
        for KeyButton in self.KeypadButton:    
            @eventEx(KeyButton, ['Pressed', 'Released', 'Repeated'])
            def ButtonPressed(button:Button, state):
                if state == 'Pressed':
                    button.SetState(1)
                    if len(button.Name) == 1 and self.KeypadLabel.State == 0:
                        self.KeypadString += button.Name
                        if self.HidePin == True:
                            self.UpdateLabel("*" * len(self.KeypadString))
                        else:
                            self.UpdateLabel(self.KeypadString)
                    else:
                        print('Invalid Button')
                elif state == 'Repeated':
                    if len(button.Name) == 1 and self.KeypadLabel.State == 0:
                        self.KeypadString += button.Name
                        if self.HidePin == True:
                            self.UpdateLabel("*" * len(self.KeypadString))
                        else:
                            self.UpdateLabel(self.KeypadString)
                else:
                    button.SetState(0)
                    
    def UpdateLabel(self,NewString):
            self.KeypadLabel.SetText(NewString)
    
    def ClearKeypad(self):
        self.KeypadString = ''
        self.UpdateLabel(self.KeypadString)

    def AcceptandClear(self):
        print(self.KeypadString)
        if self.KeypadString in self.AcceptedPasscodes:
            print('Password Accepted' , self.KeypadString)
            self.KeypadLabel.SetText('Accepted')
            self.KeypadLabel.SetState(2)
            @Wait(1)
            def WaitClearKeypadSuccess():
                self.KeypadLabel.SetState(0)
                self.ClearKeypad()
            return True
        else:
            print('Password Denied')
            self.KeypadLabel.SetText('Incorrect PIN')
            self.KeypadLabel.SetState(1)
            @Wait(2)
            def WaitClearKeypadFail():
                self.KeypadLabel.SetState(0)
                self.ClearKeypad()
            return False


