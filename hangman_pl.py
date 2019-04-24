import codecs
import random
import time
import sys

def losowanko(lista_slow, y, litslo, slowo):  # losuje słowo z listy i drukuje '_' za kazda litere
    z = random.choice(lista_slow).lower()
    for i in z:  # dodaje tyle '_', ile liter w slowie
        y.append('_')
    for i in z:  # dodaje litery slowa
        litslo.append(i)
        slowo.append(i)

def rysunek(zycia):  # drukuje obrazek wisielca w zal. od liczby skuch
    if len(zycia) == 0:
        print('\n')
    elif len(zycia) == 1:
        print('\n |\n |\n |\n |\n_|_\n')
    elif len(zycia) == 2:
        print('  _\n |\n |\n |\n |\n_|_\n')
    elif len(zycia) == 3:
        print('  _\n |  |\n |\n |\n |\n_|_\n')
    elif len(zycia) == 4:
        print('  _\n |  |\n |  o\n |\n |\n_|_\n')
    elif len(zycia) == 5:
        print('  _\n |  |\n |  o\n |  +\n |\n_|_\n')
    elif len(zycia) == 6:
        print('  _\n |  |\n |  o\n | -+\n |\n_|_\n')
    elif len(zycia) == 7:
        print('  _\n |  |\n |  o\n | -+-\n |\n_|_\n')
    elif len(zycia) == 8:
        print('  _\n |  |\n |  o\n | -+-\n | /\n_|_\n')
    elif len(zycia) == 9:
        print('  _\n |  |\n |  o\n | -+-\n | / \ \n_|_\n')

def krok(zycia, y, litery, uzyte, litslo):  # wykonuje sie, dopoki y nie sanie sie lista liter slowa lub
    while len(zycia) < 9 and '_' in y:  # liczba skuch nie wyniesie 9
        print('  '.join(y))  # drukuje elementy listy y jako str
        print('\nOto litery, które masz do dyspozycji:')
        print(litery)
        print('A to litery, które użyłeś:')
        print(uzyte)
        x = input('Wpisz literę tutaj: ')
        num = []  # lista, ktora bd resetowana przy kazdym przejsciu petli
        if x in litery:
            if x in litslo:
                for i in range(len(litslo)):
                    if x == litslo[i]:
                        num.append(i)  # dodaje do listy numery liter
                        litslo[i] = '-'  # zamieniam odgadniete litery
                litery.remove(x)  # usuwam litere z listy dostepnych liter
                uzyte.append(x)  # dodaje litere do zuzytych liter
                for i in num:
                    for j in range(len(y)):
                        if j == i:
                            y[j] = x  # zamieniam odp. '_' na litere
                print(4 * '\n')
            else:
                print(4 * '\n' + 'Błąd!')
                litery.remove(x)  # usuwam litere z listy dostepnych liter
                uzyte.append(x)  # dodaje litere do zuzytych liter
                zycia.append('.')  # dodaje element do listy skuch
            rysunek(zycia)  # drukuje odpowiedni obrazek (zeby pojawial sie
        else:  # przy kazdym przejsciu, nie tylko, gdy skucha)
            print(5 * '\n')
            print('Litera wykorzystana lub niepoprawna fraza!\n\
Spróbuj jeszcze raz.\n\n')

def wisielec():  # funkcja 'zbiorcza'
    try:
        x = sys.argv[1]
    except:
        print('Błąd! Wprowadź drugi argument - nazwę pliku ze słowami.')
        exit()
    plik = codecs.open(x, 'r', 'utf-8').read()  # otwieram i czytam
    lista_slow = plik.split()  # tworze liste slow z pliku

    # tworze potrzebne listy; lista polskich liter
    literypl = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', \
              'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'q', 'r', \
              's', 'ś', 't', 'u', 'w', 'v', 'x', 'y', 'z', 'ź', 'ż']
    literyang = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', \
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x', \
               'y', 'z']
    uzyte = []  # lista uzytych liter
    zycia = []  # lista okreslajaca liczbe skuch
    litslo = []  # lista liter wylosowanego slowa, ktora zmienia sie w trakcie
    y = []  # lista '_', symbolizujacych litery slowa; zmienia sie w trakcie
    slowo = []  # lista liter slowa, ktora nie zmienia sie w trakcie

    print('Witaj w grze wisielec!\n')  # poczatek programu, zasady gry
    time.sleep(1)
    print('Oto zasady:\n\
- za chwilę zostanie wylosowane dla Ciebie słowo, które będziesz zgadywać,\n\
- zgadywać będziesz, wpisując pojedynczo litery w wyznaczone miejsce,\n\
- wpisuj zawsze jedną małą literę,\n\
- każda litera, którą zgadniesz, zostanie wpisana w miejsce kreski, która ją \
symbolizuje,\n\
- wygrasz, gdy zgadniesz całe słowo,\n\
- przegrasz, gdy wykorzystasz wszystkie szanse (9) - zostanie narysowany \
cały wisielec.\n')
    time.sleep(0.5)
    print('Za chwilę rozpocznie się gra...\n\n')
    time.sleep(3)
    losowanko(lista_slow, y, litslo, slowo)  # losuje slowo
    pl = False  # sprawdzam, czy polskie litery w liscie slow
    for i in plik:
        for j in 'ąćęłńóśźż':
            if i.lower() == j:
                pl = True
                break
    if pl:
        krok(zycia, y, literypl, uzyte, litslo)  # mechanizm gry
    else:
        krok(zycia, y, literyang, uzyte, litslo)  # mechanizm gry
    if len(zycia) >= 9:
        print('Przegrałeś!\nSzukane słowo to:')
        print('  '.join(slowo))
    elif not '_' in y:
        print('  '.join(y))
        print('\nUdało Ci się!\nWygrałeś!')
    print('\nDzięki za grę!')
    time.sleep(1)

wisielec()