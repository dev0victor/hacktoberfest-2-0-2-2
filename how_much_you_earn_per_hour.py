# -*- coding: utf-8 -*-
"""
Make a program that asks how much you earn per hour and the number of hours worked in the month.
Calculate and show the total of your salary in that month, knowing that 11% is deducted for Income Tax,
8% for the INSS and 5% for the union, make a program that gives us the gross salary, how much you paid to the INSS, how much he paid to the union and the net salary.
Note that Gross Salary - Discounts = Net Salary. Calculate deductions and net salary,
"""
hour_price = int(input("How much do you earn per hour? "))
hours_worked = int(input("How many hours did you work this month? "))

gross_salary = hour_price * hours_worked
    
iR = (11*gross_salary)//100
    
iNSS = (8*gross_salary)//100
    
union = (5*gross_salary) //100
    
net_salary = gross_salary - iR - iNSS - union

print("The salary is: BRL %.2f" %net_salary)