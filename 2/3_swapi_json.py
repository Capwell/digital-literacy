import requests

response = requests.get('https://swapi.dev/api/starships/9/')

print(response.json())  
# Напечатаем и тип данных объекта, полученного в результате преобразования:
print(type(response.json())) 