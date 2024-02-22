# 03/idn.py

import pyvisa as visa


print("-------------PROGRAM INIT-----------------")

# For windows, leave argument to blank
# rm = visa.ResourceManager()

# Linux uses pyvisa-py backend with pyusb
rm = visa.ResourceManager("@py")


for name in rm.list_resources():
    print(name)
    if "USB" in name and "INSTR" in name:
        inst = rm.open_resource(name)
        print(inst.query("*IDN?"))
        inst.close()


print("-------------PROGRAM END-----------------")