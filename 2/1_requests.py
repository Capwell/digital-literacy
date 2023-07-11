# У python есть очень много дополнительных библиотек на все случаи жизни
# например, модуль requests для работы запросами
# python -m pip install requests -- устанавливаем
# Импортируем для использования 
import requests

# Отправляем GET-запрос:
response = requests.get(
    'http://info.cern.ch/hypertext/WWW/TheProject.html'
)
print(response.text)
# url = 'http://innopolis.university'
# url = 'http://proninteam.ru'

# print(response.text)
print(dir(response))
# print(response.headers)



