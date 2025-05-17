import pandas as pd

data = pd.read_csv('students.csv')

print("первые 5 строк:")
print(data.head())

print("\nинформация о данных:")
print(data.info())

print("\nстатистика:")
print(data.describe())

average_score = data['Score'].mean()
print(f"\nсредний балл студентов: {average_score}")

students_per_group = data['Group'].value_counts()
print("\nколичество студентов в каждой группе:")
print(students_per_group)
