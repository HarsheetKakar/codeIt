import json
import pyrebase

configuration_file = open("config.json",'r')
config = json.loads((configuration_file.read()))
configuration_file.close()

firebase = pyrebase.initialize_app(config)

class Entries:
    def __init__(self,sender,language,codeBody):
        self.user = {
        "sender" : sender,
        "language" : language,
        "codeBody" : codeBody
        }

    def getDict(self):
        return self.user

    def getJSON(self):
        return json.dumps(self.user)

if __name__ == '__main__':
    python = r"""print("hello")"""
    cpp = r"""#include<iostream>

using namespace std;

int main()
{
    cout<<"Hello World";
    return 0;
}
"""
    u1 = Entries("harsheet","python",python)
    u2 = Entries("anshul","c++",cpp)
    db = firebase.database()
    auth = firebase.auth()
    try:
        auth.create_user_with_email_and_password("testUser1@gmail.com","123456")
        auth.create_user_with_email_and_password("testUser2@gmail.com","123456")
    except Exception:
        pass
    user1 = auth.sign_in_with_email_and_password("testUser1@gmail.com","123456")
    user2 = auth.sign_in_with_email_and_password("testUser2@gmail.com","123456")
    db.child("Code").push(u1.getDict(),user1["idToken"])
    db.child("Code").push(u2.getDict(),user2["idToken"])
