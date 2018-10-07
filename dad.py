import requests
from random import choice

topic = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"

response = requests.get(url, params={"term": topic}, headers={"Accept": "Application/json"})
data = response.json()

total = data["total_jokes"]
jokes = [result["joke"] for result in data["results"]]

if total == 0:
    print("Sorry, I don't have jokes about {}! Please try again.".format(topic))
elif total == 1:
    print("I've got one joke about {}. Here it is: {}".format(topic, jokes[0]))
else:
    print("I've got {} jokes about {}. Here's one: {}".format(total, topic, choice(jokes)))