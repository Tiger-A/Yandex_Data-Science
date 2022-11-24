import pandas
import seaborn

data = pandas.read_csv("polomki.csv", index_col='Магазин')
data['Неделя 14'] = data['Неделя 14'] * 100
seaborn.heatmap(data)