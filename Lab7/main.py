from os import read


def Show():
    print("\tСписок робітників")
    keys_list = list(employees.keys())
    
    for key in keys_list:
        print(key + " – " + employees[key])
        
def Add():
    name = input("Введіть прізвище нового працівника: ")
    adress = input("Введіть адресу нового працівника: ")
    
    employees.update({ name: adress })
    
def Delete():
    key = input("Введіть прізвище для видалення: ")
    
    if key in employees:
        employees.pop(key)
    else:
        "Ключ не знайдений"
    
def ShowSorted():
    print("\tСписок робітників")
    keys_list = list(employees.keys())
    
    keys_list.sort()

    for key in keys_list:
        print(key + " – " + employees[key])
        
def SearchItem():
    key = input("Введіть прізвище для пошуку: ")

    if key in employees:
        print("Робітник ", key, ", Проживає за адресою ", employees[key])
    else:
        print("Робітник відсутній в базі даних")

employees = {"Сергієв" : "вулиця Революції Гідності, 2", "Кудін" : "вулиця Гулака-Артемовського, 9", "Стус" : "провулок Зіновія Красовицького, 5", "Дорошенко" : "Гончарна вулиця, 34", "Куравльов" : "вулиця Лучанська, 45"}
employees.update( {"Кубиків" : "3-я Заводська вулиця, 2", "Кожедуб" : "вулиця Берегова, 2", "Андропов" : "вулиця Ярославни, 68" , "Хамер" : "вулиця Володимира Затуливітра, 35", "Джонсон" : "вулиця Шота Руставелі, 37"} )

command_key = " "

print("\
Для пошуку за ім'ям введіть 0\n\
Для виводц відсортованого словника введіть 1\n\
Для виводу словника введіть 2\n\
Для додавання працівника введіть 3\n\
Для видалення працівника введіть 4\n\
Для виходу введіть ентер\n")

while(command_key != ""):
    command_key = input("Введіть індекс команди _\b")
    if command_key == "0":
        SearchItem()
    elif command_key == "1":
        ShowSorted()
    elif command_key == "2":
        Show()
    elif command_key == "3":
        Add()
    elif command_key == "4":
        Delete()
