import string
import itertools
#this is a prebuilt thing that allows you to create data
#instead of storing, it builds it right then
#saves storage
def nums():
    yield 1
    yield 2
    yield 3
# print([x for x in nums()])
def letters():
    #capwords("yar skjdg sdg. dsjf fdgh") capatilizes sentences
    for c in string.ascii_lowercase:
        yield c
# for lt in letters():
#     print(lt)
def prim():
    yield 2
    prim_cache=[2]
    for i in itertools.count(3,2):
        is_pri=True
        for p in prim_cache:
            if i%p==0:
                is_pri=False
                break
        if is_pri:
            prim_cache.append(i)
            yield i
        if len(prim_cache)>100:
            break
# for i in prim():
#     print(i)
squre=(x**2 for x in itertools.count(1))
for x in squre:
    print(x)
    if x>1329:
        pass
        # break