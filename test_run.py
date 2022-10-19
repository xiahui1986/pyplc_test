from control.run_now import run
from multiprocessing import Process
def r():
    p1 = Process(target=run, args=("DB1.DBW0", "short"))
    p2 = Process(target=run, args=("DB1.DBW2", "short"))
    p3 = Process(target=run, args=("DB1.DBD4", "real"))
    p4 = Process(target=run, args=("DB1.DBD8", "int"))
    p1.start()
    p2.start()
    p3.start()
    p4.start()

if __name__=="__main__":
    r()