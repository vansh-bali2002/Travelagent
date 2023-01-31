# Travel Agent Bot
# Author: Macklin Tsang and Vansh Bali
# Date: Jan 16, 2023

# The purpose of this bot is to suggest trips with prices included based on the information provided by the user.

import random

# 1. Display the welcome message

print('''
Welcome ! I am your friendly travel agent bot.
I will ask you some questions , and make a
recommendation based on your answer .
If you are interested , I will provide you
with a one -time password to create a user
account on our website 
''')

# 2. Prompt for the users name

name = input("What is your name? --> ")
print("Hello dear " + name + " ! \n")

# 3. Prompt for the users age.

age = int(input("What is your age? --> "))

if age > 64:
    print("Great ! We offer a senior discount ." + "\n" + "For every year over 64 , you get 1% off ." + "\n")
    discount=age-64
else:
    print()
    discount=0

# 4. Prompt for number of nights the user wants to stay.

nights = int(input('For how many nights do you want to stay? --> '))

# 5. Ask user if they like cultural and classical music.

music = input('Do you like cultural and classical music?' + "\n" + "Please answer y/n. --> ").lower().strip("!?.")

# 6. Ask user if they like beaches and surfing.

beach = input('Do you like beaches and surfing?' + "\n" + "Please answer y/n. --> ").lower().strip("!?.")

# 7. Based on user response, determine whether they will be offered a trip to Vienna or Bali or none.

# This is the formula to calculate the total costs for Bali & Vienna vacation.
# The calculation is (Flight+Hotel*nights) * Discount (if necessary)

Bali = (849.93 + (235.35 * nights)) * (1.0 - int(discount)/100)

Vienna = (997.93 + (143.84 * nights)) * (1.0 - int(discount)/100)

# If the user selected no to both questions, the bot will not offer any trips.

if beach == "n" and music == "n":
    print("\n" + "I am sorry, we do not have any trips to offer at this point.")

# If the user selected yes to both questions, it will select the most expensive trip.

if beach == "y" and music == "y":
    if Vienna > Bali:
        print('')
        print("How about a trip to Vienna?")
        print("Flight: 997.93$")
        print("Hotel: 143.84$/night")
        print("Discount: " + str(discount) + "%")
        print("Total for " + str(nights) + " nights (incl. discounts): "+ str(Vienna) + "$")
    else:
        print('')
        print("How about a trip to Bali?")
        print("Flight: 849.93$")
        print("Hotel: 235.35$/night")
        print("Discount: " + str(discount) + "%")
        print("Total for " + str(nights) + " nights (incl. discounts): " + str(Bali) + "$")

# If the user selected yes for music, and no for beaches, the bot will select the trip to Vienna.

if music == "y" and beach == "n":
    print('')
    print("How about a trip to Vienna?")
    print("Flight: 997.93$")
    print("Hotel: 143.84$/night")
    print("Discount: " + str(discount) + "%")
    print("Total for " + str(nights) + " nights (incl. discounts): " + str(Vienna) + "$")

# If the user selected yes for beaches but no for music, the bot will select a trip to Bali.

if music == "n" and beach == "y":
    print('')
    print("How about a trip to Bali?")
    print("Flight: 849.93$")
    print("Hotel: 235.35$/night")
    print("Discount: " + str(discount) + "%")
    print("Total for " + str(nights) + " nights (incl. discounts): " + str(Bali) + "$")

# User-defined Password generation function
# There is no input, the function is returning the user one time password (string)

def password():

    # This will select the first character of the user's name
    password_first_character = str(name[0])

    # This will select the last character
    password_last_character = str(name[-1])

    # The variable will save the remainder of the age divided by 8
    n = age % 8

    # Create a variable and set it to the formula of the password.
    password = password_last_character * int(n) + password_first_character + (random.randint(0, 5) * "!")
    return password

# 8. Ask if the user would like to make an account, regardless of whether or not they are offered a trip.

print('')

account = input("Are you interested , and want to create a user account ?" + "\n" + "Please answer y/ n. --> ").lower().strip("!?.")

# If they are not interested in creating an account, the program will say sorry and to consider the service again.
if account == "n":
    print("Sorry to hear that . Please consider using our service again .")

# If they are interested in creating an account, them display the one time password and a goodbye message
elif account =="y":
    print("Looking forward to working with you! ")
    print("Your one time password is: " + password())
    print("Goodbye.")