import pandas as pd

data = pd.read_csv('students.csv')

filtered_students = data[data['Score'] > 80]

sorted_students = filtered_students.sort_values(by='Score', ascending=False)

print("студенты с баллом выше 80, отсортированные по убыванию балла:")
print(sorted_students)

oldest_student = data.loc[data['Age'].idxmax()]
youngest_student = data.loc[data['Age'].idxmin()]

print("\nсамый старший студент:")
print(oldest_student)

print("\nсамый младший студент:")
print(youngest_student)
