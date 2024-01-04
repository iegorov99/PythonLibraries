import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv('Housing.csv')

# Часть 1 (8 баллов, по 2 на каждый вопрос).
# Вам нужно будет ответить на следующие вопросы:
# Найдите количество спален(bedrooms) в самом дешёвом доме. Если таких несколько, укажите наименьшее значение.

CountBedroomsMin = data[data['price'] == data['price'].min()]['bedrooms'].min()
print(f'Количество спален в самом дешёвом доме = {CountBedroomsMin}')

# Найдите количество домов, в которых количество спален не больше количества ванных(bathrooms).

CountHouses = data[data['bedrooms'] <= data['bathrooms']].shape[0]
print(f"Количество домов, в которых количество спален не больше количества ванных = {CountHouses}")

# Сколько стоит самый дешёвый дом с гостевой комнатой(guestroom)?

CheapestHouse = data[data['guestroom'] == 'yes']['price'].min()
print(f'Самый дешёвый дом с гостевой комнатой стоит {CheapestHouse}')

# Рассмотрим дома ценой от 5.000.000 или до 2.000.000 денег. Какая часть из них может похвастаться кондиционированием воздуха(airconditioning)?

houses = data[(data['price'] >= 2000000) & (data['price'] <= 5000000)]
airconditioningYES = houses[houses['airconditioning'] == 'yes']
result = len(airconditioningYES)/len(houses)
print(f'количество домов ценой от 5.000.000 или до 2.000.000 = {len(houses)},\nколичество домов с кондиционером = {len(airconditioningYES)},'
      f'\nпроцентное соотношение домов с кондиционерами = {round(result, 2)}')

# Часть 2 (10 баллов).
# Постройте график, на котором будут отмечены все квартиры в виде точек, у которых x координата это цена(price), а y - площадь(area). 
# Отметьте разными цветами точки, которые соответствуют квартирам с разным количеством парковочных мест(parking). Не забывайте о прозрачности.

# data['parking'].unique()
# colors = {0:'green', 1:'orange', 2:'red', 3:'purple'}
# data.plot(kind='scatter', x='price', y='area', c=data['parking'].map(colors), alpha=0.5)
# plt.show()

# Часть 3 (20 баллов).
# Постройте на одном поле 4 поля с графиками, на каждом из которых будут отмечены точки-квартиры, где x - цена, а y - площадь. 
# На первом графике разными цветами отметьте наличие/отсутствие гостевой комнаты(guestroom), 
# на втором - подвала(basement), на третьем - обогрева с помощью горячей воды(hotwaterheating) и на четвёртом - предбанника(prefarea). 
# На графиках обязательно должны быть подписи осей, подпись графика(title), сетка, подписи с информацией о том, что обозначает каждый график. 
# Дополнительная кастомизация крайне приветствуется.

fig, ax = plt.subplots(2, 2, figsize=(20, 20))

sb.scatterplot(data=data, x=data['price'], y=data['area'], hue=data['guestroom'], palette='bright', alpha=0.5, ax=ax[0, 0]).set_title('Наличие гостевой комнаты')
sb.scatterplot(data=data, x=data['price'], y=data['area'], hue=data['basement'], palette='bright', alpha=0.5, ax=ax[0, 1]).set_title('Наличие подвала')
sb.scatterplot(data=data, x=data['price'], y=data['area'], hue=data['hotwaterheating'], palette='bright', alpha=0.5, ax=ax[1, 0]).set_title('Наличие обогрева с помощью горячей воды')
sb.scatterplot(data=data, x=data['price'], y=data['area'], hue=data['prefarea'], palette='bright', alpha=0.5, ax=ax[1, 1]).set_title('Наличие предбанника')
plt.show()

# Часть 4 (12 баллов).
# Постройте 2 гистограммы распределения цены на одном графике. 
# Одна должна соответствовать домам с наличием кондиционирования(airconditioning), а другой с отсутствием. 
# Одна гистограмма может частично закрывать другую и данных может быть невидно. Решите эту проблему. 
# График гистограмм должен быть оформлен не хуже предыдущих графиков.

sb.histplot(data=data, x='price', hue='airconditioning', palette='bright', multiple='dodge', alpha=0.4).set_title('Кондиционирование')
plt.show()
