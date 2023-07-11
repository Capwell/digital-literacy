import requests

response = requests.get('https://swapi.dev/api/starships/9/')
# Напечатаем в терминале содержимое ответа сервера...
print(response.text)
# ...и его тип
print(type(response.text))


