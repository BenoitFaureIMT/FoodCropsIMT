from commodity import Commodity
from indicator import Indicator

class Measurement:
    def __init__(self, year: int, value: float, timeperiodId: int, timeperiodDesc: str, commodity: Commodity, indicator: Indicator):
        self.__year = year
        self.__value = value
        self.__timeperiodld = timeperiodId
        self.__timeperiodDesc = timeperiodDesc
        self.commodity = commodity
        self.indicator = indicator

