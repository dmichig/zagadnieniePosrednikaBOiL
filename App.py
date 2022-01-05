import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):

        super().__init__(master)

        self.odbiorcaFikcyjny = None
        self.dostawcaFikcyjny = None

        self.lDostawcow = 3
        self.lOdbiorcow = 3

        self.calkowitaPodaz = 0
        self.calkowityPopyt = 0

        self.dostawcy = []
        self.odbiorcy = []

        self.entriesDostawcyCena = []
        self.entriesDostawcyIlosc = []

        self.entriesOdbiorcyCena = []
        self.entriesOdbiorcyIlosc = []

        self.entriesMacierzTransportu =[]
        self.macierzTransportu = []

        self.macierzZyskowjednostkowych = []

        self.tabelaWykonanychPrzewozow = []

        self.tabelaStanuPotrzeb = []





