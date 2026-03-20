from extronlib.interface import SerialInterface, EthernetClientInterface
from extronlib.system import Wait, ProgramLog

class DeviceClass:
    def __init__(self):

        self.Debug = False
        self.Models = {}

        self.Commands = {
            'ChannelLevel': {'Parameters': ['Channel', 'Area', 'Fade'], 'Status': {}},
            'SceneRecall': {'Parameters': ['Area', 'Fade'], 'Status': {}},
            'SceneSave': {'Parameters': ['Area'], 'Status': {}},
            'StopFade': {'Parameters': ['Channel', 'Area'], 'Status': {}},
            'RaiseChannelLevel' : {'Parameters': ['Channel', 'Area'], 'Status': {}},
            'LowerChannelLevel' : {'Parameters': ['Channel', 'Area'], 'Status': {}}
        }

    @staticmethod
    def __ConstraintChecker(*args):

        try:
            for x in args:
                if not x['Min'] <= x['Value'] <= x['Max']:
                    return False
            return True
        except (KeyError, TypeError):
            return False
        
    def SetChannelLevel(self, value, qualifier):

        Channel = {
            'Min':      0,
            'Max':      999,
            'Value':    qualifier['Channel']
        }

        Area = {
            'Min':      1,
            'Max':      65535,
            'Value':    qualifier['Area']
        }

        Fade = {
            'Min':      0,
            'Max':      999,
            'Value':    qualifier['Fade']
        }

        Level = {
            'Min':      0,
            'Max':      100,
            'Value':    value
        }

        if self.__ConstraintChecker(Channel, Area, Fade, Level):
            ChannelLevelCmdString = '@SC{0}:A{1}:L{2}:F{3}\r'.format(Channel['Value'],
                                                                     Area['Value'],
                                                                     Level['Value'],
                                                                     Fade['Value'])
            self.__SetHelper('ChannelLevel', ChannelLevelCmdString, value, qualifier)
            #print(ChannelLevelCmdString)
        else:
            self.Discard('Invalid Command for SetChannelLevel')

    def SetSceneRecall(self, value, qualifier):

        Area = {
            'Min':      1,
            'Max':      65535,
            'Value':    qualifier['Area'],
        }

        Fade = {
            'Min':      0,
            'Max':      999,
            'Value':    qualifier['Fade']
        }

        Scene = {
            'Min':      0,
            'Max':      999,
            'Value':    value
        }

        if self.__ConstraintChecker(Area, Fade, Scene):
            SceneRecallCmdString = '@SS{0}:A{1}:F{2}\r'.format(Scene['Value'], Area['Value'], Fade['Value'])
            self.__SetHelper('SceneRecall', SceneRecallCmdString, value, qualifier)
            #print(SceneRecallCmdString)
        else:
            self.Discard('Invalid Command for SetSceneRecall')

    def SetSceneSave(self, value, qualifier):

        Area = {
            'Min':      1,
            'Max':      65535,
            'Value':    qualifier['Area']
        }

        Scene = {
            'Min':      0,
            'Max':      999,
            'Value':    value
        }

        if self.__ConstraintChecker(Area, Scene):
            SceneSaveCmdString = '@SA{0}:A{1}\r'.format(Scene['Value'], Area['Value'])
            self.__SetHelper('SceneSave', SceneSaveCmdString, value, qualifier)
        else:
            self.Discard('Invalid Command for SetSceneSave')

    def SetStopFade(self, value, qualifier):

        Channel = {
            'Min':      0,
            'Max':      999,
            'Value':    qualifier['Channel']
        }

        Area = {
            'Min':      1,
            'Max':      65535,
            'Value':    qualifier['Area']
        }

        if self.__ConstraintChecker(Channel, Area):
            StopFadeCmdString = '@SF{0}:A{1}\r'.format(Channel['Value'], Area['Value'])
            self.__SetHelper('StopFade', StopFadeCmdString, value, qualifier)
        else:
            self.Discard('Invalid Command for SetStopFade')

    def SetRaiseChannelLevel(self, value, qualifier):

        Channel = {
            'Min':      0,
            'Max':      999,
            'Value':    qualifier['Channel']
        }

        Area = {
            'Min':      1,
            'Max':      65535,
            'Value':    qualifier['Area']
        }

        if self.__ConstraintChecker(Channel, Area):
            RaiseChannelLevelCmdString = '@CR{0}:A{1}\r'.format(Channel['Value'], Area['Value'])
            self.__SetHelper('RaiseChannelLevel', RaiseChannelLevelCmdString, value, qualifier)
            #print(RaiseChannelLevelCmdString)
        else:
            self.Discard('Invalid Command for SetRaiseChannelLevel')

    def SetLowerChannelLevel(self, value, qualifier):

        Channel = {
            'Min':      0,
            'Max':      999,
            'Value':    qualifier['Channel']
        }

        Area = {
            'Min':      1,
            'Max':      65535,
            'Value':    qualifier['Area']
        }

        if self.__ConstraintChecker(Channel, Area):
            LowerChannelLevelCmdString = '@CL{0}:A{1}\r'.format(Channel['Value'], Area['Value'])
            self.__SetHelper('LowerChannelLevel', LowerChannelLevelCmdString, value, qualifier)
            #print(LowerChannelLevelCmdString)
        else:
            self.Discard('Invalid Command for SetLowerChannelLevel')

    def __SetHelper(self, command, commandstring, value, qualifier):

        self.Debug = True

        self.Send(commandstring)


    ######################################################    
    # RECOMMENDED not to modify the code below this point
    ######################################################

    # Send Control Commands
    def Set(self, command, value, qualifier=None):
        method = getattr(self, 'Set%s' % command, None)
        if method is not None and callable(method):
            method(value, qualifier)
        else:
            raise AttributeError(command + 'does not support Set.')

class SerialClass(SerialInterface, DeviceClass):

    def __init__(self, Host, Port, Baud=9600, Data=8, Parity='None', Stop=1, FlowControl='Off', CharDelay=0, Mode='RS232', Model =None):
        SerialInterface.__init__(self, Host, Port, Baud, Data, Parity, Stop, FlowControl, CharDelay, Mode)
        self.ConnectionType = 'Serial'
        DeviceClass.__init__(self)
        # Check if Model belongs to a subclass
        if len(self.Models) > 0:
            if Model not in self.Models: 
                print('Model mismatch')              
            else:
                self.Models[Model]()

    def Error(self, message):
        portInfo = 'Host Alias: {0}, Port: {1}'.format(self.Host.DeviceAlias, self.Port)
        print('Module: {}'.format(__name__), portInfo, 'Error Message: {}'.format(message[0]), sep='\r\n')
  
    def Discard(self, message):
        self.Error([message])

class SerialOverEthernetClass(EthernetClientInterface, DeviceClass):

    def __init__(self, Hostname, IPPort, Protocol='TCP', ServicePort=0, Model=None):
        EthernetClientInterface.__init__(self, Hostname, IPPort, Protocol, ServicePort)
        self.ConnectionType = 'Serial'
        DeviceClass.__init__(self) 
        # Check if Model belongs to a subclass       
        if len(self.Models) > 0:
            if Model not in self.Models: 
                print('Model mismatch')              
            else:
                self.Models[Model]()

    def Error(self, message):
        portInfo = 'IP Address/Host: {0}:{1}'.format(self.IPAddress, self.IPPort)
        print('Module: {}'.format(__name__), portInfo, 'Error Message: {}'.format(message[0]), sep='\r\n')
  
    def Discard(self, message):
        self.Error([message])

    def Disconnect(self):
        EthernetClientInterface.Disconnect(self)
        self.OnDisconnected()

class EthernetClass(EthernetClientInterface, DeviceClass):

    def __init__(self, Hostname, IPPort, Protocol='UDP', ServicePort=0, Model=None):
        EthernetClientInterface.__init__(self, Hostname, IPPort, Protocol, ServicePort)
        self.ConnectionType = 'Ethernet'
        DeviceClass.__init__(self) 
        # Check if Model belongs to a subclass       
        if len(self.Models) > 0:
            if Model not in self.Models: 
                print('Model mismatch')              
            else:
                self.Models[Model]()

    def Error(self, message):
        portInfo = 'IP Address/Host: {0}:{1}'.format(self.IPAddress, self.IPPort)
        print('Module: {}'.format(__name__), portInfo, 'Error Message: {}'.format(message[0]), sep='\r\n')
  
    def Discard(self, message):
        self.Error([message])

    def Disconnect(self):
        EthernetClientInterface.Disconnect(self)
        self.OnDisconnected()