#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      s201016279
#
# Created:     10/04/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
grade = raw_input("What is your numeric grade?")
grade = float(grade)

if grade >=94:
    print("Your letter grade is A.")

elif grade >=90:
    print("Your letter grade is A-.")

elif grade >=87:
    print("Your letter grade is B+.")

elif grade >=83:
    print("Your letter grade is B.")

elif grade >=80:
    print("Your letter grade is B-.")

elif grade >=77:
    print("Your letter grade is C+.")

elif grade >=73:
    print("Your letter grade is C.")

elif grade >=70:
    print("Your letter grade is C-.")

elif grade >=67:
    print("Your letter grade is D+.")

elif grade >=60:
    print("Your letter grade is D.")

else :
    print("Your letter grade is F.")

