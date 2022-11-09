from abc import ABC
from descriptable import Descripable

class Unit(Descripable): 
    def __init__(self, id:int, name:str):
        self.id = id
        self.name  = name
    
    def describe(self):
        print("Unit | ", self.name, " | ", self.id)


class Volume(Unit):
    def __init__(self, id:int):
        super(Volume, self).__init__(id, "Volume")


class Price(Unit):
    def __init__(self, id:int):
        super(Price, self).__init__(id, "Price")


class Weight(Unit):
    def __init__(self, id:int, multiplier:float):
        super(Weight, self).__init__(id, "Weight")
        self.__multiplier = multiplier
    
    def describe(self):
        print("Unit | ", self.name, " | ", self.id, " | ", self.__multiplier)


class Surface(Unit):
    def __init__(self, id:int):
        super(Surface, self).__init__(id, "Surface")


class Count(Unit):
    def __init__(self, id:int, what:str):
        super(Count, self).__init__(id, "Count")
        self.__what = what
    
    def describe(self):
        print("Unit | ", self.name, " | ", self.id, " | ", self.__what)


class Ratio(Unit):
    def __init__(self, id:int):
        super(Ratio, self).__init__(id, "Ratio")