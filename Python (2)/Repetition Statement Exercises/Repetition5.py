#-------------------------------------------------------------------------------
# Name:        Reptition5
# Purpose:
#
# Author:      s201016279
#
# Created:     19/04/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Num = raw_input("How many marks are being inputted?")
Num = int(Num)
Num2 = Num
total = 0

while (Num >0):
    mark = raw_input("What is your mark?")
    mark = int(mark)
    total = total + mark
    Num -=1

print("The average is " + str(total/Num2))