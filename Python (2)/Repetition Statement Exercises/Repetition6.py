#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      s201016279
#
# Created:     19/04/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
while True:
    Num = raw_input("Please enter a number between 1 and 7 only")
    Num = int(Num)

    if Num ==1:
        print("The day of the week is Sunday")

    elif Num ==2:
        print("The day of the week is Monday")

    elif Num ==3:
        print("The day of the week is Tuesday")

    elif Num ==4:
        print("The day of the week is Wednesday")

    elif Num ==5:
        print("The day of the week is Thursday")

    elif Num ==6:
        print("The day of the week is Friday")

    elif Num ==7:
        print("The day of the week is Saturday")

    else:
        print("Invalid Input")

    Con = raw_input("Would you like to try again?")
    if Con =="yes"or Con == "Yes":
        continue
    else:
        break


print("Have a nice day!")







