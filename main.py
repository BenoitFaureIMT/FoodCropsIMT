import argparse
from commodity import CommodityGroup
from indicator import IndicatorGroup

from foodcropsdataset import FoodCropsDataset

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", type = str, default = "FeedGrains.csv", help = "path to dataset")
    parser.add_argument("--commodity_string", type = str, default = None, help = "commodity group name")
    parser.add_argument("--indicator_string", type = str, default = None, help = "indicator group name")
    parser.add_argument("--location_string", type = str, default = None, help = "location name")
    parser.add_argument("--unit_name", type = str, default = None, help = "unit name")
    opt = parser.parse_args()
    return opt

def main(dataset_path = 'FeedGrains.csv', commodity_string = None, indicator_string = None, location_string = None, unit_name = None):
    f = FoodCropsDataset()
    f.load(dataset_path)
    
    cGroup = None if commodity_string is None else CommodityGroup[commodity_string]
    iGroup = None if indicator_string is None else IndicatorGroup[indicator_string]
    unitV = None if unit_name is None else f.unitsRegistry[unit_name]
    d = f.findMeasurement(commodityGroup = cGroup, indicatorGroup = iGroup, geographicalLocation = location_string, unit = unitV)
    f.displayMeasurments(d)


if __name__ == "__main__":
    opt = parse_opt()
    main(**vars(opt))