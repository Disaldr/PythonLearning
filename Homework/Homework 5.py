# Напишите функцию prime(number), в которую передается натуральное число, большее единицы. Функция должна возвращать строку «Простое число» в случае, если оно простое, и строку «Составное число» в противном случае.

number = int(input("Введите число: "))


def prime(number):
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return 'Простое число' if counter == 2 \
        else 'Составное число'

print(prime(number))
