def comparePayoffs(amount, rate, monthly):
    month = 0
    year = 0
    while amount >= 0:
        amount = amount * (1 + (rate / 100 / 12)) - 500
        month = month + 1
        if month == 12:
            year = year + 1
            month = 0
    return (year, month)


print(comparePayoffs(60000, 5, 750))
