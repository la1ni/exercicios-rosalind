n = 33  # num de meses decorridos
k = 4  # quantidade de pares de coelhos gerados a cada mês
coelhos_r = [0]  # coelhos em idade reprodutiva
coelhos_nr = [1]  # coelhos filhotes
for c in range(1, n):
    coelhos_r.append((coelhos_nr[c-1])+(coelhos_r[c-1]))
    coelhos_nr.append((coelhos_r[c-1]*k))
soma = (coelhos_nr[n-1]+coelhos_r[n-1])
print(soma)
