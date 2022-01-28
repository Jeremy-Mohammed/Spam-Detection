#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      s201016279
#
# Created:     03/05/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Personal Info
while True:
    print (" ")
    print ("Please enter your information.")
    print (" ")
    FName = raw_input ("What is your first name?")
    LName = raw_input ("What is your last name?")
    HRTeach = raw_input ("Who is your homeroom teacher?")
    while True:
        HRNum = raw_input ("What is your homeroom number?")
        try:
            HRNum = int(HRNum)
            break

        except:
            print(" ")
            print("Please enter digits only.")
            continue

    Email = raw_input ("What is your E-mail?")

    while True:
        PhNum = raw_input ("What is your phone number?")
        try:
            PhNum = int(PhNum)
            break

        except:
            print(" ")
            print("Please enter digits only.")
            continue

    break