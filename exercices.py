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


# Escreva uma função que receba uma lista de números e retorne
# somente os que estiverem entre 1 e 100, inclusive.
# Defina uma função auxiliar para ajudar neste exercício.
def zeroHundr(L):
    def filtr(x): return x > 0 and x < 100
    return list(filter(filtr, L))


# Escreva uma função que receba uma lista de números e retorne
# somente aqueles que forem pares. Defina uma função auxiliar para ajudar neste exercício.
# Ex: print(evenRet([1, 2, 98, 105, -3])) = [2,98]
def evenRet(L):
    def filtr(x): return (x % 2) == 0
    return list(filter(filtr, L))


# Crie uma função charFound(c,s) que verifique se o caracter c está contido na string.
# O resultado deve ser True ou False. Você não deve usar o operador in.
# Defina uma função auxiliar para ajudar neste exercício.
# Ex.     print(charFound('c', 'ratinho taroso comeu chuchu')) = [False, False, True, True]
def charFound(l, string):
    strInput = str(string).split()
    mapAux = list(map(lambda x: x.__contains__(l), strInput))
    return mapAux


# Escreva uma função que receba uma lista de strings e retorne uma nova lista
# com adição de marcações HTML (p.ex.: p) antes e depois de cada string.
# Ex. print(HTMLBuilder(['c', 'ratinho taroso comeu chuchu']))
# = ['<p>c</p>', '<p>ratinho taroso comeu chuchu</p>']
def HTMLBuilder(L):
    mapAux = list(map(lambda x: "<p>" + x + "</p>", L))
    return mapAux


# inicializador
if __name__ == "__main__":
    print(HTMLBuilder(['c', 'ratinho taroso comeu chuchu']))
