# 03/resource_scan.py

import pyvisa as visa


print("-------------PROGRAM INIT-----------------")

# For windows, leave argument to blank
# rm = visa.ResourceManager()

# Linux uses pyvisa-py backend with pyusb
rm = visa.ResourceManager("@py")


for name in rm.list_resources():
    print(name)


print("-------------PROGRAM END-----------------")
