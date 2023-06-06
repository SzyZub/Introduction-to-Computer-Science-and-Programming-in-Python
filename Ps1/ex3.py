salary = float(input("Enter the annual salary:"))
def func(x):
    why = 0
    steps = 0
    r = 0.04
    semi_annual_raise = 0.07
    total_cost = 1000000
    portion_down_payment = 0.25 * total_cost
    tab = [0, 10000]
    temp = None
    while why == 0:
        steps = steps + 1
        months_remaining = 36
        annual_salary = x       
        portion_saved = int((tab[1] + tab[0])/2)
        current_savings = 0
        while months_remaining >= 1:
            if months_remaining % 6 == 0 and months_remaining != 36:
                annual_salary = annual_salary + annual_salary * semi_annual_raise
            current_savings = current_savings*r/12 + current_savings + portion_saved/10000 * annual_salary/12
            months_remaining = months_remaining - 1
        if temp == current_savings:
            print("It is not possible to pay the down payment in three years.")
            return
        temp = current_savings
        if current_savings >= portion_down_payment + 100:
            tab[1] = int((tab[1] + tab[0])/2)
        elif current_savings <= portion_down_payment - 100:
            tab[0] = int((tab[1] + tab[0])/2)    
        else:
            savings_rate = portion_saved
            why = 1
        
    print("Best savings rate: ", savings_rate / 10000)
    print("Steps in bisection search: ", steps)
func(salary)
