from ContBancar import ContBancar
from Banca import Banca

cont1 = ContBancar(1111, 'Bogdan', 100)
cont2 = ContBancar(1112, "Ana Tanevska", 400)
banca1 = Banca('Nordea')
banca1.adauga_cont(cont1)
banca1.adauga_cont(cont2)
banca1.afiseaza_conturi()
cont1.depunere(100)
cont1.depunere(500)
cont2.depunere(400)
cont1.retragere(200)
cont2.retragere(1000)
cont1.sold_disponibil()
cont2.sold_disponibil()
banca1.efectueaza_transfer(1111, 1112, 50)
banca1.efectueaza_transfer(1111, 1112, 100)

