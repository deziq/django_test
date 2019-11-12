import datetime

class car(object):
    limite_storicita = 30
    n_auto = 0
    def __init__(self,marca,modello,anno,colore,motore,consumoKM):
        self.marca      = marca
        self.modello    = modello
        self.anno       = anno
        self.colore     = colore
        self.motore     = motore
        self.consumoKM  = consumoKM

        car.n_auto += 1

    def full_name(self):
        return f'Possiedo una {self.marca} {self.modello} di colore {self.colore}'

    def storico(self):
        now = datetime.datetime.now()
        anno = now.year # now.month, now.day, now.hour, now.minute, now.second
        storicita = anno-self.anno
        msg = ''
        if storicita >= self.limite_storicita:
            msg = 'auto storica'
        else:
            msg = 'auto non storica'
        return msg

    def calcoloConsumo(self,km):
        consumo = int(self.consumoKM * km)
        return f'{consumo} lt'


ferrari = car("Ferrari","Enzo",1995,"Rosso","V12",0.36)
lamborghini = car("Lamborghini","Murcielago",1998,"Giallo","V10",0.58)
ferrari.limite_storicita = 40
print(ferrari.storico())
print(ferrari.full_name())
print(ferrari.calcoloConsumo(150))
#print(ferrari.__dict__)
#print(car.__dict__)
print(car.n_auto)