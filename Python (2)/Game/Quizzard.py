#-------------------------------------------------------------------------------
# Name:        Quizzard
# Purpose:     Fun random quiz game with a potential prize!
#
# Author:      s201016279
#
# Created:     25/04/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Introduction to Game
print ("Welcome to The Greatest Trivia game, Quizzard presented to you by Kurlysha.co")
Name = raw_input ("What is your name?")
print ("Let's begin ") +(Name) + (".")
print ("There are 10 questions, that will be given to you randomly. Questions closer to 1 are easy, questions closer to 10 are difficult.")
print ("You could win up to $3000!")
print (" ")

#Estimate Win
while True:
    Estimate = raw_input ("How much do you think you will win?")
    try:
        Estimate = int(Estimate)

    except:
        print(" ")
        print("That is not a valid number!")
        continue
    if Estimate >3000:
        print("You cannot win over $3000!")
        continue
    elif Estimate >=2000:
        print("$") + str(Estimate) + (" is a high estimate!")
        break
    elif Estimate >=1000:
        print("$") + str(Estimate) + (" is a good estimate!")
        break
    elif Estimate >=1:
        print("You think you'll only win $") +str(Estimate) + ("!? Well, good luck!")
        break
    else:
        print("You think you won't win anything?! You should be more confident!")
        break

#Start
print ("Let's Begin.")

#Winnings
Mon = 0

#Q1
while True:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Ajax")
    print("2. Montreal")
    print("3. Toronto")
    print("4. Markham")
    Q1 = raw_input("What is the capital of Ontario?")
    try:
            Q1 = int(Q1)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Q1 == 3:
        Mon += 100
        print("Correct!")
        break
    elif Q1 != 3:
        print("Sorry that's not the answer! You have lost all of your earnings, good try. :(")
        print("The correct answer is 3. Toronto")
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

#Q2
while Q1 == 3:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Great Slave Lake")
    print("2. Lake Superior")
    print("3. Lake Ontario")
    print("4. Great Bear Lake")
    Q2 = raw_input("What is the largest lake in Canada?")
    try:
            Q2 = int(Q2)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Q2 == 4:
        Mon += 100
        print("Correct!")
        break
    elif Q2 != 4:
        print("Sorry that's not the answer! You have lost all of your earnings, good try. :(")
        print("The correct answer is 4. Great Bear Lake")
        Mon -= 100
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

#Q3
while Q1 == 3 and Q2 == 4 :
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Mars")
    print("2. Earth")
    print("3. Jupiter")
    print("4. Saturn")
    Q3 = raw_input("Name the fourth planet farthest from the sun planet in the solar system.")
    try:
            Q3 = int(Q3)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Q3 == 1:
        Mon += 200
        print("Correct!")
        break
    elif Q3 != 1:
        print("Sorry that's not the answer! You have lost all of your earnings, good try. :(")
        print("The correct answer is 1. Mars")
        Mon -= 200
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

#Q4
while Q1 == 3 and Q2 == 4 and Q3 == 1:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Alexander Graham Bell")
    print("2. Thomas Edison")
    print("3. Albert Einstein")
    print("4. Erick Hassin")
    Q4 = raw_input("Who invented the lightbulb?")
    try:
            Q4 = int(Q4)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Q4 == 2:
        Mon += 200
        print("Correct!")
        break
    elif Q4 !=2:
        print("Sorry that's not the answer! You have lost all of your earnings, good try. :(")
        print("The correct answer is 2. Thomas Edison")
        Mon -= 400
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

#Q5
while Q1 == 3 and Q2 == 4 and Q3 == 1 and Q4 == 2:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. 1.5 x 10^8 AU")
    print("2. 15 AU")
    print("3. 1 AU")
    print("4. 1.5 X 10^5 AU")
    Q5 = raw_input("What is the distance from Earth to the Sun in astronomical units?")
    try:
            Q5 = int(Q5)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Q5 == 3:
        Mon += 300
        print("Correct!")
        break
    elif Q5 != 3:
        print("Sorry that's not the answer! You have lost all of your earnings, good try. :(")
        print("The correct answer is 3. 1 AU")
        Mon -= 600
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

#Q6
while Q1 == 3 and Q2 == 4 and Q3 == 1 and Q4 == 2 and Q5 == 3:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Kinguin")
    print("2. Arctic")
    print("3. Essentio")
    print("4. Gento")
    Q6 = raw_input("What is the fastest species of penguin?")
    try:
            Q6 = int(Q6)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Q6 == 4:
        Mon += 300
        print("Correct!")
        break
    elif Q6 != 4:
        print("Sorry that's not the answer! You have lost all of your earnings, good try. :(")
        print("The correct answer is 4. Gento")
        Mon -= 900
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

#Q7
while Q1 == 3 and Q2 == 4 and Q3 == 1 and Q4 == 2 and Q5 == 3 and Q6 == 4:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. October 12th")
    print("2. August 9th")
    print("3. January 26th")
    print("4. July 1st")
    Q7 = raw_input("On what date is Australia Day?")
    try:
            Q7 = int(Q7)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Q7 == 3:
        Mon += 400
        print("Correct!")
        break
    elif Q7 != 3:
        print("Sorry that's not the answer! You have lost all of your earnings, good try. :(")
        print("The correct answer is 3. January 26th")
        Mon -= 1200
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

#Q8
while Q1 == 3 and Q2 == 4 and Q3 == 1 and Q4 == 2 and Q5 == 3 and Q6 == 4 and Q7 ==3:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. Nelson Mandela")
    print("2. Martin Luther King Jr.")
    print("3. Barack Obama")
    print("4. Mahatma Gandhi")
    Q8 = raw_input("Who is the first black president of South America?")
    try:
            Q8 = int(Q8)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Q8 == 1:
        Mon += 400
        print("Correct!")
        break
    elif Q8 != 1:
        print("Sorry that's not the answer! You have lost all of your earnings, good try. :(")
        print("The correct answer is 1. Nelson Mandela")
        Mon -= 1600
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

#Q9
while Q1 == 3 and Q2 == 4 and Q3 == 1 and Q4 == 2 and Q5 == 3 and Q6 == 4 and Q7 ==3 and Q8 == 1:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. 28 Teeth")
    print("2. 38 Teeth")
    print("3. 24 Teeth")
    print("4. 32 Teeth")
    Q9 = raw_input("How many teeth does the average human adult have?")
    try:
            Q9 = int(Q9)

    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Q9 == 4:
        Mon += 400
        print("Correct!")
        break
    elif Q9 != 4:
        print("Sorry that's not the answer! You have lost all of your earnings, good try. :(")
        print("The correct answer is 4. 32 Teeth")
        Mon -= 2000
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue

#Q10
while Q1 == 3 and Q2 == 4 and Q3 == 1 and Q4 == 2 and Q5 == 3 and Q6 == 4 and Q7 ==3 and Q8 == 1 and Q9 == 4:
    print(" ")
    print("Please input the digit that is before the answer you choose!")
    print("1. 67%")
    print("2. 71%")
    print("3. 77%")
    print("4. 81%")
    Q10 = raw_input("How much of Earth's surface is covered in water?")
    try:
            Q10 = int(Q10)
    # Check for valid input
    except:
        print(" ")
        print("That is not a valid answer!")
        continue
    if Q10 == 2:
        Mon += 600
        print("Correct!")
        print(" ")
        print("Congratulations!! You have answered all 10 questions correctly.")
        print("You win the maximum cash amount of $") + str(Mon) +("!!!")
        break
    elif Q10 != 2:
        print("Sorry that's not the answer! You have lost all of your earnings, good try. :(")
        print("The correct answer is 2. 71%")
        Mon -= 2400
        break
    else:
        print(" ")
        print("Please put in an integer between 1 and 4!")
        continue
#Loss
if Q1 != 3 or Q2 != 4 or Q3 != 1 or Q4 != 2 or Q5 != 3 or Q6 != 4 or Q7 !=3 or Q8 != 1 or Q9 != 4 or Q10 != 2:
    print (" ")
    print ("Sorry you have received $") + str(Mon) + ("!")
    print ("Good game.")