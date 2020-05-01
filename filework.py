path = 'pi_million_digits.txt'

with open(path) as file:
    lines = file.readlines()

pi_string = ""
for line in lines:
    pi_string += line

print(pi_string[:10])

birthday = input("Введите дату рождения: ")
index = pi_string.find(birthday)
if index != -1:
    print(index)
    print(pi_string.count(birthday))
else:
    print("В числе Пи не рождаются! ")

