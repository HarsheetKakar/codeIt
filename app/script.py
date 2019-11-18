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

def compileIt(user,key):
    language = user["language"]
    code = user["codeBody"]
    if(language == "Python"):
        print("python")
        p = open("./python/py.py",'w')
        p.write(code)
        p.close()
        os.system("python ./python/py.py > result.txt")

    elif(language == "C++"):
        print("c++")
        with open("./c/cpp.cpp","w") as p:
            p.write(code)
        if(platform.system() == "Windows"):
            os.system("g++ -o cpp ./c/cpp.cpp&cpp.exe > result.txt")
        elif(platform.system() == "Linux"):
            os.system("g++ ./c/cpp.cpp")
            os.system("chmod +x a.out")
            os.system("./a.out > result.txt")

    with open("result.txt","r") as p:
        ans = p.read()
        result = {
        "sender": user["sender"],
        "result": ans,
        "debugResult": "",
        }
        result = json.dumps(result)
        db.child("Result").child(key).set(result)


def stream_handler(message):
    user = message["data"]
    key = message["path"]
    print(user)
    print(key)
    try:
        if("language" not in user):
            for i in user.keys():
                compileIt(user[i],i)
        else:
            compileIt(user,key)

    except TypeError:
        pass

my_stream = db.child("Code").stream(stream_handler)
