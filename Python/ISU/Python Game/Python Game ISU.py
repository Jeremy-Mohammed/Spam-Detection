#-------------------------------------------------------------------------------
# Name:        Undead
# Purpose:     Undead is an RPG zombie-based game where you are a lone surviver
#              trying to escape a zombie apocalyse.
#
# Author:      Jeremy Mohammed
#
# Created:     26/05/2017
#-------------------------------------------------------------------------------
#Setting Variables
Start = "A"
Option = "A"
ChapterSela = 0
ChapterSelb = 0
ChapterSelc = 0



#Importing
import time
from random import randint

#Beginning of Game
#Title Card
print (" ")
print ("_".center (120,"_"))
time.sleep(1)
print (" _    _        _                                 _____       ".center (120))
print ("| |  | |      | |                               |_   _|      ".center (120))
print ("| |  | |  ___ | |  ___   ___   _ __ ___    ___    | |   ___  ".center (120))
print ("| |/\| | / _ \| | / __| / _ \ | '_ ` _ \  / _ \   | |  / _ \ ".center (120))
print ("\  /\  /|  __/| || (__ | (_) || | | | | ||  __/   | | | (_) |".center (120))
print (" \/  \/  \___||_| \___| \___/ |_| |_| |_| \___|   \_/  \___/ ".center (120))
print (" ")
time.sleep (0.5)
print ("                                                     _______      ".center (120))
time.sleep (0.5)
print ("                                                    (  ____ )     ".center (120))
time.sleep (0.5)
print ("         _        ______   _______  _______  ______(  )    ( )    ".center (120))
time.sleep (0.5)
print ("|\     /|( (    /|(  __  \ (  ____ \(  ___  )(  __  \__)    \ )   ".center (120))
time.sleep (0.5)
print ("| )   ( ||  \  ( || (  \  )| (    \/| (   ) || (  \  )       \ )  ".center (120))
time.sleep (0.5)
print ("| |   | ||   \ | || |   ) || (__    | (___) || |   ) |        ) ) ".center (120))
time.sleep (0.5)
print ("| |   | || (\ \) || |   | ||  __)   |  ___  || |   | |      _/ /  ".center (120))
time.sleep (0.5)
print ("| |   | || | \   || |   ) || (      | (   ) || |   ) |     |   )  ".center (120))
time.sleep (0.5)
print ("| (___) || )  \  || (__/  )| (____/\| )   ( || (__/  )      \_/   ".center (120))
time.sleep (0.5)
print ("(_______)|/    )_)(______/ (_______/|/     \|(______/             ".center (120))
time.sleep(1)
print (" ")
print ("_".center (120,"_"))
print (" ")
print (" ")

#Name
while True:
    Name = raw_input ("Please input your first name only.")
    #Check for letters only
    if Name.isalpha() == False:
        print (" ")
        print ("Please enter letters only.")
        continue
    else:
    #Check if correct
        while True:
            print (" ")
            print (" ")
            print ("_".center (120,"_"))
            print (" ")
            time.sleep(1)
            print (" ")
            print (("Your first name is ") + Name.capitalize() + (".")).center(120)
            NameY = raw_input ("Is this correct?")
            if NameY == "Yes" or NameY == "yes":
                NameY = "Yes"
                break
            elif NameY == "No" or NameY == "no":
                NameY = "No"
                break
            else:
                print (" ")
                print ("Please input 'Yes' or 'No'.".center(120))
                continue
    if NameY == "Yes":
        print (" ")
        print (("A file has been saved as '") + Name.capitalize() +("' for your progress.")).center(120)
        print (" ")
        time.sleep(1)
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")
        break
    else:
        continue

#Loop to come back to menu
while Start == "A":
    #Menu
    #Setting variables for loop to reset for every play
    Thirst = 0
    Hunger = 0
    Health = 100
    Score = 0
    Finished ="C"
    Chapter = 0
    Intro = "Stop"
    Dead = 0
    while Option == "A":
        print (" ")
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        time.sleep(1)
        print (" _______  _______  _                ".center(120))
        time.sleep (0.2)
        print ("(       )(  ____ \( (    /||\     /|".center(120))
        time.sleep (0.2)
        print ("| () () || (    \/|  \  ( || )   ( |".center(120))
        time.sleep (0.2)
        print ("| || || || (__    |   \ | || |   | |".center(120))
        time.sleep (0.2)
        print ("| |(_)| ||  __)   | (\ \) || |   | |".center(120))
        time.sleep (0.2)
        print ("| |   | || (      | | \   || |   | |".center(120))
        time.sleep (0.2)
        print ("| )   ( || (____/\| )  \  || (___) |".center(120))
        time.sleep (0.2)
        print ("|/     \|(_______/|/    )_)(_______)".center(120))
        print (" ")

        #Options
        time.sleep (1)
        print (" ")
        print ("     =====================          =====================================       ================================".center(120))
        print ("     |  ___ _            |          |   ___ _              _            |       |   ___            _ _ _       |".center(120))
        print ("     | | _ \ |__ _ _  _  |          |  / __| |_  __ _ _ __| |_ ___ _ _  |       |  / __|_ _ ___ __| (_) |_ ___ |".center(120))
        print ("     | |  _/ / _` | || | |          | | (__| ' \/ _` | '_ \  _/ -_) '_| |       | | (__| '_/ -_) _` | |  _(_-< |".center(120))
        print ("     | |_| |_\__,_|\_, | |          |  \___|_||_\__,_| .__/\__\___|_|   |       |  \___|_| \___\__,_|_|\__/__/ |".center(120))
        print ("     |             |__/  |          |                |_|                |       |                              |".center(120))
        print ("     =====================          =====================================       ================================".center(120))
        time.sleep(1)
        print (" ")
        print ("===================".center(120))
        print ("|  ___     _ _    |".center(120))
        print ("| | __|_ _(_) |_  |".center(120))
        print ("| | _|\ \ / |  _| |".center(120))
        print ("| |___/_\_\_|\__| |".center(120))
        print ("|                 |".center(120))
        print ("===================".center(120))
        time.sleep(1)
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")

        #Option Selection
        Begin = raw_input ("Please select an option.")
        #Play
        if Begin == "Play" or Begin == "play":
            print (" ")
            print (" ")
            print ("_".center (120,"_"))
            print (" ")
            time.sleep(1)
            print (" ___ _            _   _                 ".center (120))
            print ("/ __| |_ __ _ _ _| |_(_)_ _  __ _       ".center (120))
            print ("\__ \  _/ _` | '_|  _| | ' \/ _` |_ _ _ ".center (120))
            print ("|___/\__\__,_|_|  \__|_|_||_\__, (_|_|_)".center (120))
            print ("                            |___/       ".center (120))
            time.sleep(1)
            print (" ")
            print ("_".center (120,"_"))
            print (" ")
            print (" ")
            Intro = "Go"
            Chapter = 1
            break
        #Chapters
        elif Begin == "Chapter" or Begin == "chapter" or Begin == "Chapters" or Begin == "chapters":
            while True:
                print (" ")
                print (" ")
                print ("_".center (120,"_"))
                print (" ")
                time.sleep(1)
                print ("   ___ _              _               ".center(120))
                print ("  / __| |_  __ _ _ __| |_ ___ _ _ ___ ".center(120))
                print (" | (__| ' \/ _` | '_ \  _/ -_) '_(_-< ".center(120))
                print ("  \___|_||_\__,_| .__/\__\___|_| /__/ ".center(120))
                print ("                |_|                   ".center(120))
                print (" ")
                time.sleep(1)
                print ("=================================   =================================   ================================".center(120))
                print ("|  ___               __  _ ____ |   |  ___               __  _ ___  |   |  ___             __  _ ____  |".center(120))
                print ("| |   \ __ _ _  _   /  \/ |__ / |   | |   \ __ _ _  _   /  \/ | __| |   | |   \ __ _ _  _ /  \/ |__  | |".center(120))
                print ("| | |) / _` | || | | () | ||_ \ |   | | |) / _` | || | | () | |__ \ |   | | |) / _` | || | () | | / /  |".center(120))
                print ("| |___/\__,_|\_, |  \__/|_|___/ |   | |___/\__,_|\_, |  \__/|_|___/ |   | |___/\__,_|\_, |\__/|_|/_/   |".center(120))
                print ("|            |__/               |   |            |__/               |   |            |__/              |".center(120))
                print ("=================================   =================================   ================================".center(120))
                print (" ")
                time.sleep(1)
                print ("=========================".center(120))
                print ("|  __  __               |".center(120))
                print ("| |  \/  |___ _ _ _  _  |".center(120))
                print ("| | |\/| / -_) ' \ || | |".center(120))
                print ("| |_|  |_\___|_||_\_,_| |".center(120))
                print ("|                       |".center(120))
                print ("=========================".center(120))
                time.sleep(1)
                print (" ")
                print ("_".center (120,"_"))
                print (" ")
                print (" ")
                Chapter = raw_input ("Which chapter would you like to play?")
                #Printing Selection

                #Chapter Availability
                if ChapterSela == 0 and ChapterSelb == 0 and ChapterSelc == 0:
                    print (" ")
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    time.sleep(1)
                    print (" ")
                    print ("You have not unlocked any chapters yet!".center(120))
                    print (" ")
                    print ("Play through the game until the end to unlock all chapters.".center(120))
                    print (" ")
                    time.sleep(1)
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    print (" ")
                    Chapter = 0
                    break
                #Chapter 1
                elif Chapter == "Day 013" or Chapter == "day 013" or Chapter == "1" or Chapter == "013" or Chapter == "13" and ChapterSela == 1:
                    print (" ")
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    time.sleep(1)
                    print ("  ___      _        _          _    ___               __  _ ____ ".center(120))
                    print (" / __| ___| |___ __| |_ ___ __| |  |   \ __ _ _  _   /  \/ |__ / ".center(120))
                    print (" \__ \/ -_) / -_) _|  _/ -_) _` |  | |) / _` | || | | () | ||_ \ ".center(120))
                    print (" |___/\___|_\___\__|\__\___\__,_|  |___/\__,_|\_, |  \__/|_|___/ ".center(120))
                    print ("                                              |__/               ".center(120))
                    time.sleep(1)
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    print (" ")
                    Chapter = 1
                    break

                #Chapter 2
                elif Chapter == "Day 015" or Chapter == "day 015" or Chapter == "2" or Chapter == "015" or Chapter == "15" and ChapterSelb == 2:
                    print (" ")
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    time.sleep(1)
                    print ("  ___      _        _          _    ___               __  _ ___  ".center(120))
                    print (" / __| ___| |___ __| |_ ___ __| |  |   \ __ _ _  _   /  \/ | __| ".center(120))
                    print (" \__ \/ -_) / -_) _|  _/ -_) _` |  | |) / _` | || | | () | |__ \ ".center(120))
                    print (" |___/\___|_\___\__|\__\___\__,_|  |___/\__,_|\_, |  \__/|_|___/ ".center(120))
                    print ("                                              |__/               ".center(120))
                    time.sleep(1)
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    print (" ")
                    Chapter = 2
                    break

                #Chapter 3
                elif Chapter == "Day 017" or Chapter == "day 017" or Chapter == "3" or Chapter == "017" or Chapter == "17" and ChapterSelc == 3:
                    print (" ")
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    time.sleep(1)
                    print ("  ___      _        _          _    ___               __  _ ____  ".center(120))
                    print (" / __| ___| |___ __| |_ ___ __| |  |   \ __ _ _  _   /  \/ |__  | ".center(120))
                    print (" \__ \/ -_) / -_) _|  _/ -_) _` |  | |) / _` | || | | () | | / /  ".center(120))
                    print (" |___/\___|_\___\__|\__\___\__,_|  |___/\__,_|\_, |  \__/|_|/_/   ".center(120))
                    print ("                                              |__/                ".center(120))
                    time.sleep(1)
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    print (" ")
                    Chapter = 3
                    break

                #Return to menu
                elif Chapter == "Menu" or Chapter == "menu":
                    Chapter = 0
                    break

                #If chapters not yet unlocked
                elif Chapter == "Day 013" or Chapter == "day 013" or Chapter == "1" or Chapter == "013" or Chapter == "13" and ChapterSela != 1:
                    print (" ")
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    time.sleep(1)
                    print (" ___               __  _ ____  _  _   __ _   ".center(120))
                    print ("|   \ __ _ _  _   /  \/ |__ / | \| | / //_)  ".center(120))
                    print ("| |) / _` | || | | () | |__ \ | .` |/ // _ ) ".center(120))
                    print ("|___/\__,_|\_, |  \__/|_|___/ |_|\_/_//_/ \_)".center(120))
                    print ("           |__/                              ".center(120))
                    time.sleep(1)
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    print (" ")
                    Chapter = 0
                    break
                elif Chapter == "Day 015" or Chapter == "day 015" or Chapter == "2" or Chapter == "015" or Chapter == "15" and ChapterSelb != 2:
                    print (" ")
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    time.sleep(1)
                    print (" ___               __  _ ___   _  _   __ _   ".center(120))
                    print ("|   \ __ _ _  _   /  \/ | __| | \| | / //_)  ".center(120))
                    print ("| |) / _` | || | | () | |__ \ | .` |/ // _ ) ".center(120))
                    print ("|___/\__,_|\_, |  \__/|_|___/ |_|\_/_//_/ \_)".center(120))
                    print ("           |__/                              ".center(120))
                    time.sleep(1)
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    print (" ")
                    Chapter = 0
                    break
                elif Chapter == "Day 017" or Chapter == "day 017" or Chapter == "3" or Chapter == "017" or Chapter == "17" and ChapterSelc != 3:
                    print (" ")
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    time.sleep(1)
                    print (" ___               __  _ ____   _  _   __ _   ".center(120))
                    print ("|   \ __ _ _  _   /  \/ |__  | | \| | / //_)  ".center(120))
                    print ("| |) / _` | || | | () | | / /  | .` |/ // _ ) ".center(120))
                    print ("|___/\__,_|\_, |  \__/|_|/_/   |_|\_/_//_/ \_)".center(120))
                    print ("           |__/                               ".center(120))
                    time.sleep(1)
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    print (" ")
                    Chapter = 0
                    break


                #Invalid Input
                else:
                    print ("That is not a valid chapter.".center(120))
                continue

            #Return to menu or go to chapter
            if Chapter == 1 or Chapter == 2 or Chapter == 3:
                break
            elif Chapter == 0:
                time.sleep(2)
                continue
            else:
                continue
        #Credits
        elif Begin == "Credits" or Begin == "credits":
            print (" ")
            print (" ")
            print ("_".center (120,"_"))
            print (" ")
            time.sleep(1)
            print("   ___            _ _ _       ".center(120))
            print("  / __|_ _ ___ __| (_) |_ ___ ".center(120))
            print(" | (__| '_/ -_) _` | |  _(_-< ".center(120))
            print("  \___|_| \___\__,_|_|\__/__/ ".center(120))
            print("                              ".center(120))
            print (" ")

            #Copyrights
            time.sleep(0.5)
            print ("Copyright 2017 Reyaz Corporation.".center(120))
            print (" ")
            time.sleep (0.5)
            print ("All rights reserved. Reyaz, the Reyaz logo, Undead, the Undead logo".center(120))
            time.sleep (0.5)
            print ("are trademarks and/or registered trademarks of the Reyaz Corporation in Canada and other countries.".center(120))
            time.sleep (0.5)
            print (" ")
            time.sleep (0.5)
            #Owner
            print (" ___                           _   ___      ".center(80))
            print ("| _ \_____ __ _____ _ _ ___ __| | | _ )_  _ ".center(80))
            print ("|  _/ _ \ V  V / -_) '_/ -_) _` | | _ \ || |".center(80))
            print ("|_| \___/\_/\_/\___|_| \___\__,_| |___/\_, |".center(80))
            print ("                                       |__/ ".center(80))
            time.sleep(0.5)
            print ("         _           _    _        _          _             _         ".center(120))
            time.sleep(0.5)
            print ("        /\ \        /\ \ /\ \     /\_\       / /\         /\ \        ".center(120))
            time.sleep(0.5)
            print ("       /  \ \      /  \ \\ \ \   / / /      / /  \       /  \ \       ".center(120))
            time.sleep(0.5)
            print ("      / /\ \ \    / /\ \ \\ \ \_/ / /      / / /\ \   __/ /\ \ \      ".center(120))
            time.sleep(0.5)
            print ("     / / /\ \_\  / / /\ \_\\ \___/ /      / / /\ \ \ /___/ /\ \ \     ".center(120))
            time.sleep(0.5)
            print ("    / / /_/ / / / /_/_ \/_/ \ \ \_/      / / /  \ \ \\___\/ / / /     ".center(120))
            time.sleep(0.5)
            print ("   / / /__\/ / / /____/\     \ \ \      / / /___/ /\ \     / / /      ".center(120))
            time.sleep(0.5)
            print ("  / / /_____/ / /\____\/      \ \ \    / / /_____/ /\ \   / / /    _  ".center(120))
            time.sleep(0.5)
            print (" / / /\ \ \  / / /______       \ \ \  / /_________/\ \ \  \ \ \__/\_\ ".center(120))
            time.sleep(0.5)
            print ("/ / /  \ \ \/ / /_______\       \ \_\/ / /_       __\ \_\  \ \___\/ / ".center(120))
            time.sleep(0.5)
            print ("\/_/    \_\/\/__________/        \/_/\_\___\     /____/_/   \/___/_/  ".center(120))
            time.sleep(1)
            print (" ")
            print ("_".center (120,"_"))
            print (" ")
            print (" ")
            continue

        #Exit
        elif Begin == "Exit" or Begin == "exit":
            while True:
                Exit = raw_input ("Do you wish to exit the game now?")
                if Exit == "Yes" or Exit == "yes":
                    print (" ")
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    time.sleep(1)
                    print ("  ___               _ _             ".center(120))
                    print (" / __  ___  ___  __| | |__ _  _ ___".center(120))
                    print ("| (_--/ _ \/ _ \/ _` | '_ \ || / -_)".center(120))
                    print (" \___|\___/\___/\__,_|_.__/\_, \___|".center(120))
                    print ("                           |__/     ".center(120))
                    time.sleep(1)
                    print (" ")
                    print ("_".center (120,"_"))
                    print (" ")
                    exit (" ")
                elif Exit == "No" or Exit == "no":
                    break
                else:
                    print ("Please input 'Yes' or 'No'.".center(120))
                    continue
                continue

        #Invalid input
        else:
            print ("That is not a valid option.".center(120))
            continue

    #Introduction
    if Intro == "Go":
        print (" ")
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        time.sleep(1)
        print (" ")
        print ("An outbreak has occurred within the United States.".center(120))
        time.sleep(2.5)
        print ("The virus named Infection X has infected more than half the population.".center(120))
        time.sleep(2.5)
        print ("In the city of Atkinston, everyone has been evacuated and the infected have taken over.".center(120))
        print (" ")
        time.sleep(2.5)
        print (("You, ") + str(Name.capitalize()) + (", were left behind as the last helicopter left.")).center(120)
        time.sleep(2.5)
        print ("A safehaven location has been broadcasted, approximately 50 miles southeastern in the city of San Rodriguez.".center(120))
        time.sleep(2.5)
        print ("The United Nations has made the decision to quarantine the entire country.".center(120))
        time.sleep(2.5)
        print ("To survive you must make it to the safehaven location within the next 4 days.".center(120))
        time.sleep(2.5)
        print ("")
        time.sleep(2.5)
        print ("If you fail to do this, you will be stuck in a dying country with no chance of survival.".center(120))
        print (" ")
        time.sleep(1)
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")
        time.sleep(1)
        print ("*Note:* This is a RPG game where every decision you make will change the final outcome of the game.".center(120))
        time.sleep(2.5)
        print ("To find different endings, replay the chapters after the game has finished through the Menu.".center(120))
        time.sleep(1)
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")
    #No need for 'elif' or 'else' because of variable setting from beginning and menu

    #Chapter 1 (Day 013)
    while Chapter == 1:
        ChapterSela = 1
        #Introduction
        print (" ")
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        time.sleep(1)
        print ("=================================".center(120))
        time.sleep(0.4)
        print ("|  ___               __  _ ____ |".center(120))
        time.sleep(0.4)
        print ("| |   \ __ _ _  _   /  \/ |__ / |".center(120))
        time.sleep(0.4)
        print ("| | |) / _` | || | | () | ||_ \ |".center(120))
        time.sleep(0.4)
        print ("| |___/\__,_|\_, |  \__/|_|___/ |".center(120))
        time.sleep(0.4)
        print ("|            |__/               |".center(120))
        time.sleep(0.4)
        print ("=================================".center(120))
        print (" ")
        print (" ")
        time.sleep(1)
        print ("You wake up in the storage room of a local grocery store.".center(120))
        time.sleep(2.5)
        print ("You're refreshed, not hungry or thristy, and scared to leave your safehaven.".center(120))
        time.sleep(2.5)
        print ("There's food lying around, you have 9 spaces in your bag for supplies like food and water.".center(120))

        #Water and food determiner
        while True:
            Water = raw_input("With 9 spaces, how many of them do you devote to water?")
            try:
                Water = int(Water)
            except:
                print (" ")
                print ("Please enter digits only.")
                continue

            #Confirm
            if Water >=0 and Water <=9:
                while True:
                    print (" ")
                    WaterY = raw_input (("Are you sure you want ") + str(Water) + (" bottles of water?"))
                    if WaterY == "Yes" or WaterY == "yes":
                        print (("You have put ")+ str(Water) + (" bottles of water into your backpack.")).center(120)
                        Thirst = int(Water)*10
                        Food = 9 - int(Water)
                        Hunger = int(Food)*10
                        WaterY = "Yes"
                        break
                    elif WaterY == "No" or WaterY== "no":
                        WaterY = "No"
                        break
                    else:
                        print (" ")
                        print ("Please input 'Yes' or 'No'".center(120))
                        continue
            else:
                print (" ")
                print ("Please input a number from 0 - 9.".center(120))
                continue
            if WaterY == "Yes":
                break

            #Invalid Input
            else:
                continue

        #How long thirst/hunger will last
        print (" ")
        print (("Since you have devoted ") + str(Water) + (" spaces to water.")).center(120)
        time.sleep(2.5)
        print (("You have a remaining ") + str(Food) + (" spaces for meals.")).center(120)
        time.sleep(2.5)
        print (("Your thirst is at ") + str(Thirst) + ("%, and your hunger is at ") + str(Hunger) + ("%.")).center(120)
        time.sleep(2.5)
        print ("You will lose 10% thirst every half-day, and as well 5% hunger every half-day.".center(120))
        print (" ")
        time.sleep(2.5)
        print ("You hear noises around you, maybe throughout the store or even on the roof.".center(120))
        time.sleep(2.5)
        print ("With your backpack filled with your food, water, and a baseball bat.".center(120))

        #First Supplies
        time.sleep(2.5)
        print ("You prepare to venture out, but know you can fit one more thing into your backpack.".center(120))
        time.sleep(2.5)
        print ("On the ground around you there is a flashlight, binoculars, and an axe.".center(120))

        #Picking First Supplies
        while True:
            FirstSup = raw_input("Do you pick the flashlight, binoculars, or axe?")

            #Flashlight
            if FirstSup == "Flashlight" or FirstSup == "flashlight" or FirstSup == "Flash light":
                print (" ")
                print ("A flashlight has been put into your backpack.".center(120))
                FirstSup = "Flashlight"
                break

            #Binoculars
            elif FirstSup == "Binoculars" or FirstSup == "binoculars":
                print (" ")
                print ("Binoculars have been placed into your bag.".center(120))
                FirstSup = "Binoculars"
                break

            #Axe
            elif FirstSup == "Axe" or FirstSup == "axe":
                print (" ")
                print ("An axe has been placed into your bag.".center(120))
                FirstSup = "Axe"
                break

            #Invalid Input
            else:
                print (" ")
                print ("Please input 'Flashlight' or 'Binoculars' or 'Axe'.".center(120))
                continue

        #First loss of food/hunger
        Thirst = int(Thirst) - 10
        Hunger = int(Hunger) - 5
        print (" ")
        if Thirst <=0:
            time.sleep(2.5)
            print ("Your thirst has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died halfway through Day 013 because of dehydration.".center(120))
            break
        else:
            time.sleep(2.5)
            print (("Your thirst has dropped to ") + str(Thirst) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough water for 3 and 1/2 more days.").center(120)
            Score = Score + 10
        if Hunger <=0:
            time.sleep(2.5)
            print ("Your hunger has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died halfway through Day 013 because of hunger.".center(120))
            break
        else:
            time.sleep(2.5)
            print (("Your hunger has dropped to ") + str(Hunger) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough food for 3 and 1/2 more days.").center(120)
            Score = Score + 10

        #Leave or stay in store
        print (" ")
        time.sleep(2.5)
        print ("Now being prepared to venture out you still hear noises all around you.".center(120))
        time.sleep(2.5)
        print ("Leaving now means you would definitely be confronted by something,".center(120))
        time.sleep(2.5)
        print ("but it would allow you to begin your journey to the safehaven.".center(120))
        time.sleep(2.5)
        print ("You can make sure you're fully prepared for the journey by sleeping now.".center(120))
        time.sleep(2.5)
        print ("Otherwise you'll have to sleep some other time to make sure you won't die of exhaustion.".center(120))

        #Picking to leave or stay
        while True:
            LeaSt1 = raw_input("Would you like to stay in the store or leave the store?")
            if LeaSt1 == "Stay" or LeaSt1 == "stay" or LeaSt1 == "Stay in the store" or LeaSt1 == "stay in the store":
                print (" ")
                print ("You have decided to stay the night and you have enough energy for the entire journey.".center(120))
                LeaSt1 = "Stay"
                Score = Score + 10
                break
            elif LeaSt1 == "Leave" or LeaSt1 == "leave" or LeaSt1 == "Leave the store" or LeaSt1 == "leave the store":

                #If FirstSup = Flashlight
                if FirstSup == "Flashlight":
                    time.sleep(2.5)
                    print (" ")
                    print ("You have decided to leave the store and make way to your truck across the parking lot.".center(120))
                    time.sleep(2.5)
                    print ("You use your flashlight to find a safe path to your truck.".center(120))
                    time.sleep(2.5)
                    print ("Your flashlight breaks, but you made it to your truck and drove off before the infected could get to you.".center(120))
                    time.sleep(2.5)
                    print ("You have travelled 20 miles overnight.".center(120))
                    LeaSt1 = "Leave"
                    break

                #If FirstSup else
                else:
                    time.sleep(2.5)
                    print (" ")
                    print ("You have decided to leave the store and make way to your truck across the parking lot.".center(120))
                    time.sleep(2.5)
                    print ("The exit of the store is surrounded by the infected.".center(120))
                    time.sleep(2.5)
                    print ("You use your baseball bat to it's highest potential, it breaks in the fight.".center(120))
                    time.sleep(2.5)
                    print ("You see their are still many infected alive, some claw at you cutting your arms and legs.".center(120))
                    time.sleep(2.5)
                    LeaSt1 = "Leave"

                    #If FirstSup = Axe
                    if FirstSup == "Axe":
                        print (" ")
                        time.sleep(2.5)
                        print ("You tried to take your axe out, an infected grab it and hit you with it.".center(120))
                        time.sleep(2.5)
                        HealthAxe = (randint(5,20))
                        print (("The hit from the axe dealt ") + str(HealthAxe) + ("% of your health.")).center(120)
                        Health = Health - HealthAxe
                        print (" ")
                    print ("You successfully get to your truck, but you're badly injured and the infected have damaged your truck.".center(120))
                    time.sleep(2.5)
                    print (" ")
                    print ("You have lost 50% of your health.".center(120))
                    Health = Health - 50
                    if Health <=0:
                        time.sleep(2.5)
                        print ("Your health has dropped to 0%.".center(120))
                        time.sleep(2.5)
                        print ("You have died halfway through Day 013 because of your injuries.".center(120))
                        Dead = 1
                        break
                    else:
                        time.sleep(2.5)
                        print (("You now have a total of ") + str(Health) + ("% of your health left.")).center(120)
                        time.sleep(2.5)
                        print ("You have travelled 20 miles overnight.".center(120))
                        LeaSt1 = "Leave"
                        break

            #Invalid Input
            else:
                print (" ")
                print ("Please input 'Stay' or 'Leave'.".center(120))
                continue

        #If died leaving
        if Dead == 1:
            break

        #Second loss of food/hunger
        Thirst = int(Thirst) - 10
        Hunger = int(Hunger) - 5
        print (" ")
        if Thirst <=0:
            print ("Your thirst has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died at the end of Day 013 because of dehydration.".center(120))
            break
        else:
            print (("Your thirst has dropped to ") + str(Thirst) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough water for 3 more days.").center(120)
            Score = Score + 10
        if Hunger <=0:
            print ("Your hunger has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died at the end of Day 013 because of hunger.".center(120))
            break
        else:
            print (("Your hunger has dropped to ") + str(Hunger) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough food for 3 more days.").center(120)
            Score = Score + 10


        time.sleep(1)
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")
        time.sleep(1)

        #Chapter 1 (Day 014)
        print (" ")
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        time.sleep(1)
        print ("=================================".center(120))
        time.sleep(0.4)
        print ("|  ___               __  _ _ _  |".center(120))
        time.sleep(0.4)
        print ("| |   \ __ _ _  _   /  \/ | | | |".center(120))
        time.sleep(0.4)
        print ("| | |) / _` | || | | () | |_  _||".center(120))
        time.sleep(0.4)
        print ("| |___/\__,_|\_, |  \__/|_| |_| |".center(120))
        time.sleep(0.4)
        print ("|            |__/               |".center(120))
        time.sleep(0.4)
        print ("=================================".center(120))
        print (" ")
        print (" ")
        time.sleep(1)

        #If they stayed
        if LeaSt1 == "Stay":
            print (("You, ") + str(Name.capitalize()) + (", awake to no noise, you walk to your truck with ease and leave.")).center(120)
            time.sleep(2.5)
            print ("You travel 20 miles towards the safehaven, then stop at a barn.".center(120))
            time.sleep(2.5)

        #If they left
        elif LeaSt1 == "Leave":
            print (("You, ") + str(Name.capitalize()) + (", awake hurt in your truck, you're stopped infront of a barn.")).center(120)
            time.sleep(2.5)

        #Investigate Barn
        print ("You hear a noise in the barn, there isn't another bulding for miles.".center(120))
        time.sleep(2.5)
        print ("You think, 'What could possible be in there? There isn't civilization for miles.".center(120))
        time.sleep(2.5)

        #If LeaSt1 = leave and FirstSup = Axe
        if LeaSt1 == "Leave" and FirstSup == "Axe":
            print (" ")
            print ("Before you can make a move an infected breaks your window and finishes you off.".center(120))
            time.sleep(2.5)
            print ("It must have smelt all the blood from the attack last night.".center(120))
            Finished = "B"
            break

        #Else
        else:
            while True:
                Barn = raw_input("Do you enter the barn or stay in your vehicle?")

                #Enter the Barn
                if Barn == "Enter" or Barn == "enter" or Barn == "Enter the barn" or Barn == "enter the barn":
                    print (" ")
                    print ("An infected attacked you and dealt 10% of your health.".center(120))
                    Health = Health - 10
                    if Health <=0:
                        time.sleep(2.5)
                        print ("Your health has dropped to 0%.".center(120))
                        time.sleep(2.5)
                        print ("You have died early in Day 014 because of your injuries.".center(120))
                        Finished = "B"
                        print (" ")
                        break
                    else:
                        time.sleep(2.5)
                        print (("You have ") + str(Health) + ("% health left.")).center(120)
                        time.sleep(2.5)
                        print ("If your health gets to 0% you will die due to injuries".center(120))
                        time.sleep(2.5)
                        print ("You kill it off, and notice under it there is multiple bottles of water.".center(120))
                        time.sleep(2.5)
                        print ("You grab all the bottles and tape them to the outisde of your bag.".center(120))
                        time.sleep(2.5)
                        print ("You definitely will not have to worry about water for the rest of the journey!".center(120))
                        Thirst = Thirst + 60
                        Barn = "Enter"
                        break

                #Stay in truck
                elif Barn == "Stay" or Barn == "stay" or Barn == "Stay in your vehicle" or Barn == "stay in your vehicle":
                    print (" ")
                    print ("An infected snuck up on you, and broke your window to get to you.".center(120))
                    Health = Health - 20
                    if Health <=0:
                        time.sleep(2.5)
                        print ("Your health has dropped to 0%.".center(120))
                        time.sleep(2.5)
                        print ("You have died early in Day 014 because of your injuries.".center(120))
                        Finished = "B"
                        print (" ")
                        break
                    elif Health >=1:
                        time.sleep(2.5)
                        print (("You have ") + str(Health) + ("% health left")).center(120)
                        time.sleep(2.5)
                        print ("If you health drops to 0% you will die.".center(120))
                        print (" ")
                        time.sleep(2.5)
                        print ("It has taken 20% of your health before you could kill it.".center(120))
                        time.sleep(2.5)
                        print ("You see a few crates of bread and jam just outside of the barn.".center(120))
                        time.sleep(2.5)
                        print ("You get as many as you can and squish them into your bag.".center(120))
                        time.sleep(2.5)
                        print ("You definitely will not have to worry about water for the rest of the journey!".center(120))
                        Hunger = Hunger + 60
                        Barn = "Stay"
                        break

                #Invalid input
                else:
                    print (" ")
                    print ("Please input 'Enter' or 'Stay'.".center(120))
                    continue

        #If died in barn
        if Finished == "B":
            break


        #Third loss of food/hunger
        Thirst = int(Thirst) - 10
        Hunger = int(Hunger) - 5
        print (" ")
        if Thirst <=0:
            print ("Your thirst has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died halfway through Day 014 because of dehydration.".center(120))
            break
        else:
            print (("Your thirst has dropped to ") + str(Thirst) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough water for 2 and 1/2 more days.").center(120)
            Score = Score + 10
        if Hunger <=0:
            print ("Your hunger has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died halfway through Day 014 because of hunger.".center(120))
            break
        else:
            print (("Your hunger has dropped to ") + str(Hunger) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough food for 2 and 1/2 more days.").center(120)
            Score = Score + 10

        #Speed or Stay
        time.sleep(2.5)
        print (" ")
        print ("It's getting dark, that barn would be a safe place to stay.".center(120))
        time.sleep(2.5)
        print ("There is a chance to get to the safehaven with your truck overnight.".center(120))
        time.sleep(2.5)
        print ("You don't know how much longer the truck will last, there is a 25% chance you think it'll last.".center(120))
        time.sleep(2.5)

        #Speed or Stay decision
        while True:
            BarnLorS = raw_input ("Do you want to stay in the barn overnight or leave to get to the safehaven?")

            #Stay
            if BarnLorS == "Stay" or BarnLorS == "stay" or BarnLorS == "Stay in the barn" or BarnLorS == "stay in the barn":
                print (" ")
                print ("You have decided to stay in the barn overnight.".center(120))
                BarnLorS = "Stay"
                break

            #Leave
            elif BarnLorS == "Leave" or BarnLorS == "leave" or BarnLorS == "leave to get to the safehaven" or BarnLorS == "Leave to get to the safehaven":
                print (" ")
                print ("You have decided to leave and try to get to the safehaven tonight.".center(120))
                time.sleep(2.5)
                SpeedRan = (randint(1,4))

                #If successful
                if SpeedRan == 2:
                    print (" ")
                    print ("Your truck has lasted and has gotten you the rest of the way to San Rodriguez.".center(120))
                    time.sleep(2.5)
                    print ("You have found a spot to be evacuated and you're now resting guarded by the military.".center(120))
                    Score = Score + 200
                    time.sleep(2.5)
                    Finished = "A"
                    break

                #If not successful
                else:
                    print (" ")
                    print ("Your truck broke down half way to the safehaven.".center(120))
                    time.sleep(2.5)
                    print ("A group of the infected got to into your vehicle.".center(120))
                    time.sleep(2.5)
                    if FirstSup == "Axe":
                        print ("You went down fighting with your axe.".center(120))
                        break
                    else:
                        print ("You stood no chance..".center(120))
                        Finished = "B"
                        break

            #Invalid input
            else:
                print (" ")
                print ("Please input 'Leave' or 'Stay'.".center(120))
                continue

        #If finished
        if Finished == "A" or Finished == "B":
            break

        #Fourth loss of food/hunger
        Thirst = int(Thirst) - 10
        Hunger = int(Hunger) - 5
        print (" ")
        if Thirst <=0:
            print ("Your thirst has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died at the end of Day 014 because of dehydration.".center(120))
            break
        else:
            print (("Your thirst has dropped to ") + str(Thirst) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough water for 2 more days.").center(120)
            Score = Score + 10
        if Hunger <=0:
            print ("Your hunger has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died at the end of Day 014 because of hunger.".center(120))
            break
        else:
            print (("Your hunger has dropped to ") + str(Hunger) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough food for 2 more days.").center(120)
            Score = Score + 10

        time.sleep(1)
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")
        time.sleep(1)
        Chapter = 2
        break

    #Chapter 2 (Day 015)
    while Chapter == 2:
        ChapterSelb = 2
        #Introduction
        print (" ")
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        time.sleep(1)
        print ("=================================".center(120))
        time.sleep(0.4)
        print ("|  ___               __  _ ___  |".center(120))
        time.sleep(0.4)
        print ("| |   \ __ _ _  _   /  \/ | __| |".center(120))
        time.sleep(0.4)
        print ("| | |) / _` | || | | () | |__ \ |".center(120))
        time.sleep(0.4)
        print ("| |___/\__,_|\_, |  \__/|_|___/ |".center(120))
        time.sleep(0.4)
        print ("|            |__/               |".center(120))
        time.sleep(0.4)
        print ("=================================".center(120))
        print (" ")
        print (" ")
        time.sleep(1)
        print (("You, ") + str(Name.capitalize()) + (", woke up in the barn and want to quickly be on your way.")).center(120)
        time.sleep(2.5)
        print ("Before you leave you see 4 water bottles and 2 pieces of food.".center(120))

        #Adding food decision
        while True:
            AddFoodorWater1 = raw_input ("Do you take the water or the food?")

            #Water
            if AddFoodorWater1 == "Water" or AddFoodorWater1 == "water" or AddFoodorWater1 == "The water" or AddFoodorWater1 == "the water":
                print (" ")
                print ("You have decided to take the 4 bottles of water.".center(120))
                Thirst = Thirst + 40
                break

            #Food
            elif AddFoodorWater1 == "Food" or AddFoodorWater1 == "food" or AddFoodorWater1 == "The food" or AddFoodorWater1 == "the food":
                print (" ")
                print ("You have decided to take the 2 pieces of food.".center(120))
                Hunger = Hunger + 20
                break

            #Invalid Input
            else:
                print (" ")
                print ("Please input 'Water' or 'Food'.".center(120))

        #Scout ahead
        print (" ")
        time.sleep(2.5)
        print ("There are stairs up to the roof of the barn.".center(120))
        time.sleep(2.5)
        print ("It is very high, you could definitely scout out the route from up there.".center(120))
        time.sleep(2.5)

        #Decision to scout ahead
        while True:
            Scout = raw_input ("Do you want to scout ahead?")

            #stayed in store with flashlight
            if Scout == "Yes" or Scout == "yes" and LeaSt1 == "Stay" and FirstSup == "Flashlight":
                print (" ")
                print ("You don't see a better path in the distance anywhere.".center(120))
                time.sleep(2.5)
                print ("While walking back down you notice some bandages using your flashlight.".center(120))
                time.sleep(2.5)
                print ("You grab them and use them to heal yourself fully, there aren't any left over.".center(120))
                Health = (Health - Health) + 100
                break

            #left store with flashlight
            elif Scout == "Yes" or Scout == "yes" and LeaSt1 == "Leave" and FirstSup == "Flashlight":
                print (" ")
                print ("You don't see a better path in the distance anywhere.".center(120))
                time.sleep(2.5)
                break

            #stayed in store with axe
            elif Scout == "Yes" or Scout == "yes" and LeaSt1 == "Stay" and FirstSup == "Axe":
                print (" ")
                print ("You don't see a better path in the distance anywhere.".center(120))
                time.sleep(2.5)
                print ("While walking back down you notice a lock cabinet and break it open with your axe.".center(120))
                time.sleep(2.5)
                print ("You find some bandages, grab them, and use them to fully heal you.".center(120))
                Health = (Health - Health) + 100
                break

            #got binoculars
            elif Scout == "Yes" or Scout == "yes" and FirstSup == "Binoculars":
                print (" ")
                print ("You don't see a better path in the distance anywhere.".center(120))
                time.sleep(2.5)
                print ("You look back in the direction you came and you see a military vehicle in the far distance.".center(120))
                time.sleep(2.5)
                print ("You wait around at the top of the barn and notice they're coming your way!".center(120))
                time.sleep(2.5)
                print ("You go down, hit the horn on your truck, and they come pick you up.".center(120))
                Score = Score + 200
                Finished = "A"
                break

            #no
            elif Scout == "No" or Scout == "no":
                print (" ")
                print ("You decided not to go scout out the path.".center(120))
                break

            #Invalid Input
            else:
                print (" ")
                print ("Please input 'Yes' or 'No'.".center(120))
                continue

        #If finished with binoculars
        if Finished == "A":
            break

        #Fifth loss of food/hunger
        Thirst = int(Thirst) - 10
        Hunger = int(Hunger) - 5
        print (" ")
        if Thirst <=0:
            print ("Your thirst has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died halfway through Day 015 because of dehydration.".center(120))
            break
        else:
            print (("Your thirst has dropped to ") + str(Thirst) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough water for 1 and 1/2 more days.").center(120)
            Score = Score + 10
        if Hunger <=0:
            print ("Your hunger has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died halfway through Day 015 because of hunger.".center(120))
            break
        else:
            print (("Your hunger has dropped to ") + str(Hunger) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough food for 1 and 1/2 more days.").center(120)
            Score = Score + 10

        #Leaving barn
        print (" ")
        print ("Finally leaving the barn, you make your way towards San Rodriguez.".center(120))
        time.sleep(2.5)
        print ("You get 10 more miles with the truck before it breaks down, just as you enter a city.".center(120))
        time.sleep(2.5)
        print ("You're about 20 miles away, you'll have alot of walking to do.".center(120))
        time.sleep(2.5)
        print ("It's getting late and you have one more day to get to the safehaven.".center(120))
        time.sleep(2.5)
        print ("You hear infected throughout the city, if you go they will see you.".center(120))
        time.sleep(2.5)
        print ("You could stay in your truck and be safe, but that would make time a problem.".center(120))

        #Go through night or not
        while True:
            NightWalk = raw_input ("Do you want to walk or stay?")

            #Walk
            if NightWalk == "Walk" or NightWalk == "walk":
                print (" ")
                print ("The infected attacked you and dealt 40% of your health.".center(120))
                Health = Health - 40
                if Health <=0:
                        time.sleep(2.5)
                        print ("Your health has dropped to 0%.".center(120))
                        time.sleep(2.5)
                        print ("You have died at the end of Day 015 because of your injuries.".center(120))
                        Finished = "B"
                        print (" ")
                        break
                elif Health >=1:
                    time.sleep(2.5)
                    print (("You have ") + str(Health) + ("% health left")).center(120)
                    time.sleep(2.5)
                    print ("If you health drops to 0% you will die.".center(120))
                    print (" ")
                    print ("You covered about 15 miles in your night walk.".center(120))
                    time.sleep(2.5)
                    print ("You just need to cover 5 more miles in Day 016 to make it to the safehaven.".center(120))
                    Score = Score + 10
                    NightWalk = "Walk"
                    break

            #Stay
            elif NightWalk == "Stay" or NightWalk == "stay":
                print (" ")
                print ("You decided to stay the night in your truck.".center(120))
                NightWalk = "Stay"
                break

            #Invalid Input
            else:
                print (" ")
                print ("Please input 'Walk' or 'Stay'".center(120))
                continue

        #If died due to walk
        if Finished == "B":
            break

        #Sixth loss of food/hunger
        Thirst = int(Thirst) - 10
        Hunger = int(Hunger) - 5
        print (" ")
        if Thirst <=0:
            print ("Your thirst has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died at the end of Day 015 because of dehydration.".center(120))
            break
        else:
            print (("Your thirst has dropped to ") + str(Thirst) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough water for 1 more day.").center(120)
            Score = Score + 10
        if Hunger <=0:
            print ("Your hunger has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died at the end of Day 015 because of hunger.".center(120))
            break
        else:
            print (("Your hunger has dropped to ") + str(Hunger) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough food for 1 more day.").center(120)
            Score = Score + 10

        time.sleep(1)
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")
        time.sleep(1)

         #Chapter 2 (Day 016)
        print (" ")
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        time.sleep(1)
        print ("================================".center(120))
        time.sleep(0.4)
        print ("|  ___               __  _  __ |".center(120))
        time.sleep(0.4)
        print ("| |   \ __ _ _  _   /  \/ |/ / |".center(120))
        time.sleep(0.4)
        print ("| | |) / _` | || | | () | / _ \|".center(120))
        time.sleep(0.4)
        print ("| |___/\__,_|\_, |  \__/|_\___/|".center(120))
        time.sleep(0.4)
        print ("|            |__/              |".center(120))
        time.sleep(0.4)
        print ("================================".center(120))
        print (" ")
        print (" ")
        time.sleep(1)

        #They walk for NightWalk
        if NightWalk == "Walk":
            print ("A hoard of infected must have caught onto your bleeding from last night.".center(120))
            time.sleep(2.5)
            print ("The safehaven is 5 miles away, you could try to make a run for it.".center(120))
            time.sleep(2.5)
            print ("The hoard is small, you could try to fight them off.".center(120))

        #Run or fight
            while True:
                RunFight1 = raw_input ("Do you want to run or fight?")

                #Run
                if RunFight1 == "Run" or RunFight1 == "run":
                    print (" ")
                    print ("You made a run for it towards San Rodriguez.".center(120))
                    time.sleep(2.5)
                    print ("You got to the safehaven, fully exhausted, but notice the hoard followed you.".center(120))
                    time.sleep(2.5)
                    print ("The hoard has gotten huge, stragglers must have joined in when they were chasing you.".center(120))
                    time.sleep(2.5)
                    print ("Before the military could close the entrace, the hoard of infected broke and and got to everyone.".center(120))
                    time.sleep(2.5)
                    print ("This safehaven was therefore cut off from the rest due to the take over, all the survivors died.".center(120))
                    Finished = "B"
                    break

                #Fight
                elif RunFight1 == "Stay" or RunFight1 == "stay":
                    print (" ")
                    print ("You decide to hold your ground and fight.".center(120))
                    time.sleep(2.5)
                    print ("You take out the small hoard, bashing them, they take 40% of your health in return.".center(120))
                    Health = Health - 40
                    if Health <=0:
                        time.sleep(2.5)
                        print ("Your health has dropped to 0%.".center(120))
                        time.sleep(2.5)
                        print ("You have died halfway through Day 016 because of your injuries.".center(120))
                        Finished = "B"
                        print (" ")
                        break
                    elif Health >=1:
                        time.sleep(2.5)
                        print (("You have ") + str(Health) + ("% health left")).center(120)
                        time.sleep(2.5)
                        print ("If you health drops to 0% you will die.".center(120))
                        print (" ")
                        time.sleep(2.5)
                        print ("You are exhausted and take a break for a couple hours in a house off to the side of the road.".center(120))
                        break

                #Invalid Input
                else:
                    print (" ")
                    prnt ("Please input 'Run' or 'Fight'.".center(120))
                    continue

        #They stay for NightWalk
        elif NightWalk == "Stay":
            print ("You wake up, 1 day left to get to the safehaven 20 miles away.".center(120))
            time.sleep(2.5)
            print ("You don't plan to take any breaks, this is your last chance of survival.".center(120))
            time.sleep(2.5)
            print ("You begin to walk along the road, walking for hours.".center(120))
            time.sleep(2.5)
            print ("15 miles down, a small hoard of infected come your way, you fight them off.".center(120))
            time.sleep(2.5)
            print ("In doing so you they took 40% of your health.".center(120))
            Health = Health - 40
            if Health <=0:
                time.sleep(2.5)
                print ("Your health has dropped to 0%.".center(120))
                time.sleep(2.5)
                print ("You have died halfway through Day 016 because of your injuries.".center(120))
                Finished = "B"
                print (" ")
                break
            elif Health >=1:
                time.sleep(2.5)
                print (("You have ") + str(Health) + ("% health left")).center(120)
                time.sleep(2.5)
                print ("If you health drops to 0% you will die.".center(120))
                print (" ")
                time.sleep(2.5)
                print ("You are tired and go into a house at the side of the road to refresh.".center(120))


        #If died running from hoard
        if Finished == "B":
            break

        #Seventh loss of food/hunger
        Thirst = int(Thirst) - 10
        Hunger = int(Hunger) - 5
        print (" ")
        if Thirst <=0:
            print ("Your thirst has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died halfway through Day 016 because of dehydration.".center(120))
            break
        else:
            print (("Your thirst has dropped to ") + str(Thirst) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough water for 1/2 more of a day.").center(120)
            Score = Score + 10
        if Hunger <=0:
            print ("Your hunger has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died halfway through Day 016 because of hunger.".center(120))
            break
        else:
            print (("Your hunger has dropped to ") + str(Hunger) + ("%.")).center(120)
            time.sleep(2.5)
            print ("Remember to make sure you have enough food for 1/2 more of a day.").center(120)
            Score = Score + 10

        #Food/water in house
        print (" ")
        time.sleep(2.5)
        print ("The house has been almost cleaned out, except for some water and food.".center(120))
        time.sleep(2.5)
        print ("There isn't much, but it should help you get the rest of the way.".center(120))

        #Adding food decision
        while True:
            AddFoodorWater2 = raw_input ("Do you take the water or the food?")

            #Water
            if AddFoodorWater2 == "Water" or AddFoodorWater2 == "water" or AddFoodorWater2 == "The water" or AddFoodorWater2 == "the water":
                print (" ")
                print ("You have decided to take the 2 bottles of water.".center(120))
                Thirst = Thirst + 20
                break

            #Food
            elif AddFoodorWater2 == "Food" or AddFoodorWater2 == "food" or AddFoodorWater2 == "The food" or AddFoodorWater2 == "the food":
                print (" ")
                print ("You have decided to take the 1 piece of food.".center(120))
                Hunger = Hunger + 10
                break

            #Invalid Input
            else:
                print (" ")
                print ("Please input 'Water' or 'Food'.".center(120))

        #Trying to leave the house
        print (" ")
        time.sleep(2.5)
        print ("Just as you're going to leave the house, multiple infected surround the exits.".center(120))
        time.sleep(2.5)
        print ("There is no where to go, you can stay in the house or try to go through them.".center(120))

        #Leave or Stay in house
        while True:
            LeaSt2 = raw_input ("Do you want to leave or stay?")

            #Leave
            if LeaSt2 == "Leave" or LeaSt2 == "leave":
                print (" ")
                print ("You attempt to leave the house but the infected scratch you and claw at you taking 10% of your health.".center (120))
                Health = Health - 10
                if Health <=0:
                    time.sleep(2.5)
                    print ("Your health has dropped to 0%.".center(120))
                    time.sleep(2.5)
                    print ("You have died at the end of Day 016 because of your injuries.".center(120))
                    Finished = "B"
                    print (" ")
                    break
                elif Health >=1:
                    time.sleep(2.5)
                    print (("You have ") + str(Health) + ("% health left.")).center(120)
                    time.sleep(2.5)
                    print ("If you health drops to 0% you will die.".center(120))
                    print (" ")
                    time.sleep(2.5)
                    print ("You decide to barricade yourself in the house overnight, otherwise they will kill you.".center(120))
                    break

            #Stay
            elif LeaSt2 == "Stay" or LeaSt2 == "stay":
                print (" ")
                print ("You decide to barricade yourself in the house overnight, otherwise they will kill you.".center(120))
                Score = Score + 10
                break

            #Invalid Input
            else:
                print (" ")
                print ("Please input 'Leave' or 'Stay'.")
                continue

        #If died in house
        if Finished == "B":
            break

        #Eighth loss of food/hunger
        Thirst = int(Thirst) - 10
        Hunger = int(Hunger) - 5
        print (" ")
        if Thirst <=0:
            print ("Your thirst has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died at the end of Day 016 because of dehydration.".center(120))
            break
        else:
            print (("Your thirst has dropped to ") + str(Thirst) + ("%.")).center(120)
            time.sleep(2.5)
            print ("You have successfully stayed hydrated for the duration of the days.").center(120)
            Score = Score + 10
        if Hunger <=0:
            print ("Your hunger has dropped to 0%.".center(120))
            time.sleep(2.5)
            print ("You have died at the end of Day 016 because of hunger.".center(120))
            break
        else:
            print (("Your hunger has dropped to ") + str(Hunger) + ("%.")).center(120)
            time.sleep(2.5)
            print ("You have succesfully stayed sustained for the duration of the days.").center(120)
            Score = Score + 10

        time.sleep(1)
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")
        time.sleep(1)
        Chapter = 3
        break

    #Chapter 3 (Day 017)
    while Chapter == 3:
        ChapterSelc = 3
        #Introduction
        print (" ")
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        time.sleep(1)
        print ("================================".center(120))
        time.sleep(0.4)
        print ("|  ___             __  _ ____  |".center(120))
        time.sleep(0.4)
        print ("| |   \ __ _ _  _ /  \/ |__  | |".center(120))
        time.sleep(0.4)
        print ("| | |) / _` | || | () | | / /  |".center(120))
        time.sleep(0.4)
        print ("| |___/\__,_|\_, |\__/|_|/_/   |".center(120))
        time.sleep(0.4)
        print ("|            |__/              |".center(120))
        time.sleep(0.4)
        print ("================================".center(120))
        print (" ")
        print (" ")
        time.sleep(1)
        print (" ")
        print ("It's the morning of Day 017, you don't know when in the day the safehaven will be evacuated.".center(120))
        time.sleep(2.5)
        print ("You can't see any infected outside, you could try to make a run for it or stay and make sure they're gone.".center(120))

        #Leave or stay in house 2
        while True:
            LeaSt3 = raw_input ("Do you want to leave or stay?")

            #Leave if low health
            if LeaSt3 == "Leave" or LeaSt3 == "leave" and NightWalk == "Walk":
                Dmg1 = (randint(5,10))
                print (" ")
                print ("You leave the house, but the infected scratch you and claw at you taking ") + str(Dmg1) + ("% of your health.".center (120))
                Health = Health - Dmg1
                if Health <=0:
                    time.sleep(2.5)
                    print ("Your health has dropped to 0%.".center(120))
                    time.sleep(2.5)
                    print ("You have died early in Day 017 because of your injuries.".center(120))
                    Finished = "B"
                    print (" ")
                    break
                elif Health >=1:
                    time.sleep(2.5)
                    print (("You have ") + str(Health) + ("% health left")).center(120)
                    time.sleep(2.5)
                    print ("You run to the safehaven.".center(120))
                    time.sleep(2.5)
                    print ("Just as they seem to be packing up you make it.".center(120))
                    time.sleep(2.5)
                    print (str(Name.capitalize()) + (",you've successfully gotten into a helicopter and have left the country.")).center(120)
                    Score = Score + 200
                    Finished = "A"
                    print (" ")
                    break

            #Leave if low health
            elif LeaSt3 == "Leave" or LeaSt3 == "leave" and NightWalk == "Stay":
                Dmg2 = (randint(20,50))
                print (" ")
                print (("You leave the house, but the infected scratch you and claw at you taking ") + str(Dmg2) + ("% of your health.")).center (120)
                Health = Health - Dmg2
                if Health <=0:
                    time.sleep(2.5)
                    print ("Your health has dropped to 0%.".center(120))
                    time.sleep(2.5)
                    print ("You have died early in Day 017 because of your injuries.".center(120))
                    Finished = "B"
                    print (" ")
                    break
                elif Health >=1:
                    time.sleep(2.5)
                    print (("You have ") + str(Health) + ("% health left")).center(120)
                    time.sleep(2.5)
                    print ("You run to the safehaven.".center(120))
                    time.sleep(2.5)
                    print ("Just as they seem to be packing up you make it.".center(120))
                    time.sleep(2.5)
                    print (str(Name.capitalize()) + (",you've successfully gotten into a helicopter and have left the country.")).center(120)
                    Score = Score + 200
                    Finished = "A"
                    print (" ")
                    break


            #Stay
            elif LeaSt3 == "Stay" or LeaSt3 == "stay":
                print (" ")
                print ("You decide to stay in the house, infected do comeback and are outside again.".center(120))
                time.sleep(2.5)
                print ("By the time you can get out it's already mid-day 017.".center(120))
                time.sleep(2.5)
                print ("You make your way to the safehaven, but on your arrival you see it has already been evacuated.".center(120))
                Finished = "B"
                break

            #Invalid Input
            else:
                print (" ")
                print ("Please input 'Leave' or 'Stay'.")
                continue

        time.sleep(1)
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")
        time.sleep(1)
        break

    #Conclusion


    #End Game Credits if won
    if Finished == "A":
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")
        time.sleep(1)
        print ("  ___                        _        _      _   _             ".center(120))
        print (" / __|___ _ _  __ _ _ _ __ _| |_ _  _| |__ _| |_(_)___ _ _  ___".center(120))
        print ("| (__/ _ \ ' \/ _` | '_/ _` |  _| || | / _` |  _| / _ \ ' \(_-<".center(120))
        print (" \___\___/_||_\__, |_| \__,_|\__|\_,_|_\__,_|\__|_\___/_||_/__/".center(120))
        print ("              |___/                                            ".center(120))
        print (" ")
        print ("__   __          _  _                ___           _            ".center(120))
        print ("\ \ / /__ _  _  | || |__ ___ _____  | _ ) ___ __ _| |_ ___ _ _  ".center(120))
        print (" \ V / _ \ || | | __ / _` \ V / -_) | _ \/ -_) _` |  _/ -_) ' \ ".center(120))
        print ("  |_|\___/\_,_| |_||_\__,_|\_/\___| |___/\___\__,_|\__\___|_||_|".center(120))
        print (" ")
        print (" ")
        time.sleep (0.5)
        print ("                                                     _______      ".center (120))
        time.sleep (0.5)
        print ("                                                    (  ____ )     ".center (120))
        time.sleep (0.5)
        print ("         _        ______   _______  _______  ______(  )    ( )    ".center (120))
        time.sleep (0.5)
        print ("|\     /|( (    /|(  __  \ (  ____ \(  ___  )(  __  \__)    \ )   ".center (120))
        time.sleep (0.5)
        print ("| )   ( ||  \  ( || (  \  )| (    \/| (   ) || (  \  )       \ )  ".center (120))
        time.sleep (0.5)
        print ("| |   | ||   \ | || |   ) || (__    | (___) || |   ) |        ) ) ".center (120))
        time.sleep (0.5)
        print ("| |   | || (\ \) || |   | ||  __)   |  ___  || |   | |      _/ /  ".center (120))
        time.sleep (0.5)
        print ("| |   | || | \   || |   ) || (      | (   ) || |   ) |     |   )  ".center (120))
        time.sleep (0.5)
        print ("| (___) || )  \  || (__/  )| (____/\| )   ( || (__/  )      \_/   ".center (120))
        time.sleep (0.5)
        print ("(_______)|/    )_)(______/ (_______/|/     \|(______/             ".center (120))
        time.sleep(1)
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")

        #Credits
        print (" ")
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        time.sleep(1)
        print("   ___            _ _ _       ".center(120))
        print("  / __|_ _ ___ __| (_) |_ ___ ".center(120))
        print(" | (__| '_/ -_) _` | |  _(_-< ".center(120))
        print("  \___|_| \___\__,_|_|\__/__/ ".center(120))
        print("                              ".center(120))
        print (" ")

        #Copyrights
        time.sleep(0.5)
        print ("Copyright 2017 Reyaz Corporation.".center(120))
        print (" ")
        time.sleep (0.5)
        print ("All rights reserved. Reyaz, the Reyaz logo, Undead, the Undead logo".center(120))
        time.sleep (0.5)
        print ("are trademarks and/or registered trademarks of the Reyaz Corporation in Canada and other countries.".center(120))
        time.sleep (0.5)
        print (" ")
        time.sleep (0.5)

        #Owner
        print (" ___                           _   ___      ".center(80))
        print ("| _ \_____ __ _____ _ _ ___ __| | | _ )_  _ ".center(80))
        print ("|  _/ _ \ V  V / -_) '_/ -_) _` | | _ \ || |".center(80))
        print ("|_| \___/\_/\_/\___|_| \___\__,_| |___/\_, |".center(80))
        print ("                                       |__/ ".center(80))
        time.sleep(0.5)
        print ("         _           _    _        _          _             _         ".center(120))
        time.sleep(0.5)
        print ("        /\ \        /\ \ /\ \     /\_\       / /\         /\ \        ".center(120))
        time.sleep(0.5)
        print ("       /  \ \      /  \ \\ \ \   / / /      / /  \       /  \ \       ".center(120))
        time.sleep(0.5)
        print ("      / /\ \ \    / /\ \ \\ \ \_/ / /      / / /\ \   __/ /\ \ \      ".center(120))
        time.sleep(0.5)
        print ("     / / /\ \_\  / / /\ \_\\ \___/ /      / / /\ \ \ /___/ /\ \ \     ".center(120))
        time.sleep(0.5)
        print ("    / / /_/ / / / /_/_ \/_/ \ \ \_/      / / /  \ \ \\___\/ / / /     ".center(120))
        time.sleep(0.5)
        print ("   / / /__\/ / / /____/\     \ \ \      / / /___/ /\ \     / / /      ".center(120))
        time.sleep(0.5)
        print ("  / / /_____/ / /\____\/      \ \ \    / / /_____/ /\ \   / / /    _  ".center(120))
        time.sleep(0.5)
        print (" / / /\ \ \  / / /______       \ \ \  / /_________/\ \ \  \ \ \__/\_\ ".center(120))
        time.sleep(0.5)
        print ("/ / /  \ \ \/ / /_______\       \ \_\/ / /_       __\ \_\  \ \___\/ / ".center(120))
        time.sleep(0.5)
        print ("\/_/    \_\/\/__________/        \/_/\_\___\     /____/_/   \/___/_/  ".center(120))
        time.sleep(1)
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")

    #If lost
    elif Finished == "B":
        print (" ")
        print ("_".center (120,"_"))
        print (" ")
        print (" ")
        time.sleep(1)
        print ("__   __          _  _                ___     _ _        _   _____    ".center(120))
        print ("\ \ / /__ _  _  | || |__ ___ _____  | __|_ _(_) |___ __| | |_   _|__ ".center(120))
        print (" \ V / _ \ || | | __ / _` \ V / -_) | _/ _` | | / -_) _` |   | |/ _ |".center(120))
        print ("  |_|\___/\_,_| |_||_\__,_|\_/\___| |_|\__,_|_|_\___\__,_|   |_|\___/".center(120))
        print ("".center(120))
        print (" ")
        print (" ")
        time.sleep(0.5)
        print (" _______           _______          _________          _______ ".center(120))
        time.sleep(0.5)
        print ("(  ____ \|\     /|(  ____ )|\     /|\__   __/|\     /|(  ____ |".center(120))
        time.sleep(0.5)
        print ("| (    \/| )   ( || (    )|| )   ( |   ) (   | )   ( || (    \/".center(120))
        time.sleep(0.5)
        print ("| (======| |===| || (====)|| |===| |===| |===| |===| || (======".center(120))
        time.sleep(0.5)
        print ("(_____  )| |   | ||     __)( (   ) )   | |   ( (   ) )|  __)   ".center(120))
        time.sleep(0.5)
        print ("======) || |===| || (\ (====\ \=/ /====| |====\ \_/ /=| (======".center(120))
        time.sleep(0.5)
        print ("/\____) || (___) || ) \ \__  \   /  ___) (___  \   /  | (____/|".center(120))
        time.sleep(0.5)
        print ("\_______)(_______)|/   \__/   \_/   \_______/   \_/   (_______/".center(120))
        time.sleep(0.5)
        print ("".center(120))

    #Score
    if Score >=200:
        print (str(Name.capitalize()) + (" achieved a very high score of") + str(Score) + ("! Awesome Job!")).center(120)
        continue

    else:
        print (str(Name.capitalize()) + (" achieved a score of ") + str(Score) + (". Try again to get a higher score!")).center(120)
        continue

