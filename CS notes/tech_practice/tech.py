# Write a program that has 3 classes on a file called "tech.py". Those classes should be Tech (the parent class), Phone, and Laptop (the child classes) 
# 1. Tech should initialize name and storage
# (Note that storage should be an integer!)
# 2. Phone should initialize color
# Have a __str__ method that prints out "A {color} {name} with {storage} of storage."
# EXAMPLE: A sage Pixel 5 with 128GB of storage
# have a __repr__ method that prints "Phone({the name}, {storage}, {the color})
# EXAMPLE: Phone(Pixel 5, 128, sage)
# 3. Laptop should initialize size
# - Have a __str__ method that prints out "{size}-inch {name} with {storage} of storage."
#      EXAMPLE: 15-inch MacBook Pro with 256GB of storage.
# -have a __repr__ method that prints "Laptop({the name}, {storage}, {the size})
#      EXAMPLE: Laptop(MacBook Pro, 256, 15)
# (NOTE: Size should be an integer!)
# Then on your main.py page import tech.py
# Instantiate an instance of phone and an instance of laptop and print both instances, and print the repr for both instances. 
class tech:
    def __init__(self,name,storage):
        self.nm,self.stor=name,storage
class phone(tech):
    def __init__(self,name,storage,color):
        super().__init__(name,storage)
        self.col=color
    def __str__(self):
        return f"a {self.col} {self.nm} with {self.stor}GB of storage"
    def __repr__(self):
        return f"phone({self.nm}, {self.stor}, {self.col})"
class laptop(tech):
    def __init__(self,name,storage,size):
        super().__init__(name,storage)
        self.sz=size
    def __str__(self):
        return f"{self.sz}-inch {self.nm} with {self.stor}GB of storage"
    def __repr__(self):
        return f"laptop({self.nm}, {self.stor}, {self.sz})"
# print(phone("bob",158,"red"))