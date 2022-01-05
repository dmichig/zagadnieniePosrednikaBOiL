import tkinter as tk
from dostawca import Dostawca
from odbiorca import Odbiorca
from przewoz import Przewoz
from App import App

if __name__ == '__main__':

    window = tk.Tk()
    app = App(window)
    app.grid()

    label1 = tk.Label(app, text="Problem pośrednika").grid(column=0, row=0)

    labelLDostawcow = tk.Label(app, text="Liczba dostawców: 3").grid(column=0, row=1)
    labelLOdbiorcow = tk.Label(app, text="Liczba odbiorców: 3").grid(column=0, row=2)

    def readInfoDostawcy(numer):
        d = Dostawca(int(app.entriesDostawcyCena[numer].get()), int(app.entriesDostawcyIlosc[numer].get()))
        app.dostawcy.append(d)

    def readInfoOdbiorcy(numer):
        o = Odbiorca(int(app.entriesOdbiorcyCena[numer].get()), int(app.entriesOdbiorcyIlosc[numer].get()))
        app.odbiorcy.append(o)

    def getInfoDostawcy():
        for i in range(0, 3):
            d = Dostawca(int(app.entriesDostawcyCena[i].get()), int(app.entriesDostawcyIlosc[i].get()))
            app.dostawcy.append(d)

    def getInfoOdbiorcy():
        for i in range(0, 3):
            o = Odbiorca(int(app.entriesOdbiorcyCena[i].get()), int(app.entriesOdbiorcyIlosc[i].get()))
            app.odbiorcy.append(o)

    tk.Label(app, text="Dane dostawców").grid(column=0, row=3)

    for i in range(0, 3):
        tk.Label(app, text="Cena").grid(column=(2*i), row=4)
        tk.Label(app, text="Podaż").grid(column=(2*i), row=5)

        entryCena = tk.Entry(app)
        entryCena.grid(column=((2*i)+1), row=4)
        app.entriesDostawcyCena.append(entryCena)

        entryIlosc = tk.Entry(app)
        entryIlosc.grid(column=((2*i)+1), row=5)
        app.entriesDostawcyIlosc.append(entryIlosc)

    tk.Button(app, text="Pobierz dane", command=getInfoDostawcy).grid(column=1, row=6)

    tk.Label(app, text="Dane odbiorców").grid(column=0, row=7)

    for i in range(0, 3):
        tk.Label(app, text="Cena").grid(column=(2 * i), row=8)
        tk.Label(app, text="Popyt").grid(column=(2 * i), row=9)

        entryCena = tk.Entry(app)
        entryCena.grid(column=((2 * i) + 1), row=8)
        app.entriesOdbiorcyCena.append(entryCena)

        entryIlosc = tk.Entry(app)
        entryIlosc.grid(column=((2 * i) + 1), row=9)
        app.entriesOdbiorcyIlosc.append(entryCena)

    tk.Button(app, text="Pobierz dane", command=getInfoOdbiorcy).grid(column=1, row=10)

    labelMT = tk.Label(app, text="*").grid(column=0, row=11)

    for i in range(1, 4):
        tk.Label(app, text="d{0}".format(i)).grid(column=0, row=11+i)
        tk.Label(app, text="o{0}".format(i)).grid(column=i, row=11)

    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            entry = tk.Entry(app)
            entry.grid(column=1+j, row=12+i)
            row.append(entry)
        app.entriesMacierzTransportu.append(row)

    def getMacierzTransportu():
        for i in range(0, 3):
            row = []
            for j in range(0, 3):
                row.append(int(app.entriesMacierzTransportu[i][j].get()))
            app.macierzTransportu.append(row)


    tk.Button(app, text="Pobierz koszty transportu", command=getMacierzTransportu).grid(column=0, row=15)
    tk.Label(app, text="--------------------------------------------").grid(column=0, row=16)


    def Oblicz():

        for i in range(0, 3):
            app.calkowitaPodaz = app.calkowitaPodaz + app.dostawcy[i].podaz
            app.calkowityPopyt = app.calkowityPopyt + app.odbiorcy[i].popyt
            app.tabelaStanuPotrzeb.append(app.odbiorcy[i].popyt)

        if app.calkowityPopyt != app.calkowitaPodaz:
            app.dostawcaFikcyjny = Dostawca(0, app.calkowityPopyt)
            app.odbiorcaFikcyjny = Odbiorca(0, app.calkowitaPodaz)

        for i in range(0, 3):
            row = []

            for j in range(0, 3):
                odbiorca = app.odbiorcy[j]
                dostawca = app.dostawcy[i]

                zyskJednostkowy = odbiorca.cenaSprzedazy - dostawca.kosztZakupu - app.macierzTransportu[i][j]

                row.append(zyskJednostkowy)

            app.macierzZyskowjednostkowych.append(row)

        tk.Label(app, text="Macierz zysków jednostkowych").grid(column=0, row=18)
        tk.Label(app, text="*").grid(column=0, row=19)

        for i in range(1, 4):
            tk.Label(app, text="d{0}".format(i)).grid(column=0, row=19 + i)
            tk.Label(app, text="o{0}".format(i)).grid(column=i, row=19)

        for i in range(0, 3):
            for j in range(0, 3):
                label = tk.Label(app, text="{0}".format(app.macierzZyskowjednostkowych[i][j]))
                label.grid(column=1 + j, row=20 + i)

        maxZysk = app.macierzZyskowjednostkowych[0][0]
        idDostawcy = 0
        idOdbiorcy = 0

        IDold=[]

        while any(app.tabelaStanuPotrzeb) > 0:
            for i in range(0, 3):
                for j in range(0, 3):
                    if app.macierzZyskowjednostkowych[i][j] > maxZysk:
                        maxZysk = app.macierzZyskowjednostkowych[i][j]
                        idDostawcy = i
                        idOdbiorcy = j

            IDold.append([idDostawcy, idOdbiorcy])

            if app.dostawcy[idDostawcy].stanPosiadania>0 and app.odbiorcy[idOdbiorcy].stanPotrzeb > 0:
                if app.dostawcy[idDostawcy].stanPosiadania>app.odbiorcy[idOdbiorcy].stanPotrzeb:
                    ilosc = app.odbiorcy[idOdbiorcy].stanPotrzeb
                    app.tabelaWykonanychPrzewozow.append(Przewoz(idDostawcy, idOdbiorcy, maxZysk, ilosc))
                    app.tabelaStanuPotrzeb[idOdbiorcy] = app.tabelaStanuPotrzeb[idOdbiorcy] - ilosc
                else:
                    ilosc = app.dostawcy[idDostawcy].stanPosiadania
                    app.tabelaWykonanychPrzewozow.append(Przewoz(idDostawcy, idOdbiorcy, maxZysk, ilosc))
                    app.tabelaStanuPotrzeb[idOdbiorcy] = app.tabelaStanuPotrzeb[idOdbiorcy] - ilosc


    tk.Button(app, text="OBLICZ", command=Oblicz).grid(column=0, row=17)





    window.mainloop()
