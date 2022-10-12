from enum import Enum, auto

class CommodityGroup(Enum):
    CORN = auto()
    BARLEY = auto()
    OATS = auto()
    SORGHUM = auto()
    BYPRODUCT_FEEDS = auto()
    COARSE_GRAINS = auto()
    HAY = auto()
    FEED_GRAINS = auto()
    ANIMAL_PROTEIN_FEEDS = auto()
    GRAIN_PROTEIN_FEEDS = auto()
    PROCESSED_FEEDS = auto()
    ENERGY_FEEDS = auto()
    OTHER = auto()

class Commodity:
    def __init__(self, group:CommodityGroup, id: int, name: str):
        self.id = id
        self.__name = name