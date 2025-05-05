#Problem 1
humidity_level = float(input("Enter current humidity level: ")) #Ask user for current humidity level

if humidity_level < 40: #If humidity level is less than 40 then print the message
    print("Turn on the high-intensity misting system, wait 3 minutes and check again.")
elif humidity_level < 50 and humidity_level > 40: #If humidity level is between 40 and 50, print the message
    print("Turn on the low-intensity misting system, wait 3 minutes and check again.")
else: #if humidity level is above 50, print the message
    print("The humidity level is satisfactory.")

#Problem 2
user_month = int(input("Enter month as a number (1-12): ")) #Ask user to input a month
user_day = int(input("Enter day as a number (1-31): ")) #Ask user to input a day
user_year = int(input("Enter year as a two digit number (0-99): ")) #Ask user to input a year

if user_month < 1 or user_month > 12: #Check if the provided month is valid
    print("Invalid month. Please enter a valid month.")
if user_day < 1 or user_day > 31: #Check if the provided day is valid
    print("Invalid day. Please enter a valid day.")
if user_year < 0 or user_year > 99: #Check if the provided year is valid
    print("Invalid year. Please enter a valid year.")

#Check if the provded month, day, and year is valid
if user_month >= 1 and user_month <= 12 and user_day >= 1 and user_day <= 31 and user_year >= 0 and user_year <= 99:
    if user_year == user_month * user_day: #If valid, check if it is a magic date
        print("This is a magic date!") #Prints if it is a magic date
    else:
        print("This is not a magic date!") #Prints if it is not a magic date
