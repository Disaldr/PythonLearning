level = int(input("Выберите уровнеь сложности: 1 - легкий, 2 - средний, 3 - сложный: "))
if level = 1
print("У вас 12 попыток")
if level = 2
print("У вас 9 попыток")
if level = 3
print("У вас 6 попыток")

import random

number = print(random.randint(1,10))
guess = int(input("\nУгадай: "))
tries = 12

while guess != the_number and tries < 12:
        print ("Это была попытка №", tries)
        if guess > the_number:
            print("Меньше...")
        else:
            print("Больше...")
        guess = int(input("\Угадай: "))
        tries += 1

 if tries == 12:
        print ("\nПроигрыш, это было число ", the_number)
        defeats += 1
    else:
        print ("\nВыигрыш, это было число ", the_number)
        print "Это заняло", tries, "попыток!"
        wins += 1
