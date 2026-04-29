class Kitob:
    def __init__(self, nom, muallif, narx):
        self.nom = nom
        self.muallif = muallif
        self.narx = narx

    def malumotlar(self):
        print(self.nom, self.muallif, self.narx)

    def narx_ozgartirish(self, toz):
        if toz > 0:
            self.narx = toz
        else:
            print("xato")

a  = Kitob("Abdulla Qodiriy", "O'tgan kunlar", 60000)
a.malumotlar()
a.narx_ozgartirish(10000)
a.malumotlar()

# 2
class Talaba:
    def __init__(self, ism, kurs, baholash):
        self.ism = ism
        self.kurs = kurs
        self.baholash = baholash

    def malumotlar(self):
        print(self.ism)
        print(self.kurs)
        print(self.baholash)

    def orta_baho(self):
        print(self.baholash // 2)

a = Talaba("Bunyod", 2, 100)
a.malumotlar()
a.orta_baho()
a.malumotlar()

# 3
class Avtomobil:
    def __init__(self, model, yil, tezlik):
        self.model = model
        self.yil = yil
        self.tezlik = tezlik

    def info(self):
        print(self.model)
        print(self.yil)
        print(self.tezlik)

    def tezlik_oshir(self, tez):
        print(f"Tezlik oshdi: {self.tezlik + tez}")

a = Avtomobil("cobalt", 2026, 100)
a.info()
a.tezlik_oshir(100)
a.info()

# 4
class BankHisobi:
    def __init__(self, egsi, balans):
        self.egsi = egsi
        self.balans = balans

    def balansni_kor(self):
        print(self.egsi)
        print(self.balans)

    def pul_qosh(self,q_pul):
        print(f"Bul qilsdi: {self.balans + q_pul}")

a = BankHisobi("s0br", 100)
a.balansni_kor()
a.pul_qosh(100)
a.balansni_kor()

# 5
class Kuchuk(Hayvon):
    def __init__(self):
        super().__init__("Kuchuk", "Vov-vov!")


class Mushuk(Hayvon):
    def __init__(self):
        super().__init__("Mushuk", "Miyov!")


k = Kuchuk()
k.ovoz_chiqar()

m = Mushuk()
m.ovoz_chiqar()
