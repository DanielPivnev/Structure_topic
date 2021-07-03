companies = []
incomes = []
sentences = [['Companies with higher year income than average year income: '],
             ['Companies with exactly year income than average year income: '],
             ['Companies with lower year income than average year income: ']]
average_year_income = 0


for i in range(int(input('Enter the amount of companies: '))):
    companies.append(input(f'Enter the name of {i + 1}. company: '))
    incomes.append(list(input('Enter the income the quarters in millions: ').split()))
    year_income = 0
    for j in range(len(incomes[i])):
        incomes[i][j] = float(incomes[i][j])
        year_income += incomes[i][j]
    incomes[i].append(year_income)

for i in range(len(incomes)):
    average_year_income += incomes[i][4]
average_year_income /= 4

for i in range(len(incomes)):
    if incomes[i][4] > average_year_income:
        sentences[0].append(companies[i])
    elif incomes[i][4] == average_year_income:
        sentences[1].append(companies[i])
    else:
        sentences[2].append(companies[i])

print('\n' + '-'*60)
for i in range(len(sentences)):
    if len(sentences[i]) > 1:
        print(sentences[i][0])
        for j in range(1, len(sentences[i])):
            print(f'- {sentences[i][j]}')
        print()
