from enum import Enum

from descripable import Descripable


# creation de la classe CommodityGroup qui est une énumération des différente commodity possible

class CommodityGroup(Enum):
    CORN = 12
    BARLEY = 9
    OATS = 17
    SORGHUM = 20
    BYPRODUCT_FEEDS = 10
    COARSE_GRAINS = 11
    HAY = 16
    FEED_GRAINS = 14
    ANIMAL_PROTEIN_FEEDS = 8
    GRAIN_PROTEIN_FEEDS = 15
    PROCESSED_FEEDS = 19
    ENERGY_FEEDS = 13
    OTHER = 18


class Commodity(Descripable):
    # Constructeur de la classe commodity
    def __init__(self, group: CommodityGroup, id: int, name: str):
        self.id = id
        self.__name = name
        self.group = group

    def describe(self):
        print(self.__name, " | Commodity #", self.id, " subset of ", self.group.name)
