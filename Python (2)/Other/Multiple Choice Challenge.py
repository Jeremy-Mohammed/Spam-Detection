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


print("Welcome to the Basic Canadian Knowledge quiz!")
name = raw_input("What is your name?")
print("Good luck " + name + "!!")
print(" ")

Score = 0

#Q1
while True:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Calgary")
    print("2. Toronto")
    print("3. Manitoba")
    print("4. Ottawa")
    Cap = raw_input("What is the capital of Canada?")
    try:
            Cap = int(Cap)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Cap == 4:
        Score += 1
        break
    elif Cap >=1 and Cap <5:
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

#Q2
while True:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. 100 Years old")
    print("2. 150 Years old")
    print("3. 200 Years old")
    print("4. 148 Years old")
    Year = raw_input("How old is Canada as of its birthday in 2017?")
    try:
            Year = int(Year)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Year == 2:
        Score += 1
        break
    elif Year >=1 and Year <5:
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

#Q3
while True:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. British Columbia")
    print("2. Ontario")
    print("3. Quebec")
    print("4. Nunavut")
    Size = raw_input("What is Canada's largest province/territory?")
    try:
            Size = int(Size)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Size == 4:
        Score += 1
        break
    elif Size >=1 and Size <5:
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue
#Q4
while True:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. 35.5 Million")
    print("2. 32.5 Million")
    print("3. 36.5 Million")
    print("4. 37.5 Million")
    Pop = raw_input("What is the approximate population of Canada in January 2017?")
    try:
            Pop = int(Pop)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Pop == 3:
        Score += 1
        break
    elif Pop >=1 and Pop <5:
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue
#Q5
while True:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Ontario")
    print("2. Quebec")
    print("3. British Columbia")
    print("4. New Brunswick")
    PopPT = raw_input("Which province/territory has the highest population?")
    try:
            PopPT = int(PopPT)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if PopPT == 1:
        Score += 1
        break
    elif PopPT >=1 and PopPT <5:
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue
#Q6
while True:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Yukon")
    print("2. Nunavut")
    print("3. Newfoundland and Labrador")
    print("4. Northwest Territories")
    North = raw_input("What is the most northern province/territory?")
    try:
            North = int(North)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if North == 2:
        Score += 1
        break
    elif North >=1 and North <5:
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue
#Q7
while True:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Yukon")
    print("2. Manitoba")
    print("3. New Brunswick")
    print("4. Nova Scotia")
    West = raw_input("What is the most western province/territory?")
    try:
            West = int(West)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if West == 1:
        Score += 1
        break
    elif West >=1 and West <5:
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue
#Q8
while True:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Saskatchewan")
    print("2. Manitoba")
    print("3. Newfoundland and Labrador")
    print("4. Alberta")
    East = raw_input("What is the most eastern province/territory?")
    try:
            East = int(East)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if East == 3:
        Score += 1
        break
    elif East >=1 and East <5:
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue
#Q9
while True:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. 1973")
    print("2. 2001")
    print("3. 1867")
    print("4. 1999")
    Nun = raw_input("What year did Nunavut become a part of Canada?")
    try:
            Nun = int(Nun)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Nun == 4:
        Score += 1
        break
    elif Nun >=1 and Nun <5:
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue
#Q10
while True:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Ontario, Newfoundland and Labrador, Nova Scotia, Manitoba")
    print("2. New Brunswick, Ontario, Nova Scotia, Quebec")
    print("3. Manitoba, Alberta, Ontario, Saskatchewan")
    print("4. Ontario, Saskatchewan, Nunavut, British Columbia")
    First = raw_input("What were the first four provinces/territories of Canada?")
    try:
            First = int(First)

    except:
        print(" ")
        print("That is not a valid answer!")
        ccontinue
    if First == 2:
        Score += 1
        break
    elif First >=1 and First <5:
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

print(" ")
print(" ")
print("You've finished the quiz " + name +"!")
if Score ==10:
    print("Perfect! You got a score of 10/10!!")
    print("A+")

elif Score ==9:
    print("Amazing job! You got a score of 9/10!")
    print("A")

elif Score ==8:
    print("Great job! You got a score of 8/10!")
    print("A-")

elif Score ==7:
    print("Good job! You got a score of 7/10!")
    print("B")

elif Score ==6:
    print("You got a score of 6/10!")
    print("C")

elif Score ==5:
    print("You got a score of 5/10.")
    print("D")

else:
    print("You got a score of " + str(Score)+ "/10")
    print("F")