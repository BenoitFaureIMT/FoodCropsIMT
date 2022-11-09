import pandas as pd
dataset = pd.read_csv('FeedGrains.csv')
tot = dataset.shape[0]
width = 50
for index, __ in dataset.iterrows():
    percent = 100.0*index/tot
    left = width*percent/100
    right = width-left
    print("\r[", '*'*int(left), ' '*int(right), "]", round(percent), '%', sep="", end="", flush=True)