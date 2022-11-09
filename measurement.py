from commodity import Commodity
from descripable import Descripable
from indicator import Indicator

class Measurement(Descripable):
    def __init__(self, id: int, year: int, value: float, timeperiodId: int, timeperiodDesc: str, commodity: Commodity, indicator: Indicator):
        self.id = id
        self.__year = year
        self.__value = value
        self.__timeperiodld = timeperiodId
        self.__timeperiodDesc = timeperiodDesc
        self.commodity = commodity
        self.indicator = indicator

    def describe(self):
        print("Measurement | ", self.__year, " ", self.__timeperiodDesc, " ", self.__timeperiodld, " | ", self.__value)
        self.commodity.describe()
        self.indicator.describe()