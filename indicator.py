from enum import Enum, auto

class Indicator:
    def __init__(self,id: str,frequency: int,frequencyDesc: str,geogLocation: str):
        self.id = id
        self.__frequency = frequency
        self.__frequencyDesc = frequencyDesc
        self.__geogLocation = geogLocation

class IndicatorGroup(Enum):
    EXPORTS_AND_IMPORTS = auto()
    SUPPLY_AND_USE = auto()
    PRICES = auto()
    FEED_PRICE_FED = auto()
    TRANSPORTATION = auto()
    ANIMAL_UNIT_INDEXES = auto()
