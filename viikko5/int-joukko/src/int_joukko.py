KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti if kapasiteetti is not None else KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko if kasvatuskoko is not None else OLETUSKASVATUS

        if not isinstance(self.kapasiteetti, int) or self.kapasiteetti < 0:
            raise ValueError("Väärä kapasiteetti")
        if not isinstance(self.kasvatuskoko, int) or self.kasvatuskoko < 0:
            raise ValueError("Väärä kasvatuskoko")

        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm == len(self.ljono):
                self.kasvata_taulukkoa()
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        return False
    
    def kasvata_taulukkoa(self):
        uusi_ljono = self._luo_lista(len(self.ljono) + self.kasvatuskoko)
        for i in range(self.alkioiden_lkm):
            uusi_ljono[i] = self.ljono[i]
        self.ljono = uusi_ljono

    def poista(self, n):
        if n in self.ljono[:self.alkioiden_lkm]:
            indeksi = self.ljono.index(n)
            self.ljono[indeksi:self.alkioiden_lkm-1] = self.ljono[indeksi+1:self.alkioiden_lkm]
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list() + b.to_int_list():
            tulos.lisaa(numero)
        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            if numero in b.to_int_list():
                tulos.lisaa(numero)
        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        for numero in a.to_int_list():
            tulos.lisaa(numero)
        for numero in b.to_int_list():
            tulos.poista(numero)
        return tulos

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
