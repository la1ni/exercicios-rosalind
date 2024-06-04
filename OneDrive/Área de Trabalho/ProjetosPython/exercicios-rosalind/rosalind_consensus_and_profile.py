import numpy as np
from funções_rosalind import dividing_strings_in_sequences, remove_string
import re
dataset = '''
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
'''

lista_com_todos_os_termos = dividing_strings_in_sequences(dataset)
lista_apenas_com_strings = remove_string(lista_com_todos_os_termos, '.Rosalind.\d{,3}')

tamanho_padrao_da_str = len(lista_apenas_com_strings[0])

dicionario_com_contador = {}

def contadores(lista = list):
    lista_de_letras = ["A", "C", "T", "G"]
    for item in lista:
        for coluna in item:
            for letra in lista_de_letras:

                dicionario_com_contador[f'{letra}']=[f'{c}']
    return dicionario_com_contador

contadores(lista_apenas_com_strings)





