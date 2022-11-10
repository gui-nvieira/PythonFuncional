
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


# inicializador
if __name__ == "__main__":
    print(ll2py(mSort(py2ll([81, 4, 6, 8, 10]))))
