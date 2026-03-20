import json
from extronlib.system import File

BaseCredentialDict = {
    'IPCP Pro 250 xi': {
        'username': 'admin', 
        'password': 'A2CJNNL'
    },
    'TLP Pro 725M': {
        'username': 'admin', 
        'password': 'A2CJNNL'
    }
}
#dictionary with default username:password

def GetUsername(device:str) ->str:
    '''
    This function returns a `username` for `device` or None
    '''
    if BaseCredentialDict.get(device):
        return BaseCredentialDict.get(device).get('username')
    else:
        print('No username found for {} device'.format(device))

def GetPassword(device:str) ->str:
    '''
    This function returns a `password` for `device` or None
    '''
    if BaseCredentialDict.get(device):
        return BaseCredentialDict.get(device).get('password')
    else:
        print('No password found for {} device'.format(device))

if File.Exists('credentials.json'): #if file already exist on sftp
    with File('credentials.json', 'r') as CredFile:
        try:
            CredentialsDict = json.load(CredFile) #type:dict
            for device in BaseCredentialDict.keys():
                if CredentialsDict.get(device):
                    if CredentialsDict.get(device).get('username') and CredentialsDict.get(device).get('password') \
                    and CredentialsDict.get(device) != BaseCredentialDict.get(device):
                        BaseCredentialDict[device] = CredentialsDict.get(device)
                        print('Credentials for {} updated from the file'.format(device))
                    else:
                        print('Using default credentials for {}'.format(device))
                else:
                    print('credentials.json file was missing an entry for {}, updated from default'.format(device))
        except json.JSONDecodeError as err:
            print('credentials.json is misconfigured and will be overwriten with default values')
            

       
else:
    print('no credentials.json found, a new one is created with default values')

with File('credentials.json', 'w') as CredFile: 
    json.dump(BaseCredentialDict, CredFile)









