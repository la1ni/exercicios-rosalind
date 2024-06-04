from math import comb
from itertools import combinations

lista_todos_os_individuos = []
def adiciona_letra(letra=str, quant=int):
    for n in range(0, quant):
        lista_todos_os_individuos.append(letra)
    return

possibilidades_acasalamento = ()
def acasalamento(l = list):
    comb = combinations(l, 2)
    possibilidades_acasalamento = list(comb)
    return possibilidades_acasalamento

lista_probabilidade_duplas = []
def probabilidade_duplas(lista =  list):
    pr_mn = 0
    pr_nn = 0
    pr_mm = 0
    for item in lista:
        if item == ('m', 'n'):
            pr_mn = pr_mn + 1
        if item == ('n', 'n'):
            pr_nn += 1
        if item == ('m', 'm'):
            pr_mm += 1
    lista_probabilidade_duplas.append(pr_mn/(total_combinacoes))
    lista_probabilidade_duplas.append(pr_nn/(total_combinacoes))
    lista_probabilidade_duplas.append(pr_mm/(total_combinacoes))
    return lista_probabilidade_duplas

tres_numeros = (input("Cole o número de indivíduos das populações k, m e n respectivamente, sem vírgulas: "))
lista_com_os_tres = [int(numero) for numero in tres_numeros.split()]

adiciona_letra("k", lista_com_os_tres[0])
adiciona_letra("m", lista_com_os_tres[1])
adiciona_letra("n", lista_com_os_tres[2])

total_individuos = sum(lista_com_os_tres)
total_combinacoes = comb(total_individuos, 2)

a = acasalamento(lista_todos_os_individuos)
b = probabilidade_duplas(a)

soma_final = 1 - (((b[0]*(1/2))+(b[1])+(b[2]*(1/4))))
print(round(soma_final,5))









