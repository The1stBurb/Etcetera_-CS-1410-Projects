#composition is a class that exists inside another class
#vampire class has a monster class (inside): True
#monster class has a vampire class: False
#class has an other class
class car:
    def __init__(self,make,model,year,engine):
        self.mk,self.mdl,self.yr=make,model,year
        self.eng=engine
    def __str__(self):
        return f"A {self.mdl} {self.mk} from {self.yr} with {self.eng}"
class engine:
    def __init__(self,config,displacement,horspwr,torque):
        self.con,self.dis,self.hp,self.tq=config,displacement,horspwr,torque
    def __str__(self):
        return f"an engine with {self.hp} horsepower, {self.tq} torque, {self.dis} displacement, and a config of {self.con}."
    def ign(self):
        print("vroom vroom")
engn=engine("v36.5","3.141596","456","0.1")
mc=car("frog","toyadoy","4391",engn)
print(mc)
mc.eng.ign()
#to acces a composite class, you have to call the item that holds the class^^ aka you need to call .eng to call .ign(), because .ign() isn't part mc
#composite has other class, inheritance IS the other class