'''

All Touchpanel UI functionality
including navigation and feedback

'''
# Python imports

# Extron Library imports
from extronlib.system import MESet, Wait, File
from extronlib.ui import Button, Label, Level, Knob

# Project imports
from modules.helper.ModuleSupport import eventEx
from devices import devTP, devLights, devTV, devShades, GVEServer
import json
import ui.tlpAV
import ui.tlpLights
import ui.tlpShades
import ui.tlpKeypad
import control.Light_Control
import control.Shades_Control
import control.TV_Control
import CommonFunctions as cf
import variables as var



# Set Room Number Label
lblRoomNmbr = Label(devTP, 901)
lblRoomNmbr.SetText(cf.RoomNumber)
lblTVConnect = Label(devTP, 902)
lblLightingarea = Label(devTP, 908)
lblGVEStatus = Label(devTP, 909)





btnNAVAV = Button(devTP, 11)
btnNAVLights = Button(devTP, 12)
btnNAVShades = Button(devTP, 13)
btnNAVTech = Button(devTP, 10, holdTime=5)
NavPagesGroup = MESet([btnNAVAV, btnNAVLights, btnNAVShades, btnNAVTech,])


popups_dict ={btnNAVAV: 'Display AV Popup',
              btnNAVLights: 'Lighting Control Popup',
              btnNAVShades: 'Shade Control Popup',
              btnNAVTech: 'Technician Popup'
              }

@eventEx(NavPagesGroup.Objects, 'Pressed')
def NavPagesGroupObjectsPressed(button:Button, state:str):
        print(button.Name, state)
        if button == btnNAVShades:
                if cf.RmHasShades == 1:
                        devTP.ShowPopup(popups_dict[button])
                        NavPagesGroup.SetCurrent(button)
        elif button == btnNAVTech:
                return
        else:
                devTP.ShowPopup(popups_dict[button])
                NavPagesGroup.SetCurrent(button)

@eventEx(btnNAVTech, 'Held')
def btnNAVTechHeld(button:Button, state:str):
        print(button.Name, state)
        devTP.ShowPopup('Keypad')
        ui.tlpKeypad.Keypad.AcceptedPasscodes = ui.tlpKeypad.SettingsPasscodes



btnHasShades = Button(devTP, 998)

@eventEx(btnHasShades, 'Pressed')
def HasShadesPressed(button:Button, state:str):
        print(button.Name, state)
        if button.State == 1:
                button.SetState(0)
                cf.rmData['Settings']['HasShades'] = 0
                cf.RmHasShades = 0
                btnNAVShades.SetVisible(0)
                button.SetText('Room Does Not\nHave Shades')
                
        elif button.State == 0:
                button.SetState(1)
                cf.rmData['Settings']['HasShades'] = 1
                cf.RmHasShades = 1
                btnNAVShades.SetVisible(1)
                button.SetText('Room Has\nShades')
        cf.SaveFile(cf.rmData, cf.IPCPHostName +'_RoomData.json')
                




##              -- Runtime Events

#if Room does not have shades make button invisible
if cf.RmHasShades == 0:
       btnNAVShades.SetVisible(0)
       btnHasShades.SetState(0)
       btnHasShades.SetText('Room Does Not\nHave Shades')
elif cf.RmHasShades == 1:
       btnNAVShades.SetVisible(1)
       btnHasShades.SetState(1)
       btnHasShades.SetText('Room Has\nShades')

lblLightingarea.SetText(str(cf.LightArea))




#GVE Send/Receive

@eventEx(devTP, ['Online', 'Offline'])
def MainTLPStatus(device, state):
    GVEServer.SendStatus(cf.gveTPID, 'Connection', state)


@eventEx(GVEServer, 'DiagnosticReceiveText')
def GVEReceiveText(server, data):
    print('<<' + data)

@eventEx(GVEServer, 'DiagnosticSendText')
def GVESendText(server, data):
    print('>>' + data)

@eventEx(GVEServer, ['GVEServerConnected', 'GVEServerDisconnected'])
def GVEServerConnected(server, state):
    lblGVEStatus.SetText('GVE '+ state)

@eventEx(GVEServer, 'ReceiveGVECommand')
def GVEExecuteCommand(server, data):
    device, command, parameter = data[0], data[1], data[2]
    print('Execute {0} - {1} {2}'.format(device, command, parameter))
    if device == cf.gveDispID:
        print('Set Display {0} {1}'.format(command, parameter))
        if command == 'Power':
                if parameter == 'On':
                    control.TV_Control.PowerButtonEvent(ui.tlpAV.btnON, 'Pressed')
                elif parameter == 'Off':
                    control.TV_Control.PowerButtonEvent(ui.tlpAV.btnOFF, 'Pressed')
        elif command == 'Source':
                if parameter == 'HDMI 1':
                      control.TV_Control.PowerButtonEvent(ui.tlpAV.btnHDMI1, 'Pressed')
                if parameter == 'HDMI 2':
                      control.TV_Control.PowerButtonEvent(ui.tlpAV.btnHDMI2, 'Pressed')
                if parameter == 'Embd Player':
                      control.TV_Control.PowerButtonEvent(ui.tlpAV.btnCastVid, 'Pressed')



#       Device Feedback



def TVConnectionStatus_callback(cmd, value, qualifier):
    print(cmd, value, qualifier)
    if value == 'Connected':
        print("Yes")
        lblTVConnect.SetText('Connected')
        GVEServer.SendStatus(cf.gveDispID, 'Connection', 'Connected')
        @Wait(6)
        def dummy():
            devTV.Update('Power')
    elif value == 'Disconnected':
        print("no")
        lblTVConnect.SetText('Disconnected')
        GVEServer.SendStatus(cf.gveDispID, 'Connection', 'Disconnected')
    
    if cmd == 'Volume':
           ui.tlpAV.volTV = value
    if cmd == 'AudioMute':
                if value == 'On':
                        ui.tlpAV.btnTVMute.SetState(1)
                elif value == 'Off':
                        ui.tlpAV.btnTVMute.SetState(0)


devTV.SubscribeStatus('ConnectionStatus', None, TVConnectionStatus_callback)
devTV.SubscribeStatus('Volume', None, TVConnectionStatus_callback)
devTV.SubscribeStatus('AudioMute', None, TVConnectionStatus_callback)


#print('CALLED NAV')