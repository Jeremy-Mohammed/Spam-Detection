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

Name = raw_input(" What is your name?")
Num = raw_input("Please input a positive integer")
Num = int(Num)

while Num >0:
    Name = Name + "!"
    Num -=1

print Name