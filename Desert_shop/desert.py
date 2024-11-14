
# Sample Run
# attribute tax_percent is in DessertItem class
# method calculate_cost is abstract in DessertItem and concrete in all inheriting subclasses
# method calculate_tax is concrete in DessertItem and is NOT overrriden in any inheriting subclasses
# pytest test cases have been created or modified as described above
# PDF receipt output file should look similar to the sample run shown above
# Your workspace should have the following 7 files:
# desserts.py
# dessertshop.py
# test_dessert.py
# test_candy.py
# test_cookie.py
# test_icecream.py
# test_sundae.py
# This way you don’t end up with one huge test file.

from abc import ABC,abstractmethod
class dsrtItm(ABC):
    def __init__(self,nm):#,nm):
        self.nm=nm
        self.txp=7.25
    def __str__(self):
        return f"Type: {self.__class__.__name__}\nName: {self.nm}\nQuantity: {self.quan}\nPrice Per: {self.pp_}"
    @abstractmethod
    def cost(self):
        return self.quan*self.pp_
    def calctx(self):
        return round((self.txp*self.cost())*100)/100
    def gt_nm(self):
        return self.nm
    def get_quan(self):
        return self.quan
    
class candy(dsrtItm):#("candy")
    def __init__(self,nm,weg,ppp):
        super().__init__(nm)
        self.quan=weg
        self.pp_=ppp
    def cost(self):
        return self.quan*self.pp_

class cookie(dsrtItm):#("cookie")
    def __init__(self,nm,quan,ppd):
        super().__init__(nm)
        self.quan=quan
        self.pp_=ppd
    def cost(self):
        return self.quan*self.pp_
    
class iceCream(dsrtItm):#("ice cream")
    def __init__(self,nm,scps,pps):
        super().__init__(nm)
        self.quan=scps
        self.pp_=pps
    def cost(self):
        return self.quan*self.pp_
    
class sunday(iceCream):#("sunday")
    def __init__(self,nm,scps,pps,top,ppt):
        super().__init__(nm,scps,pps)
        self.tp=top
        self.qun=1
        self.ppt=ppt
    def cost(self):
        return self.quan*self.pp_+self.ppt
    def __str__(self):
        return f"Type: {self.__class__.__name__}\nName: {self.nm}\nQuantity: {self.quan}\nPrice Per: {self.pp_}\nWith: {self.tp}\nPrice of: {self.ppt}"