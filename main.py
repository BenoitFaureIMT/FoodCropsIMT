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
    parser.add_argument("--list_locations", action='store_true', help = "print valid location names")
    parser.add_argument("--unit_id", type = int, default = None, help = "unit id")
    parser.add_argument("--list_units", action='store_true', help = "print valid unit ids")
    opt = parser.parse_args()
    return opt

def main(dataset_path = 'FeedGrains.csv', commodity_string = None, indicator_string = None, location_string = None, list_locations = False, unit_id = None, list_units = False):
    f = FoodCropsDataset()
    f.load(dataset_path)

    if list_locations:
        f.display_location_names()
    
    if list_units:
        f.display_unit_names()

    if list_locations or list_units:
        return
    
    try:
        cGroup = None if commodity_string is None else CommodityGroup[commodity_string.upper()]
    except:
        print("Commodity Group name was not found, valid Commodity Group names are:")
        for e in CommodityGroup:
            print(e.name)
        return
    
    try:
        iGroup = None if indicator_string is None else IndicatorGroup[indicator_string.upper()]
    except:
        print("Indicator Group name was not found, valid Indicator Group names are:")
        for e in IndicatorGroup:
            print(e.name)
        return

    try:
        unitV = None if unit_id is None else  f.unitsRegistry[unit_id]
    except:
        print("Unit ID was not found, to get a list of valid unit ids add argument --list_units")
        return
    
    if(not f.locationExists(location_string)):
        print("No measurments correspond to the location, to get a list of valid locations add argument --list_locations")

    m = f.findMeasurement(commodityGroup = cGroup, indicatorGroup = iGroup, geographicalLocation = location_string, unit = unitV)
    f.displayMeasurments(m)


if __name__ == "__main__":
    opt = parse_opt()
    main(**vars(opt))