import clr
import sys
import os

sys.path.append(os.getcwd() + "/dll")
#clr.FindAssembly('plc_for_python.dll')
clr.AddReference('plc_for_python')
from plc_for_python import *


class PyPLCS7:
    def __init__(self, plc_type, ip, rack, slot):
        plc_code = 0
        if plc_type in ["S7200", "s7200", "200", ]:
            plc_code = 0
        elif plc_type in ["S7300", "s7300", "300"]:
            plc_code = 10
        elif plc_type in ["S7400", "s7400", "400"]:
            plc_code = 20
        elif plc_type in ["S71200", "s71200", "1200"]:
            plc_code = 30
        elif plc_type in ["S71500", "s71500", "1500"]:
            plc_code = 40
        self.plc = PyPlc(plc_code, ip, rack, slot)

    def open(self):
        self.plc.PLCOpen()

    def close(self):
        self.plc.PLCClose()

    def WriteF(self, address, val, data_type):
        if data_type in ["short", ]:
            data_type = "short"
        if data_type in ["int", "Int", "long"]:
            data_type = "int"
        if data_type in ["real", "float"]:
            data_type = "float"
        if data_type in ["bool", "Bool", "boolean", "Boolean"]:
            data_type = "bool"
        self.plc.WriteF(address, val, data_type)

    def ReadBool(self, address):
        return self.plc.ReadBool(address)

    def ReadShort(self, address):
        return self.plc.ReadShort(address)

    def ReadInt(self, address):
        return self.plc.ReadInt(address)

    def ReadReal(self, address):
        return self.plc.ReadReal(address)
