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

            # Création Unit

            comod = self.FoodCropFactory.createCommodity(CommodityGroup[SC_Commodity_Desc], SC_Commodity_ID, SC_Commodity_Desc)
            indic = self.FoodCropFactory.createIndicator(SC_Attribute_ID, SC_Frequency_ID, SC_Frequency_Desc, SC_GeographyIndented_Desc, IndicatorGroup[SC_Group_Desc], '''UNIT''')

            self.FoodCropFactory.createMeasurement(index, Year_ID, Amount, Timeperiod_ID,Timeperiod_Desc, comod, indic)

    def findMeasurement(self, commodityGroup: CommodityGroup= None, indicatorGroup: IndicatorGroup = None, geographicalLocation: str = None, unit: Unit = None) -> List[Measurement]:
        return None

