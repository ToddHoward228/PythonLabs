print("\tЗавдання 1")

N = int(input("Введіть розмір масиву "))

vector = [0] * N

print("Введіть елементи мисиву")

for i in range(0, N):
    vector[i] = int(input())

print("Максимальний елемент = ", max(vector))

print("\tЗавдання 2")

N = int(input("Введіть розмір матриці "))

matrix = [[0] * N for i in range(N)]

for i in range(0, N):
    for j in range(0, N - i):
        matrix[i][j] = N - i - j;

for i in range(0, N):
    print(matrix[i])
