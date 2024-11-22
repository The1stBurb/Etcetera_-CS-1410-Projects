class app:
    def __init__(self,name,describ,cat):
        self.nm,self.des,self.cat=name,describ,cat
    def __str__(self):
        return f"Name: {self.nm}\n Description: {self.des}\n Category: {self.cat}"