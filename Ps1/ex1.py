total_cost = float(input("Enter the price of the dream home:"))
annual_salary = float(input("Enter the annual salary:"))
portion_saved = float(input("Enter how much of the salary will be saved for the downpayment(using the format 0.x):"))
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
months = 0
while current_savings < portion_down_payment:
    current_savings = current_savings*r/12 + current_savings + portion_saved * annual_salary/12
    months = months + 1
print(months)