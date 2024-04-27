from encodings import utf_8
import json

def Show(dict_employees):
    list_employee = list(dict_employees)
    for key in list_employee:
        print(key + " \n\tАдреса – " + dict_employees[key]["adress"] + "\n\tПосада – " + dict_employees[key]["position"])
        
def Search(dict_employees):
    key = input("Введіть прізвище для пошуку: ")
    print(key + " \n\tАдреса – " + dict_employees[key]["adress"] + "\n\tПосада – " + dict_employees[key]["position"])
    
def Search_First_Char(dict_employees):
    first_char = input("Введіть першу літеру прізвища: ")
    
    list_employees = list(dict_employees)
    for key in list_employees:
        if key[0] == first_char:
            print(key + " \n\tАдреса – " + dict_employees[key]["adress"] + "\n\tПосада – " + dict_employees[key]["position"])
        
        
def Delete(dict_employees):
    key = input("Введіть прізвище для видалення: ")
    
    if key in dict_employees:
        dict_employees.pop(key)
    else:
        "Ключ не знайдений"
    with open("Employees.json", "w", encoding= "utf_8") as update_file:
        update_file.write(json.dumps(dict_employees))
        
def Add(dict_employees):
    second_name = input("Введіть Прізвище нового працівника: ")
    adress = input("Введіть Адрусу нового працівника: ")
    position = input("Введіть Посаду нового працівника: ")
    
    dict_employees.update( { second_name : { "adress" :  adress, "position" : position} } )
    
    with open("Employees.json", "w", encoding= "utf_8") as update_file:
        update_file.write(json.dumps(dict_employees))


emloyees_file = open("Employees.json", "r", encoding= "utf_8")

emloyees = json.load(emloyees_file)

print("\
Для пошуку за першою літерою введіть 0\n\
Для пошуку за прізвищем введіть 1\n\
Для виведення всіх працівників введіть 2\n\
Для додавання працівника введіть 3\n\
Для видалення працівника введіть 4\n\
Для виходу введіть ентер\n")

while(command_key != ""):
    command_key = input("Введіть індекс команди _\b")
    if command_key == "0":
        Search_First_Char()
    elif command_key == "1":
        Search()
    elif command_key == "2":
        Show()
    elif command_key == "3":
        Add()
    elif command_key == "4":
        Delete()
