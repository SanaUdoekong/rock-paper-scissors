# If the two players choose the same “character” it’s a tie, and the game repeats
# Rock beats Scissors
# Paper beats Rock
# Scissors beats Paper
# You have been tasked to create a simple version of this game with Python. In your version, one player will be controlled by the computer and the other player controlled by you - the user (i.e CPU vs Player). 

# You should make use of the inbuilt Python module random and its choice method.
import random

def play_game():
    # Create a list to store all possible options:
    # "R" for "rock", 
    # "P" for "paper", 
    # "S" for "scissors".
    choices = ["R", "P", "S"]

    # When the program is run, ask the user to pick an option between "R", "P" or "S"
    user_input = input("Welcome to Rock-Paper-Scissors! Pick an option('R':'Rock', 'P':'Paper', 'S':'Scissors'): ")
    user_move = ''
    # If user input is invalid (not amongst our options), print an error, and ask for their input again (should be a loop)
    while user_input.upper() not in choices:
        print('Please pick a valid option! \n')
        user_input = input("Welcome to Rock-Paper-Scissors! Pick an option('R':'Rock', 'P':'Paper', 'S':'Scissors'): ")
        break

    if user_input.upper() == "R":
        user_move = 'Rock'
    elif user_input.upper() == "P":
        user_move = 'Paper'
    elif user_input.upper() == "S":
        user_move = 'Scissors'

    # Use the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).
    computer_move = random.choice(choices)
    cpu_move = ''

    if computer_move == "R":
        cpu_move = 'Rock'
    elif computer_move == "P":
        cpu_move = 'Paper'
    elif computer_move == "S":
        cpu_move = 'Scissors'

    # Print both player's moves in the format: `Player (Rock) : CPU (Paper)`
    print(f"Player ({user_move}) : CPU ({cpu_move})")
    compareMoves(user_input.upper(), computer_move)

# Check both player's moves:
# If there is a winner, print the winner, and the program ends. 
def compareMoves(player, cpu):
    if (player == 'R' and cpu == 'S') or (player == 'P' and cpu == 'R') or (player == 'S' and cpu == 'P'):
        print('You win!')
        # If it's a tie (the computer and player pick the same move), restart the game from step 3
    elif(player == cpu):
        print("It's a tie, rematch! \n")
        play_game()
    else:
        print('You lose!')


play_game()