from foodCropFactory import FoodCropFactory

import pandas as pd
from foodCropFactory import FoodCropFactory


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






