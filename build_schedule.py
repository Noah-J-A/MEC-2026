import json

with open("schedule.json", "r") as file:
    data = json.load(file)

schedule = data["daily schedule"]

