import os
import json
import pyrebase

os.system("python {}".format("code_generator.py"))

config_file = open("config.json",'r')
config = json.loads(config_file.read())
config_file.close()

firebase = pyrebase.initialize_app(config)
db = firebase.database()

users = db.child('users').get()

for user in users.each():
    key = user.key()
    user = json.loads(user.val())
    if(user["language"] == "python"):
        code = user["code"]
        p = open("./python/py.py",'w')
        p.write(code)
        p.close()
        os.system("python ./python/py.py > result.txt")
        p = open("result.txt","r")
        ans = p.read()
        db.child("users").child(key).child("result").set(ans)
