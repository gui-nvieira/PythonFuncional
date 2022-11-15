import csv

file = open('./campeonato-brasileiro-full.csv', 'r', encoding='utf-8')
data = csv.reader(file)

for row in data:
    print(row)


# função de teste
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
