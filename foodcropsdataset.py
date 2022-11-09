import math

from typing import List

from commodity import CommodityGroup
from foodCropFactory import FoodCropFactory

import pandas as pd
from foodCropFactory import FoodCropFactory
from indicator import IndicatorGroup
from measurement import Measurement
from units import Unit, Weight, Volume, Price, Surface, Count, Ratio


class FoodCropsDataset(FoodCropFactory):
    def __init__(self):
        super().__init__()

        self.__commodityGroupMeasurementIndex = {}
        self.__indicatorGroupMeasurementIndex = {}
        self.__locationMeasurementIndex = {}
        self.__unitMeasurementIndex = {}

        self.__measurments = {}

    def load(self, datasetPath: str):
        dataset = pd.read_csv(datasetPath)
        #Progress bar
        tot = dataset.shape[0]
        width = 50

        for index, row in dataset.iterrows():
            
            # Read row's columns
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

            #Declare indexes
            commodIndex = CommodityGroup["OTHER"] if math.isnan(SC_GroupCommod_ID) else CommodityGroup(SC_GroupCommod_ID)
            indicatorIndex = IndicatorGroup(SC_Group_ID)
            locationIndex = SC_GeographyIndented_Desc

            # Create commodity
            comod = self.createCommodity(commodIndex, SC_Commodity_ID, SC_Commodity_Desc)
            # Create unit
            unit = self.__getUnit(SC_Unit_ID, SC_Unit_Desc)
            # Create Indicator
            indic = self.createIndicator(SC_Attribute_ID, SC_Frequency_ID, SC_Frequency_Desc, locationIndex, indicatorIndex, unit)

            # Store measurements
            self.__measurments[index] = self.createMeasurement(index, Year_ID, Amount, Timeperiod_ID, Timeperiod_Desc, comod, indic)

            # Index measurements
            if commodIndex in self.__commodityGroupMeasurementIndex:
                self.__commodityGroupMeasurementIndex[commodIndex].append(index)
            else:
                self.__commodityGroupMeasurementIndex[commodIndex] = [index]

            if indicatorIndex in self.__indicatorGroupMeasurementIndex:
                self.__indicatorGroupMeasurementIndex[indicatorIndex].append(index)
            else:
                self.__indicatorGroupMeasurementIndex[indicatorIndex] = [index]

            if locationIndex in self.__locationMeasurementIndex:
                self.__locationMeasurementIndex[locationIndex].append(index)
            else:
                self.__locationMeasurementIndex[locationIndex] = [index]
            
            if unit in self.__unitMeasurementIndex:
                self.__unitMeasurementIndex[unit].append(index)
            else:
                self.__unitMeasurementIndex[unit] = [index]

            #Progress bar update
            percent = 100.0*index/tot
            left = width*percent/100
            right = width-left
            print("\r[", '*'*int(left), ' '*int(right), "]", round(percent), '%', sep="", end="", flush=True)
        print()

    def __getUnit(self, unitID:int, unitName:str):
        
        volume = ['Carloads originated', '1,000 liters', 'Gallons']
        price = ['Index (1984=100)', 'Dollars','Cents']
        weight = {'Million bushels': 1000000, 'Bushels': 1, 'Bushel': 1, 'Cwt': 1, '1,000 metric tons': 1000, 'Million metric tons': 1000000, '1,000 tons': 1000, 'Tons': 1, 'Ton': 1, 'Pound': 1, 'Short ton': 1, 'Metric tons': 1, 'Million animal units': 1000000}
        surface = ['Million acres', '1,000 acres', '1,000 hectare', 'Acre','Hectare']
        count = []
        ratio = ['Ratio']
        ratioUnit = {'Dollars per bushel': ['Dollars','Bushel'], 'Dollars per cwt': ['Dollars','Cwt'], 'Bushels per acre': ['Bushels','Acre'], 'Tons per acre': ['Tons','Acre'], 'Dollars per ton': ['Dollars','Ton'], 'Cents per pound': ['Cents','Pound'], 'Dollars per short ton': ['Dollars','Short ton'], 'Metric tons per hectare': ['Metric tons','Hectare']}

        def getUnit_notReferenced(unitName_bis:str):
            if unitName_bis in volume:
                return Volume(-1, unitName_bis)
            elif unitName_bis in price:
                return Price(-1, unitName_bis)
            elif unitName_bis in weight:
                return Weight(-1, weight[unitName_bis], unitName_bis)
            elif unitName_bis in surface:
                return Surface(-1, unitName_bis)
            elif unitName_bis in count:
                return Count(-1, count[unitName_bis], unitName_bis)
            elif unitName_bis in ratio:
                return Ratio(-1, unitName_bis)
            return Unit(-1, "Unit not referenced")

        if unitName in volume:
            return self.createVolume(unitID, unitName)
        elif unitName in price:
            return self.createPrice(unitID, unitName)
        elif unitName in weight:
            return self.createWeight(unitID, weight[unitName], unitName)
        elif unitName in surface:
            return self.createSurface(unitID, unitName)
        elif unitName in count:
            return self.createCount(unitID, count[unitName], unitName)
        elif unitName in ratio:
            return self.createRatio(unitID, unitName)
        elif unitName in ratioUnit:
            unit1 = getUnit_notReferenced(ratioUnit[unitName][0])
            unit2 = getUnit_notReferenced(ratioUnit[unitName][1])
            return self.createUnitRatio(unitID, unit1, unit2, unitName)
        
        return None

    def findMeasurement(self, commodityGroup: CommodityGroup= None, indicatorGroup: IndicatorGroup = None, geographicalLocation: str = None, unit: Unit = None) -> List[Measurement]:
        possibilities = [self.__commodityGroupMeasurementIndex.get(commodityGroup), self.__indicatorGroupMeasurementIndex.get(indicatorGroup),
        self.__locationMeasurementIndex.get(geographicalLocation), self.__unitMeasurementIndex.get(unit)]

        minInd = 0
        for i in range(1, len(possibilities)):
            if possibilities[i] is None:
                continue
            if possibilities[minInd] is None or len(possibilities[minInd]) > len(possibilities[i]):
                minInd = i
        
        hold = {}
        if possibilities[minInd] is None:
            hold = self.__measurments
        else:
            for i in possibilities[minInd]:
                if all([j == minInd or possibilities[j] is None or i in possibilities[j] for j in range(len(possibilities))]):
                    hold[i] = self.__measurments[i]
        
        return hold
    
    def displayMeasurments(self, dics:dict):
        print("--------------Printing ", len(dics.values()), " values--------------")
        for v in dics.values():
            v.describe()
            print("-------")
        print("----------------------DONE---------------------")