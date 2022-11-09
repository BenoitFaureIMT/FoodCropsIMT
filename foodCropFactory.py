from measurement import Measurement
from units import Unit, Weight, Volume, Price, Surface, Count, Ratio, UnitRatio
from commodity import CommodityGroup, Commodity
from indicator import IndicatorGroup, Indicator


class FoodCropFactory:
    def __init__(self):
        self.unitsRegistry = {}
        self.indicatorsRegistry = {}
        self.commodityRegistry = {}

    def createVolume(self, id: int, name:str) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Volume(id, name)
        return self.unitsRegistry[id]

    def createPrice(self, id: int, name:str) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Price(id, name)
        return self.unitsRegistry[id]

    def createWeight(self, id: int, weight: float, name:str) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Weight(id, weight, name)
        return self.unitsRegistry[id]

    def createSurface(self, id: int, name:str) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Surface(id, name)
        return self.unitsRegistry[id]

    def createCount(self, id: int, what: str, name:str) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Count(id, what, name)
        return self.unitsRegistry[id]

    def createRatio(self, id: int, name:str) -> Unit:
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = Ratio(id, name)
        return self.unitsRegistry[id]
    
    def createUnitRatio(self, id: int, unit1:Unit, unit2:Unit, name:str):
        if id not in self.unitsRegistry:
            self.unitsRegistry[id] = UnitRatio(id, unit1, unit2, name)
        return self.unitsRegistry[id]

    def createCommodity(self, group: CommodityGroup, id: int, name: str) -> Commodity:
        if id not in self.commodityRegistry:
            self.commodityRegistry[id] = Commodity(group, id, name)
        return self.commodityRegistry[id]

    def createIndicator(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                        unit: Unit) -> Indicator:
        if id not in self.indicatorsRegistry:
            self.indicatorsRegistry[id] = Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup, unit)
        return self.indicatorsRegistry[id]

    def createMeasurement(self, id: int, year: int, value: float, timepreriodId: int, timeperiodDesc: str,
                          commodity: Commodity, indicator: Indicator) -> Measurement:
        return Measurement(id, year, value, timepreriodId, timeperiodDesc, commodity, indicator)

