import subprocess
import platform
import socket
import time
import os
from rich import print

from matplotlib.dates import HOURS_PER_DAY

# lista = ["local", "date", "list", "list -a",
#          "ping", "echo me", "help", "exit"]
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Py Terminal [ Version 1.00 ]")
while True:
    code = input(">>>")
    # if code != lista:
    #     print(f"'{code}' is not recognized as an command,\nUse help command.")
    if code == "ping":
        host = input("Enter Website To ping: ")
        number = input("Enter How many times To ping: ")

        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
    if code == "local":
        print("Your Local IPS is: " + host_ip)
        print("Your Desktop Name is: " + host_name)
    if code == "date":
        print("The Local Date is: " + time.strftime("%m/%d/%Y"))
    if code == "list":
        dir_list = os.listdir(path)
        print("Files & Directories in '", path, "' :")
        print(dir_list)
    if code == "list -a":
        file = input("Enter the Direct File Path to Read: ")
        dir_list2 = os.listdir(file)
        print("Files & Directories in '", file, "':")
        print(dir_list2)
    if code == "echo me":
        echo = input("What do you want me to Echo: ")
        print(echo)
    if code == "help":
        print("Commands: ")
        print("\tlocal\n\tdate\n\tlist\n\tlist -a\n\tping\n\techo me\n\thelp\n\texit")
    if code == "exit":
        os._exit(0)
