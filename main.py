# This script imports API data from several modules and formats them into a
#  daily email with the weather, trivia and a joke.
# This script runs on PythonAnywhere

import os
import smtplib
from emails import email_list
from sun_times import sun_times_list
from weather import weather_list
from trivia import trivia_questions, trivia_answers
from joke import joke_text

my_email = "********"
my_password = os.environ.get("GMAIL_PASSWORD")
divider = "\n\n*      *      *      *      *      *      *      *      *      *      *      *      *\n\n"
space = "\n\n\n\n\n\n"

for i in range(len(email_list)):
    # build each email recipients customized text
    address = email_list[i]["addresses"]

    email_text = "To: " + ", ".join(address) + "\n"
    email_text += f"Subject:Sunrise/Sunset Times for {email_list[i]['place']} (UTC-5)\n\n"
    email_text += f"{sun_times_list[i]}\n\n"
    email_text += f"{weather_list[i]}"
    email_text += divider
    email_text += trivia_questions
    email_text += divider
    email_text += joke_text
    email_text += divider
    email_text += trivia_answers
    email_text += space
    email_text += "This is an automated message from anb-daily.\n"
    email_text += "Astronomical data provided by https://sunrise-sunset.org (API).\n"
    email_text += "Weather forecast data provided by https://openweathermap.org (API).\n"
    email_text += "Trivia questions provided by https://opentdb.com (API).\n"
    email_text += "Joke of the Day provided by https://v2.jokeapi.dev/.\n"
    email_text += "Automated email service provided by https://www.pythonanywhere.com/."

    # alternate text in case unusual characters produce an error
    email_simple = "To: " + ", ".join(address) + "\n"
    email_simple += f"Subject:Sunrise/Sunset Times for {email_list[i]['place']} (UTC-5)\n\n"
    email_simple += f"{sun_times_list[i]}\n\n"
    email_simple += f"{weather_list[i]}"
    email_simple += divider
    email_simple += joke_text
    email_simple += space
    email_simple += "This is an automated message from anb-daily.\n"
    email_simple += "Astronomical data provided by https://sunrise-sunset.org (API).\n"
    email_simple += "Weather forecast data provided by https://openweathermap.org (API).\n"
    email_simple += "Joke of the Day provided by https://v2.jokeapi.dev/.\n"
    email_simple += "Automated email service provided by https://www.pythonanywhere.com/."

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=address,
                msg=email_text
                )
    except UnicodeEncodeError:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=address,
                msg=email_text
                )