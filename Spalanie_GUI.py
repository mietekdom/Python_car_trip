import tkinter
from tkinter import messagebox

def policz_koszt():
    dystans = int(dystans_entry.get())
    spalanie = float(spalanie_entry.get())
    cena = float(entry_cena_paliwa.get())
    koszt = dystans / 100 * spalanie * cena

    messagebox.showinfo('Przelicz', f'Koszt przejazdu {koszt}!')


root = tkinter.Tk()
root.title('Koszt przejazdu!') #nazwa okienka

root.columnconfigure(0, weight=1)

dystans_lable = tkinter.Label(root, text='Podaj dystans: ') #tekst pisany w okienku
dystans_lable.grid(row=0, column=0)

dystans_entry = tkinter.Entry(root) #miejsce na wpisanie tekstu
dystans_entry.grid(row=0, column=1)



spalanie_lable = tkinter.Label(root, text='Podaj spalanie: ') #tekst pisany w okienku
spalanie_lable.grid(row=1, column=0)

spalanie_entry = tkinter.Entry(root) #miejsce na wpisanie tekstu
spalanie_entry.grid(row=1, column=1)



lable_cena_paliwa = tkinter.Label(root, text='Podaj cene paliwa: ') #tekst pisany w okienku
lable_cena_paliwa.grid(row=2, column=0)

entry_cena_paliwa = tkinter.Entry(root) #miejsce na wpisanie tekstu
entry_cena_paliwa.grid(row=2, column=1)



button = tkinter.Button(root, text='Przelicz!', command= policz_koszt) #dodawanie przycisku
button.grid(row=3, column=0, columnspan=2, sticky=tkinter.W+tkinter.E)


root.mainloop()