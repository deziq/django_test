import datetime

class dipendente(object):
    
    aumento = 1.2
    n_team = 0

    def __init__(self,nome,cognome,stipendio):
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio
        self.email = f'{self.cognome}.{self.nome}@mail.it'.lower()
        
        dipendente.n_team += 1

    def full_name(self):
        return f'{self.cognome} {self.nome}'

    def calcola_aumento(self):
        self.stipendio = int(self.stipendio*self.aumento)

    @classmethod
    def set_aumento(cls,valore):
        cls.aumento = valore

    @classmethod
    def create_from_string(cls,stringa):
        cognome,nome,stipendio = stringa.split('-');
        return cls(cognome,nome,stipendio)

class developer(dipendente):
    aumento = 1.8
    def __init__(self,nome,cognome,stupendio,linguaggi=None):
        super().__init__(nome,cognome,stupendio)
        if linguaggi is None:
            self.linguaggi = []
        else:
            self.linguaggi = linguaggi

    def add_lng(self,lng):
        if lng not in self.linguaggi:
            self.linguaggi.append(lng)
        else:
            return 'Linguaggio esistente'

    def remove_lng(self,lng):
        if lng in self.linguaggi:
            self.linguaggi.remove(lng)
    
    def show_lng(self):
        for lng in self.linguaggi:
            print('--->',lng)


    def __str__(self):
        return f'Il dipendente {self.full_name()} ({self.email}) guadagna {int(self.stipendio*12)} Euro all\'anno'

    def __repr__(self):
        return f'{self.full_name()}'


class manager(dipendente):
    aumento = 2.2

    def __init__(self, nome, cognome, stipendio,team=None):
        super().__init__(nome, cognome, stipendio)
        if team is None:
            self.team = []
        else:
            self.team = team
    
    def add_developer(self,dip):
        if developer not in self.linguaggi:
            self.team.append(developer)
        else:
            return 'Dipendente esistente'

    def remove_developer(self,dip):
        if developer in self.dipendenti:
            self.team.remove(developer)
    
    def show_developer(self):
        for developer in self.team:
            print('--->',developer.full_name())
    


giovanni = developer('Giovanni','Allevi',1500);
filippo = developer('Filippo','Bianchi',1800);
franco = developer('Franco','Neri',1700);
vito = developer('Vito','Rossi',1900);
giulia = developer.create_from_string('Giulia-Loreto-1440');

vito.add_lng('Java')
vito.add_lng('Python')
vito.add_lng('Delphi')
vito.add_lng('PHP')
vito.add_lng('ReactJS')


aldo = manager('Aldo','Brando',4000,[vito])
print(aldo.email)

print(vito)

print(repr(vito))

'''
#import unicodedata
def testa_parole(parola):
    indice = (len(parola) -1)
    nuova_parola = ""
    print(input('scrivi è:'))
    while indice >= 0:
        nuova_parola += parola[indice]
        indice -= 1
    if nuova_parola == parola:
        message = 'La parola passata è un palindromo! ' + nuova_parola
        print(message)#.encode('utf8'))
        #print()
    else:
        print('Mi dispiace, la parola inserita non è un palindromo...')


#testa_parole('ISSI')


def traduttore():
    print(
    #Ciao! questo programma traduce un testo passato in "rövarspråket".
    #Ció significa che raddoppia ogni consonante delle parole e ci mette una "o" in mezzo...
    )

    vocali = "aeiou"
    specials = [" ", ",", ".", "?", "!", '"',"'"]
    
    while True:
        testo = input('\nInserisci il testo che desideri tradurre -> ')
        tradotta = ""
        for x in testo:
            if x in vocali or x in specials:
                tradotta += x #tradotta = tradotta + x
            else:
                tradotta = tradotta + x + "o" + x

        print(f"Ecco a te la traduzione! '{tradotta}'")

        if input("\nDesidere tradurre un'altra frase? ") == "no":
            break

#traduttore()
'''

import os
import platform

def sys_info():
    print(f"Il Sistema attualmente in uso è: " + platform.system())
    print("OS rilevato: " + os.name)
    print("OS rilevato: " + platform.platform())
    print("Aggiornato alla Versione: " + platform.release())

sys_info()


import keyboard  # using module keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
        else:
            pass
    except:
        break  # if user pressed a key other than the given key the loop will break