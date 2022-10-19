import pymongo
from configparser import ConfigParser

class DBWrite():
    def __init__(self):
        cp=ConfigParser()
        cp.read("conf.cfg")
        self.myclient = pymongo.MongoClient(cp.get("db","pymongo_client"))
        self.mydb = self.myclient[cp.get("db","pymongo_db")]
        self.mycol = self.mydb[cp.get("db","pymongo_col")]

    def write(self,v):
        self.mycol.insert_one(v)
