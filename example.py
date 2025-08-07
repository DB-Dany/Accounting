from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Имя", "Зарплата", "Должность"]
table.add_row(["Иван Иванов", 75000, "Бухгалтер"])
table.add_row(["Петр Петров", 90000, "Менеджер"])
table.add_row(["Сидор Сидоров", 120000, "Директор"])

print(table)