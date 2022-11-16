import csv
from functools import reduce


# função de visualização dos valores tratados
def show(title, fileName, f):
    print('---- '+title+' ----')
    with open(fileName, 'r', encoding='utf-8') as file:
        data = csv.DictReader(file)
        newData = f(data)
        try:
            iterator = iter(newData)
        except TypeError:
            print(newData)
        else:
            for row in newData:
                print((row))


# função para retornar todos os dados que incluem um termo dentro de certas colunas, nesse caso é um time
def getTeam(team):
    return lambda data: filter(lambda e: e['mandante'] == team or e['visitante'] == team, data)
# teste     -show('getTeam', './campeonato-brasileiro-full.csv', getTeam('Fluminense'))


# função para retornar o ano de cada jogo
def getYear(match):
    dateStr = match['data']
    yearStr = dateStr[:4]
    return int(yearStr)


# função para adicionar ano em uma cópia do dicionário original
def addYearField(match):
    newMatch = dict(match)
    newMatch['ano'] = getYear(match)
    return newMatch


# função para criar o novo dict, usando o getYear
def addYear(data): return map(addYearField, data)
# teste   -show('addYear', './campeonato-brasileiro-full.csv', addYear)


# função para mapear a sequencia de jogos em uma lista de gols
def match2goals(d):
    return map(lambda e: int(e['mandante_placar']) + int(e['visitante_placar']), d)


# função para contar o número de gols totais no csv
def countGoals(data):
    listGoals = match2goals(data)
    return reduce(lambda acc, e: acc + e, listGoals, 0)
# teste   -show('goals', './campeonato-brasileiro-full.csv', countGoals)


# função para retornar os jogos de um determinado ano
def filterYear(year):
    return lambda data: filter(lambda e: getYear(e) == year, data)
#teste  -show('filterYear', './campeonato-brasileiro-full.csv', filterYear(2005))


# inicializador
if __name__ == "__main__":
    show('filterYear', './campeonato-brasileiro-full.csv', filterYear(2005))
