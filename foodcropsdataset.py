from foodCropFactory import FoodCropFactory

import pandas as pd

class FoodCropsDataset(FoodCropFactory):
    def __init__(self):
        super().__init__()
    
    def load(self, datasetPath:str):
        return pd.read_csv(datasetPath)
    