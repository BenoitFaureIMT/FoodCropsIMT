from measurement import Measurement
from units import Unit, Weight, Volume, Price, Surface, Count, Ratio
from commodity import CommodityGroup, Commodity
from indicator import IndicatorGroup, Indicator


class FoodCropFactory:
    def __init__(self):
        self.unitsRegistry = []
        self.indicatorsRegistry = []
        self.commodityRegistry = []

    def createVolume(self, id: int) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Volume(id)
        return self.unitsRegistry[id]

    def createPrice(self, id: int) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Price(id)
        return self.unitsRegistry[id]

    def createWeight(self, id: int, weight: float) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Weight(id, weight)
        return self.unitsRegistry[id]

    def createSurface(self, id: int) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Surface(id)
        return self.unitsRegistry[id]

    def createCount(self, id: int, what: str) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Count(id, what)
        return self.unitsRegistry[id]

    def createRatio(self, id: int) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Ratio(id)
        return self.unitsRegistry[id]

    def createCommodity(self, group: CommodityGroup, id: int, name: str) -> Commodity:
        if id not in self.commodityRegistry:
            self.commodityRegistry[id] = Commodity(group, id, name)
        return self.commodityRegistry[id]

    def createIndicator(self, id: int, frequency: int, fredDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                        unit: Unit) -> Indicator:
        if id not in self.indicatorsRegistry:
            self.indicatorsRegistry[id] = Indicator(id, frequency, fredDesc, geogLocation, indicatorGroup, unit)
        return self.indicatorsRegistry

    def createMeasurement(self, id: int, year: int, value: float, timepreriodId: int, timeperiodDesc: str,
                          commodity: Commodity, indicator: Indicator) -> Measurement:
        return Measurement(year, value, timepreriodId, timeperiodDesc, commodity, indicator)

