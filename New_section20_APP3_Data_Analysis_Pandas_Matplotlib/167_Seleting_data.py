import pandas

data = pandas.read_csv("./data/reviews.csv")
# print(data)

# Selecting Single Column
print(data['Rating'])
print(type(data['Rating']))
print(data['Rating'].mean())

# Selecting Multiple columns
print(data[['Rating', 'Comment']])
print(type(data[['Rating', 'Comment']]))

# Selecting Single row
print(data.iloc[3])
print(type(data.iloc[3]))

# Selecting Multiple Rows
print(data.iloc[3:5])
print(type(data.iloc[3:5]))

# Selecting a section
print(data.iloc[0:5, 1:3])
print(data[['Rating', 'Comment']].iloc[:4])
print(type(data[['Rating', 'Comment']].iloc[:4]))

# Selecting a cell
print(data.iloc[0:1, 0:1])
print(data['Rating'].iloc[1])
print(type(data['Rating'].iloc[1]))

print(data.at[3, 'Rating'])
