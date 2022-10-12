from indicator import Indicator
from commodity import Commodity
class Measurement:
    def __init__(self,year: int,value: float,timeperiodld: float,timeperiodDescr: str):
        self.__year = year
        self.__value = value
        self.__timeperiodld = timeperiodld
        self.__timeperiodDescr = timeperiodDescr

    def measurement(self, id:int,year:int, value:float, timeperiodld:int, timeperiodDesc:str, commodity:Commodity,indicator:Indicator):

