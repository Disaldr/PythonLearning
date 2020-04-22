import random

num = int(input("Под какое количество патронов обойма?: "))
real_bullets = int(input("Сколько патронов в обойме?: "))
bullets = [0 for i in range(num-real_bullets)]
bullets += [1 for j in range(real_bullets)]
print(bullets)

a = int(input("Точно хочешь сыграть? Если да, то напиши 1, а если нет, то 0: "))

while a == 1:
    if random.choice(bullets) == 1:
        print("Ты проиграл! Хочешь сыграть еще раз?")
    else:
        print("Ты выиграл! Хочешь сыграть еще раз?")
        a = int(input("Если да, то напиши 1, а если нет, то 0: "))
print("Спасибо за игру")
