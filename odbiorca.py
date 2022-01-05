class Odbiorca:
    def __init__(self, cenaSprzedazy, popyt):
        self.cenaSprzedazy = cenaSprzedazy
        self.popyt = popyt
        self.stanPotrzeb = popyt

    def aktualizujStanPotrzeb(self, liczba):
        self.stanPotrzeb = self.stanPotrzeb - liczba