from PyPLCS7 import PyPLCS7
from configparser import ConfigParser

class plc_r():

    def __init__(self):
        cp=ConfigParser()
        cp.read("conf.cfg")
        self.ip = cp.get("plc", "ip")
        self.plc_type=cp.get("plc","plc_type")
        self.rack = cp.get("plc", "rack")
        self.slot = cp.get("plc", "slot")
        self.plc_name=cp.get("plc","plc_name")
        self.plc=PyPLCS7.PyPLCS7(plc_type=self.plc_type,ip=self.ip,
                                 rack=self.rack,slot=self.slot)

    def plc_open(self):
        self.plc.open()

    def plc_close(self):
        self.plc.close()

    def read_value(self,address,data_type):
        if data_type in ["short"]:
            return self.plc.ReadShort(address)
        if data_type in ["int"]:
            return self.plc.ReadInt(address)
        if data_type in ["real"]:
            return self.plc.ReadReal(address)
        if data_type in ["bool"]:
            return self.plc.ReadBool(address)

