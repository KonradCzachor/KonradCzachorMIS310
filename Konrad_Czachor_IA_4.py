budget = 0.0 #Variable to store the budget
total_expenses = 0.0 #Variable to store total expenses
expense = 1.0 #Variable for expenses
def main(): #Main function to call other functions and run the program
    global budget #Use the budget variable from earlier
    budget = float(input("Enter your monthly budget: $")) #Ask the user to provide their monthly budget and store it in budget variable

    budget_difference() #Call the budget_difference function
    budget_status() #Call the budget_status function

def budget_difference(): #Function to calculate the budget difference
    global total_expenses #Use the total_expenses variable from earlier
    global expense #Use the expense variable from earlier

    while expense != 0: #If the expense variable is not equal to 0, keep running the loop, if it is 0 then exit the loop
        expense = float(input("Enter an expense made: $")) #Ask user to enter an expense

        total_expenses += expense #Add the user provided expense to the total_expenses variable to keep a running total

def budget_status(): #Function to output if the budget was followed
    global budget #Use the budget variable from earlier
    global total_expenses #Use the total_expenses variable from earlier

    difference = budget - total_expenses #Calculate the difference between the budget and total expenses, store it in the difference variable

    print(f"Total Expenses: ${total_expenses:.2f}") #Print how much the user spent
    print(f"Budget Remaining: ${difference:.2f}") #Print how much of the budget is left

    if difference > 0: #If the difference is greater than 0, then the user was under budget
        print("Well done! You're under budget!")
    elif difference < 0: #If the difference is less than 0, then the user was over budget
        print("Plan better next time! You are over budget!")
    else: #If the difference was exactly 0, then the user was right on budget.
        print("Good planning! You are exactly on budget!")

main() #Call the main function to run the program