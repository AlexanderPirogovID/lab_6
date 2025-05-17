import pandas as pd

data = pd.read_csv('students.csv')

print("проверка на наличие пропусков:")
print(data.isnull().sum())

mean_score = data['Score'].mean()
data['Score'].fillna(mean_score, inplace=True)

print("\nпосле заполнения пропусков в столбце Score:")
print(data)

data.dropna(subset=['Group'], inplace=True)

print("\nпосле удаления строк с пропусками в столбце Group:")
print(data)
