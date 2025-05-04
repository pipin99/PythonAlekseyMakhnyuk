n = int(input("Введите натуральное число n: "))

for i in range(n, 0, -1):
    row = ""
    for j in range(1, i + 1):
        row += str(j)
    print(row)