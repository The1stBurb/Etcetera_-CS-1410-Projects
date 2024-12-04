#use in classses
#start and end with __
#exists even if you don't write it, writing it out just overrideds it
#like __init__
class web:
    def __init__(self):
        self.m=0
    def eat(self):
        print("web")
    def __lt__(self,ot):
        return self.m<ot.m
#prints them, includes parent class methods
class wab(web):
    def __init__(self):
        self.m=2
w=wab()
a=web()
print(dir(w),w.__dict__)
qwr=[w,a]
print(qwr[0].__class__.__name__,qwr[1].__class__.__name__)
qwr.sort()
print(qwr[0].__class__.__name__,qwr[1].__class__.__name__)
print(id(w),id(a))
#some are not "methods"
# __dict__ is just list of attributes(vars in classes)