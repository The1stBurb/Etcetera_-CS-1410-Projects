from backpackager import paged
from abc import ABC,abstractmethod
class dsrtItm(ABC):
    def __init__(self,nm,pack):#,nm):
        self.nm=nm
        self.txp=0.725
        self.packa=paged(pack)
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
        #Candy Corn, 1.5lbs, $0.25/lb, $0.38, 0.03
class candy(dsrtItm):#("candy")
    def __init__(self,nm,weg,ppp):
        super().__init__(nm,"Bag")
        self.quan=weg
        self.pp_=ppp
    def cost(self):
        return self.quan*self.pp_
    def __str__(self):
        return f"{self.nm} ({self.packa}), {self.quan}lbs, ${self.pp_}/lb, ${self.cost()}, {self.calctx()}"

class cookie(dsrtItm):#("cookie")
    def __init__(self,nm,quan,ppd):
        super().__init__(nm,"Box")
        self.quan=quan
        self.pp_=ppd
    def cost(self):
        return self.quan*self.pp_
    def __str__(self):
        return f"{self.nm}, ({self.packa}) {self.quan} dozens, ${self.pp_}/dzn, ${self.cost()}, {self.calctx()}"
    
class iceCream(dsrtItm):#("ice cream")
    def __init__(self,nm,scps,pps):
        super().__init__(nm,"Bowl")
        self.quan=scps
        self.pp_=pps
    def cost(self):
        return self.quan*self.pp_
    def __str__(self):
        return f"{self.nm} ({self.packa}), {self.quan} scoops, ${self.pp_}/scp, ${self.cost()}, {self.calctx()}"
    
class sunday(iceCream):#("sunday")
    def __init__(self,nm,scps,pps,top,ppt):
        super().__init__(nm,scps,pps)
        self.tp=top
        self.qun=1
        self.ppt=ppt
        self.packa.pack="Boat"
    def cost(self):
        return self.quan*self.pp_+self.ppt
    def __str__(self):
        return f"{self.nm} ({self.packa}), {self.quan} scoops, ${self.pp_}/scp, ${self.cost()}, {self.calctx()}\n {self.tp} topping, {self.qun}, {self.ppt}, , , "
    # def __str__(self):
    #     return f"Type: {self.__class__.__name__}\nName: {self.nm}\nQuantity: {self.quan}\nPrice Per: {self.pp_}\nWith: {self.tp}\nPrice of: {self.ppt}"
    # print(candy("",1,2).calctx())