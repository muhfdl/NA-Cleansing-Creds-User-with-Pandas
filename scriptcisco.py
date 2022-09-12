import paramiko
import time
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('creds-cleansing.xlsx')
devices = [
    {
        'ip_address' : df['IP Address'][0],
        'vendor' : 'cisco',
        'username' : df['Username'][0],
        'password' : df['Password'][0]
    },
    {
        'ip_address' : df['IP Address'][1],
        'vendor' : 'cisco',
        'username' : df['Username'][1],
        'password' : df['Password'][1]
    },
    {
        'ip_address' : df['IP Address'][2],
        'vendor' : 'cisco',
        'username' : df['Username'][2],
        'password' : df['Password'][2]
    },
    {
        'ip_address' : df['IP Address'][3],
        'vendor' : 'cisco',
        'username' : df['Username'][3],
        'password' : df['Password'][3]
    }
]

interface=input('What interface do you want to configure?\n')
print("----------------------------------------")
address=input('Enter Ip Address and NetMask\n')
print("----------------------------------------\n")

print("Interface is: "+interface)
print("IP Address is: "+address)

input=input('\npress enter to continue')

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for device in devices:
    ssh_client.connect(hostname=device['ip_address'],username=device['username'], password=device['password'])
    print("\nSuccess login to {}".format(device['ip_address']))

    if device['vendor'] == 'cisco':
        conn = ssh_client.invoke_shell()

        # Input Configuration to Devices
        print("----------------------------------------")
        print("# Configure Device")
        conn.send("conf t\n")
        conn.send("int "+interface+"\n")
        time.sleep(2)
        conn.send("ip add "+address+"\n")
        time.sleep(2)
        conn.send("no shutdown\n")
        conn.send("end\n")
        time.sleep(3)
        conn.send("wr\n")
        time.sleep(3)
        output = conn.recv(65535)
        print(output.decode())

        # Verify Configuration
        print("----------------------------------------")
        print("# Verify Configuration\n")
        conn.send("terminal length 0\n")
        conn.send("show ip int br\n")
        time.sleep(2)
        output = conn.recv(65535)
        print(output.decode())

        # Check Version Devices
        print("----------------------------------------")
        print("# Version Check\n")
        conn.send('terminal length 0\n')
        conn.send("show version\n")
        time.sleep(3)
        output = conn.recv(65535)
        print(output.decode())

        # Backup Configuration
        print("----------------------------------------")
        print("# Backup Configuration\n")
        conn.send('terminal length 0\n')
        conn.send("show running-config\n")
        time.sleep(5)
        
        output = conn.recv(65535)
        write = open(device['ip_address']+'.txt','w')
        write.write(output.decode())
        print(output.decode())

    ssh_client.close()