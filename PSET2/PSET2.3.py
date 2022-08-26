balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12.0

lowerbound = balance/12
upperbound = (balance * (1 + monthlyInterestRate)**12)/12

# print(lowerbound, upperbound)

while True:
    test_balance = balance
    monthly_pay = (lowerbound + upperbound)/2
    print('Payment:', monthly_pay)
    for i in range(12):
        unpaid_balance = test_balance - monthly_pay
        test_balance = unpaid_balance + (unpaid_balance*monthlyInterestRate)
        print('Monthly Balance: ', test_balance)
    if abs(test_balance) <= 0.01: break
    elif test_balance > 0: lowerbound = monthly_pay
    else: upperbound = monthly_pay

print('Lowest Payment: ', round(monthly_pay, 2))