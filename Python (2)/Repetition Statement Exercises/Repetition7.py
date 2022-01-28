#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      s201016279
#
# Created:     20/04/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import randint
num=randint(1,100)
Guess = 0

while Guess !=num:
    Guess = raw_input("What do you think the number is?")
    Guess = int(Guess)
    if Guess >num:
        print("Your guess is too high!")

    elif Guess <num:
        print("Your guess is too low!")

    elif Guess ==num:
        print("You've guessed the number right number of " +str(num) + "!")
        break





