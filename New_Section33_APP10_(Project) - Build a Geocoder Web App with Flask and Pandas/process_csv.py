import pandas
from geopy.geocoders import ArcGIS


def process_csv_start():
    arcGis = ArcGIS()
    error = None
    df = pandas.read_csv('upload.csv')
    print(df.head())
    if 'address' in df.keys() or 'Address' in df.keys():
        try:
            df['location'] = df['address'].apply(lambda x: arcGis.geocode(x, timeout=1000))
            df['lat'] = df['location'].apply(lambda x: x.latitude)
            df['long'] = df['location'].apply(lambda x: x.longitude)
        except KeyError as e:
            try:
                df['location'] = df['Address'].apply(lambda x: arcGis.geocode(x, timeout=1000))
                df['lat'] = df['location'].apply(lambda x: x.latitude)
                df['long'] = df['location'].apply(lambda x: x.longitude)
            except KeyError as e2:
                print("Address is not present")
    else:
        error = "Address Column is not present"

    print(df.head())
    return df, error
