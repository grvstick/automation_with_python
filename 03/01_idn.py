import pyvisa as visa

# For windows, leave argument to blank
# rm = visa.ResourceManager()

# Linux uses pyvisa-py backend with pyusb
rm = visa.ResourceManager("@py")

print("INIT")
inst = None

for dev in rm.list_resources():
    print(dev)
    if "SDL" in dev:
        inst = rm.open_resource(dev)

if inst is not None:
    print(inst.query("*IDN?\n"))
