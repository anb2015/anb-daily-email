# grabs a joke and gets exported to main.py for email

import requests

url = 'https://icanhazdadjoke.com'
headers = {
    'Accept': 'text/plain',
    'User-Agent': 'MyApp (anb-daily-email) Contact me at anb2015@gmail.com'
}
response = requests.get(
    url,
    params={"type": "general"},
    headers={
        'Accept': 'text/plain',
        'User-Agent': 'anb-daily-email anb2015@gmail.com'
    }
)

today_joke = response.text.encode("utf-8").decode("ascii", "ignore")
today_joke = f"Joke of the Day:\n\n{today_joke}"
