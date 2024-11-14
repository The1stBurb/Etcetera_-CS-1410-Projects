#cathc 0 div, file not found, vlaue error, type error, index error
# num=int(input("tell me a num: "))
# num2=int(input("tell me another num: "))
# print(f"{str(num)} plus {str(num2)} is {num+num2}")
# try:
#     print(sakjgdsa)
# except TypeError:
#     print("ferg")
class negNumErr:
    pass
def tryr(t):
    try:
        num=int(input(t))
        raise negNumErr("kjsadg")
    except:
        print("Thats wrong!")
        num=tryr(t)
    return num
num=tryr("tell me a num: ")
num2=tryr("tell me another num: ")
print(f"{str(num)} plus {str(num2)} is {num+num2}")
try:#try this code
    pass
except TypeError:#if error run this
    pass
else:#if no error run this
    pass
finally:#always runs
    pass