#use in classses
#start and end with __
#exists even if you don't write it, writing it out just overrideds it
#like __init__
class web:
    def __init__(self):
        self.m=0
    def eat(self):
        print("web")
#prints them, includes parent class methods
class wab(web):
    pass
w=wab()
print(dir(w),w.__dict__)
#some are not "methods"
# __dict__ is just list of attributes(vars in classes)