# Retrieves formatted joke from https://sv443.net/jokeapi/v2/
import requests

JOKEAPI_URL = "https://v2.jokeapi.dev/joke/Miscellaneous,Pun?blacklistFlags=nsfw,racist,sexist," \
              "explicit&format=txt&type=single?idRange=1-1368"

response = requests.get(url=JOKEAPI_URL)
joke_text = f"Joke of the Day:\n\n{response.text}"
