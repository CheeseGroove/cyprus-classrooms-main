"""
This is the place to define each of the devices in the system.
* Extron control devices (e.g. all extronlib.device objects)
* CS Module devices
* User defined devices (e.g. all extronlib.interface objects or custom python coded devices)

Note: This is for definition only.  Connection and logic defined in system.py (see below).
"""

# Python imports

# Extron Library imports
# !#01 add SPDevice to extronlib.device imports
from extronlib.device import ProcessorDevice, UIDevice
from extronlib.interface import SerialInterface, RelayInterface, DigitalIOInterface, EthernetClientInterface

# Project imports
import modules.device.drap_controller_IntelliflexIO_vCustom as modShades
import modules.device.view_tdisplay_IFP_Series_v1_3_0_0 as modTV
import modules.device.ilt_lc_EG2_SI_2_v1_10_0_0 as modLights
from modules.helper.ConnectionHandler import GetConnectionHandler
from modules.project.credentials import GetPassword, GetUsername
from gve_interface import gveClient



# Instantiation of Control System
devIPCP = ProcessorDevice('Classroom Processor')

# Inst Touchpanel
devTP = UIDevice('Classroom Touchpanel')

# Inst Switcher
devLights = modLights.EthernetClass('10.118.50.4', 30088, Model='EG2')
if devLights.Connected:
    print("Connected to Lighting Gateway")


# Inst TV Control
devTV_interface = modTV.SerialClass(devIPCP, 'COM2', Model='IFP8650')
devTV = GetConnectionHandler(devTV_interface, 'Power', DisconnectLimit=120, pollFrequency=120)

# Inst Shades Control
devShades = modShades.SerialClass(devIPCP , 'COM1',  Model='Intelliflex I/O')


#GVE Interface
GVEServer = gveClient('0.0.0.0', devIPCP)


#print('IMPORT DEVICES')