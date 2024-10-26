import random

win_rules = {'Rock': ['Scissors', 'Lizard'],
            'Paper': ['Rock', 'Spock'],
            'Scissors': ['Paper', 'Lizard'],
            'Lizard': ['Paper', 'Spock'],
            'Spock': ['Rock', 'Scissors']}

first = input("Enter your choice: ")
second = random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])

if (first not in win_rules.keys()) or (second not in win_rules.keys()):
    print("Err")
elif first == second:
    print("Tie")
elif second in win_rules[first]:
    print(f"You won! My choice: {second}")
elif first in win_rules[second]:
    print(f'I won! My choice: {second}')