#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      s201016279
#
# Created:     10/04/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
weight = raw_input("What is your weight in kilograms?")
height = raw_input("What is your height in metres?")
weight = float(weight)
height = float(height)

BMI = weight/(height*height)

if BMI >=30:
    print("Your BMI is obese.")

elif BMI >=25:
    print("Your BMI is overweight.")

elif BMI >=18.5:
    print("Your BMI is normal weight.")

elif BMI <18.5:
    print("Your BMI is underweight.")