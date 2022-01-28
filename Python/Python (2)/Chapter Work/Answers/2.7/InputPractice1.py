#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      s201016279
#
# Created:     04/04/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

name = raw_input("What is your first and last name?")
street = raw_input("What is your street number, name, and type?")
city = raw_input("What city do you live in?")
province = raw_input("What province/state/territory do you live in?")
postal = raw_input("What is your postal code?")
print("     ") + (name)
print(street) + (", ") + (city) + (", ") + (province)
print("         ") + (postal)

