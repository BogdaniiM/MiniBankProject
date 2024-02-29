from ContBancar import ContBancar
class Banca():
    def __init__(self, nume_banca):
        self.nume_banca = nume_banca
        self.conturi = {}

    def adauga_cont(self, cont):
        self.conturi[cont.numar_cont] = cont


    def afiseaza_conturi(self):
        for numar_cont, cont in self.conturi.items():
            print(f"Contul {numar_cont} este detinut de {cont.detinator} si are soldul de {cont.sold} lei ")

    def efectueaza_transfer(self, numar_cont_sursa, numar_cont_destinatie, suma):
        self.numar_cont_sursa = numar_cont_sursa
        self.numar_cont_destinatie = numar_cont_destinatie
        self.suma = suma
        if numar_cont_sursa in self.conturi and numar_cont_destinatie in self.conturi:
            cont_sursa = self.conturi[numar_cont_sursa]
            cont_retragere = self.conturi[numar_cont_destinatie]
            rezultat_retragere = cont_retragere.retragere(suma)
            rezultat_depunere = cont_sursa.depunere(suma)
            print(f'A fost retrasa {rezultat_retragere} din contul {cont_retragere}\nA fost depusa {rezultat_depunere} din contul {cont_sursa}')
        else:
            print('Conturi invalide')
