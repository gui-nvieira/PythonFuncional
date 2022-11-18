# função para receber uma string e transformar em uma lista de caracteres em ordem
def str2List(name):
    return [letter for letter in name]


# inicializador
if __name__ == "__main__":
    print(str2List('Fluminense'))
