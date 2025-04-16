import random

#Function for a dice roll
def roll_dice():
    return random.randint(1, 6)

#Function to play a round of dice
def play_round(player1roll, player2roll):
    if player1roll > player2roll: #Print if Player 1 has a higher number then Player 2
        print(f"Player 1 rolls a {player1roll}, Player 2 rolls a {player2roll}. Player 1 wins the round.")
    elif player1roll < player2roll: #Print if Player 1 has a lower number than Player 1
        print(f"Player 1 rolls a {player1roll}, Player 2 rolls a {player2roll}. Player 2 wins the round.")
    else: #Print if it is a tie
        print(f"Player 1 rolls a {player1roll}, Player 2 rolls a {player2roll}. The round is a tie.")

#Main function
def main():
    rounds_to_play = int(input("How many rounds would you like to play? ")) #Ask user to provide how many rounds to play

    player1wins = 0 #Variable to keep track of Player 1s wins
    player2wins = 0 #Variable to keep track of Player 2s wins
    ties = 0 #Variable to keep track of ties

    for rounds in range(rounds_to_play): #For loop to iterate through the user provided number of rounds
        player1roll = roll_dice() #Call the roll_dice() function to roll the dice for player 1
        player2roll = roll_dice() #Call the roll_dice() function to roll the dice for player 2

        if player1roll > player2roll: #If Player 1 has a higher number than Player 2, add one to player1wins
            player1wins += 1
        elif player1roll < player2roll: #If Player 1 has a lower number than Player 2, add one to player2wins
            player2wins += 1
        else:
            ties += 1 #If it ends in a tie, add 1 to ties

        play_round(player1roll, player2roll) #Print result of each round

    #Print Final score for each player and ties
    print(f"Final Score: Player 1 won {player1wins} round(s). "
          f"Player 2 won {player2wins} round(s). "
          f"{ties} round(s) ended in a tie.")

    if player1wins > player2wins: #If Player 1 has a higher number than Player 2, print that Player 1 was the winner
        print(f"Overall Winner: Player 1")
    elif player1wins < player2wins:
        print(f"Overall Winner: Player 2") #If Player 1 has a lower number than Player 2, print that Player 2 was the winner
    else:
        print(f"Overall Winner: No one, it has ended in a tie.") #If ties was higher than both player 1 and player 2 wins, then print that it ended in a tie.

#Call main function to start
main()
