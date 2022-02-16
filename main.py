waga_elementow = []
n = int(input("Podaj liczbę elementów jaką chcesz wysłać: "))

for i in range (1,n+1):
    print("Podaj wagę elementu ",i)
    element = float(input())
    waga_elementow.append(element)


liczba_paczek = 0
wyslane_kilogramy = 0
waga_paczki = 0
paczki = []

for i in range (0,n):
    if (0 < waga_elementow[i] < 1) or waga_elementow[i] > 10 :
        print("Nieprawidłowa waga! ELement musi być cieższy niż 1 kg i lżejszy niż 10 kg. Program kończy pracę.")
        wyslane_kilogramy=0
        break
    wyslane_kilogramy += waga_elementow[i]
    waga_paczki += waga_elementow[i]
    if waga_paczki >= 20:
        if waga_paczki > 20:
            waga_paczki -= waga_elementow[i]
            paczki.append(waga_paczki)
            print(f'Wysłano paczkę o wadze: {waga_paczki} kg')
            waga_paczki = waga_elementow[i]
        else:
            paczki.append(waga_paczki)
            print(f'Wysłano paczkę o wadze: {waga_paczki} kg')
            waga_paczki = 0
        liczba_paczek += 1
    if waga_elementow[i] == 0:
        liczba_paczek += 1
        paczki.append(waga_paczki)
        print(f'Wysłano paczkę o wadze: {waga_paczki} kg')
        break
    if i == (n-1) :
        liczba_paczek += 1
        paczki.append(waga_paczki)
        print(f'Wysłano paczkę o wadze: {waga_paczki} kg')


print('Wysłano ', len(paczki) ,' paczki')
print(f'Wysłano w sumie {wyslane_kilogramy} kg')
print('Wysłano ', 20*len(paczki)-wyslane_kilogramy, 'puste kilogramy-brak optymalnego pakowania')
print("Najwięcej pustych kilogramów miała paczka numer", (paczki.index(min(paczki))+1), 'ważyła: ', min(paczki), 'kg' )
