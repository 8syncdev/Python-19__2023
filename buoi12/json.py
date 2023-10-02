import json


with open('buoi12/FILE/INPUT.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data)