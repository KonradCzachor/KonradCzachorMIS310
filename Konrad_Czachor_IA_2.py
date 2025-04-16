#Problem 1
user_age = int(input("Enter your age: ")) #Ask the user to input an age
if user_age <= 1: #If user_age is less than 1 then print the below message
    print(f"The person is {user_age} years old. Therefore, this person is an infant.")
elif user_age < 13 and user_age > 1: #If user_age is less than 13 but greater than 1 then print the below message
    print(f"The person is {user_age} years old. Therefore, this person is a child.")
elif user_age >= 13 and user_age < 20: #If user_age is greater than or equal to 13 but less than 20 then print the below message
    print(f"The person is {user_age} years old. Therefore, this person is a teenager.")
elif user_age >= 20 and user_age < 65: #If user_age is greater than for equal to 20 but less than 65 then print the below message
    print(f"The person is {user_age} years old. Therefore, this person is an adult.")
elif user_age >= 65: #If user_age is greater than for equal to 65 then print the below message
    print(f"The person is {user_age} years old. Therefore, this person is a senior.")

#Problem 2
user_input = int(input("Enter a number from 1-10 to receive the corresponding Roman number: ")) #Ask the user to input a number
if user_input == 1: #If user_Input is equal to 1 then print I
    print("I")
elif user_input == 2: #If user_Input is equal to 2 then print II
    print("II")
elif user_input == 3: #If user_Input is equal to 3 then print III
    print("III")
elif user_input == 4: #If user_Input is equal to 4 then print IV
    print("IV")
elif user_input == 5: #If user_Input is equal to 5 then print V
    print("V")
elif user_input == 6: #If user_Input is equal to 6 then print VI
    print("VI")
elif user_input == 7: #If user_Input is equal to 7 then print VII
    print("VII")
elif user_input == 8: #If user_Input is equal to 8 then print VIII
    print("VIII")
elif user_input == 9: #If user_Input is equal to 9 then print IX
    print("IX")
elif user_input == 10: #If user_Input is equal to 10 then print X
    print("X")
else: #If user_input is not between 1-10 then print the error message.
    print(f"{user_input} is not a valid number to convert to a Roman number. Please enter a number between 1 and 10.")