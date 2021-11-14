import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("./data/reviews.csv", parse_dates=['Timestamp'])
print(df.head())

rate_by_course = df.groupby("Course Name").count()
print(rate_by_course)

rating_count_series = rate_by_course['Rating']

plt.pie(rating_count_series, labels=rating_count_series.index)
plt.show()


plt.bar(rating_count_series.index, rating_count_series)
plt.show()