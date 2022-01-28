#-------------------------------------------------------------------------------
# Name:        Club Sign-up
# Purpose:     To allow students to easily sign up for clubs in their school.
#
# Author:      Jeremy Mohammed
#
# Created:     01/05/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Setting Variables
Again = "A"
Days = 3
Days2 = 3
Gra = 1

#Intro
print ("_".center(90,"_"))
print ("Club Sign-up!")
print ("Your online database for signing up for clubs in your high school with ease.")
print (" ")

#Club Decision
while Again != ("No") or Again != ("no"):
    print (" ")
    print ("Clubs:")
    print ("1. Robotics")
    print ("2. Student Council")
    print ("3. Student Government")
    print ("4. D.E.C.A")
    print ("5. Soccer")
    print ("6. Volleyball")
    print ("7. Basketball")
    print ("8. Swimming")
    print ("9. Newspaper")
    print ("10. Music")
    print (" ")

#Club Output
    try:
        Club = raw_input ("What club would you like to join?")
        #Robotics
        if Club == ("1") or Club == ("1.") or Club == ("Robotics") or Club == ("robotics"):
            print ("You have selected to join Robotics club!")
            print (" ")
            print ("The club takes place on Monday.")
            print ("The club starts at 3pm.")
            print ("Mr. Johnson is the leader of the club.")
            print ("The club takes place in room 3315.")
            print ("You may be going to a robotics meet in Toronto.")
            print ("You may need to purchase a $5 shirt for participation in the club.")
            print ("The average needed for the club is 85%.")
            print ("The leader's room is 3315.")
        #Student Council
        elif Club == ("2") or Club == ("2.") or Club == ("Student Council") or Club == ("student council"):
            print ("You have selected to join Student Council!")
            print (" ")
            print ("The club takes place on Tuesday.")
            print ("The club starts at 3pm.")
            print ("Mr. Fazel is the leader of the club.")
            print ("The club takes place in room 3221.")
            print ("You may be going to Wonderland for a conference.")
            print ("You may need to purchase a $5 shirt for participation in the club.")
            print ("The average needed for the club is 70%.")
            print ("The leader's room is 3222.")
        #Student Government
        elif Club == ("3") or Club == ("3.") or Club == ("Student Government") or Club == ("student covernment"):
            print ("You have selected to join Student Government!")
            print (" ")
            print ("The club takes place on Wednesday.")
            print ("The club starts at 3pm.")
            print ("Mrs. Henry is the leader of the club.")
            print ("The club takes place in room 3221.")
            print ("You may be going to Wonderland for a conference.")
            print ("You may need to purchase a $5 shirt for participation in the club.")
            print ("The average needed for the club is 75%.")
            print ("The leader's room is 3221.")
        #D.E.C.A
        elif Club == ("4") or Club == ("4.") or Club == ("D.E.C.A") or Club == ("d.e.c.a"):
            print ("You have selected to join D.E.C.A!")
            print (" ")
            print ("The club takes place on Thursday.")
            print ("The club starts at 3pm.")
            print ("Mrs. Woods is the leader of the club.")
            print ("The club takes place in room 3204.")
            print ("You may be going to a D.E.C.A. meet in Toronto.")
            print ("You may need to purchase a $5 shirt for participation in the club.")
            print ("The average needed for the club is 80%.")
            print ("The leader's room is 3204.")
        #Soccer
        elif Club == ("5") or Club == ("5.") or Club == ("Soccer") or Club == ("soccer"):
            print ("You have selected to join the Soccer team!")
            print (" ")
            print ("The club takes place on Tuesday and Thursday.")
            print ("The club starts at 7am.")
            print ("Mr. Chapman is the leader of the club.")
            print ("The club takes place in Gym B.")
            print ("You may be going to various schools to compete against others.")
            print ("You may need to purchase a jersey for $10 for participation in the club.")
            print ("The average needed for the club is 65%.")
            print ("The leader's room is 3108.")
        #Volleyball
        elif Club == ("6") or Club == ("6.") or Club == ("Volleyball") or Club == ("volleyball"):
            print ("You have selected to join the Volleyball team!")
            print (" ")
            print ("The club takes place on Monday and Wednesday.")
            print ("The club starts at 7am.")
            print ("Mrs. Radice is the leader of the club.")
            print ("The club takes place in Gym B.")
            print ("You may be going to various schools to compete against others.")
            print ("You may need to purchase a jersey for $10 for participation in the club.")
            print ("The average needed for the club is 65%.")
            print ("The leader's room is 3206.")
        #Basketball
        elif Club == ("7") or Club == ("7.") or Club == ("Basketball") or Club == ("basketball"):
            print ("You have selected to join the Basketball team.")
            print (" ")
            print ("The club takes place on Tuesday and Friday.")
            print ("The club starts at 7am.")
            print ("Mr. Geett is the leader of the club.")
            print ("The club takes place in Gym B.")
            print ("You may be going to various schools to compete against others.")
            print ("You may need to purchase a jersey for $10 for participation in the club.")
            print ("The average needed for the club is 65%.")
            print ("The leader's room is 3228.")
        #Swimming
        elif Club == ("8") or Club == ("8.") or Club == ("Swimming") or Club == ("swimming"):
            print ("You have selected to join the Swimming team!")
            print (" ")
            print ("The club takes place on Monday and Thursday.")
            print ("The club starts at 7am.")
            print ("Mrs. Sessa is the leader of the club.")
            print ("The club takes place in Gym A.")
            print ("You may be going to recreational centres for practices and meets.")
            print ("You may need to purchase a $20 swimsuit for participation in the club.")
            print ("The average needed for the club is 65%.")
            print ("The leader's room is 3132.")
        #Newspaper
        elif Club == ("9") or Club == ("9.") or Club == ("Newspaper") or Club == ("newspaper"):
            print ("You have selected to join Newspaper club!")
            print (" ")
            print ("The club takes place on Wednesday.")
            print ("The club takes place during lunch.")
            print ("Mrs. Wells is the leader of the club.")
            print ("The club takes place in room 3105.")
            print ("You may need to purchase a $5 shirt for participation in the club.")
            print ("The average needed for the club is 75%")
            print ("The leader's room is 3105.")
        #Music
        elif Club == ("10") or Club == ("10.") or Club == ("Music") or Club == ("music"):
            print ("You have selected to join Music club!")
            print (" ")
            print ("The club takes place on Friday.")
            print ("The club starts at 3pm.")
            print ("Mrs. Fletcher is the leader of the club.")
            print ("The club takes place in room 3157.")
            print ("You may be going to various schools to perform.")
            print ("You may need to purchase a $5 shirt for participation in the club.")
            print ("The average needed for the club is 70%.")
            print ("The leader's room is 3157.")
        #Check for white space
        elif Club.isspace() == True:
            print ("You didn't write anything!")
            print(" ")
            continue
        #Check for valid input
        else:
            print ("That is not a valid club.")
            print (" ")
            continue

    #Setting average and simplifying 'Club' Variable
        #Robotics
        if Club == ("1") or Club == ("1.") or Club == ("Robotics") or Club == ("robotics"):
            ClubAver = 85
            Club = ("Robotics")
        #Student Council
        elif Club == ("2") or Club == ("2.") or Club == ("Student Council") or Club == ("student council"):
            ClubAver = 70
            Club = ("Student Council")
        #Student Government
        elif Club == ("3") or Club == ("3.") or Club == ("Student Government") or Club == ("student covernment"):
            ClubAver = 75
            Club = ("Student Government")
        #D.E.C.A
        elif Club == ("4") or Club == ("4.") or Club == ("D.E.C.A") or Club == ("d.e.c.a"):
            ClubAver = 80
            Club = ("D.E.C.A")
        #Soccer
        elif Club == ("5") or Club == ("5.") or Club == ("Soccer") or Club == ("soccer"):
            ClubAver = 65
            Club = ("Soccer")
        #Volleyball
        elif Club == ("6") or Club == ("6.") or Club == ("Volleyball") or Club == ("volleyball"):
            ClubAver = 65
            Club = ("Volleyball")
        #Basketball
        elif Club == ("7") or Club == ("7.") or Club == ("Basketball") or Club == ("basketball"):
            ClubAver = 65
            Club = ("Basketball")
        #Swimming
        elif Club == ("8") or Club == ("8.") or Club == ("Swimming") or Club == ("swimming"):
            ClubAver = 65
            Club = ("Swimming")
        #Newspaper
        elif Club == ("9") or Club == ("9.") or Club == ("Newspaper") or Club == ("newspaper"):
            ClubAver = 75
            Club = ("Newspaper")
        #Music
        elif Club == ("10") or Club == ("10.") or Club == ("Music") or Club == ("music"):
            ClubAver = 70
            Club = ("Music")
        #No else because no ther possible input besides ^
    except KeyboardInterrupt:
        Test = raw_input("Would you like to continue?")
        if Test == "Yes" or Test == "yes":
            continue
        else:
            print ("Have a good day.")
            exit ("_".center(90,"_"))

    #Personal Info
    while Again != ("Yes") or Again != ("yes"):
        print (" ")
        print ("Please enter your information for the club leader.")
        print (" ")

    #First Name
        while True:
            try:
                FName = raw_input ("What is your first name?")
            except KeyboardInterrupt:
                Test = raw_input("Would you like to continue?")
                if Test == "Yes" or Test == "yes":
                    continue
                else:
                    print ("Have a good day.")
                    exit ("_".center(90,"_"))
            #Check for white space
            if FName.isspace() == True:
                print (" ")
                print ("You didn't write anything!")
            else:
                #Check for letters only
                if FName.isalpha() == False:
                    print (" ")
                    print ("Please enter letters only.")
                    continue
                else:
                #Check if correct
                    print (" ")
                    print ("Your first name is ") + FName.capitalize() + (".")
                    try:
                        FNameY = raw_input ("Is this correct?")
                        if FNameY == "Yes" or FNameY == "yes":
                            break
                        else:
                            continue
                    except KeyboardInterrupt:
                        Test = raw_input("Would you like to continue?")
                        if Test == "Yes" or Test == "yes":
                            continue
                        else:
                            print ("Have a good day.")
                            exit ("_".center(90,"_"))

        #Last Name
        while True:
            try:
                LName = raw_input ("What is your last name?")
            except KeyboardInterrupt:
                Test = raw_input("Would you like to continue?")
                if Test == "Yes" or Test == "yes":
                    continue
                else:
                    print ("Have a good day.")
                    exit ("_".center(90,"_"))
            #Check for white space
            if LName.isspace() == True:
                print (" ")
                print ("You didn't write anything!")
            else:
                #Check for letters only
                if LName.isalpha() == False:
                    print (" ")
                    print ("Please enter letters only.")
                    continue
                else:
                #Check if correct
                    print (" ")
                    print ("Your last name is ") + LName.capitalize() + (".")
                    try:
                        LNameY = raw_input ("Is this correct?")
                        if LNameY == "Yes" or LNameY == "yes":
                            break
                        else:
                            continue
                    except KeyboardInterrupt:
                        Test = raw_input("Would you like to continue?")
                        if Test == "Yes" or Test == "yes":
                            continue
                        else:
                            print ("Have a good day.")
                            exit ("_".center(90,"_"))

        #Homeroom
        while True:
            try:
                HRNum = raw_input ("What is your homeroom number?")
            except KeyboardInterrupt:
                Test = raw_input("Would you like to continue?")
                if Test == "Yes" or Test == "yes":
                    continue
                else:
                    print ("Have a good day.")
                    exit ("_".center(90,"_"))
            #Check for white space
            if HRNum.isspace() == True:
                print (" ")
                print ("You didn't write anything!")
            #Check for valid input
            else:
                try:
                    HRNum = int(HRNum)
                except:
                    print (" ")
                    print ("Please enter digits only.")
                    continue
                if HRNum >=3101 and HRNum <=3160:
                #Check if correct
                    print (" ")
                    print ("Your homeroom is ") + str(HRNum) + (".")
                    try:
                        HRNumY = raw_input ("Is this correct?")
                        if HRNumY == "Yes" or HRNumY == "yes":
                            break
                        else:
                            continue
                    except KeyboardInterrupt:
                        Test = raw_input("Would you like to continue?")
                        if Test == "Yes" or Test == "yes":
                            continue
                        else:
                            print ("Have a good day.")
                            exit ("_".center(90,"_"))
                elif HRNum >=3201 and HRNum <=3230:
                #Check if correct
                    print (" ")
                    print ("Your homeroom is ") + str(HRNum) + (".")
                    try:
                        HRNumY = raw_input ("Is this correct?")
                        if HRNumY == "Yes" or HRNumY == "yes":
                            break
                        else:
                            continue
                    except KeyboardInterrupt:
                        Test = raw_input("Would you like to continue?")
                        if Test == "Yes" or Test == "yes":
                            continue
                        else:
                            print ("Have a good day.")
                            exit ("_".center(90,"_"))
                elif HRNum >=3301 and HRNum <=3330:
                #Check if correct
                    print (" ")
                    print ("Your homeroom is ") + str(HRNum) + (".")
                    try:
                        HRNumY = raw_input ("Is this correct?")
                        if HRNumY == "Yes" or HRNumY == "yes":
                            break
                        else:
                            continue
                    except KeyboardInterrupt:
                        Test = raw_input("Would you like to continue?")
                        if Test == "Yes" or Test == "yes":
                            continue
                        else:
                            print ("Have a good day.")
                            exit ("_".center(90,"_"))
                else:
                    print (" ")
                    print ("That is not a homeroom within your school.")
                    continue

        #Email
        while True:
            try:
                Email = raw_input ("What is your E-mail?")
            except KeyboardInterrupt:
                Test = raw_input("Would you like to continue?")
                if Test == "Yes" or Test == "yes":
                    continue
                else:
                    print ("Have a good day.")
                    exit ("_".center(90,"_"))
            #Check for white space
            if Email.isspace() == True:
                print (" ")
                print ("You didn't write anything!")
            else:
                #Check if correct
                print (" ")
                print ("Your E-mail is ") + Email + (".")
                try:
                    EmailY = raw_input ("Is this correct?")
                    if EmailY == "Yes" or EmailY == "yes":
                        break
                    else:
                        continue
                except KeyboardInterrupt:
                    Test = raw_input("Would you like to continue?")
                    if Test == "Yes" or Test == "yes":
                        continue
                    else:
                        print ("Have a good day.")
                        exit ("_".center(90,"_"))

        #Phone Number
        while True:
            try:
                PhNum = raw_input ("What is your phone number?")
            except KeyboardInterrupt:
                Test = raw_input("Would you like to continue?")
                if Test == "Yes" or Test == "yes":
                    continue
                else:
                    print ("Have a good day.")
                    exit ("_".center(90,"_"))
            #Check for white space
            if PhNum.isspace() == True:
                print (" ")
                print ("You didn't write anything!")
            #Check for valid input
            else:
                try:
                    PhNum = int(PhNum)
                except:
                    print (" ")
                    print ("Please enter digits only.")
                    continue
                if PhNum >=1000000000 and PhNum <=9999999999:
                #Check if correct
                    print (" ")
                    print ("Your phone number is ") + str(PhNum) + (".")
                    try:
                        PhNumY = raw_input ("Is this correct?")
                        if PhNumY == "Yes" or PhNumY == "yes":
                            break
                        else:
                            continue
                    except KeyboardInterrupt:
                        Test = raw_input("Would you like to continue?")
                        if Test == "Yes" or Test == "yes":
                            continue
                        else:
                            print ("Have a good day.")
                            exit ("_".center(90,"_"))
                elif PhNum == 0:
                #Check if correct
                    print (" ")
                    print ("Your phone number is ") + str(PhNum) + (".")
                    try:
                        PhNumY = raw_input ("Is this correct?")
                        if PhNumY == "Yes" or PhNumY == "yes":
                            break
                        else:
                            continue
                    except KeyboardInterrupt:
                        Test = raw_input("Would you like to continue?")
                        if Test == "Yes" or Test == "yes":
                            continue
                        else:
                            print ("Have a good day.")
                            exit ("_".center(90,"_"))
                else:
                    print (" ")
                    print ("That is not a valid phone number.")

        #Average
        while True:
            try:
                Aver = raw_input ("What was your average from last year?")
            except KeyboardInterrupt:
                Test = raw_input("Would you like to continue?")
                if Test == "Yes" or Test == "yes":
                    continue
                else:
                    print ("Have a good day.")
                    exit ("_".center(90,"_"))
            #Check for white space
            if Aver.isspace() == True:
                print (" ")
                print ("You didn't write anything!")
            #Check for valid input
            else:
                try:
                    Aver = float(Aver)

                except:
                    print (" ")
                    print ("Please enter digits only.")
                    continue
                if Aver >= 0 and Aver <=100:
                #Check if correct
                    print (" ")
                    print ("Your average from last year was ") + str(Aver) + ("%.")
                    try:
                        AverY = raw_input ("Is this correct?")
                        if AverY == "Yes" or AverY == "yes":
                            break
                        else:
                            continue
                    except KeyboardInterrupt:
                        Test = raw_input("Would you like to continue?")
                        if Test == "Yes" or Test == "yes":
                            continue
                        else:
                            print ("Have a good day.")
                            exit ("_".center(90,"_"))
                else:
                    print (" ")
                    print ("That is not a possible average.")
                    continue

        #Grade
        while True:
            try:
                Grade = raw_input ("What grade are you in?")
            except KeyboardInterrupt:
                Test = raw_input("Would you like to continue?")
                if Test == "Yes" or Test == "yes":
                    continue
                else:
                    print ("Have a good day.")
                    exit ("_".center(90,"_"))
            #Check for white space
            if Grade.isspace() == True:
                print (" ")
                print ("You didn't write anything!")
            #Check for valid input
            else:
                try:
                    Grade = int(Grade)

                except:
                    print (" ")
                    print ("Please enter digits only.")
                    continue
                if Grade == 9 or Grade == 10 or Grade == 11 or Grade == 12:
                    print (" ")
                    print ("You are in grade ") + str(Grade) + (".")
                    try:
                        GradeY = raw_input ("Is this correct?")
                        if GradeY == "Yes" or GradeY == "yes":
                            break
                        else:
                            continue
                    except KeyboardInterrupt:
                        Test = raw_input("Would you like to continue?")
                        if Test == "Yes" or Test == "yes":
                            continue
                        else:
                            print ("Have a good day.")
                            exit ("_".center(90,"_"))
                else:
                    print (" ")
                    print ("That is not a grade within your school.")
                    continue
        break

#Average Valid
    #Too Low
    VAver = Aver - ClubAver
    if VAver <0:
        FVAver = VAver*-1
        print (" ")
        print ("Your average is ") + str(FVAver) + ("% too low to join this club.")
    #High Enough
    else:
        print (" ")
        print ("You have a high enough average to join ") + Club + ("!")

#Grade Opportunities
    #Robotics
    while VAver >=0:
        if Club == ("Robotics"):
            print (" ")
            if Grade == 10 or Grade == 11 or Grade == 12:
                print ("There are opportunities in your grade!")
                Gra = 2
                break
            else:
                print ("Sorry, there are no opportunities in your grade.")
                break
        #Student Council
        elif Club == ("Student Council"):
            print (" ")
            if Grade == 9 or Grade == 10:
                print ("There are opportunities in your grade!")
                Gra = 2
                break
            else:
                print ("Sorry, there are no opportunities in your grade.")
                break
        #Student Government
        elif Club == ("Student Government"):
            print (" ")
            if Grade == 11 or Grade == 12:
                print ("There are opportunities in your grade!")
                Gra = 2
                break
            else:
                print ("Sorry, there are no opportunities in your grade.")
                break
        #D.E.C.A
        elif Club == ("D.E.C.A"):
            print (" ")
            if Grade == 11 or Grade == 12:
                print ("There are opportunities in your grade!")
                Gra = 2
                break
            else:
                print ("Sorry, there are no opportunities in your grade.")
                break
        #Soccer
        elif Club == ("Soccer"):
            print (" ")
            if Grade == 10 or Grade == 11:
                print ("There are opportunities in your grade!")
                Gra = 2
                break
            else:
                print ("Sorry, there are no opportunities in your grade.")
                break
        #Volleyball
        elif Club == ("Volleyball"):
            print (" ")
            if Grade == 11 or Grade == 12:
                print ("There are opportunities in your grade!")
                Gra = 2
                break
            else:
                print ("Sorry, there are no opportunities in your grade.")
                break
        #Basketball
        elif Club == ("Basketball"):
            print (" ")
            if Grade == 9 or Grade == 10 or Grade == 11 or Grade == 12:
                print ("There are opportunities in your grade!")
                Gra = 2
                break
        #Swimming
        elif Club == ("Swimming"):
            print (" ")
            if Grade == 10 or Grade == 11 or Grade == 12:
                print ("There are opportunities in your grade!")
                Gra = 2
                break
            else:
                print ("Sorry, there are no opportunities in your grade.")
                break
        #Newspaper
        elif Club == ("Newspaper"):
            print (" ")
            if Grade == 10 or Grade == 11 or Grade == 12:
                print ("There are opportunities in your grade!")
                Gra = 2
                break
            else:
                print ("Sorry, there are no opportunities in your grade.")
                break
        #Music
        elif Club == ("Music"):
            print (" ")
            if Grade == 11 or Grade == 12:
                print ("There are opportunities in your grade!")
                Gra = 2
                break
            else:
                print ("Sorry, there are no opportunities in your grade.")
                break
        #No else because no ther possible input besides ^

#Available Days
    while VAver >= 0 and Days != 2 and Days2 == 3 and Gra == 2:
        if Club == ("Robotics"):
            #Robotics
            while Days != 2 and Days2 == 3:
                try:
                    Days = raw_input ("Are you available on Monday?")
                except KeyboardInterrupt:
                    Test = raw_input("Would you like to continue?")
                    if Test == "Yes" or Test == "yes":
                        continue
                    else:
                        print ("Have a good day.")
                        exit ("_".center(90,"_"))
                #Check for white space
                if Club.isspace() == True:
                    print (" ")
                    print ("You didn't write anything!")
                #Check for valid input
                else:
                    if Days == ("Yes") or Days == ("yes"):
                        print (" ")
                        print ("You are available during Robotics!")
                        Days = 2
                        Days2 = 4
                        break
                    elif Days == ("No") or Days == ("no"):
                        print (" ")
                        print ("Sorry you are not available for Robotics.")
                        Days = 2
                        Days2 = 5
                        break
                    else:
                        print (" ")
                        print ("Please answer with 'Yes' or 'No'.")
                        continue
        elif Club == ("Student Council"):
            #Student Council
            while  Days != 2 and Days2 == 3:
                try:
                    Days = raw_input ("Are you available on Tuesday?")
                except KeyboardInterrupt:
                    Test = raw_input("Would you like to continue?")
                    if Test == "Yes" or Test == "yes":
                        continue
                    else:
                        print ("Have a good day.")
                        exit ("_".center(90,"_"))
                #Check for white space
                if Club.isspace() == True:
                    print (" ")
                    print ("You didn't write anything!")
                #Check for valid input
                else:
                    if Days == ("Yes") or Days == ("yes"):
                        print (" ")
                        print ("You are available during Student Council!")
                        Days = 2
                        Days2 = 4
                        break
                    elif Days == ("No") or Days == ("no"):
                        print (" ")
                        print ("Sorry you are not available for Student Council.")
                        Days = 2
                        Days2 = 5
                        break
                    else:
                        print (" ")
                        print ("Please answer with 'Yes' or 'No'.")
                        continue
        elif Club == ("Student Government"):
            #Student Government
            while  Days != 2 and Days2 == 3:
                try:
                    Days = raw_input ("Are you available on Wednesday?")
                except KeyboardInterrupt:
                    Test = raw_input("Would you like to continue?")
                    if Test == "Yes" or Test == "yes":
                        continue
                    else:
                        print ("Have a good day.")
                        exit ("_".center(90,"_"))
                #Check for white space
                if Club.isspace() == True:
                    print (" ")
                    print ("You didn't write anything!")
                #Check for valid input
                else:
                    if Days == ("Yes") or Days == ("yes"):
                        print (" ")
                        print ("You are available during Student Government!")
                        Days = 2
                        Days2 = 4
                        break
                    elif Days == ("No") or Days == ("no"):
                        print (" ")
                        print ("Sorry you are not available for Student Government.")
                        Days == 2
                        Days2 = 5
                        break
                    else:
                        print (" ")
                        print ("Please answer with 'Yes' or 'No'.")
                        continue
        elif Club == ("D.E.C.A"):
            #D.E.C.A
            while  Days != 2 and Days2 == 3:
                try:
                    Days = raw_input ("Are you available on Thursday?")
                except KeyboardInterrupt:
                    Test = raw_input("Would you like to continue?")
                    if Test == "Yes" or Test == "yes":
                        continue
                    else:
                        print ("Have a good day.")
                        exit ("_".center(90,"_"))
                #Check for white space
                if Club.isspace() == True:
                    print (" ")
                    print ("You didn't write anything!")
                #Check for valid input
                else:
                    if Days == ("Yes") or Days == ("yes"):
                        print (" ")
                        print ("You are available during D.E.C.A!")
                        Days = 2
                        Days2 = 4
                        break
                    elif Days == ("No") or Days == ("no"):
                        print (" ")
                        print ("Sorry you are not available for D.E.C.A.")
                        Days = 2
                        Days2 = 5
                        break
                    else:
                        print (" ")
                        print ("Please answer with 'Yes' or 'No'.")
                        continue
        elif Club == ("Soccer"):
            #Soccer
            while  Days != 2 and Days2 == 3:
                try:
                    Days = raw_input ("Are you available on Tuesday and Thursday?")
                except KeyboardInterrupt:
                    Test = raw_input("Would you like to continue?")
                    if Test == "Yes" or Test == "yes":
                        continue
                    else:
                        print ("Have a good day.")
                        exit ("_".center(90,"_"))
                #Check for white space
                if Club.isspace() == True:
                    print (" ")
                    print ("You didn't write anything!")
                #Check for valid input
                else:
                    if Days == ("Yes") or Days == ("yes"):
                        print (" ")
                        print ("You are available during Soccer!")
                        Days = 2
                        Days2 = 4
                        break
                    elif Days == ("No") or Days == ("no"):
                        print (" ")
                        print ("Sorry you are not available for Soccer.")
                        Days = 2
                        Days2 = 5
                        break
                    else:
                        print (" ")
                        print ("Please answer with 'Yes' or 'No'.")
                        continue
        elif Club == ("Volleyball"):
            #Volleyball
            while  Days != 2 and Days2 == 3:
                try:
                    Days = raw_input ("Are you available on Monday and Wednesday?")
                except KeyboardInterrupt:
                    Test = raw_input("Would you like to continue?")
                    if Test == "Yes" or Test == "yes":
                        continue
                    else:
                        print ("Have a good day.")
                        exit ("_".center(90,"_"))
                #Check for white space
                if Club.isspace() == True:
                    print (" ")
                    print ("You didn't write anything!")
                #Check for valid input
                else:
                    if Days == ("Yes") or Days == ("yes"):
                        print (" ")
                        print ("You are available during Volleyball!")
                        Days = 2
                        Days2 = 4
                        break
                    elif Days == ("No") or Days == ("no"):
                        print (" ")
                        print ("Sorry you are not available for Volleyball.")
                        Days = 2
                        Days2 = 5
                        break
                    else:
                        print (" ")
                        print ("Please answer with 'Yes' or 'No'.")
                        continue
        elif Club == ("Basketball"):
            #Basketball
            while  Days != 2 and Days2 == 3:
                try:
                    Days = raw_input ("Are you available on Tuesday and Friday?")
                except KeyboardInterrupt:
                    Test = raw_input("Would you like to continue?")
                    if Test == "Yes" or Test == "yes":
                        continue
                    else:
                        print ("Have a good day.")
                        exit ("_".center(90,"_"))
                #Check for white space
                if Club.isspace() == True:
                    print (" ")
                    print ("You didn't write anything!")
                #Check for valid input
                else:
                    if Days == ("Yes") or Days == ("yes"):
                        print (" ")
                        print ("You are available during Basketball!")
                        Days = 2
                        Days2 = 4
                        break
                    elif Days == ("No") or Days == ("no"):
                        print (" ")
                        print ("Sorry you are not available for Basketball.")
                        Days == 2
                        Days2 = 5
                        break
                    else:
                        print (" ")
                        print ("Please answer with 'Yes' or 'No'.")
                        continue
        elif Club == ("Swimming"):
            #Swimming
            while  Days != 2 and Days2 == 3:
                try:
                    Days = raw_input ("Are you available on Monday and Thursday?")
                except KeyboardInterrupt:
                    Test = raw_input("Would you like to continue?")
                    if Test == "Yes" or Test == "yes":
                        continue
                    else:
                        print ("Have a good day.")
                        exit ("_".center(90,"_"))
                #Check for white space
                if Club.isspace() == True:
                    print (" ")
                    print ("You didn't write anything!")
                #Check for valid input
                else:
                    if Days == ("Yes") or Days == ("yes"):
                        print (" ")
                        print ("You are available during Swimming!")
                        Days = 2
                        Days2 = 4
                        break
                    elif Days == ("No") or Days == ("no"):
                        print (" ")
                        print ("Sorry you are not available for Swimming.")
                        Days = 2
                        Days2 = 5
                        break
                    else:
                        print (" ")
                        print ("Please answer with 'Yes' or 'No'.")
                        continue
        elif Club == ("Newspaper"):
            #Newspaper
            while  Days != 2 and Days2 == 3:
                try:
                    Days = raw_input ("Are you available on Wednesday?")
                except KeyboardInterrupt:
                    Test = raw_input("Would you like to continue?")
                    if Test == "Yes" or Test == "yes":
                        continue
                    else:
                        print ("Have a good day.")
                        exit ("_".center(90,"_"))
                #Check for white space
                if Club.isspace() == True:
                    print (" ")
                    print ("You didn't write anything!")
                #Check for valid input
                else:
                    if Days == ("Yes") or Days == ("yes"):
                        print (" ")
                        print ("You are available during Newspaper!")
                        Days = 2
                        Days2 = 4
                        break
                    elif Days == ("No") or Days == ("no"):
                        print (" ")
                        print ("Sorry you are not available for Newspaper.")
                        Days = 2
                        Days2 = 5
                        break
                    else:
                        print (" ")
                        print ("Please answer with 'Yes' or 'No'.")
                        continue
        elif Club == ("Music"):
            #Music
            while  Days != 2 and Days2 == 3:
                try:
                    Days = raw_input ("Are you available on Friday?")
                except KeyboardInterrupt:
                    Test = raw_input("Would you like to continue?")
                    if Test == "Yes" or Test == "yes":
                        continue
                    else:
                        print ("Have a good day.")
                        exit ("_".center(90,"_"))
                #Check for white space
                if Club.isspace() == True:
                    print (" ")
                    print ("You didn't write anything!")
                #Check for valid input
                else:
                    if Days == ("Yes") or Days == ("yes"):
                        print (" ")
                        print ("You are available during Music!")
                        Days = 2
                        Days2 = 4
                        break
                    elif Days == ("No") or Days == ("no"):
                        print (" ")
                        print ("Sorry you are not available for Music.")
                        Days = 2
                        Days2 = 5
                        break
                    else:
                        print (" ")
                        print ("Please answer with 'Yes' or 'No'.")
                        continue
        break
    #No else because no ther possible input besides ^
    while Days2 == 4 and Gra == 2:
        print (" ")
        print ("You have all the requirements to join this club.")
        while True:
            #Confirmation of Club
            try:
                Confirm = raw_input (("Would you like to join ") + Club + ("?"))
            except KeyboardInterrupt:
                Test = raw_input("Would you like to continue?")
                if Test == "Yes" or Test == "yes":
                    continue
                else:
                    print ("Have a good day.")
                    exit ("_".center(90,"_"))
            if Confirm == ("Yes") or Confirm == ("yes"):
                print(" ")
                print ("You have been reserved a spot in ") + Club + ("!")
                break
            elif Confirm == ("No") or Confirm == ("no"):
                print (" ")
                print ("You have not been reserved a spot in ") + Club + (".")
                break
            else:
                print (" ")
                print ("Please answer with 'Yes' or 'No'.")
                continue
        break
    #Re-apply
    while True:
        try:
            Again = raw_input ("Would you like to apply for another club?")
        except KeyboardInterrupt:
            Test = raw_input("Would you like to continue?")
            if Test == "Yes" or Test == "yes":
                continue
            else:
                    print ("Have a good day.")
                    exit ("_".center(90,"_"))
        #Check for white space
        if Club.isspace() == True:
            print (" ")
            print ("You didn't write anything!")
        #Check for valid input
        else:
            if Again == ("Yes") or Again == ("yes"):
                break
            elif Again == ("No") or Again == ("no"):
                break
            else:
                print (" ")
                print ("Please answer with 'Yes' or 'No'.")
                continue
    if Again == ("Yes") or Again == ("yes"):
        continue
    else:
        print (" ")
        print ("Have a nice day!")
        exit ("_".center(90,"_"))