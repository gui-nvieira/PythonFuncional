# função para receber uma string e transformar em uma lista de caracteres em ordem
def str2List(name):
    return [letter for letter in name]
# teste:     -print(str2List(('Fluminense')))


# função que recebe uma string e transforma em uma lista que contenha somente os caracteres maiúsculos
def up2List(name):
    return [letter for letter in name if letter.isupper()]
# teste       -print(up2List(('Fluminense, Bahia')))


# função que capitaliza todos os chars
def letters2CapList(name):
    return [letter.upper() for letter in name if letter.isalpha()]
# teste       -print(letters2CapList(('Fluminense, Bahia')))


# função com maps e filters para retornar apenas as letras minúsculas de uma string, capitalizadas
def lowLet2CapList1(s):
    L0 = filter(lambda x: x.isalpha(), s)
    L1 = filter(lambda y: y.islower(), L0)
    return list(map(lambda z: z.upper(), L1))
# teste       -print(lowLet2CapList1(('Fluminense Bahia')))


# Mesma função acima, porém utiizando compreensão de listas
def lowLet2CapList(s):
    return [letter.upper() for letter in s if letter.isalpha() and letter.islower()]
# teste       -print(lowLet2CapList(('Fluminense Bahia')))


# função que inverte a caixa das letras presentes em uma string
def invCase(name):
    return [letter.upper() if letter.islower() else letter.lower() for letter in name if letter.isalpha()]
# teste       -print(invCase(('Fluminense Bahia')))


# Função que transpõe uma matriz
def traspMatrix(matrix):
    NUM_ROW = len(matrix[0])
    return [[row[i] for row in matrix] for i in range(NUM_ROW)]
#teste		-print(traspMatrix([[0, 1], [2, 3], [3, 4]]))


# inicializador
if __name__ == "__main__":
    print(traspMatrix([[0, 1], [2, 3], [3, 4]]))
