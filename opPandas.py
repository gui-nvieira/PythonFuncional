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


# inicializador
if __name__ == "__main__":
    countGoalsPerStadium(df0)
