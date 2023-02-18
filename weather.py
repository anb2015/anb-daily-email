# Imports lat/long from email subscribers list and retrieves relevant weather data

from emails import email_list
import requests
import os

weather_list = []

for i in range(len(email_list)):
    lat = email_list[i]["lat"]
    lon = email_list[i]["lon"]
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
    next_12_data = [hourly[i] for i in range(12)]
    next_12_temp = [
        f'{str(round(i.get("temp")))} F -- {i.get("weather")[0]["main"].capitalize()} ('
        f'{i.get("weather")[0]["description"]}) -- {round(i.get("wind_speed"))} mph winds'
        for i in next_12_data]
    next_12_formatted = "\n".join(next_12_temp)

    daily = data.get("daily")
    next_7_data = [daily[i] for i in range(7)]
    next_7_list = [i.get("temp") for i in next_7_data]
    next_7_highs = [round(i.get("max")) for i in next_7_list]
    next_7_lows = [round(i.get("min")) for i in next_7_list]
    next_7_weather = [i.get("weather") for i in next_7_data]
    next_7_main = [next_7_weather[i][0].get("main") for i in range(7)]
    next_7_descr = [next_7_weather[i][0].get("description") for i in range(7)]
    next_7_wind = [round(i.get("wind_speed")) for i in next_7_data]
    next_7_string = ""
    for i in range(7):
        next_7_string += f"high {next_7_highs[i]}, "
        next_7_string += f"low {next_7_lows[i]} -- "
        next_7_string += f"{next_7_main[i].capitalize()} ({next_7_descr[i]}) -- "
        next_7_string += f"{next_7_wind[i]} mph winds\n"
    next_7_string = f"Forecast the next 7 days:\n{next_7_string}"
    next_7_string = next_7_string[:-1]

    weather = f"The current temperature for your location is {round(current_temp)} F.\n" \
              f"It feels like {round(feels_like)} F.\n" \
              f"The humidity is {humidity}%.\n" \
              f"The wind speed is {round(wind_speed)} mph.\n" \
              f"{main.capitalize()} ({description}) expected.\n\n" \
              f"Forecast the next 12 hours:\n{next_12_formatted}\n\n" \
              f"{next_7_string}"

    weather_list.append(weather)
