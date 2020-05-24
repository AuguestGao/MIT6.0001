# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#part a
annual_salary=float(input("Enter your annual salary: "))
portion_saved=float(input("Enter portion of your salary you can save: "))
total_cost=float(input("Enter your dream house total cost: "))

portion_down_payment=0.25
current_saving=0
r=0.04 #annual_rate
monthly_salary=annual_salary/12
month=0

while current_saving < portion_down_payment*total_cost:
    current_saving = current_saving + current_saving*r/12 + monthly_salary*portion_saved
    month=month+1
    
print("\nNeed {} months to pay Down Payment!".format(month))

#part b