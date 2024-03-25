
print("\tЗавдання 1")

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))

X: float;

if (a == b):
    X = 2;
elif (a > b):
    X = a * b + 1
elif (a < b):
    X = (a**3 + 1)
    
print("X = ", X)

print("\tЗавдання 2")

x = 1
while(4 * x + 5 != 25):
    x += 1
    
print("x = ", x)

print("\tЗавдання 3")

N = int(input("Введіть N: "))

for i in range(1, N):
    print();
    for j in range(1, N):
        if(N - i >= j):
            print(j, end = ' ')
print()
