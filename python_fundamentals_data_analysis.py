import pandas
import seaborn

data = pandas.read_csv("polomki.csv", index_col='Магазин')
data['Неделя 14'] = data['Неделя 14'] * 100
seaborn.heatmap(data)







Постройте столбчатую диаграмму, отражающую значения конверсии из списка conversions по неделям (столбец 'week_number').

import pandas
data = pandas.read_csv('app_stats.csv')

payments = list(data['payments'])
installs = list(data['installs'])

conversions = []

for index in range(len(payments)):
    conversions.append(payments[index] / installs[index])

# ваш код здесь
import seaborn
seaborn.barplot(x=data['week_number'], y=conversions)