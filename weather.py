# Imports lat/long from email subscribers list and retrieves relevant weather data

from emails import email_list
import requests
import os
from datetime import datetime

weather_list = []

for num in range(len(email_list)):
    place = email_list[num]["place"]
    lat = email_list[num]["lat"]
    lon = email_list[num]["lon"]
    owm_acct = os.environ.get("OWM_ACCT_NUM")

    parameters = {
        "lat": lat,
        "lon": lon,
        "appid": owm_acct,
        "units": "imperial",
        }

    response = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=parameters)
    response.raise_for_status()
    data = response.json()

    current = data["current"]
    current_temp = current["temp"]
    feels_like = current["feels_like"]
    humidity = current["humidity"]
    wind_speed = current["wind_speed"]
    main = current["weather"][0]["main"]
    description = current["weather"][0]["description"]

    hourly = data.get("hourly")

    # today's high and low:
    next_24_data = [hourly[i] for i in range(24)]
    next_24_temp_list = []
    for i in next_24_data:
        next_24_temp_list.append(round(i["temp"]))
    today_high = max(next_24_temp_list)
    today_low = min(next_24_temp_list)

    # next 12 hours:
    next_12_data = [hourly[i] for i in range(12)]
    next_12_time_object = [datetime.fromtimestamp(i["dt"]) for i in next_12_data]
    next_12_time_hour = [i.strftime("%H") for i in next_12_time_object]
    next_12_temp = []
    for i in range(12):
        next_12_temp_element = ""
        next_12_temp_element += f"{next_12_time_hour[i]}:00 -- "
        next_12_temp_element += f"{round(next_12_data[i].get('temp'))} F -- "
        next_12_temp_element += f"{next_12_data[i].get('weather')[0]['main'].capitalize()} "
        next_12_temp_element += f"({next_12_data[i].get('weather')[0]['description']}) -- "
        next_12_temp_element += f"{round(next_12_data[i].get('wind_speed'))} mph winds"
        next_12_temp.append(next_12_temp_element)
    next_12_formatted = "\n".join(next_12_temp)

    # next 7 days:
    daily = data.get("daily")
    next_7_data = [daily[i] for i in range(8)]
    next_7_day_object = [datetime.fromtimestamp(i["dt"]) for i in next_7_data][1:]
    next_7_day_name = ["Today"]
    next_7_day_name.extend([i.strftime("%A") for i in next_7_day_object])
    next_7_list = [i.get("temp") for i in next_7_data]
    next_7_highs = [round(i.get("max")) for i in next_7_list][:-1]
    next_7_lows = [round(i.get("min")) for i in next_7_list][1:]
    next_7_weather = [i.get("weather") for i in next_7_data][:-1]
    next_7_main = [next_7_weather[i][0].get("main") for i in range(7)]
    next_7_descr = [next_7_weather[i][0].get("description") for i in range(7)]
    next_7_wind = [round(i.get("wind_speed")) for i in next_7_data][:-1]
    next_7_string = ""
    for i in range(7):
        next_7_string += f"{next_7_day_name[i]}: "
        next_7_string += f"Daytime high {next_7_highs[i]} F "
        next_7_string += f"with {next_7_main[i].capitalize()} ({next_7_descr[i]}) "
        next_7_string += f"and {next_7_wind[i]} mph winds "
        next_7_string += f"followed by overnight low {next_7_lows[i]} F.\n"
    next_7_string = f"Forecast the next 7 days:\n{next_7_string}"
    next_7_string = next_7_string[:-1]

    weather = f"The current temperature for {place} is {round(current_temp)} F.\n" \
              f"It feels like {round(feels_like)} F.\n" \
              f"Today's high temperature: {today_high} F.\n" \
              f"Tonight's low temperature: {next_7_lows[0]} F.\n" \
              f"The humidity is {humidity}%.\n" \
              f"The wind speed is {round(wind_speed)} mph.\n" \
              f"{main.capitalize()} ({description}) expected.\n\n" \
              f"Forecast the next 12 hours:\n{next_12_formatted}\n\n" \
              f"{next_7_string}"

    weather_list.append(weather)
