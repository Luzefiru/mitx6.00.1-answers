balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12.0
monthly_pay = 10

while True:
    test_balance = balance
    for i in range(12):
        unpaid_balance = test_balance - monthly_pay
        test_balance = unpaid_balance + (unpaid_balance*monthlyInterestRate)
    if test_balance <= 0: break
    monthly_pay += 10

print('Lowest Payment: ', monthly_pay)