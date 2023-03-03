# Retrieves 5 trivia questions and formats them using Open Trivia Database

import requests
from random import choice, shuffle
import html

category = choice([25, 13, 13, 10, 21])
difficulties = choice(["easy", "medium", "medium", "medium", "hard"])

parameters = {
    "amount": 5,
    "type": "multiple",
    "difficulty": difficulties,
    "category": category
    }

response2 = requests.get("https://opentdb.com/api.php", params=parameters)
response2.raise_for_status()
data2 = response2.json()

question_data = data2["results"]

trivia_questions = f"Trivia Questions ({question_data[0]['category']}):\n\n"
count = 1
for i in question_data:
    trivia_questions += html.unescape(f"{count}. {i['question']}\n")
    answer_list = [i["correct_answer"]]
    components = i["incorrect_answers"]
    for j in components:
        answer_list.append(j)
    answer_list = [html.unescape(i) for i in answer_list]
    shuffle(answer_list)
    trivia_questions += "..........".join(answer_list)
    trivia_questions += "\n\n"
    count += 1
trivia_questions = trivia_questions[:-2]
trivia_questions = trivia_questions.encode('utf-8').decode('ascii', 'ignore')


trivia_answers = ":srewsnA aivirT"
count_a = 1
for i in question_data:
    trivia_answers += f"\n{html.unescape(i['correct_answer'][::-1])} .{count_a}"
    count_a += 1
trivia_answers = trivia_answers.encode('utf-8').decode('ascii', 'ignore')
