def comparePayoffs(amount, rate, monthly):
    month = 0
    year = 0
    while amount >= 0:
        amount = amount - monthly
        print(amount)
        monthly = monthly * (rate / 100 / 12)
        print(monthly)
        month = month + 1
        if month == 12:
            year = year + 1
            month = 0
    return (year, month)


print(comparePayoffs(60000, 5, 500))
