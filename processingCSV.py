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


# função pra retornar um par de ano e número de gols
def year2Goals(data):
    return lambda year: (year, countGoals(filterYear(year)(data)))


# função pra fazer o mapeamento dos gols por ano
def mapYear2Goals(data):
    listData = list(data)
    years = range(2003, 2022)
    return map(year2Goals(listData), years)
# teste  -show('mapYear2Goals', './campeonato-brasileiro-full.csv', mapYear2Goals)


# função alinhada unindo as duas funções acima
def mapYear2Goals2(data):
    listData = list(data)

    def year2Goals(year): return \
        (year, countGoals(filterYear(year)(listData)))
    years = range(2003, 2022)
    return map(year2Goals, years)
#teste  -show('mapYear2Goals', './campeonato-brasileiro-full.csv', mapYear2Goals2)


# mesma função acima, mas com uma abordagem diferente
def countGoalsPerYear(data):
    return lambda listGoals, year: \
        listGoals + [(year, countGoals(filterYear(year)(data)))]


# continução, agora usando reduce
def goalsPerYear(data):
    listdata = list(data)
    years = range(2003, 2022)
    return reduce(countGoalsPerYear(listdata), years, [])
# teste   -show('goalsPerYear', './campeonato-brasileiro-full.csv',goalsPerYear)


# função para extrair os nomes do CSV
def extractTeam(teamSet, match):
    teamName = match['mandante']
    teamSet.add(teamName)
    return teamSet


# função allteams que encontra todos os times que já jogaram alguma edição do Brasileirão
def allTeams(d):
    return reduce(extractTeam, d, set())
# teste   -show('AllTeams', './campeonato-brasileiro-full.csv', allTeams)


# função que encontra o número total de gols que foram marcados por um dado time
def goalsOfTeam(team, data):
    def goalsOfTeamAux(match):
        if match['mandante'] == team:
            return int(match['mandante_placar'])
        elif match['visitante'] == team:
            return int(match['visitante_placar'])
        else:
            return 0
    numOfGoals = map(goalsOfTeamAux, data)
    return reduce(lambda a, b: a+b, numOfGoals, 0)


# auxiliar para reduzir a função a apenas uma variável chamada,
# onde a segunda ficará implícita no lambda da função que será invocada
# nesse caso, o que temos é uma função currificada
def auxGoalsOfTeam(team):
    return lambda data: goalsOfTeam(team, data)


# função para fazer uma lista de pares de um time e a quantidade de gols totais
# marcados, em ordem decrescente.
def allGoalsPerTeam(data):
    dataList = list(data)
    teams = allTeams(dataList)

    def mapper(data):
        return lambda team: (team, goalsOfTeam(team, data))

    goalsPerTeam = list(map(mapper(dataList), teams))
    goalsPerTeam.sort(key=lambda e: e[1], reverse=True)
    return goalsPerTeam
# teste     -show('goalsOfTeams', './campeonato-brasileiro-full.csv',allGoalsPerTeam)


# inicializador
if __name__ == "__main__":
    show('goalsOfTeams', './campeonato-brasileiro-full.csv',
         allGoalsPerTeam)
