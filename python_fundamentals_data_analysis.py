# import pandas
# import seaborn

# data = pandas.read_csv("polomki.csv", index_col='Магазин')
# data['Неделя 14'] = data['Неделя 14'] * 100
# seaborn.heatmap(data)







# Постройте столбчатую диаграмму, отражающую значения конверсии из списка conversions по неделям (столбец 'week_number').

# import pandas
# data = pandas.read_csv('app_stats.csv')

# payments = list(data['payments'])
# installs = list(data['installs'])

# conversions = []

# for index in range(len(payments)):
#     conversions.append(payments[index] / installs[index])

# # ваш код здесь
# import seaborn
# seaborn.barplot(x=data['week_number'], y=conversions)




# min_required_area = 40 # минимальная требуемая площадь
# max_affordable_price = 190000 # максимально допустимая арендная ставка
# third_ring_radius = 6.7 # максимальное расстояние от центра

# open_hours_number = 18 # количество рабочих часов в сутки
# traffic2visitors_average_ratio = 1 / 225 # средняя доля посетителей от числа прохожих
# traffic2visitors_pessimistic_ratio = 1 / 300 # минимальная доля посетителей от числа прохожих
# visitors2purchases_average_ratio = 0.1 # средняя доля покупателей от числа посетителей
# visitors2purchases_pessimistic_ratio = 0.05 # минимальная доля покупателей от числа посетителей
# average_order_value = 21000 # средняя стоимость покупки
# average_order_value_pessimistic = 20000 # минимальная стоимость покупки
# trade_margin = 0.2 # наценка
# days_in_months = 30 # количество рабочих дней в месяц

# # множитель для расчёта прибыльности в среднем сценарии
# income_multiplier_average = (open_hours_number * 
#                              traffic2visitors_average_ratio *
#                              visitors2purchases_average_ratio *
#                              average_order_value *
#                              trade_margin *
#                              days_in_months)

# # множитель для расчёта прибыльности в пессимистичном сценарии
# income_multiplier_pessimistic = (open_hours_number * 
#                                  traffic2visitors_pessimistic_ratio *
#                                  visitors2purchases_pessimistic_ratio *
#                                  average_order_value_pessimistic *
#                                  trade_margin *
#                                  days_in_months)

# number_of_employees = 2 # количество продавцов
# employee_salary = 50000 # зарплата продавца
# tax_multiplier = 1.43 # множитель для расчёта зарплаты с налогами

# # зарплатная часть расходов
# addition_to_expenses = number_of_employees * employee_salary * tax_multiplier

# # минимальная ожидаемая прибыль
# min_expected_profits = 500000

# import pandas
# realty_df = pandas.read_csv('yandex_realty_data.csv')

# filtered_objects_area = []
# filtered_objects_price = []
# filtered_objects_traffic = []
# filtered_objects_address = []
# filtered_objects_profits = []

# for index in range(len(realty_df)):
#     if (realty_df['floor'][index] == 1 and
#         realty_df['area'][index] >= min_required_area and
#         realty_df['price'][index] <= max_affordable_price and
#         realty_df['commercial_type'][index] in ['FREE_PURPOSE', 'RETAIL'] and
#         realty_df['distance'][index] <= third_ring_radius and
#         realty_df['already_taken'][index] == 0 and
#         realty_df['competitors'][index] <= 1):
#         filtered_objects_area.append(realty_df['area'][index])
#         filtered_objects_price.append(realty_df['price'][index])
#         filtered_objects_traffic.append(realty_df['traffic'][index])
#         filtered_objects_address.append(realty_df['address'][index])
#         filtered_objects_profits.append(realty_df['traffic'][index] * 
#         income_multiplier_average - (realty_df['price'][index] + 
#         addition_to_expenses))

# for index in range(len(filtered_objects_profits)):
#     if filtered_objects_profits[index] > min_expected_profits:
#         print(filtered_objects_price[index])
#         print(filtered_objects_traffic[index])
#         print(filtered_objects_address[index])
#         print(filtered_objects_profits[index])
#         print(filtered_objects_traffic[index] * income_multiplier_pessimistic - 
#         (filtered_objects_price[index] + addition_to_expenses))
#         print('----------')




# import pandas
# import seaborn

# data = pandas.read_csv('support_data.csv')

# segment = list(data['segment'])
# robocats = list(data['robocats'])

# # список сегментов, чтобы цикл мог пройти по ним
# names = ['Segment 0', 'Segment 1', 'Segment 2']

# # список, в который будем складывать средние значения
# means = []

# # внешний цикл по названиям сегментов
# for name in names:
#     # код внутри - почти то же, что было раньше
#     cats = 0
#     counter = 0
#     # внутренний цикл
#     for index in range(len(data)):
#         # в этой строке заменили название сегмента на переменную цикла
#         if segment[index] == name:
#             cats += robocats[index] 
#             counter += 1
#     means.append(cats / counter)


# 



# import requests

# request_headers = {
#     'Accept-Language': 'ru'  # попросим материал на русском языке
# }

# # сходим почитать блоги про IT, строкой передаём URL платформы habr
# response = requests.get('https://habr.com', headers=request_headers)

# print(response.text)




# import requests


# cities = [
#     'Омск',
#     'Калининград',
#     'Челябинск',
#     'Владивосток',
#     'Красноярск',
#     'Москва',
#     'Екатеринбург'
# ]


# def make_url(city):
#     # в URL задаём город, в котором узнаем погоду
    
#     return f'http://wttr.in/{city}'



# def make_parameters():
#     params = {
#         'format': 2,  # погода одной строкой
#         'M': ''  # скорость ветра в "м/с"
#     }
#     return params


# def what_weather(city):
#     # Напишите тело этой функции.
#     # Не изменяйте остальной код!
#     try:
    
#         # response = requests.get(make_url(city), make_parameters())
#         # print(f'{make_url(city)}, {make_parameters()}')
#         response = requests.get(url = make_url(city), params = make_parameters())
#         return response.text
#     except requests.ConnectionError: 
#         print('<ошибка на сервере погоды>')

    
# print('Погода в городах:')
# for city in cities:
#     print(city, what_weather(city))



# import datetime as dt
# import requests

# DATABASE = {
#     'Сергей': 'Омск',
#     'Соня': 'Москва',
#     'Алексей': 'Калининград',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск',
#     'Артём': 'Владивосток',
#     'Петя': 'Михайловка'
# }

# UTC_OFFSET = {
#     'Москва': 3,
#     'Санкт-Петербург': 3,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Самара': 4,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Воронеж': 3,
#     'Пермь': 5,
#     'Волгоград': 4,
#     'Краснодар': 3,
#     'Калининград': 2,
#     'Владивосток': 10
# }


# def format_count_friends(count_friends):
#     if count_friends == 1:
#         return '1 друг'
#     elif 2 <= count_friends <= 4:
#         return f'{count_friends} друга'
#     else:
#         return f'{count_friends} друзей'


# def what_time(city):
#     offset = UTC_OFFSET[city]
#     city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
#     f_time = city_time.strftime("%H:%M")
#     return f_time


# def what_weather(city):
#     url = f'http://wttr.in/{city}'
#     weather_parameters = {
#         'format': 2,
#         'M': ''
#     }
#     try:
#         response = requests.get(url, params=weather_parameters)
#     except requests.ConnectionError:
#         return '<сетевая ошибка>'
#     if response.status_code == 200:
#         return response.text
#     else:
#         return '<ошибка на сервере погоды>'


# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count_string = format_count_friends(len(DATABASE))
#         return f'У тебя {count_string}'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE.keys())
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'


# def process_friend(name, query):
#     if name in DATABASE:
#         city = DATABASE[name]
#         if query == 'ты где?':
#             return f'{name} в городе {city}'
#         elif query == 'который час?':
#             if city not in UTC_OFFSET:
#                 return f'<не могу определить время в городе {city}>'
#             time = what_time(city)            
#             return f'Там сейчас {time}'
#         elif query == 'как погода?':
#             return what_weather(city)
        
#         else:
#             return '<неизвестный запрос>'
#     else:
#         return f'У тебя нет друга по имени {name}'


# def process_query(query):
#     tokens = query.split(', ')
#     name = tokens[0]
#     if name == 'Анфиса':
#         return process_anfisa(tokens[1])
#     else:
#         return process_friend(name, tokens[1])


# def runner():
#     queries = [
#         'Анфиса, сколько у меня друзей?',
#         'Анфиса, кто все мои друзья?',
#         'Анфиса, где все мои друзья?',
#         'Анфиса, кто виноват?',
#         'Коля, ты где?',
#         'Соня, что делать?',
#         'Антон, ты где?',
#         'Алексей, который час?',
#         'Артём, который час?',
#         'Антон, который час?',
#         'Петя, который час?',
#         'Коля, как погода?',
#         'Соня, как погода?',
#         'Антон, как погода?'
#     ]
#     for query in queries:
#         print(query, '-', process_query(query))


# runner()






# movies_table = [
#     ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111],
#     ['Крёстный отец', 'США', 1972, 'драма, криминал', 175, 8.730],
#     ['Тёмный рыцарь', 'США', 2008, 'фантастика, боевик, триллер', 152, 8.499],
#     ['Список Шиндлера', 'США', 1993, 'драма', 195, 8.818],
#     ['Властелин колец: Возвращение Короля', 'Новая Зеландия', 2003, 'фэнтези, приключения, драма', 201, 8.625],
#     ['Криминальное чтиво', 'США', 1994, 'триллер, комедия, криминал', 154, 8.619],
#     ['Хороший, плохой, злой', 'Италия', 1966, 'вестерн', 178, 8.521],
#     ['Бойцовский клуб', 'США', 1999, 'триллер, драма, криминал', 139, 8.644],
#     ['Харакири', 'Япония', 1962, 'драма, боевик, история', 133, 8.106],
#     ['Сталкер', 'СССР', 1979, 'фантастика, драма, детектив', 163, 8.083],
#     ['Иди и смотри', 'СССР', 1985, 'драма, военный', 136, 8.094]
# ]

# # напишите ваш код здесь
# for i in movies_table:
#     i.append('Кинопоиск')
    

# for movie in movies_table:
#     for elem in movie:
#         print(f'{elem:<45}', end='')
#     print()



# # название, страна, год, жанр, продолжительность (мин.), рейтинг Кинопоиска 
# movies_table = [
#     ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111],
#     ['Крёстный отец', 'США', 1972, 'драма, криминал', 175, 8.730],
#     ['Тёмный рыцарь', 'США', 2008, 'фантастика, боевик, триллер', 152, 8.499],
#     ['Список Шиндлера', 'США', 1993, 'драма', 195, 8.818],
#     ['Властелин колец: Возвращение Короля', 'Новая Зеландия', 2003, 'фэнтези, приключения, драма', 201, 8.625],
#     ['Криминальное чтиво', 'США', 1994, 'триллер, комедия, криминал', 154, 8.619],
#     ['Хороший, плохой, злой', 'Италия', 1966, 'вестерн', 178, 8.521],
#     ['Бойцовский клуб', 'США', 1999, 'триллер, драма, криминал', 139, 8.644],
#     ['Харакири', 'Япония', 1962, 'драма, боевик, история', 133, 8.106],
#     ['Сталкер', 'СССР', 1979, 'фантастика, драма, детектив', 163, 8.083],
#     ['Иди и смотри', 'СССР', 1985, 'драма, военный', 136, 8.094]
# ]

# # отсортируем таблицу по возрастанию рейтинга — то есть по пятому элементу подсписков
# movies_table_sorted = sorted(movies_table, key=lambda row: row[5])

# # блок для вывода результата на экран
# for movie in movies_table_sorted: # для каждого списка в списке movies_table_sorted
#     for elem in movie: # перебираем элементы очередного списка
#         print(f'{elem:<45}', end='') # выравнивание каждого элемента по левому краю с фиксированной шириной строки 45
#     print() # переводим на новую строку после вывода информации об очередном фильме







# # Напишите функцию filter_by_genre, которая принимает два аргумента:
# # data: список списков с информацией о фильмах,
# # genre: название жанра, по умолчанию — 'драма'.
# # Функция возвращает данные о фильмах в жанре 'драма'. Если жанров несколько — 'драма' будет среди них.

# # функция печати таблицы, принимает на вход список списков, ничего не возвращает (неявно возвращается None)
# def print_movie_table(data):
#     for movie in data:
#         for elem in movie:
#             print(f'{elem:<45}', end='')
#         print()


# # определите функцию filter_by_genre здесь
# def filter_by_genre(data, genre='драма'):
#     movies_table_filtered = []
#     for i in data:
#         if 'драма' in i[3]:
#             movies_table_filtered.append(i)
          
#     return movies_table_filtered

# movies_table = [
#     ['Побег из Шоушенка', 'США', 1994, 'драма', 142, 9.111],
#     ['Крёстный отец', 'США', 1972, 'драма, криминал', 175, 8.730],
#     ['Тёмный рыцарь', 'США', 2008, 'фантастика, боевик, триллер', 152, 8.499],
#     ['Список Шиндлера', 'США', 1993, 'драма', 195, 8.818],
#     ['Властелин колец: Возвращение Короля', 'Новая Зеландия', 2003, 'фэнтези, приключения, драма', 201, 8.625],
#     ['Криминальное чтиво', 'США', 1994, 'триллер, комедия, криминал', 154, 8.619],
#     ['Хороший, плохой, злой', 'Италия', 1966, 'вестерн', 178, 8.521],
#     ['Бойцовский клуб', 'США', 1999, 'триллер, драма, криминал', 139, 8.644],
#     ['Харакири', 'Япония', 1962, 'драма, боевик, история', 133, 8.106],
#     ['Сталкер', 'СССР', 1979, 'фантастика, драма, детектив', 163, 8.083],
#     ['Иди и смотри', 'СССР', 1985, 'драма, военный', 136, 8.094]
# ]

# movies_table_filtered = filter_by_genre(movies_table)
# print_movie_table(movies_table_filtered)



# import pandas as pd

# df = pd.read_csv('music_log.csv')
# genre_fight = df[['genre', 'Artist']]
# genre_pop = df.loc[df.loc[:,'genre'] == 'pop']['genre'].count()
# print(f'Число прослушанных треков в жанре поп равно {genre_pop}')
# genre_rock = df.loc[df.loc[:,'genre'] == 'rock']['genre'].count()
# print(f'Число прослушанных треков в жанре рок равно {genre_rock}')
# if genre_pop > genre_rock:
#     print('Поп-музыку слушают больше.')
# elif genre_pop < genre_rock:
#     print('Рок слушают больше.')
# else:
#     print('Поп и рок слушают одинаково часто.')


# import pandas as pd
# df = pd.read_csv('music_log_upd_col.csv')
# df['track_name'] = df['track_name'].fillna('unknown')
# df['artist_name'] = df['artist_name'].fillna('unknown')
# df = df.dropna(subset=['genre_name'])
# df.info()



# # импортируйте библиотеку pandas
# import pandas

# # считайте csv-файл 'music_log.csv' в переменную df
# df = pandas.read_csv('music_log.csv')

# # переименуйте названия столбцов df
# df = df.rename(columns={'  user_id': 'user_id', 'total play': 'total_play', 'Artist': 'artist'})

# # объявите список columns_to_replace с названиями столбцов track, artist, genre
# columns_to_replace = ['track', 'artist', 'genre']                        
                       
# # заполните отсутствующие значения столбцов из списка columns_to_replace значением 'unknown' в цикле
# for column in columns_to_replace:
#     df[column] = df[column].fillna('unknown')
     
# # удалите строки-дубликаты из датафрейма df
# df = df.drop_duplicates().reset_index(drop=True) 

# # выведите на экран первые 20 строчек обновлённого набора данных df
# print(df.head(20)) 



# import pandas as pd
# df = pd.read_csv('music_log_upd.csv')

# genre_grouping = df.groupby('user_id')['genre_name']

# def user_genres(group):
#     for col in group:
#         if len(col[1]) > 50:
#             user = col[0]
#             return user

# search_id = user_genres(genre_grouping)

# music_user = df[df['user_id'] == search_id]
# music_user = music_user[music_user['total_play_seconds'] !=0]

# # print(music_user)

# sum_music_user = music_user.groupby('genre_name')['total_play_seconds'].sum()
# # print(sum_music_user)
# count_music_user = music_user.groupby('genre_name')['genre_name'].count()
# # print(count_music_user)
# final_sum = sum_music_user.sort_values(ascending=False)
# # print(final_sum)
# final_count = count_music_user.sort_values(ascending=False)
# print(final_count)




# Начало исследования
# Обзор данных
# Исходные данные хранятся в файле .csv. Чтобы исследовать их средствами pandas, эту библиотеку нужно импортировать:
# import pandas as pd 
# Тогда станет доступен метод для чтения csv-файлов — read_csv(). Прочитаем файл по адресу из аргумента, преобразуем его в таблицу и сохраним в переменную df:
# df = pd.read_csv('music_log.csv') 
# Теперь с данными можно работать. Посмотрим первые 15 строчек таблицы:
# print(df.head(15)) # выведет первые 15 строк таблицы 
# Нужно убедиться в том, что данные прошли предобработку. В них не должно быть пропусков и дубликатов.  
# Пропущенные значения выявляет метод isna(), а подсчитывает — метод sum():
# # подсчёт пропусков в данных
# print(df.isna().sum()) 
# Дубликаты, повторяющиеся строки, выявляют методом duplicated() и подсчитывают тем же sum():
# # подсчёт дубликатов
# print(df.duplicated().sum()) 
# Если обе проверки не выявили проблемы в данных, значит, они готовы для анализа.



# import pandas as pd
# df = pd.read_csv('music_log_upd.csv')

# pop_music = df[df['genre_name'] == "pop"]

# pop_music = (pop_music[pop_music['total_play_seconds'] != 0])

# pop_music_max_total_play =  pop_music['total_play_seconds'].max()
 
# # print(pop_music_max_total_play)

# pop_music_max_info = (pop_music[pop_music['total_play_seconds'] == pop_music['total_play_seconds'].max()]) 
# #print(pop_music_max_info)

# pop_music_min_total_play = pop_music['total_play_seconds'].min()
# #print(pop_music_min_total_play)

# pop_music_min_info = (pop_music[pop_music['total_play_seconds'] == pop_music['total_play_seconds'].min()]) 
# #print(pop_music_min_info)

# pop_music_median = pop_music['total_play_seconds'].median()
# #print(pop_music_median)

# pop_music_mean = pop_music['total_play_seconds'].mean()
# print(pop_music_mean)


# import pandas as pd

# logs = pd.read_csv('/datasets/logs.csv')

# visits = logs.groupby('source')['user_id'].count() # количество визитов
# purchase = logs.groupby('source')['purchase'].sum() # количество покупок

# conversion = purchase / visits # поделите количество покупок на количество визитов
# print(conversion)