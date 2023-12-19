import pandas as pd

dataframe = pd.DataFrame([[1, "Ivan", 5.0], [2, "Sergey", 4.3],
                          [3, "Dmitry", 4.5], [4, "Ilya", 4.9], 
                          [5, "Nikita", 3.3], [6, "Anton", 2.2], 
                          [7, "Vladimir", 4.4]], columns=["#", "Name", "Score"], index=["a", "b", "c", "d", "e", "f", "g"])

print(dataframe[:3])
print(dataframe[-3:])

dataframe.to_csv('myDataFrame')
