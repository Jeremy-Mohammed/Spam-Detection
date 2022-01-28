#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      s201016279
#
# Created:     07/04/2017
# Copyright:   (c) s201016279 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Inputting information from the user
company = raw_input("What is your company's name?")
street = raw_input("What street is your business located on?")
phone = raw_input("What is your business's phone number?")
date = raw_input("What is the date today?")
time = raw_input("What time is it? (h:mm tt format)")
barber = raw_input("What is the barber's name who performed on the customer?")
customer = raw_input("What is the customer's name?")
couponr = raw_input("What date is the receipt coupon vaild until?")
valuer = raw_input("What is the value of the receipt coupon? (Numerical)")
price = raw_input("What is the price of the haircut? (Numerical)")
tendered = raw_input("How much did the customer tender to the cashier? (Numerical)")
coupon = raw_input("What is the value of the coupon given by customer? (Numerical)")

#Calculating sales
hn = (float(price) - float(coupon))
ht = (float(hn) * float(1.13))
change = (float(tendered) - float(ht))
change = float(change)

#Outputting Receipt
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" ")
print("          ") + (company)
print(" ")
print("       ") + (street) + (" ") + (phone)
print("  ") + ("   ") + ("   ") + (time) + (" ") + (date) + (" ") + (barber)
print("  ")
print(" ") + (customer)
print(" ")
print(" ") + ("Haircut") + ("                   ") + ("   ") + ("$") + (price)
print(" ")
print("   ") + ("$") + (coupon) + ("     ") + ("Coupon") + ("   ") + (" Subtotal")+ ("   ") + ("$") + (str(hn))
print("                    ") +("Total") + ("   ") + ("$") + str(ht)
print(" ")+ ("   ") + ("    ") + ("          ") +  ("Amt Tendered") + ("   ") + ("$") + (tendered)
print("                    ") + ("Change") + ("   ") + ("$") + str(change)
print(" ")
print(" ") + ("Thank you for choosing ") + (company) + ("!")
print(" ")
print(" ") + ("  ") + ("$") + (valuer) + (" NOT VALID WITH OTHER OFFERS")
print(" ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" ")
print(" ") + ("    ") + ("Coupon valid until ") + (couponr)