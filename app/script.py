import os
import json
import pyrebase
import platform
import stat

config_file = open("./config.json",'r')
config = json.loads(config_file.read())
config_file.close()

firebase = pyrebase.initialize_app(config)
db = firebase.database()

users = db.child('Code').get()

def python_compile(code):
    with open("./python/py.py",'w') as p:
        p.write(code)
    os.system("python ./python/py.py > result.txt")

def cpp_compile(code):
    with open("./cpp/cpp.cpp","w") as p:
        p.write(code)
    if(platform.system() == "Windows"):
        os.chdir("./cpp")
        os.system("g++ -o cpp ./cpp.cpp&cpp.exe > ../result.txt")
        os.chdir("../")
    elif(platform.system() == "Linux"):
        os.system("g++ ./c/cpp.cpp")
        os.system("chmod +x a.out")
        os.system("./a.out > result.txt")

def java_compile(code):
    with open("./java8/java8.java","w") as p: #for now put the class name as java8
        p.write(code)
    os.system("javac ./java8/java8.java")
    os.chdir("./java8")
    os.system("java java8 > ../result.txt")
    os.chdir("../") #changing it back to original directory

def compileIt(user,key):
    language = user["language"]
    code = user["codeBody"]
    if(language == "Python"):
        python_compile(code)

    elif(language == "C++"):
        cpp_compile(code)

    elif(language == "Java8"):
        java_compile(code)

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
    try:
        if("language" not in user):
            for i in user.keys():
                compileIt(user[i],i)
        else:
            compileIt(user,key)

    except TypeError:
        pass

my_stream = db.child("Code").stream(stream_handler)
