from configparser import ConfigParser
cp=ConfigParser()
cp.read("conf.cfg")
print(cp.get('plc','text'))

print(cp.get("plc","ip"))
cp.set("plc","text","123444")
cp.write(open("conf.cfg","w+"))
print(cp.get('plc','text'))
