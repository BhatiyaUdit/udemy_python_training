import mysql.connector
from datetime import datetime

print(datetime.now(), " before con")

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

print(datetime.now(), " after con")

cursor = con.cursor()

word = 'rain'

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

print(datetime.now(), " after fetch")
print(results)

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")


# Exercise to combine both app1 and mysql-connector


