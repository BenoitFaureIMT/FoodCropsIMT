from enum import Enum

class Indicator:
    def __init__(self, id: str, frequency: int, frequencyDesc: str, geogLocation: str):
        self.id = id
        self.__frequency = frequency
        self.__frequencyDesc = frequencyDesc
        self.__geogLocation = geogLocation

class IndicatorGroup(Enum):
    EXPORTS_AND_IMPORTS = 3
    SUPPLY_AND_USE = 2
    PRICES = 1
    FEED_PRICE_FED = 7
    TRANSPORTATION = 4
    ANIMAL_UNIT_INDEXES = 5
