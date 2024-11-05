from employee import employee,gret
from app import app
from csv import reader
emp=employee("Marc","VP Sales")
print(emp)
gret()
apps=[]
with open("app_list.csv","r")as apl:
    cr=reader(apl,delimiter=",")
    next(cr)
    for nm,dis,cat in cr:
        apps.append(app(nm,dis,cat))
for ap in apps:
    print(ap)