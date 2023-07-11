import requests
# Сохраните в словарь названия всех кораблей, их пассажировместимость.
# https://swapi.dev/api/starships/

ships = {}

current_page = 'https://swapi.dev/api/starships'
current_page_results = requests.get(current_page).json()['results']
for i in current_page_results:
    ships[i['model']] = i['passengers']
print(ships)


 
