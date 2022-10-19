from model.db_write import DBWrite
from model.plc_r import plc_r
from multiprocessing import Process
from datetime import datetime
import  time

def run(address, data_type):
    p_r = plc_r()
    d_w = DBWrite()
    p_r.plc_open()
    while True:
        v = p_r.read_value(address, data_type)
        d = {
            "plc_name": p_r.plc_name,
            "plc_ip": p_r.ip,
            "plc_type": p_r.plc_type,
            "rack": p_r.rack,
            "slot": p_r.slot,
            "address":address,
            "data_type": data_type,
            "value":v,
            "datetime":datetime.now(),
            "time_int":time.time(),
        }
        d_w.write(d)


if __name__ == "__main__":
    p1 = Process(target=run, args=("DB1.DBW0", "short"))
    p2 = Process(target=run, args=("DB1.DBW2", "short"))
    p3 = Process(target=run, args=("DB1.DBD4", "int"))
    p4 = Process(target=run, args=("DB1.DBD8", "real"))
