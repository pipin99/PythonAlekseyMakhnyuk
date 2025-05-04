n = int(input("Введите натуральное число n: "))
max_width = 2 * n - 1

for i in range(n, 0, -1):
    left = ''.join(str(j) for j in range(i, 0, -1))
    right = ''.join(str(j) for j in range(2, i + 1))
    numbers = left + right
    spaces = ' ' * ((max_width - len(numbers)) // 2)
    print(spaces + numbers)