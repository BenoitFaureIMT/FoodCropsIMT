from measurement import Measurement
from units import Unit
from commodity import CommodityGroup, Commodity
from indicator import IndicatorGroup, Indicator


class FoodCropFactory:
    def __init__(self):
        self.unitsRegistry = []
        self.indicatorsRegistry =[]
        self.commodityRegistry = []

    def createVolume(self, id: int) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry.append(id,)
        return id


    def createPrice(self, id: int)-> Unit:
        return None

    def createWeight(self, id: int, weight: float) -> Unit:
        return None

    def createSurface(self,id: int) -> Unit:
        return None

    def createCount(self,id: int, what: str) -> Unit:
        return None

    def createRatio(self, id: int) -> Unit:
        return None

    def createCommodity(self, group: CommodityGroup, id: int, name, str) -> Commodity:
        return None

    def createIndicator(self, id: int, frequency: int, fredDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup, unit: Unit) -> Indicator:
        return None

    def createMeasurement(self, id: int, year: int, value: float, timepreriodId: int, timeperiodDesc: str, commodity: Commodity, indicator: Indicator) -> Measurement:
        return None






