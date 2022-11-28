import pandas as pd


# importando o csv para um variável dataframe df0
df0 = pd.read_csv("./campeonato-brasileiro-full.csv")


# escreva uma função que retorne todos os jogos de um determinado time
def getMatches(matches, team):
    return matches[(matches['mandante'] == team) | (matches['visitante'] == team)]
# teste: 		-print((getMatches(df0, 'Fluminense')).index.size)


# escreva uma função que receba um dataframe e um nome de time e conte quantos gols
# foram marcados pelo time, seja como mandante ou visitante
def countGoals(matches, team):
    goalsM = matches[(matches['mandante'] == team)]['mandante_placar'].sum()
    goalsV = matches[(matches['visitante'] == team)]['visitante_placar'].sum()
    return goalsM + goalsV
# teste:        -print(countGoals(df0, "Fluminense"))


# escrever uma função onde conta os todos os gols de jogos
# em que um determinado time participou do jogo
def countGoalsAll(matches, team):
    fMatches = getMatches(matches, team)
    return fMatches['mandante_placar'].sum() + fMatches['visitante_placar'].sum()
# teste 		-print(countGoalsAll(df0, "Fluminense"))


# Função que retorna todos os estádios sem valores duplicados, onde
# jogos de um determinado time aconteceram
def getAllLocations(matches, team):
    tMatches = getMatches(matches, team)
    return list(tMatches['arena'].drop_duplicates())
#teste 		-print(getAllLocations(df0, "Fluminense"))


# funcao que retorna a quantidade de jogos de um certo time que ocorreu em cada estadio
def getLocationFreq(matches, team):
    tMatches = getMatches(matches, team)
    return tMatches['arena'].value_counts()
# teste 		-print(getLocationFreq(df0, "Fluminense"))


# funcao que imprime quantos gols foram marcados em cada estadio
def countGoalsPerStadium(matches):
    goalsAtStadium = matches.groupby('arena').sum()
    totalGoals = goalsAtStadium['mandante_placar'] + \
        goalsAtStadium['visitante_placar']
    for std in totalGoals.index:
        print("%16s: %d" % (std, totalGoals[std]))
# teste 			-countGoalsPerStadium(df0)


# Função que conta qantos gols foram marcados por um time (com Apply)
def goalsFromTeam(matches, team):
    def countGoals(s):
        if s['mandante'] == team:
            return s['mandante_placar']
        elif s['visitante'] == team:
            return s['visitante_placar']
    return matches.apply(countGoals, axis=1).sum()
#teste      -print(goalsFromTeam(df0, "Fluminense"))


# função que conte vitórias, empates e derrotas de um certo time
def countResults(matches, team):
    def won(s): return s['mandante'] == team and s['mandante_placar'] > s['visitante_placar'] or \
        s['visitante'] == team and s['visitante_placar'] > s['mandante_placar']
    nWins = matches.apply(won, axis=1).sum()

    def draw(s): return s['mandante'] == team and s['mandante_placar'] == s['visitante_placar'] or \
        s['visitante'] == team and s['visitante_placar'] == s['mandante_placar']
    nDraws = matches.apply(draw, axis=1).sum()

    def loss(s): return s['mandante'] == team and s['mandante_placar'] < s['visitante_placar'] or \
        s['visitante'] == team and s['visitante_placar'] < s['mandante_placar']
    nLosses = matches.apply(loss, axis=1).sum()

    return (nWins, nDraws, nLosses)
#teste: 		-print(countResults(df0, "Fluminense"))


# função que conte a quantidade de pontos feitos por um time
def numPoints(matches, team):
    (wins, draws, losses) = countResults(matches, team)
    return (team, 3*wins+draws)
#teste 		-    print(numPoints(df0, "Fluminense"))


# função que retorna os times que participaram do campeonato
def getAllTeams(mts):
    mandantes = mts['mandante']
    visistantes = mts['visitante']
    return pd.concat([mandantes, visistantes]).drop_duplicates()


# função que constrói uma tabela de pontos de todos os campeonatos, ordenado pela quantidade de pontos
def builtFinalResultTable(matches):
    teams = getAllTeams(matches)
    results = [numPoints(matches, team) for team in teams]
    rank = sorted(results, reverse=True, key=lambda x: x[1])
    for (team, points) in rank:
        print("%s: %d" % (team, points))
# teste 		-    print(builtFinalResultTable(df0))


# inicializador
if __name__ == "__main__":
    print(builtFinalResultTable(df0))
