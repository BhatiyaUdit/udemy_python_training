import json
from datetime import datetime
print(datetime.now())
data = json.load(open("../data/data.json"))

print(type(data))

print(data['rain'])
print(datetime.now())