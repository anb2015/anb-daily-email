# Retrieves sunrise and sunset from sunrise-sunset.org's API
# Data based on lat/long specified in imported email_list

import requests
from emails import email_list

lat_lng = []

for i in range(len(email_list)):
    lat = email_list[i]["lat"]
    lng = email_list[i]["lon"]
    lat_lng.append((lat, lng))

sun_times_list = []

for j in range(len(lat_lng)):
    params = {
        "lat": lat_lng[j][0],
        "lng": lat_lng[j][1],
        "formatted": 0,
        }

    response1 = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response1.raise_for_status()
    data1 = response1.json()

    sunrise_hour = "0" + str(int(data1["results"]["sunrise"].split("T")[1][:2]) - 5)
    sunrise_rest = data1["results"]["sunrise"][2:].split("T")[1][2:5]
    sunset_hour = str(int(data1["results"]["sunset"].split("T")[1][:2]) - 5)
    sunset_rest = data1["results"]["sunset"][2:].split("T")[1][2:5]
    day_length_sec = data1["results"]["day_length"]
    day_length_hr = day_length_sec // 3600
    day_length_min = (day_length_sec % 3600) // 60
    sunrise_local = sunrise_hour + sunrise_rest
    sunset_local = sunset_hour + sunset_rest
    day_length = f"{day_length_hr} hours {day_length_min} minutes"

    sunrise_string = f"This morning's sunrise: {sunrise_local}"
    sunset_string = f"This evening's sunset: {sunset_local}"
    day_length_string = f"Today's light will last {day_length}."

    sun_times_string = f"{sunrise_string}\n{sunset_string}\n{day_length_string}"
    sun_times_list.append(sun_times_string)
