def celsius_to_kelvin(cels):
    return cels + 273.15


monday_temperatures = [9.1, 8.8, -270.15]

for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))