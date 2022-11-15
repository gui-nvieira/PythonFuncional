from math import sqrt
from functools import reduce


# função para dar o último valor de uma lista ou tupla encadeada
def tail(L):
    return L[1]


# função para retornar o primeiro valor de uma lista ou tupla
def head(L):
    return L[0]


# função recursiva que transforma uma lista nativa em uma lista encadeada
def py2ll(L):
    if not L:
        return None
    else:
        return (L[0], py2ll(L[1:]))


# função recursiva que transforma uma lista encadeada em uma lista nativa
def ll2py(L):
    if not L:
        return []
    else:
        H = head(L)
        T = tail(L)
        return [H] + ll2py(T)


# função pura para informar o tamanho de uma lista encadeada
def size(L):
    if not L:
        return 0
    else:
        return 1 + size(tail(L))


# funçao pura para informar o fatorial de um número
def fact(N):
    if not N:
        return None
    elif N == 0 or N == 1:
        return 1
    else:
        return (N*(fact(N-1)))


# Função que divide uma lista em duas metades e que os parametros abaixo sejam verdadeiros:
# e in L =>  e in L0 || e in L1
# size(L) == size (L0) + size(L1)
# abs(size(L0) - size(L1)) <= 1
def split(L):
    if not L:
        return (None, None)
    elif not tail(L):
        return (L, None)
    else:
        H0 = head(L)
        H1 = head(tail(L))
        (T0, T1) = split(tail(tail(L)))
        return ((H0, T0), (H1, T1))


# função que retorna true quando a lista for ordenada em ordem crescente e false quando o oposto
def sorted(L):
    if not L:
        return True
    elif not tail(L):
        return True
    else:
        C1 = head(L) <= head(tail(L))
        return C1 and sorted(tail(L))


# Função apra receber duas listas (L0 e L1) e retornar uma lista L que as seguintes propriedades são verdadeiras:
# e in L0 || e in L1 => e in L
# size(L0) + size(L1) == size (L)
# sorted(L0) && sorted (L1) => sorted(L)
def merge(L0, L1):
    if not L0:
        return L1
    elif not L1:
        return L0
    else:
        H0 = head(L0)
        T0 = tail(L0)
        H1 = head(L1)
        T1 = tail(L1)
        if H0 < H1:
            return (H0, merge(T0, L1))
        else:
            return (H1, merge(L0, T1))


# função pura msort (merge sort) que recebe uma lista L e retorna uma lista LL, tal que as seguintes propriedades
# sejam verdadeiras:
# e in L <=> e in LL
# sorted(LL)
def mSort(L):
    if not L:
        return None
    elif not tail(L):
        return L
    else:
        (L0, L1) = split(L)
        return merge(mSort(L0), mSort(L1))


# função test que recebe três parametros:
# - Um título para o teste
# - Uma expressão a ser testada
# - O Valor esperado
def test(title, value, expected):
    print("[" + title + "] " + str(value))
    if value == expected:
        print("Pass")
    else:
        print("Fail")


# função que incrementa cada elemento de uma lista, produzindo uma nova lista (map)
def incL(L):
    if not L:
        return None
    else:
        return (head(L)+1, incL(tail(L)))


# função que calcula o fatorial de cada elemento de uma lista encadeada, produzindo uma nova lista (map):
def factL(L):
    if not L:
        return None
    else:
        return (fact(head(L)), factL(tail(L)))


# função que converte para string cada elemento de uma lista encadeada (map)
def strL(L):
    if not L:
        return None
    else:
        return (str(head(L)), strL(tail(L)))


# estrutura padrão para map ou mapa:
def mapL(L, f):
    if not L:
        return None
    else:
        return (f(head(L)), mapL(tail(L), f))
# testar:	- fatoriais:	print(test("map-fac", mapL(py2ll([2, 3]), fact), (2, (6, None))))
#  		 	- incrementos: 	print(test("map-inc-lam", mapL(py2ll([1, 2]), (lambda x: x+1)), (2, (3, None))))


# função que recebe uma lista L e um inteiro N e produz uma lista de cada elemento de L aumentado de N:
def incN(L, N):
    return mapL(L, (lambda x: x + N))
# testar:	- print(test("test-incN", incN(py2ll([2, 3, 5]), 5), (7, (8, (10, None)))))


# experimento com closures:
def make_inc_3(n):
    return lambda x: x+n
# testar:	- print((make_inc_3(5)(2)))


# função que recebe uma lista L e um predicado f e produz uma nova lista com cada elemento de L
# que seja verdade para f
def filterL(L, f):
    if not L:
        return None
    else:
        T = filterL(tail(L), f)
        H = head(L)
        return (H, T) if f(H) else T


# função para filtrar numeros impares para incluir em filterL
def filterOdds(L):
    return filterL(L, (lambda x: not x % 2))
# teste:	- print(filterOdds(py2ll([2, 3, 8])))


# função apra filtrar valores que são string
def filterString(L):
    return filterL(L, lambda x: isinstance(x, str))
# teste:	- print(filterString(py2ll([2, "3", 8]))))


# função para descobrir numeros primos:
def prime(a):
    if a < 2:
        return False
    for x in range(2, int(sqrt(a))+1):
        if a % x == 0:
            return False
    return True


# função para aplicar filtro para números primos, retornando-os:
def filterPrime(L):
    return filterL(L, prime)
# teste: 		- print(filterPrime(py2ll([2, 3, 8, 17, 21, 51]))


# função que recebe duas listas e concatena elas:
def appendL(L1, L2):
    if not L1:
        return L2
    else:
        return (head(L1), appendL(tail(L1), L2))
# teste: 		- print(appendL(py2ll([2, 3, 8, 17, 21, 51]), py2ll([7, 23, 56])))


# função que recebe uma lista l e retorna uma nova lista com os elementos L ordenados em ordem ascendente
# QuickSort:
def qSortL(L):
    if not L:
        return None
    else:
        H = head(L)
        T = tail(L)
        Smalls = qSortL(filterL(T, (lambda x: x < H)))
        Bigs = qSortL(filterL(T, lambda x: x >= H))
        return appendL(appendL(Smalls, (H, None)), Bigs)
# teste: 		- print(qSortL(py2ll([5, 9, 14, 22, 1, 43, 12])))


# função para colocar a primeira letra de cada palavra em maiúscula
def capitalize(L):
    return mapL(L, lambda x: x.capitalize())
# teste:        - print(capitalize(py2ll(["abacate", "banana", "chuchu"])))


# função para retornar apenas a primeira letra de cada palavra em maiúscula
def firstLetter(L):
    return mapL(L, lambda x: x[0].capitalize())
# teste:        - print(firstLetter(py2ll(["abacate", "banana", "chuchu"])))


# função Reduce:
# teste com strings:
    # print(reduce((lambda acc, x: acc + ";" + x),
    #       ["abacate", "banana", "chuchu"]))
#  teste com ints:
    # print(reduce(lambda a, b: a*b, [1, 2, 3, 4, 5]))


# inicializador
if __name__ == "__main__":
    print("Hey!")
