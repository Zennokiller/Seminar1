# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input("Ввведите трехзначное число: ")
a = int(number[0])
b = int(number[1])
c = int(number[2])
print("Сумма цифр числа ", number, " = ",a+b+c)