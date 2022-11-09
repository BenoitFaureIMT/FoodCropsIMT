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
        # test Antoine
        dataset = pd.read_csv(datasetPath)
        index = dataset.head(1)
        dataset.index = index
        size = dataset.shape()

        for index, row in dataset.iterrows():

    def findMeasurement(self, commodityGroup: CommodityGroup= None, indicatorGroup: IndicatorGroup = None, geographicalLocation: str = None, unit: Unit = None) -> List[Measurement]:
        return None







