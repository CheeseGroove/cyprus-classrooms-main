"""
The system is the place to define system logic, automation, services, etc. as a whole.  It should
provide an *Initialize* method that will be called in main to start the start the system after
variables, devices, and UIs have been defined.

Examples of items in the system file:
* Clocks and scheduled things
* Connection of devices that need connecting
* Set up of services (e.g. ethernet servers, CLIs, etc.)
"""

# Python imports

# Extron Library imports

# Project imports
from devices import devLights, devTV, devShades, devTP
from modules.helper.ModuleSupport import eventEx
import CommonFunctions
import ui.tlpNAV



def Initialize():
    # Connect all devices
    devTV.Connect()
    devTP.ShowPage('Display Main Page')
    devTP.ShowPopup('Display AV Popup')
    print('System Initialized')
