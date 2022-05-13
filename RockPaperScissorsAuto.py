from random import choice
from time import sleep

possible_values = ["rock", "paper", "scissors"]
round_count = int(input('Enter Rounds: '))
computer_score = 0
player_score = 0
game_history = []

while round_count != 0:

    computer = choice(possible_values)
    player = choice(possible_values)
    game_history.append([computer, player])
    computer_win_condition = [['rock', 'scissors'],
                              ['paper', 'rock'],
                              ['scissors', 'paper']]
    if computer == player:
        print('\x1b[0;0;31m' + 'Match Result:',
              '\x1b[0;2;36m', 'Draw', '\x1b[0m')
        sleep(0.5)
    elif [computer, player] in computer_win_condition:
        print('\x1b[0;0;31m' + 'Match Result:',
              '\x1b[0;2;33m', 'Computer Wins', '\x1b[0m')
        computer_score += 1
        sleep(0.5)
    else:
        print('\x1b[0;0;31m' + 'Match Result:',
              '\x1b[0;2;32m', 'Player Wins', '\x1b[0m')
        player_score += 1
        sleep(0.5)
    round_count -= 1

if player_score > computer_score:
    print(f"\n\x1b[0;2;37mTotal Match Result: \x1b[0;2;32mPlayer Won")
    sleep(0.5)
elif player_score == computer_score:
    print(f"\n\x1b[0;2;37mTotal Match Result: \x1b[0;2;36mDraw")
    sleep(0.5)
else:
    print(f"\n\x1b[0;2;37mTotal Match Result: \x1b[0;2;33mComputer Won")
    sleep(0.5)

print(f"\x1b[0;2;37mHistory[Computer, Player]: \x1b[0;2;47m{game_history}\x1b[0;2;30m")
