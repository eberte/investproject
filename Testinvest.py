def comparePayoffs(amount, rate, monthly1, monthly2):
    amount2 = amount
    month1 = 0
    year1 = 0
    month2 = 0
    year2 = 0
    while amount >= 0:
        amount = amount * (1 + (rate / 100 / 12)) - monthly1
        month1 = month1 + 1
        if month1 == 12:
            year1 = year1 + 1
            month1 = 0
    while amount2 >= 0:
        amount2 = amount2 * (1 + (rate / 100 / 12)) - monthly2
        month2 = month2 + 1
        if month2 == 12:
            year2 = year2 + 1
            month2 = 0
    return [(year1, month1), (year2, month2)]


print(comparePayoffs(60000, 5, 500, 750))
