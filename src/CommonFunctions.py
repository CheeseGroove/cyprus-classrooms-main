
'''

This page is for commonly called functions across multiple pages such as button press feedback

'''

from extronlib.system import MESet, Wait, File, Timer
from extronlib.ui import Button, Label, Level, Knob, Slider
import devices as dev
import json
import variables as var



#####Button feedback types

def BtnFB_MomentaryType(button :Button, state :str):
    if state is 'Pressed':
        button.SetState(1)
    else:
        button.SetState(0)

def BtnFB_ToggleType(button :Button, state:str):
    if button.State == 1:
        button.SetState(0)
    else:
        button.SetState(1)









####################### SAVE AND LOAD JSON PERSISTENT SETTINGS #############

ltData = {}

RoomNumber = ''
LightArea = ''
RmHasShades = ''

gveRoomID = ''
gveDispID = ''
gveProcID = ''
gveTPID = ''

IPCPHostName = dev.devIPCP.Hostname
IPAddress = dev.devIPCP.IPAddress
IPCPMacAddress = dev.devIPCP.MACAddress
IPCPFirmware = dev.devIPCP.FirmwareVersion
IPCPModel = dev.devIPCP.ModelName
IPCPSerial = dev.devIPCP.SerialNumber
RoomID = dev.devIPCP.SystemSettings

TPIPAddress = dev.devTP.IPAddress
TPMac = dev.devTP.MACAddress
TPModel = dev.devTP.ModelName
TPSerial = dev.devTP.SerialNumber
TPFirmware = dev.devTP.FirmwareVersion

rmData = {'Processor Info': {'IP Address': IPAddress,
                             'Mac Address': IPCPMacAddress,
                             'Model': IPCPModel,
                             'Serial #': IPCPSerial,
                             'Firmware': IPCPFirmware},
          'Touchpanel Info': {'IP Address': TPIPAddress,
                             'Mac Address': TPMac,
                             'Model': TPModel,
                             'Serial #': TPSerial,
                             'Firmware': TPFirmware},
          'Settings': {}
          }


#Settings Page Labels for IPCP and Touchpanel info##

lblIPCPIP = Label(dev.devTP, 910)
lblIPCPMAC = Label(dev.devTP, 911)
lblIPCPSerial = Label(dev.devTP, 912)
lblIPCPFirmware = Label(dev.devTP, 913)

lblIPCPIP.SetText(str(IPAddress))
lblIPCPMAC.SetText(str(IPCPMacAddress))
lblIPCPSerial.SetText(str(IPCPSerial))
lblIPCPFirmware.SetText(str(IPCPFirmware))

lblTPIP = Label(dev.devTP,914)
lblTPMAC = Label(dev.devTP, 915)
lblTPSerial = Label(dev.devTP, 916)
lblTPFirmware = Label(dev.devTP, 917)

lblTPIP.SetText(str(TPIPAddress))
lblTPMAC.SetText(str(TPMac))
lblTPSerial.SetText(str(TPSerial))
lblTPFirmware.SetText(str(TPFirmware))


#print(RoomID)


#Load json for room Data and fill dictionary
def LoadRoomData(fileName:str):
    global rmData
    if File.Exists(fileName):
        with File(fileName, 'r') as file:
            rmData = json.load(file)
        return True
    else:
        return False
    

#load json for lighting data and fill dictionary
def LoadLightData(fileName:str):
    global ltData
    if File.Exists(fileName):
        with File(fileName, 'r') as file:
            ltData = json.load(file)
        return True
    else:
        return False

#Save/create json file on processor
def SaveFile(data:dict, fileName):
    with File(fileName, 'w') as file:
        json.dump(data, file, indent=4)


#Load lighting data if json exists, if json doesnt exist, set defaults
if LoadLightData('Cyprus Lighting Info.json'):
    print('lighting file found')
    print(IPAddress)
    if IPAddress in ltData and ltData[IPAddress] is not None:
        
        LightArea = int(ltData[IPAddress]['LightArea'])
        RoomNumber = ltData[IPAddress]['RoomNumber']
        print("Light Area: ", LightArea, "Room Number: ", RoomNumber)
        gveProcID = ltData[IPAddress]['gveProcID']
        gveTPID = ltData[IPAddress]['gveTPID']
        gveDispID = ltData[IPAddress]['gveDispID']
        gveRoomID = ltData[IPAddress]['gveRoomID']
    else:
        print("No IP Found in Lighting File")
        LightArea = 1
        RoomNumber = 'No Lighting\nIP Found. Setting default area.'
else:
    print('NO lighting FILE')
    LightArea = 1
    RoomNumber = 'No Lighting\nFile'

#IF Room Data Exists, then pull values, otherwise create JSON with default values
if LoadRoomData(IPCPHostName +'_RoomData.json'):
    print(IPCPHostName +' Room Data Found')
    #Set Shades Variable
    RmHasShades = rmData['Settings']['HasShades']
    #Set Processor and TP info before overwriting json
    rmData['Processor Info'] = {'IP Address': IPAddress,
                                'Mac Address': IPCPMacAddress,
                                'Model': IPCPModel,
                                'Serial #': IPCPSerial,
                                'Firmware': IPCPFirmware}
    rmData['Touchpanel Info'] = {'IP Address': TPIPAddress,
                                 'Mac Address': TPMac,
                                 'Model': TPModel,
                                 'Serial #': TPSerial,
                                 'Firmware': TPFirmware}
    SaveFile(rmData, IPCPHostName +'_RoomData.json')
else:
    print(IPCPHostName +' Room Data not Found')
    RmHasShades = 1
    rmData['Settings'] = {'Zone 1': 'Front',
                          'Zone 2': 'Rear',
                          'Zone 3': 'Rear',
                          'Zone 4': 'Front',
                          'HasShades':  1,
                          'RearZoneEnable': 1}
    print(rmData)
    SaveFile(rmData, IPCPHostName +'_RoomData.json')
    print(IPCPHostName +' RoomData Json Created')




@Timer(30)
def updateLighting(timer, count):
    if LoadLightData('Cyprus Lighting Info.json'):
        print("Updated Lighting Data")
