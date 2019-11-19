
'''
a,b = 19,11
if a <= b:
    print(f'{a} è minore di {b}')
elif b == a:
    print('I valori sono uguali.')
else:
    print(f'{b} è minore di {a}')
'''


'''
for j in range(100):
    if j >= 0: print(j)
'''


'''
while True:
    n = 0
    guess = int(input('Inserisci un numero da 1 a 10: '))
    if guess == n:
        print('Hai indovinato!')
        break  # numero indovinato, interrompi il ciclo
    else:
        print('Ritenta sarai più fortunato')
'''

'''
import os,glob
file_dir = 'F:\Mes Projets Mobile\Android Astuces LST111'
os.chdir(file_dir)
for file in glob.glob('*.png'):
    print(file)
'''


'''
for num in range(1,101):
    if num % 2 == 0:
        print(f'{num} è divisibile per 2')
    else:
        print(f'{num} non è divisibile per 2')
'''

stringa = 'ciao come stai'
coso = [item for item in stringa]
print(len(coso))