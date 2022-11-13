from enum import Enum
from descripable import Descripable
from units import Unit

# creation de la classe IndicatorGroup qui est une énumération des différents indicator possible
class IndicatorGroup(Enum):
    EXPORTS_AND_IMPORTS = 3
    SUPPLY_AND_USE = 2
    PRICES = 1
    FEED_PRICE_FED = 7
    TRANSPORTATION = 4
    ANIMAL_UNIT_INDEXES = 5
    QUANTITIES_FED = 6


class Indicator(Descripable):
    # Constructeur de la classe Indicator
    def __init__(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                 unit: Unit):
        self.id = id
        self.__frequency = frequency
        self.__freqDesc = freqDesc
        self.__geogLocation = geogLocation
        self.indicatorGroup = indicatorGroup
        self.unit = unit
    
    def describe(self):
        print(self.indicatorGroup.name,  " | Indicator #", self.id, ", frequency ", self.__frequency, " ", self.__freqDesc, ", location ", self.__geogLocation)
        self.unit.describe()
