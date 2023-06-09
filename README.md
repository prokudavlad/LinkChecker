# Опис скрипту для тестування посилань

Цей скрипт призначений для тестування списку посилань, вказаних у файлі [JSON](https://uk.wikipedia.org/wiki/JSON)

## Встановлення та залежності

Для роботи скрипта потрібний встановлений інтерпретатор [Python](https://www.python.org/) версії 3 та встановлені бібліотеки [json](https://uk.wikipedia.org/wiki/JSON) та [requests](https://pypi.org/project/requests/). Інсталяцію бібліотек можна виконати за допомогою менеджера пакетів [pip](https://ru.wikipedia.org/wiki/Pip_(%D0%BC%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80_%D0%BF%D0%B0%D0%BA%D0%B5%D1%82%D0%BE%D0%B2)):

> pip install json
> pip install requests

### Використання скрипту

* Створіть файл links.json і додайте список посилань, які ви хочете протестувати. Формат файлу має бути наступним:
>[
  {
    "url": "https://www.ukr.net/news/main.html"
  },
  {
    "url": "https://www.example.com/invalid_page"
  },
  {
    "url": "https://rabota.ua/ua/employer"
  },
  {
    "url": "https://rozetka.com.ua/ua/computers-notebooks/c80253/"
  }
]

* Збережіть файл links.json у тій же папці, що містить скрипт.

* У скрипті link_checker.py замініть рядок 'links.json' на шлях до файлу links.json, якщо вони знаходяться в різних папках.

* Запустіть сценарій link_checker.py. Він виконає запити до кожного посилання та виведе відповідні повідомлення про помилки чи успіх.

#### Приклад роботи скрипту

* Припустимо, файл links.json містить наступні посилання:

> [
  {
    "url": "https://www.ukr.net/news/main.html"
  },
  {
    "url": "https://www.example.com/invalid_page"
  },
  {
    "url": "https://rabota.ua/ua/employer"
  },
  {
    "url": "https://rozetka.com.ua/ua/computers-notebooks/c80253/"
  }
]

* Під час запуску скрипта ви отримаєте наступний висновок:

> Success: https://rabota.ua/ua/employer
>> Success: https://rozetka.com.ua/ua/computers-notebooks/c80253/

* Це означає, що запити до кожного посилання успішно виконані без помилок.
> Обробка помилок

* Якщо під час виконання запиту на посилання виникає помилка, наприклад, пов'язана зі з'єднанням або кодом відповіді від сервера, скрипт виведе відповідне повідомлення
> Error 403: 403 Forbidden - https://www.ukr.net/news/main.html
>> Error 404: 404 Not Found - https://www.example.com/invalid_page
