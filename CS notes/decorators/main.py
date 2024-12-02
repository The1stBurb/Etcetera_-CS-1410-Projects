#exists in a class, like @abstractmethod
#has the @ symbol and than changes the next method, an add-on, ithout changin the contents pof the func

#this is the decorator
def cough(func):
    def func_wrapper():
        print("ahem")
        #stuff that goes boom before func  ^^^
        func()
        #stuff after  vvvvv
        print("ahem")
    return func_wrapper
@cough
def akwrd():
    print("whats 8/0?")
akwrd()