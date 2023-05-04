import os
import random
from configparser import ConfigParser

# i = 0
# for i in range(1, 1000):
#     i += 1
#     katalog = f'C:/Users/Kacper/Desktop/pliki-do-sortu/'
#     plik = f'plik-numer-{i}-katalog_{random.randint(1, 3)}.txt'
#     os.mkdir(f'{katalog}{plik}')


config = ConfigParser()
config.read('config.ini')
savedSource = config.get('paths', 'source')
savedtarget = config.get('paths', 'target')
savedtarget1 = config.get('paths', 'target1')
savedtarget2 = config.get('paths', 'target2')
savedtarget3 = config.get('paths', 'target3')
savedSchema = config.get('schemas', 'schema')
savedSchema1 = config.get('schemas', 'schema1')
savedSchema2 = config.get('schemas', 'schema2')
savedSchema3 = config.get('schemas', 'schema3')

# configTargetList2 = [config.get('schemas', f'schema') if i == 0 else config.get('schemas', f'schema{i}') for i in range(0,4)]

# print(configTargetList2)

# for file in os.listdir(savedSource):
#     if file.endswith(tuple(configTargetList2)):
#         print(file)

for file in os.listdir(savedSource):
    if file.endswith(savedSchema) or file.endswith(savedSchema1) or file.endswith(savedSchema2) or file.endswith(savedSchema3):
        print(file)
    else:
        print(f'{file} doesnt end with any schema')