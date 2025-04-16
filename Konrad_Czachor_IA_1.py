#Problem 1
projected_sales = float(input("What is the projected amount of sales?: ")) #Ask the user to input a value for the projected sales
profit_percentage = 0.23 #Constant variable set to 23% for the profit margin
projected_profit = projected_sales * profit_percentage #Calculate the projected profit from the users input and the profit percentage

print(f"The projected profit from your input is ${projected_profit:.2f}") #Output the final result

#Problem 2
total_duration = int(input("What is the total duration of the trip(in hours)?: ")) #Ask the user to input a value for the total duration of the trip
average_speed = int(input("What is the average speed(in miles per hour)?: ")) #Ask the user to input a value for the average speed in mph
total_distance = total_duration * average_speed #Calculate the total distance traveled from the users input for duration and speed

print(f"The total distance traveled is {total_distance} miles") #Output the final result