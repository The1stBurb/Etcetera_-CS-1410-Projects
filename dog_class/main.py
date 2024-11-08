from csv import reader
class dug:
    def __init__(self,name,breed):
        self.nm,self.br=name,breed
    def __str__(self):
        return f"{self.nm} is a {self.br}!"
dugs=[]
with open("dog_class\\dug_list.csv","r")as apl:
    cr=reader(apl,delimiter=",")
    next(cr)
    for nm,bred in cr:
        dugs.append(dug(nm,bred))
for i in dugs:
    print(i)