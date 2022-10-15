# -*- coding: utf-8 -*-
"""
Write a program to calculate the reduction in the lifetime of a smoker. ask
number of cigarettes smoked per day and how many years he has smoked. Consider that a smoker
loses 10 minutes of life with each cigarette, calculate how many days of life a smoker will lose. display the
total days.
"""

cigarettes = int(input("How many cigarettes were smoked per day?" ))

years = int(input("How many years have you smoked?" ))

total_smoked = (years * 365)*cigarettes
loss = (total_smoked*10)/24

print("You will lose %d days of life" %loss)
