from functools import reduce
listt=[4,6,8,1,5,10,7]
print(listt)
def addr(n):
    return n+1
print(list(map(addr,listt)))
def mult(n):
    if n%2==0:
        return n
print(list(filter(mult,listt)))
print(list(filter(lambda n: n%2==0,listt)))
lst=["","Argentina","","Brazil","Chile","","Columbia","","Ecuador"]
print(list(filter(None,lst)))# dont use if holds 0, empty list string tuple dict, null vals

multi=lambda x,y:x*y
print(reduce(multi,listt))