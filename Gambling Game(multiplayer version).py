import random

def roll():
    return random.randint(1, 6)

while True:
    number_of_players = int(input("Enter number of players (2 -> 4):\n"))
    if 2 <= number_of_players <= 4:
        break
    print("Invalid number of players. Please enter a number between 2 and 4.")

player_score = [0] * number_of_players
max_score = int(input("Enter the winning score (e.g., 50):\n"))

while max(player_score) < max_score:
    for player_idx in range(number_of_players):
        print(f"\nPlayer {player_idx + 1}'s turn has just started! 🚀")
        print(f"Your total score is {player_score[player_idx]}")

       
        current_score = 0
        while True:
            
            while True:
                should_roll = input("Do you want to roll? (y/n): 🤔 ").lower()
                if should_roll in ['y', 'n']:
                    break
                print("Invalid input. Please enter 'y' to roll or 'n' to stop.")

            if should_roll == 'y':
                value = roll()
                print(f"You rolled a {value}!")

                if value == 1:
                    current_score = 0
                    player_score[player_idx] += current_score  
                    print(f"You rolled a 1! Your turn ends, and your score in this round is {current_score} 😓")
                    break
                else:
                    current_score += value
                    print(f"Your current turn score is {current_score}, and your total score would be {player_score[player_idx] + current_score}. 🎲")
            else:
                player_score[player_idx] += current_score
                print(f"You chose to stop rolling. Your total score is now {player_score[player_idx]}.")
                break

        if player_score[player_idx] >= max_score:
            print(f"\n🎉 Player {player_idx + 1} just won with a score of {player_score[player_idx]}! 🎉")
            exit()  
