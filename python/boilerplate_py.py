def print(*objects,seperator='',end='\n'):
    f = open("result.txt","w")
    objects = seperator.join(objects)+end
    f.write(objects)
    f.close()
