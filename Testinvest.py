import matplotlib.pyplot as pyplot


def comparePayoffs(amount, rate, monthly1, monthly2):
    amount2 = amount
    month1 = 0
    year1 = 0
    month2 = 0
    year2 = 0
    AmountList1 = []
    AmountList2 = []
    while amount >= 0:
        AmountList1.append(amount)
        amount = amount * (1 + (rate / 100 / 12)) - monthly1
        month1 = month1 + 1
        if month1 == 12:
            year1 = year1 + 1
            month1 = 0
    while amount2 >= 0:
        AmountList2.append(amount2)
        amount2 = amount2 * (1 + (rate / 100 / 12)) - monthly2
        month2 = month2 + 1
        if month2 == 12:
            year2 = year2 + 1
            month2 = 0
    if year1 > year2:
        year3 = year1 - year2
    else:
        year3 = year2 - year1
    if month1 > month2:
        month3 = month1 - month2
    else:
        month3 = month2 - month1
    if monthly1 > monthly2:
        monthly3 = monthly1 - monthly2
    else:
        monthly3 = monthly2 - monthly1
    print('If you pay %g per month, the reypament period will be %g years and \
          %g months.' % (monthly1, year1, month1))
    print('If you pay %g per month, the reypament period will be %g years and \
          %g months.' % (monthly2, year2, month2))
    print('If you pay %g more per month, the repayment period will be %g years \
          and %g months shorter.' % (monthly3, year3, month3))
    print(len(range(year1)))
    print(len(AmountList1))
    print(len(AmountList2))
    pyplot.plot(range(len(AmountList1)), AmountList1)
    pyplot.plot(range(len(AmountList2)), AmountList2)
    pyplot.xlabel('Months')
    pyplot.ylabel('Amount Balance ($)')
    pyplot.show()


comparePayoffs(60000, 5, 500, 750)
