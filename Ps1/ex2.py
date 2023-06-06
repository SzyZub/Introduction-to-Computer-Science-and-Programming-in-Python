annual_salary = float(input("Enter the annual salary:"))
portion_saved = float(input("Enter how much of the salary will be saved for the downpayment as a fraction of it(using the format 0.x):"))
total_cost = float(input("Enter the price of the dream home:"))
semi_annual_raise = float(input("Enter a semi annual raise as a decimal percentage of the salary(using the format 0.x):"))
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
months = 0
while current_savings < portion_down_payment:
    current_savings = current_savings*r/12 + current_savings + portion_saved * annual_salary/12
    if  months % 6 == 0 and months > 0:
        annual_salary = annual_salary + annual_salary * semi_annual_raise
    months = months + 1
print(months)
