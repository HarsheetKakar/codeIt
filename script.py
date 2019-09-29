import os
import json

os.system("python {}".format("code_generator.py"))
f = open("code.txt",'r')
users = json.loads(f.read())
for i in users:
    if(i["language"]=="python"):
        before = open("./python/boilerplate_py.py","r")
        p = open("./python/py.py","w")
        p.write(before.read())
        p.write(i["code"])
        p.close()
        before.close()
        os.system("python {}".format("./python/py.py"))
f.close()
