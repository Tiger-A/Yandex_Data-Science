# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }

# # Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья" 
# # в зависимости от того, какое число передано в аргументе friends_count
# def format_friends_count(friends_count):
#     if friends_count == 1:
#         return '1 друг'
#     elif 2 <= friends_count <= 4:
#         return f'{friends_count} друга'
#     else:
#         return f'{friends_count} друзей.'
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count = len(DATABASE)
#         # Вызовите функцию format_friends_count() и передайте в неё count.
#         # Отредактируйте строку ниже: в ней должно использоваться выражение, 
#         # которое вернёт функция format_friends_count(
#         return f'У тебя {format_friends_count(count)}'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE)
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'

# def process_query(query):
#     query_part = query.split(", ")
#     if query_part[0] == "Анфиса":
#          return process_anfisa(query_part[1])
#     else:
#         return process_friend(query_part[0], query_part[1])

# def process_friend(name, query):
#     if name in DATABASE:
#         if query == 'ты где?':
#             return f'{name} в городе {DATABASE[name]}'
#         else:
#             return "<неизвестный запрос>"
#     else:
#         return f'У тебя нет друга по имени {name}'
        
        
# print('Привет, я Анфиса!')
# print(process_query('Анфиса, сколько у меня друзей?'))
# print(process_query('Анфиса, кто все мои друзья?'))
# print(process_query('Анфиса, где все мои друзья?'))
# print(process_query('Анфиса, кто виноват?'))
# print(process_query('Соня, ты где?'))
# print(process_query('Коля, что делать?'))
# print(process_query('Антон, ты где?')) 



# import datetime as dt

# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь'
# }

# UTC_OFFSET = {
#     'Санкт-Петербург': 3,
#     'Москва': 3,
#     'Самара': 4,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Пермь': 5,
#     'Воронеж': 3,
#     'Волгоград': 3,
#     'Краснодар': 3,
#     'Калининград': 2
# }

# def what_time(friend):
#     # напишите код тела функции
#     # пусть она вернет время у друга из аргумента friend
#     utc_time = dt.datetime.utcnow()

    
# # Создаём промежуток времени в три часа
#     print(DATABASE[friend])
#     city = DATABASE[friend]
#     period = dt.timedelta(hours = UTC_OFFSET[city])
    
# # И прибавляем к значению времени по UTC поправку в три часа:
#     w_time = utc_time + period
#     return w_time
    
    

# print(what_time('Соня'))



import datetime as dt
import requests

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 4,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text
    else:
        return '<ошибка на сервере погоды>'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count_string = format_count_friends(len(DATABASE))
        return f'У тебя {count_string}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city not in UTC_OFFSET:
                return f'<не могу определить время в городе {city}>'
            time = what_time(city)            
            return f'Там сейчас {time}'
        elif query == 'как погода?':
            return what_weather(city)
        
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


def process_query(query):
    tokens = query.split(', ')
    name = tokens[0]
    if name == 'Анфиса':
        return process_anfisa(tokens[1])
    else:
        return process_friend(name, tokens[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?',
        'Коля, как погода?',
        'Соня, как погода?',
        'Антон, как погода?'
    ]
    for query in queries:
        print(query, '-', process_query(query))


runner()