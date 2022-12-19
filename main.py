zakupy = {
  'piekarnia': ['chleb', 'pączek', 'bułki'], 'warzywniak': ['marchew', 'seler', 'rukola']
}
zakupy = {miejsce.capitalize(): [rzeczy.capitalize() for rzeczy in lista_rzeczy] for miejsce, lista_rzeczy in zakupy.items()}


print('Lista zakupów:')

for miejsce, rzeczy in zakupy.items():
    print(f'Idę do {miejsce} i kupuję tam {rzeczy}')

ilosc_produktow = sum(len(rzeczy) for rzeczy in zakupy.values())

print(f'W sumie kupuję {ilosc_produktow} produktów.')

print()

for liczba in range(101):
    if liczba % 5 == 0:
        print(liczba)
        print(liczba*liczba*liczba)

print(1)
print(2)