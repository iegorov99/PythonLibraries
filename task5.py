import pandas as pd

data = pd.DataFrame(pd.read_csv('Customers.csv', delimiter=';'))

# Проверьте данные на наличие пропусков, а также если есть пропуски, замените или удалите их 

clean_data = data.dropna()

# print(clean_data)

# Сгруппируйте данные по столбцу ‘Profession’ и найдите средний годовой доход в каждой группе

group_data = data.groupby('Profession')['Income'].mean()

print(group_data)