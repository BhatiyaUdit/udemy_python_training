import pandas

data = pandas.read_csv("./data/reviews.csv")
print(data)
print(data.head())
print(data.shape)
print(data.columns)
print(data.hist('Rating'))
# Graph will be automatically visible in jupyter
