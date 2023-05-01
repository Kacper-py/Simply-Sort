import os
import random

i = 0
for i in range(1, 1000):
    i += 1
    katalog = f'C:/Users/Kacper/Desktop/pliki-do-sortu/'
    plik = f'plik-numer-{i}-katalog_{random.randint(1, 3)}.txt'
    os.mkdir(f'{katalog}{plik}')