from itertools import dropwhile, takewhile, count, cycle, product
# lembrar que as fnções de itertools sempre retornam iteradores,
# logo é preciso informar que tipo de dado que você quer apresentar, ex: list


# função que exclui os dados que retornam true na condição do lambda
def dropWhileEx(L):
    return list(dropwhile(lambda n: n > 0, L))
# teste      -print(dropWhileEx([6, 4, 2, 0, -2, -4]))


# função que traz os dados que retornam true na condição do lambda
def takeWhileEx(L):
    return list(takewhile(lambda n: n > 0, L))
# teste      -print(takeWhileEx([6, 4, 2, 0, -2, -4]))


# função que recebe um iterador para um arquivo,
# uma string de partida e uma string de parada, retornando todas as linhas
def readChapter(fileName, chapterNum):
    sStr = "Chapter " + str(chapterNum)
    eStr = "Chapter " + str(chapterNum + 1)
    with open(fileName) as filter:
        InIter = extractText(filter, sStr, eStr)
        for l in InIter:
            print(l)
# teste		-readChapter("./textExample.txt", 2)
# esse código está na considerada "Avaliação Preguiçosa"(Lazy evaluation),
# pois ele lê até onde as condições são satisfeitas


# Segunda versão da função acima, desta vez lendo o txt inteiro
def readChapter2(fileName, chapterNum):
    sStr = "Chapter " + str(chapterNum)
    eStr = "Chapter " + str(chapterNum + 1)
    with open(fileName) as filter:
        InIter = extractText(filter.readlines(), sStr, eStr)
        for l in InIter:
            print(l)
# teste		-readChapter2("./textExample.txt", 2)


# função para separar o texto
def extractText(lines, startStr, endStr):
    def edCond(x): return not x.startswith(endStr)
    def stCond(x): return not x.startswith(startStr)
    return takewhile(edCond, dropwhile(stCond, lines))


# teste de tempo entre a avaliação preguiçosa e a interação do texto inteiro
def testReadFile(title, readFile, fileName, chapterNum):
    from timeit import default_timer as timer
    start = timer()
    readFile(fileName, chapterNum)
    end = timer()
    print(title, end - start)
# teste 		- testReadFile("Lazy", readChapter, "./textExample.txt", 2)
# 				- testReadFile("Strict", readChapter2, "./textExample.txt", 2)


# função para teste de count
def sumIter():
    l = takewhile(lambda e: e < 10, count(1))
    return list(l)
# teste: 	-print(sumIter())


# função para teste de cycle
def sumIter2():
    return list(takewhile(lambda e: e.isupper(), cycle("Amor")))
# teste: 	-print(sumIter2())


# funcao para determinar dias de plantões de profissionais de acordo com o dia da semana e períodos de trabalho
# a funcao retorna os profissionais ciclados de acordo com o turno em formato csv
def plantao2csv():
    dias = ("Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom")
    periodos = ("D", "N")
    profs = ["Nilton", "Alberto", "Galileu", "Luiz"]
    turnos = product(dias, periodos)
    plantoes = list(zip(turnos, cycle(profs)))
    platoesFlat = ([(a, b, c) for (a, b), c in plantoes])
    for (a, b, c) in platoesFlat:
        print("%s, %s, %s" % (a, b, c))
# teste 	-plantao2csv()


# inicializador
if __name__ == "__main__":
    plantao2csv()
