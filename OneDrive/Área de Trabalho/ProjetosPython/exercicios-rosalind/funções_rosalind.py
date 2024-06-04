import re
def dividing_strings_in_sequences(string_bruta = str):
    '''
    :param string_bruta: é o texo do jeito que ele chega do rosalind. Normalmente, várias sequencias de bases
    :return: lista com cada sequência em uma posição. Caso tenha os nomes, como ">Rosalind3404" e se deseje remover, usar função remove_rosalind
    '''
    lista_limpa = []
    lista_dividida = string_bruta.strip().split("\n")
    for index, item in enumerate(lista_dividida):
        lista_limpa.append(item.strip())
    return lista_limpa

def remove_string(lista_geral= [str], termo_a_remover = str):
    '''
    :param lista_geral: recebe uma lista de strings, dentre as quais existem strings que se deseja remover
    :param termo_a_remover: recebe uma sequência de caracteres (pode ser em re) que se deseja remover
    :return: lista apenas com as strings desejadas
    '''
    lista_de_termos_a_remover = re.findall(termo_a_remover, lista_geral.__str__())
    for sequencia_de_caracteres in lista_geral:
        if sequencia_de_caracteres in lista_de_termos_a_remover:
            lista_geral.remove(sequencia_de_caracteres)
    return lista_geral