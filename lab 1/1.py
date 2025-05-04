number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
number3 = float(input("Введите третье число: "))

if number1 >= number2 and number1 >= number3:
    maximum = number1
elif number2 >= number1 and number2 >= number3:
    maximum = number2
else:
    maximum = number3

if number1 <= number2 and number1 <= number3:
    minimum = number1
elif number2 <= number1 and number2 <= number3:
    minimum = number2
else:
    minimum = number3

print(f"Максимальное число: {maximum}")
print(f"Минимальное число: {minimum}")