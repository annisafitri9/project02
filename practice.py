import requests

api_key = '21860f90-6d81-4406-9809-7e6ae17a33f7'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

print(definitions)

for definition in definitions:
    print(definition)