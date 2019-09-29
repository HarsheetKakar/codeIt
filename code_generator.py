import json

class Entries:
    def __init__(self,username,language,code):
        self.user = {
        "username" : username,
        "language" : language,
        "code" : code
        }

    def getDict(self):
        return self.user

if __name__ == '__main__':
    python = r"""print("hello")"""
    u1 = Entries("harsheet","python",python)

    f = open("code.txt","w+")
    a = []
    a.append(u1.getDict())
    f.write(json.dumps(a))
    f.close()
