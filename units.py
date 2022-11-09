from abc import ABC
from descripable import Descripable

class Unit(Descripable): 
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
    
    def describe(self):
        print(self.name, " | Unit #", self.id)


class Volume(Unit):
    def __init__(self, id:int, name:str = "Volumne"):
        super(Volume, self).__init__(id, name)


class Price(Unit):
    def __init__(self, id:int, name:str = "Price"):
        super(Price, self).__init__(id, name)


class Weight(Unit):
    def __init__(self, id:int, multiplier:float, name:str = "Weight"):
        super(Weight, self).__init__(id, name)
        self.__multiplier = multiplier
    
    def describe(self):
        print(self.__multiplier, " ", self.name, " | Unit #", self.id)


class Surface(Unit):
    def __init__(self, id:int, name:str = "Surface"):
        super(Surface, self).__init__(id, name)


class Count(Unit):
    def __init__(self, id:int, what:str, name:str = "Count"):
        super(Count, self).__init__(id, name)
        self.__what = what
    
    def describe(self):
        print(self.__what, " ", self.name, " | Unit #", self.id)


class Ratio(Unit):
    def __init__(self, id:int, name:str = "Ratio"):
        super(Ratio, self).__init__(id, name)

class UnitRatio(Unit):
    def __init__(self, id:int, unit1:Unit, unit2:Unit, name:str = "Ratio"):
        super(UnitRatio, self).__init__(id, name)
        self.unit1 = unit1
        self.unit2 = unit2
    
    def describe(self):
        super().describe()
        self.unit1.describe()
        self.unit2.describe()