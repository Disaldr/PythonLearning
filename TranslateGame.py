print("Приветствую в игре Транслятор! Введи слова и их перевод, а я проведу тестирование по этим словам")
dictionary = {}

# Цикл для заполнения словаря
while True:
    key = input("Введите слово на аглийской или Stop: ").title()
    if key == "stop":
        break

    value = input("Введите его перевод или Stop: ").title()
    if value == "Stop":
        break
    dictionary[key] = value

dictionary = list(disctionary.items())
random.shuffle(dictionary)
dictionary = dict(dictionary)
print("Сосредоточься, дыши нормально, включи голову и сдай этот тест")

scores = 0
error = 0

for key, value in dictionary.items():
    translation = input("Введи перевод слова " + key + ": ").title()
    if translation == value:
        scores +=1
    else:
        error +=1

print(scores)
    if error == 3:
        break
print("У тебя 3 ошибки.Отдохни и попробуй позже еще раз")
