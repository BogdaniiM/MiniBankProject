class ContBancar:
    def __init__(self, numar_cont, detinator):
        self.numar_cont = numar_cont
        self.detinator = detinator
        self.__sold = 2999.99

    def depunere(self, suma):
        if suma > 0:
            self.sold += suma
            return f'{suma} RON au fost depusi cu succes pe contul {self.numar_cont}. Soldul curent: {self.sold} RON.'
        else:
            return 'Suma trebuie sa fie pozitiva.'

    def retragere(self, suma_retragere):
        if suma_retragere > 0:
            if suma_retragere <= self.sold:
                self.sold -= suma_retragere
                return f'{suma_retragere} RON au fost retrasi cu succes de pe contul {self.numar_cont}. Sold curent: {self.sold} RON.'
            else:
                return 'Fonduri insuficiente'
        else:
            return 'Suma trebuie sa fie pozitiva'

    def sold_disponibil(self):
        print(f'Soldul curent al contului {self.numar_cont} este {self.sold} RON.')