import matplotlib.pyplot as plt

loan_amount = int(input("Please enter loan amount."))
annual_interest_rate = int(input("Please enter annual interest rate.")) / 100
years = int(input("Please enter number of years."))

months = years * 12
total_payment = loan_amount*((annual_interest_rate + 1)**5)
print("Your monthly payment is:", total_payment/months)

total_interest = total_payment - loan_amount
monthly_loan_payment = loan_amount/months
monthly_interest_payment = total_interest/months

interest_paid = []
principal_balance = []
x = []

for i in range(0, months+1):
    interest_paid.append(total_interest - (monthly_interest_payment*i))
    principal_balance.append(loan_amount - (monthly_loan_payment*i))
    x.append(i)

myFig, myAxes = plt.subplots(1, 2, figsize=(10, 5))
myAxes[0].set_xlabel('Month')
myAxes[0].set_ylabel('Interest paid')
myAxes[1].set_xlabel('Month')
myAxes[1].set_ylabel('Loan Balance')
myAxes[0].plot(x, interest_paid, color="b")
myAxes[1].plot(x, principal_balance, color="b")
plt.show()
