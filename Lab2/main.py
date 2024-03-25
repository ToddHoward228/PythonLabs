import math
from module import f2

def f1(a):
    return math.cos(a) + math.cos(2*a) + math.cos(6*a) + math.cos(7*a)

a = float(input("Введіть а: "))
print("Результат першої функції = ", f1(a))

n = int(input("Введіть n: "))
print("Результат другої функції = ", f2(n))
