import random

options = {'r': '🪨 (Rock)', 'p': '📃 (Paper)', 's': '✂️ (Scissors)'}

while True:
    random_choice = random.choice(list(options.keys()))

    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()

    if user_choice not in options:
        print("Please enter a valid choice (r, p, s).")
        continue

    print(f"You chose: {options[user_choice]}")
    print(f"Computer chose: {options[random_choice]}")

    if user_choice == random_choice:
        print("You and the computer chose the same option, so it's a DRAW! 🤝")
    elif (user_choice == 'r' and random_choice == 's') or \
         (user_choice == 's' and random_choice == 'p') or \
         (user_choice == 'p' and random_choice == 'r'):
        print("You WON! 😁")
    else:
        print("You LOST! 😓")

    again = input("Do you want to play again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing! Goodbye! 👋")
        break