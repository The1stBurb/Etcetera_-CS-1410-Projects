class employee:
    def __init__(self,name,title):
        self.nm,self.til=name,title
    def __str__(self):
        return f"Name: {self.nm}\n Title: {self.til}"
def gret():
    print('Hello from the "employee.py" module/page')