import pandas
import os
df1 = pandas.DataFrame([[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]])
print(df1)

print()
df1 = pandas.DataFrame([[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]], columns=["A", "B", "C", "D"])
print(df1)

print()
df1 = pandas.DataFrame([[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400]], columns=["A", "B", "C", "D"],
                       index=["ROW1", "ROW2", "ROW3"])
print(df1)

print()
print()
print("Mean df1\n", df1.mean())
print()
print("Mean of all values ", df1.mean().mean())
print()

df2 = pandas.DataFrame([{"name": "udit"}, {"name": "Eren"}, {"last": "bhatiya"}])
print(df2)
print()

env = os.environ["environment"]
print(env)