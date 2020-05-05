family = {"dad": 60, "mother": 55, "aunt": 50}
print(family['dad'])
family['uncle'] = 51
print(*family)

for key, value in family.items():
    print("Ключ - " +key+", значение - " + str(value))

    print(list(family.keys()))
    print(list(family.values()))

if 'dad' in family.keys()
    print('dad')
if 50 in family.values()
    print(50)