import calendar

def calculate_emi(principal, tenure, interest_rate):
    monthly_interest_rate = interest_rate / 12 / 100
    total_months = tenure * 12
    emi = (principal * monthly_interest_rate * pow(1 + monthly_interest_rate, total_months)) / (pow(1 + monthly_interest_rate, total_months) - 1)
    return emi

principal_amount = float(input("Enter the principal amount: "))
tenure_years = int(input("Enter the tenure in years: "))
interest_rate = float(input("Enter the interest rate (%): "))

emi = calculate_emi(principal_amount, tenure_years, interest_rate)

total_payment = 0
balance = principal_amount
total_principal = 0
total_interest = 0
total_loan_paid = 0

print("\nYear\tMonth Name\tPrincipal (A)\tInterest (B)\tTotal Payment (A+B)\tBalance\t\tLoan Paid (%)")

for year in range(1, tenure_years + 1):
    for month in range(1, 13):
        interest = balance * (interest_rate / 100 / 12)
        principal = emi - interest
        balance -= principal
        total_payment += emi
        total_principal += principal
        total_interest += interest
        total_loan_paid = (total_principal / principal_amount) * 100
        month_name = calendar.month_name[month]
        print(f"{year}\t{month_name[:3]}\t\t{principal:.2f}\t\t{interest:.2f}\t\t{emi:.2f}\t\t\t{balance:.2f}\t\t{total_loan_paid:.2f}")
        if balance <= 0:
            break
    else:
        continue
    break

print("\nTotal Principal: {:.2f}".format(total_principal))
print("Total Interest: {:.2f}".format(total_interest))
print("Total Payment: {:.2f}".format(total_payment))
print("Remaining Balance: {:.2f}".format(balance))
print("Loan Paid (%): {:.2f}".format(total_loan_paid))
