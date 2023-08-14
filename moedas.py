money = round(float(input()), 2)

notesAndCoins = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
notesAndCoins_quantity = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
j = 0


def verify_money(totalValue, noteValue):
    i = 0
    while totalValue >= noteValue:
        totalValue -= noteValue
        totalValue = round(totalValue, 2)
        i += 1

    return totalValue, i


for value in notesAndCoins:
    money, notesAndCoins_quantity[j] = verify_money(money, value)
    j += 1


j = 0
for quantity in notesAndCoins_quantity:
    moneyType = notesAndCoins[j]
    if j == 0:
        print("NOTAS:")

    if j == 6:
        print("MOEDAS:")

    if j < 6:
        answer = "{} nota(s) de R$ {:.2f}"
        print(answer.format(quantity, float(moneyType)))

    else:
        answer = "{} moeda(s) de R$ {:.2f}"
        print(answer.format(quantity, float(moneyType)))

    j += 1
