import os
import json
import pyrebase
import platform
import stat

#os.system("python {}".format("code_generator.py"))

config_file = open("./config.json",'r')
config = json.loads(config_file.read())
config_file.close()

firebase = pyrebase.initialize_app(config)
db = firebase.database()

users = db.child('Code').get()

def stream_handler(message):
    user = message["data"]
    key = message["path"]
    print(user)
    try:
        if(user["language"] == "Python"):
            print("python")
            code = user["codeBody"]
            p = open("./python/py.py",'w')
            p.write(code)
            p.close()
            os.system("python ./python/py.py > result.txt")

        elif(user["language"] == "C++"):
            print("c++")
            code = user["codeBody"]
            p = open("./c/cpp.cpp","w")
            p.write(code)
            p.close()
            if(platform.system() == "Windows"):
                print("c++ windows")
                os.system("g++ -o cpp ./c/cpp.cpp&cpp.exe > result.txt")
            elif(platform.system() == "Linux"):
                print("c++ Linux")
                os.system("g++ ./c/cpp.cpp")
                print("compiled")
                os.system("chmod +x a.out")
                os.system("./a.out > result.txt")
                print("result given")
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
        print("result sent")
    except TypeError:
        pass

my_stream = db.child("Code").stream(stream_handler)
