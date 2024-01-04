# Найдите людей, у которых возраст больше 30 и доход меньше 30000, найдите людей, которые по профессии юристы и с опытом работы больше 5 лет
import os
import pandas as pd

data = pd.DataFrame(pd.read_csv('Customers.csv', delimiter=';'))
filter_data_1 = data[(data['Age'] > 30) & (data['Income'] < 30000)]
print(filter_data_1)
input('Нажмите чтобы продолжить...')
os.system('cls')
filter_data_2 = data[(data['Profession'] == 'Lawyer') & (data['Work Experience'] > 5)]
print(filter_data_2)