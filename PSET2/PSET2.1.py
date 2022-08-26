balance = 381
annualInterestRate = 0.12
monthlyPaymentRate = 0.05

monthlyInterestRate = annualInterestRate/12

for i in range(12):
    minpay = balance * monthlyPaymentRate
    unpaid_balance = balance - minpay
    balance = unpaid_balance + (unpaid_balance*monthlyInterestRate)

    # print('Month', i+1, 'Remaining balance', round(balance, 2))

print('Remaining balance: ', round(balance, 2))