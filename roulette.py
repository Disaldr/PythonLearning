import random

bullets = [0 for i in range(6)]
bullets[0] = 1

a = int(input("Хочешь сыграть? Если да, то напиши 1, а если нет, то 0: "))

while a == 1:
    if random.choice(bullets) == 1:
        print("Ты проиграл! Хочешь сыграть еще раз?")
    else:
        print("Ты выиграл! Хочешь сыграть еще раз?")
        a = int(input("Если да, то напиши 1, а если нет, то 0: "))
print("Спасибо за игру")
