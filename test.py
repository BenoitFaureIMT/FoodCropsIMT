import pandas as pd
dataset = pd.read_csv('FeedGrains.csv')

print(dataset.SC_Group_ID[707])

for index, row in dataset.iterrows():
    print(index)
