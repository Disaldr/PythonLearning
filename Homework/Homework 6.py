# Cделать программу  финансового учета, которая на вход принимает файл, который ей указали, в котором цифры должны быть расположены построчно. Программа выдает простейшие статистики, такие как суммы и среднее, которые она записывает в файл вывода, которые она сама генерирует


full_path = ''
nums = []

with open(full_path+'HW6.txt') as file:
    lines = file.read().split('\n')
    for line in lines:
        nums.append(int(line))
        print(line)
file.close()

# sum(..., counter()).'HW6.txt'join(sequence)

filename = 'program.txt'
with open(filename, 'w') as file:
    file.write('Итоговые данные')
file.close()