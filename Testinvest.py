def comparePayoffs(amount, rate, monthly):
    month = 0
    year = 0
    while amount > 0:
        amount = amount - monthly
        print()
        monthly = monthly * (rate / 100 / 12)
        month = month + 1
        if month == 12:
            year = year + 1
            month = 0
        print(amount)
    if amount <= 0:
        return(year, month)


print(comparePayoffs(60000, 5, 500))
