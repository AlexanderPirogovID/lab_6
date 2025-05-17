import pandas as pd

data = pd.read_csv('students.csv')

grouped_data = data.groupby('Group').agg(
    Average_Score=('Score', 'mean'),
    Median_Age=('Age', 'median')
).reset_index()

print("сгруппированные данные по группам:")
print(grouped_data)

data['Passed'] = (data['Score'] >= 60).astype(int)

print("\nобновленный DataFrame с добавленным столбцом Passed:")
print(data)
