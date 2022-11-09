from typing import List

from commodity import CommodityGroup
from foodCropFactory import FoodCropFactory

import pandas as pd
from foodCropFactory import FoodCropFactory
from indicator import IndicatorGroup
from measurement import Measurement
from units import Unit


class FoodCropsDataset(FoodCropFactory):
    def __init__(self):
        super().__init__()

    def load(self, datasetPath: str):
        dataset = pd.read_csv(datasetPath)

        for index, row in dataset.iterrows():
            
            SC_Group_ID = row.get("SC_Group_ID")
            SC_Group_Desc = row.get("SC_Group_Desc")
            SC_GroupCommod_ID = row.get("SC_GroupCommod_ID")
            SC_GroupCommod_Desc = row.get("SC_GroupCommod_Desc")
            SC_Geography_ID = row.get("SC_Geography_ID")
            SortOrder = row.get("SortOrder")
            SC_GeographyIndented_Desc = row.get("SC_GeographyIndented_Desc")
            SC_Commodity_ID = row.get("SC_Commodity_ID")
            SC_Commodity_Desc = row.get("SC_Commodity_Desc")
            SC_Attribute_ID = row.get("SC_Attribute_ID")
            SC_Attribute_Desc = row.get("SC_Attribute_Desc")
            SC_Unit_ID = row.get("SC_Unit_ID")
            SC_Unit_Desc = row.get("SC_Unit_Desc")
            Year_ID = row.get("Year_ID")
            SC_Frequency_ID = row.get("SC_Frequency_ID")
            SC_Frequency_Desc = row.get("SC_Frequency_Desc")
            Timeperiod_ID = row.get("Timeperiod_ID")
            Timeperiod_Desc = row.get("Timeperiod_Desc")
            Amount = row.get("Amount")

            # Create commodity
            comod = super.createCommodity(CommodityGroup[SC_Commodity_Desc], SC_Commodity_ID, SC_Commodity_Desc)
            # Create unit
            unit = self.__getUnit(SC_Unit_ID, SC_Unit_Desc)
            #Create Indicator
            indic = super.createIndicator(SC_Attribute_ID, SC_Frequency_ID, SC_Frequency_Desc, SC_GeographyIndented_Desc, IndicatorGroup[SC_Group_Desc], unit)

            super.createMeasurement(index, Year_ID, Amount, Timeperiod_ID,Timeperiod_Desc, comod, indic)

    def __getUnit(self, unitID:int, unitName:str):
        
        volume = ['Carloads originated', '"1,000 liters"', 'Gallons']
        price = ['Index (1984=100)', 'Dollars','Cents']
        weight = {'Million bushels': 1000000, 'Bushels': 1, 'Bushel': 1, 'Cwt': 1, '"1,000 metric tons"': 1000, 'Million metric tons': 1000000, '"1,000 tons"': 1000, 'Tons': 1, 'Ton': 1, 'Pound': 1, 'Short ton': 1, 'Metric tons': 1, 'Million animal units': 1000000}
        surface = ['Million acres', '"1,000 acres"', '"1,000 hectare"', 'Acre','Hectare']
        count = []
        ratio = ['Ratio']
        ratioUnit = {'Dollars per bushel': ['Dollars','Bushel'], 'Dollars per cwt': ['Dollars','Cwt'], 'Bushels per acre': ['Bushels','Acre'], 'Tons per acre': ['Tons','Acre'], 'Dollars per ton': ['Dollars','Ton'], 'Cents per pound': ['Cents','Pound'], 'Dollars per short ton': ['Dollars','Short ton'], 'Metric tons per hectare': ['Metric tons','Hectare']}

        def getUnit_notReferenced(unitName_bis:str):
            if unitName_bis in volume:
                return super.Volume(-1, unitName_bis)
            elif unitName_bis in price:
                return super.Price(-1, unitName_bis)
            elif unitName_bis in weight:
                return super.Weight(-1, weight[unitName_bis].value, unitName_bis)
            elif unitName_bis in surface:
                return super.Surface(-1, unitName_bis)
            elif unitName_bis in count:
                return super.Count(-1, count[unitName_bis].value, unitName_bis)
            elif unitName_bis in ratio:
                return super.Ratio(-1, unitName_bis)
            return super.Unit(-1, "Unit not referenced")

        if unitName in volume:
            return super.createVolume(unitID, unitName)
        elif unitName in price:
            return super.createPrice(unitID, unitName)
        elif unitName in weight:
            return super.createWeight(unitID, weight[unitName].value, unitName)
        elif unitName in surface:
            return super.createSurface(unitID, unitName)
        elif unitName in count:
            return super.createCount(unitID, count[unitName].value, unitName)
        elif unitName in ratio:
            return super.createRatio(unitID, unitName)
        elif unitName in ratioUnit:
            unit1 = getUnit_notReferenced(ratioUnit[unitName].value[0])
            unit2 = getUnit_notReferenced(ratioUnit[unitName].value[1])
            return super.createUnitRatio(unitID, unit1, unit2, unitName)
        
        return None

    def findMeasurement(self, commodityGroup: CommodityGroup= None, indicatorGroup: IndicatorGroup = None, geographicalLocation: str = None, unit: Unit = None) -> List[Measurement]:
        return None

