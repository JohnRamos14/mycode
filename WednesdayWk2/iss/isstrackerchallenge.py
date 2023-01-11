#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
from datetime import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    # to get long and lat position of the ISS
    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]

    # # to get time stamp on when the response was generated
    time_stamp = resp["timestamp"]
    time_stamp = datetime.fromtimestamp(time_stamp)

    coords_tuple = (lon, lat)
    
    result = rg.search(coords_tuple, verbose=False)
    city = result[0]["name"]
    country = result[0]["cc"]

    print(result)

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timestamp: {time_stamp}
    Lon: {lon}
    Lat: {lat}
    City/Country: {city}, {country}
    """)

if __name__ == "__main__":
    main()

