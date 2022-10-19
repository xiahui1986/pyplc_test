import clr
import datetime as dt
import sys
import pymongo
import time
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["s71200"]
mycol=mydb['1200']

sys.path.append("g:\\py/pyplc_test/dll")
clr.FindAssembly('plc_for_python.dll')
from plc_for_python import *

test=PyPlc(30,"192.168.0.1",0,1)
test.PLCOpen()
a=test.WriteF("DB1.DBW20",123.0,"float")

while True:
    print(dt.datetime.now())
    print(test.ReadReal("DB1.DBD4"))
    mycol.insert_one({'time':time.time(),'address':"DB1.DBW20",'value':test.ReadReal("DB1.DBD4")})
    print(dt.datetime.now())
test.PLCClose()




