import os
import json
import pyrebase
import platform

#os.system("python {}".format("code_generator.py"))

config_file = open("./config.json",'r')
config = json.loads(config_file.read())
config_file.close()

firebase = pyrebase.initialize_app(config)
db = firebase.database()

users = db.child('Code').get()

for user in users.each():
    key = user.key()
    user = user.val()
    if(user["language"] == "Python"):
        code = user["codeBody"]
        p = open("./python/py.py",'w')
        p.write(code)
        p.close()
        os.system("python ./python/py.py > result.txt")

    elif(user["language"] == "C++"):
        code = user["codeBody"]
        p = open("./c/cpp.cpp","w")
        p.write(code)
        p.close()
        os.system("g++ -o cpp ./c/cpp.cpp")
        if(platform.system() == "Linux"):
            os.system("chmod 777 ./cpp")
        os.system("cpp > result.txt")
    p = open("result.txt","r")
    ans = p.read()
    p.close()
    result = {
    "sender": user["sender"],
    "result": ans,
    "debugResult": "",
    }
    result = json.dumps(result)
    db.child("Result").child(key).set(result)
