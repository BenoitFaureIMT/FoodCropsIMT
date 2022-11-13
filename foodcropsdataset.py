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

        self.__locationMeasurementIndex = {}
        self.__allMeasurementsIndex = {}

        self.__measurments = {}

    def load(self, datasetPath: str):
        dataset = pd.read_csv(datasetPath)
        #Progress bar
        tot = dataset.shape[0]
        width = 50
        mile_stone = 0

        
        # Separate columns for faster access
        SC_Group_ID = dataset["SC_Group_ID"]
        # SC_Group_Desc = dataset["SC_Group_Desc"]
        SC_GroupCommod_ID = dataset["SC_GroupCommod_ID"]
        # SC_GroupCommod_Desc = dataset["SC_GroupCommod_Desc"]
        # SC_Geography_ID = dataset["SC_Geography_ID"]
        # SortOrder = dataset["SortOrder"]
        SC_GeographyIndented_Desc = dataset["SC_GeographyIndented_Desc"]
        SC_Commodity_ID = dataset["SC_Commodity_ID"]
        SC_Commodity_Desc = dataset["SC_Commodity_Desc"]
        SC_Attribute_ID = dataset["SC_Attribute_ID"]
        # SC_Attribute_Desc = dataset["SC_Attribute_Desc"]
        SC_Unit_ID = dataset["SC_Unit_ID"]
        SC_Unit_Desc = dataset["SC_Unit_Desc"]
        Year_ID = dataset["Year_ID"]
        SC_Frequency_ID = dataset["SC_Frequency_ID"]
        SC_Frequency_Desc = dataset["SC_Frequency_Desc"]
        Timeperiod_ID = dataset["Timeperiod_ID"]
        Timeperiod_Desc = dataset["Timeperiod_Desc"]
        Amount = dataset["Amount"]

        for index in dataset.index:
            
            #Declare indexes
            SC_GroupCommod_ID_h = SC_GroupCommod_ID[index]
            commodIndex = CommodityGroup["OTHER"] if math.isnan(SC_GroupCommod_ID_h) else CommodityGroup(SC_GroupCommod_ID_h)
            indicatorIndex = IndicatorGroup(SC_Group_ID[index])
            locationIndex = SC_GeographyIndented_Desc[index].strip()

            # Create commodity
            comod = self.createCommodity(commodIndex, SC_Commodity_ID[index], SC_Commodity_Desc[index])
            # Create unit
            unit = self.__getUnit(SC_Unit_ID[index], SC_Unit_Desc[index])
            # Create Indicator
            indic = self.createIndicator(SC_Attribute_ID[index], SC_Frequency_ID[index], SC_Frequency_Desc[index], locationIndex, indicatorIndex, unit)
            # Store measurements
            self.__measurments[index] = self.createMeasurement(index, Year_ID[index], Amount[index], Timeperiod_ID[index], Timeperiod_Desc[index], comod, indic)

            # Index measurements - using nested dictionaries
            if not commodIndex in self.__allMeasurementsIndex:
                self.__allMeasurementsIndex[commodIndex] = {}

            if not indicatorIndex in self.__allMeasurementsIndex[commodIndex]:
                self.__allMeasurementsIndex[commodIndex][indicatorIndex] = {}
                
            if not locationIndex in self.__allMeasurementsIndex[commodIndex][indicatorIndex]:
                self.__allMeasurementsIndex[commodIndex][indicatorIndex][locationIndex] = {}

            if not unit in self.__allMeasurementsIndex[commodIndex][indicatorIndex][locationIndex]:
                self.__allMeasurementsIndex[commodIndex][indicatorIndex][locationIndex][unit] = [index]
            else:
                self.__allMeasurementsIndex[commodIndex][indicatorIndex][locationIndex][unit].append(index)

            # Store locations
            if not locationIndex in self.__locationMeasurementIndex:
                self.__locationMeasurementIndex[locationIndex] = 0

            percent = index/tot*100
            if (percent > mile_stone):
                #Progress bar update
                left = width*percent/100
                right = width-left
                print("\r[", '*'*int(left), ' '*int(right), "]", round(percent), '%', sep="", end="", flush=True)
                mile_stone += 1
        
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
        #Explore one or all dictionaries depending on the argument value
        selected_dics = self.__exploreDics([self.__allMeasurementsIndex], commodityGroup)
        selected_dics = self.__exploreDics(selected_dics, indicatorGroup)
        selected_dics = self.__exploreDics(selected_dics, geographicalLocation)
        selected_dics = self.__exploreDics(selected_dics, unit)
        return list(map(self.__measurments.get, [i for s in selected_dics for i in s]))
        
    def __exploreDics(self, dics, key):
        h = []
        for d in dics:
            if key is None:
                for v in d.values():
                    h.append(v)
            else:
                v = d.get(key)
                if not v is None:
                    h.append(v)
        return h
    
    def locationExists(self, geographicalLocation: str):
        if (not geographicalLocation is None) and self.__locationMeasurementIndex.get(geographicalLocation) is None:
            return False
        return True
    
    def display_location_names(self):
        print("-------------Stored location names-------------")
        for e in self.__locationMeasurementIndex.keys():
            print(e)
        print("----------------------DONE---------------------")
    
    def display_unit_names(self):
        print("---------------Stored unit names---------------")
        h = []
        for e in self.unitsRegistry.keys():
            h.append((self.unitsRegistry[e].name, e))

        maxLen = 0
        for e in h:
            if len(e[0]) > maxLen:
                maxLen = len(e[0])

        off = (maxLen - len("NAME"))//2
        off2 = maxLen - len("NAME") - off + 2
        print(" " * off, "NAME", " " * off2, "ID")
        for e in h:
            print(e[0], " " * (maxLen - len(e[0]) + 3), e[1])
        print("----------------------DONE---------------------")
    
    def displayMeasurments(self, measurments_list):
        print("--------------Printing ", len(measurments_list), " values--------------")
        for v in measurments_list:
            v.describe()
            print("-------")
        print("----------------------DONE---------------------")