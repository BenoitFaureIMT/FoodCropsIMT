# FoodCropsIMT

## Introduction

Vous trouverez dans ce repository notre programme permettant de trier facilement les données fournies dans le dataset Food Crops.

## Installation
Le module pandas est nécessaire

## Execution
Pour l'éxécuter, il suffit de lancer la commande suivante :
```
python main.py --args

optional arguments:
  --dataset_path      path to dataset             Default : "FeedGrains.csv"
  --commodity_string  commodity group name        Default : None
  --indicator_string  indicator group name        Default : None
  --location_string   location name               Default : None
  --list_locations    print valid location names  Default : False
  --unit_id           unit id                     Default : None
  --list_units        print valid unit ids        Default : False
```
Si vous n'indiquez pas un paramètre, la dataset ne sera pas trié selon ce paramètre.
Les arguments list_locations et list_units permettent de voir les nom des differentes location et identifiants des unités
