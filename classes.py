def soma(valores, x=0):
    aux = 0
    for val in valores:
        aux += val
    return aux + x

def maior(x, y):
    return x if x > y else y

def media(valores):
    total = soma(valores)
    return total / len(valores)

def valores_iguais(valores1 , valores2):
    elementos_em_comum = []
    for elemento1 in valores1:
        for elemento2 in valores2:
            if elemento1 == elemento2 and elemento1 not in elementos_em_comum:
                elementos_em_comum.append(elemento1)
                break

    return elementos_em_comum

def indice_prim_valor_igual(valores1,valores2):
    for i in range(len(valores1)):
        for j in range(len(valores2)):
            if valores1[i] == valores2[j]:
                return i
