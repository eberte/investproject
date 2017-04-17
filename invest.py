import turtle
import matplotlib.pyplot as pyplot

initial = input("initial balance in retirement account")
currentAge = input("current age of investor")
retireAge = input("desired age for retirement")
rate = input("expected nominal annual rate of return on the investment")
monthly1 = input("a monthly investment ammount")
monthly2 = input("another monthly investment ammount")


def compareInvestments(initial, currentAge, retireAge,
                       rate, monthly1, monthly2):
    monthlyRate = rate/100/12
    monthsRunning = (retireAge - currentAge)*12
    amount1 = monthly1 + (initial*(1 + monthlyRate))
    amount2 = monthly2 + (initial*(1 + monthlyRate))
    amountList1 = []
    amountList2 = []
    amountList1.append(amount1)
    amountList2.append(amount2)
    for i in range(monthsRunning):
        amount1 = monthly1 + ((1 + monthlyRate)*(amount1))
        amount2 = monthly2 + ((1 + monthlyRate)*(amount2))
        amountList1.append(amount1)
        amountList2.append(amount2)
    # The plot
    pyplot.plot(range(monthsRunning + 1), amountList1)
    pyplot.plot(range(monthsRunning + 1), amountList2)
    pyplot.xlabel("Age")
    pyplot.ylabel("Account balance")
    pyplot.show()
    # The return paragraph
    return ("The final balance from investing %g per month: %g. The final balance from investing %g per month: %g"
            % (monthly1, amount1, monthly2, amount2))


string = compareInvestments(int(initial), int(currentAge), int(retireAge),
                            float(rate), int(monthly1), int(monthly2))
print(string)
