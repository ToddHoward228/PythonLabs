import pandas as pd

employees = {
    "First Name": ["Абдула", "Петро", "Васить", "Діана", "Євгенія", "Денис"], 
    "Second Name": ["Сергієв", "Стус", "Дорошенко", "Куравльов", "Дорошенко", "Кудін"], 
    "Address": ["3-я Заводська вулиця, 2", "вулиця Ярославни, 68", "вулиця Володимира Затуливітра, 35", "вулиця Шота Руставелі, 37", "вулиця Володимира Затуливітра, 38", "вулиця Берегова, 2"]}

employees_df = pd.DataFrame(employees)

print(employees_df)

grouped_df = employees_df.groupby("Second Name").agg({"First Name": "count"}).reset_index()
grouped_df.columns = ["Second Name", "Employee Count"]

print("Змінений басє фрейм")
print(grouped_df)
