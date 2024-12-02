from operator import attrgetter
li=[9,1,8,2,7,3,6,4,5]
# print(li)
li.sort()
# print(li)
li=[9,1,8,2,7,3,6,4,5]
# print(li)
li.sort(reverse=True)
# print(li)
#tuples use:
li=(1,3,2)
# print(li)
li=sorted(li,reverse=False)
# print(li)
di={"saf":1,"sadg":3}
# print(di)
di=sorted(di)
# print(di)
class emp:
    def __init__(self,nm,ag,sal):
        self.nm=nm
        self.ag=ag
        self.sal=sal
    def __repr__(self):
        return "({},{},${})".format(self.nm,self.ag,self.sal)
def esrt(e1):
    return e1.nm
jfd=emp("jfd",2,2135.01)
fdj=emp("fdj",20,0.01)
djf=emp("djf",2000,0.0001)
emps=[jfd,fdj,djf]
semps=sorted(emps,key=esrt)#or
print(semps)
semps=sorted(emps,key=attrgetter("ag"))#or
print(semps)