import json

expenses = {"food": 150.0, "transportation": 75.0, "entertainment": 50.0}

with open("expenses.json", "w") as file:
    json.dump(expenses, file)

try:
    with open("expenses.json", "r") as file:
        loaded = json.load(file)
except FileNotFoundError:
    expenses = {}

print(expenses)