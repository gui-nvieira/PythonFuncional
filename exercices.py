from functools import reduce


# Usando LCs, defina a função vogais(palavra) que retorna o número de vogais em palavra.
# Ex: print(vogais('nasemanadaprova')) = 7 .
def vogais(palavra):
    vogAux = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    detectVog = [1 for letra in palavra if letra in vogAux]
    return reduce(lambda x, y: x+y, detectVog)


# Defina a função maisQueKVogais(string) que retorna as palavras em string com mais que k vogais.
# Ex: print(maisQueKVogais('na semana da prova', 2)) = ['semana']
def maisQueKVogais(string, k):
    fraseAux = (str(string)).split()
    return [palavra for palavra in fraseAux if (vogais(palavra) > k)]


# Implemente a função maioria que tem como parâmetros uma propriedade (descrita como uma função anônima)
# e uma lista e retorna True se mais que metade dos elementos na lista têm a propriedade.
# print(checkProp([1, 2, 1, 3, 0, 2, 4], lambda x: x >= 2)) = True
def checkProp(L, cond):
    listAux = map(cond, L)
    reduceAux = reduce(lambda x, y: x+y, listAux)
    return True if reduceAux > (len(L))/2 else False


# inicializador
if __name__ == "__main__":
    print(checkProp([1, 2, 1, 3, 0, 2, 4], lambda x: x >= 2))
