from commodity import Commodity
from indicator import Indicator


class Measurement:
    def __init__(self,year: int,value: float,timeperiodld: float,timeperiodDescr: str):
        self.__year = year
        self.__value = value
        self.__timeperiodld = timeperiodld
        self.__timeperiodDescr = timeperiodDescr
    
    def measurment(id: int, year: int, value: float, timeperiodld: float, timeperiodDesc: str, commodity: Commodity, indicator: Indicator):
        return None