from PyPLCS7 import PyPLCS7


def read_test():
    a = PyPLCS7.PyPLCS7(plc_type="s71200", ip="192.168.0.1", rack=0, slot=1)
    a.open()
    print(a.ReadShort("DB1.DBW2"))
    a.close()
