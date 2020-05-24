# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#MIT6.001 ps1-c
def saving(portion_saved, annual_salary, semi_annual_raise=0.07, r=0.04, 
           total_cost=1000000, portion_down_payment=0.25):
    portion_saved=portion_saved/10000.0
    current_saving=0
    for month in range(0,36):
        if month%6==0 and month!=0:
            annual_salary=annual_salary*(1+semi_annual_raise)
        else:
            pass
        current_saving = current_saving *(1+r/12) + annual_salary/12*portion_saved
    return current_saving
        
annual_salary=float(input("Enter your annual salary: "))
#portion_saved=float(input("Enter portion of your salary you can save: "))
total_cost=1000000 #float(input("Enter your dream house total cost: "))
semi_annual_raise=0.07 #float(input("Enter Semi-annual raise: "))

portion_down_payment=0.25
current_saving=0
r=0.04 #annual_rate
#monthly_salary=annual_salary/12

steps_bisection=1
min_p=0
max_p=10000
med_p=(min_p+max_p)//2

if total_cost*portion_down_payment-saving(max_p, annual_salary, semi_annual_raise, r, 
           total_cost, portion_down_payment)>100:
    print("It is not possible to pay the down-pay in 3 years.")
else:
    while abs(saving(med_p, annual_salary)-total_cost*portion_down_payment)>=100:
        if saving(med_p, annual_salary)>total_cost*portion_down_payment:
            max_p=med_p
        else:
            min_p=med_p
        med_p=(min_p+max_p)//2
        steps_bisection+=1
        
    print("Best saving rate: {}".format(med_p/10000))
    print("Steps in bisection search: {}".format(steps_bisection))
