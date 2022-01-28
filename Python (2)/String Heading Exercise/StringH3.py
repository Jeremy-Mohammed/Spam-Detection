#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      s201016279
#
# Created:     02/05/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
first = raw_input ("What is your first name?")
middle = raw_input ("What is your middle name?")
last = raw_input ("What is your last name?")
first = first.strip()
middle = middle.strip()
last = middle.strip()

while True:
    print ("Please input the letter before the option.")
    print ("a. Print the length of my name")
    print ("b. Print my initials")
    print ("c. Exit")
    De = raw_input ("Which option would you like?")
    if De == "a" or De == "A":
        print len(first)
        print len(middle)
        print len(last)

    elif De == "b" or De == "B":
        print first[0]
        print middle[0]
        print last [0]

    if De == "c" or De == "C":
        break

print("Goodbye")