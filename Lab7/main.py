def Show():
    print("\tСписок робітників")
    keys_list = list(employees.keys())
    
    for key in keys_list:
        print(key + " – " + employees[key])
        
def Add(name, adress):
    employees.update({ name: adress })
    
def Delete(key):
    employees.pop(key)
    
def ShowSorted():
    print("\tСписок робітників")
    keys_list = list(employees.keys())
    
    keys_list.sort()

    for key in keys_list:
        print(key + " – " + employees[key])

employees = {"Сергієв" : "вулиця Революції Гідності, 2", "Кудін" : "вулиця Гулака-Артемовського, 9", "Стус" : "провулок Зіновія Красовицького, 5", "Дорошенко" : "Гончарна вулиця, 34", "Куравльов" : "вулиця Лучанська, 45"}
employees.update( {"Кубиків" : "3-я Заводська вулиця, 2", "Кожедуб" : "вулиця Берегова, 2", "Андропов" : "вулиця Ярославни, 68" , "Хамер" : "вулиця Володимира Затуливітра, 35", "Джонсон" : "вулиця Шота Руставелі, 37"} )

searchin_list = ["Кузін", "Куравльов", "Кудін", "Кульков", "Кубиків"]

for search_item in searchin_list:
    if search_item in employees:
        print("Робітник ", search_item, ", Проживає за адресою ", employees[search_item])
    else:
        print("Робітник відсутній в базі даних")
        
Show()
Add("Тарас", "Вулиця Тараса Шевченка 23")
Delete("Дорошенко")
ShowSorted()
