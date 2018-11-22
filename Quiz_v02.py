#zjazd trzeci - praca domowa. Quiz z pytaniami.


import random

class Pytania:
    def __init__(self, pytanie, numer_poprawny):
        self.pytanie = pytanie
        self.numer_poprawny = numer_poprawny

pytania = [
    Pytania(['Kto prowadzi turniej milionerzy?:,'
              '(1) Urbanski'
              '(2) Ibisz'
              '(3) Holowczyc'], '1'),
    Pytania(['jak nazywal sie Tolek?:'
              '(1) Arbuz'
              '(2) Szparag'
              '(3) Banan'], '3'),
    Pytania(['Kto napisal ksiazke o Stasiu i Nel?:'
              '(1) Mickiewicz'
              '(2) Prus'
              '(3) Sienkiewicz'], '3'),
    Pytania(['Kto biega najszybciej?:'
             '(1) zolw'
             '(2) czlowiek'
             '(3) gepard'], '3'),
]

random.shuffle(pytania)

class Gra():
    def run_quiz(self):
        wynik = 0
        for zadane_pytanie in pytania:
            odpowiedz = input(zadane_pytanie.pytanie)

            if odpowiedz == zadane_pytanie.numer_poprawny:
                wynik += 1
                continue
            elif odpowiedz != zadane_pytanie.numer_poprawny:
                wynik += 0
                continue

        print(f' zdobyles: {wynik}', 'punkty', 'z', len(pytania), 'mozliwych')

a = Gra()
a.run_quiz()



