print("\tЗавдання 1")

def Insert(f_list, element, position):
    index = f_list.index(position)
    f_list.insert(index, element)
    return f_list

N = int(input("Введіть кількість елементів списку: "))

my_list = [0] * N

for i in range(0, N):
    my_list[i] = int(input("Введіть елемент: "))

put_el = input("Введіть елемент для вставки ")
x = int(input("Введіть елемент перед яким буде вставка "))

my_list = Insert(my_list, put_el, 6)
    
print(my_list)

print("\tЗавдання 2")

def FindDigit(f_list, value):
    for i in range(0,len(f_list)):
        if f_list[i] == value:
            return i
    return "Nan"

my_list = [65, "Луна", -90, 6.5, "Поле", 78, 69]

search_dig = int(input("Введіть шукане значення "))

result = FindDigit(my_list, search_dig)

if result == "Nan":
    print("Значення не знайдено")    
else:
    print("Значення знайдено на позиції ", result)

print("\tЗавдання 3")

alphabet = {"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"}

my_list = sorted(alphabet)

for item in my_list:
    print(item)
