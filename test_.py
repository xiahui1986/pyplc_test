from PyPLCS7 import PyPLCS7
import pymongo,time
from multiprocessing import Process
from model.db_write import DBWrite

def read_test(address):
    a = PyPLCS7.PyPLCS7(plc_type="s71200", ip="192.168.0.1", rack=0, slot=1)
    a.open()
    while True:
        #print(a.ReadShort("DB1.DBW2"))
        print(a.ReadShort(address))

    #print(a.ReadShort("DB1.DBW2"))
    #print(a.ReadReal("DB1.DBD24"))
    a.close()

if __name__=="__main__":
    p1=Process(target=read_test,args=("DB1.DBW2",))
    p2= Process(target=read_test, args=("DB1.DBW0",))
    p1.start()
    p2.start()
