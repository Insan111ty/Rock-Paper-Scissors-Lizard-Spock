win_rules = {'Rock': ['Scissors', 'Lizard'],
            'Paper': ['Rock', 'Spock'],
            'Scissors': ['Paper', 'Lizard'],
            'Lizard': ['Paper', 'Spock'],
            'Spock': ['Rock', 'Scissors']}

first = input("First player: ")
second = input("Second player: ")

if (first not in win_rules.keys()) or (second not in win_rules.keys()):
    print("Err")
elif first == second:
    print("Tie")
elif second in win_rules[first]:
    print("First player won!")
elif first in win_rules[second]:
    print('Second player won!')