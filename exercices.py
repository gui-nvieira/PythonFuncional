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


# escreva uma função que receba uma lista de nomes e retorne uma lista com a str Sr. adicionada ao início de
# cada nome EX: print(adcPron(["Carlos", "Roberto", "Marcos"])) = ['Sr. Carlos', 'Sr. Roberto', 'Sr. Marcos']
def adcPron(L):
    return list(map(lambda x: "Sr. " + x, L))


# crie uma função que conte o número de espaços contidos em uma string
# Ex:     print(countSpaces("QUE COPA BOA")) = 2
def countSpaces(string):
    stAux = list(map(lambda x: 1 if x == " " else 0, string))
    return reduce(lambda x, y: x + y, stAux)


# escreva uma função que dada uma lista de números calcule 3n*2 + 2/n +1 para cada número da lista
# use funções auxiliares
# Ex print(calcNum([1, 2, 2, 1])) = [9.0, 14.0, 14.0, 9.0]
def calcNum(L):
    def funcAux(x): return 3*(x*2) + (2/x) + 1
    return list(map(funcAux, L))


# Escreva uma função que, dada uma lista de números,
# retorne uma lista com apenas os que forem negativos.
# Defina uma função auxiliar para ajudar neste exercício.
# Ex:     print(numNeg([1, -2, 2, -1])) = [-2, -1]
def numNeg(L):
    def funcAux(x): return x < 0
    return list(filter(funcAux, L))


# inicializador
if __name__ == "__main__":
    print(numNeg([1, 2, -2, -1]))
