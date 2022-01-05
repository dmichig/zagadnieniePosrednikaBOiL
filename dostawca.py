class Dostawca:
    def __init__(self, kosztZakupu, podaz):
        self.kosztZakupu = kosztZakupu
        self.podaz = podaz
        self.stanPosiadania = podaz

    def aktualizujStanPosiadania(self, liczba):
        self.stanPosiadania = self.stanPosiadania - liczba


