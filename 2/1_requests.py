# У python есть очень много дополнительных библиотек на все случаи жизни
# например, модуль requests для работы запросами
# python -m pip install requests -- устанавливаем
# Импортируем для использования 
import requests

# Отправляем GET-запрос:
url = 'http://info.cern.ch/hypertext/WWW/TheProject.html'

response = requests.get(url)
print(response.text)
# url = 'https://stc.innopolis.university/digital_teacher'
# url = 'http://proninteam.ru'

# print(response.text)
print(dir(response))
# print(response.headers)



