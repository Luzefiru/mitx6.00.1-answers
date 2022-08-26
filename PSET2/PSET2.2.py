balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0
monthly_pay = 10

viable = False
while viable == False:
    test_balance = balance
    for i in range(12):
        unpaid_balance = test_balance - monthly_pay
        test_balance = unpaid_balance + (unpaid_balance*monthlyInterestRate)
        # print('Month', i+1, 'Remaining balance', round(test_balance, 2))
    if test_balance > 0:
        # print('not viable')
        monthly_pay += 10
    elif test_balance <= 0:
        # print('viable!')
        viable = True

print('Lowest Payment: ', monthly_pay)