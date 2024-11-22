from math import sqrt
# from math import round as rnd
fd=-100
def dist(x1,y1,x2,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)
def rond(n,dc=0):
    return round(n*10**dc)/10**dc
mx=10000000
for i in range(1,mx,1000):
    b=rond(dist(0,sqrt(i),0,sqrt(mx)),3)
    print(rond(sqrt(i),2),b,sqrt(i)-sqrt(i-1))
    if dist(0,0,sqrt(i),0)>fd:
        fd=sqrt(i)
print(rond(fd,2))