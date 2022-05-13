import itertools
from random import choice
import os

possible_values = ["rock", "paper", "scissors"]
combinations = list(itertools.product(possible_values, repeat=2))
combinations_history = {combination: 0 for combination in combinations}

game_round = 1
again = 'y'
while again == 'y':
    print('\x1b[0;5;31m', f"\nGame Round = {game_round}", '\x1b[0m')
    computer = choice(possible_values)
    player = str(input('\x1b[0;0;34m' + 'rock? paper? scissors? : '))
    print('\x1b[0;2;32m', f'Player Choice: {player}', '\x1b[0m')
    print('\x1b[0;2;33m', f'Computer Choice: {computer}', '\x1b[0m')

    if player == computer:
        print('\x1b[0;0;31m' + 'Match Result:', '\x1b[0;2;36m', 'Draw', '\x1b[0m')
    elif player == "rock" and computer == "scissors":
        print('\x1b[0;0;31m' + 'Match Result:', '\x1b[0;2;36m', 'Player Wins', '\x1b[0m')
    elif player == "rock" and computer == "paper":
        print('\x1b[0;0;31m' + 'Match Result:', '\x1b[0;2;36m', 'Computer Wins', '\x1b[0m')
    elif player == "paper" and computer == "scissors":
        print('\x1b[0;0;31m' + 'Match Result:', '\x1b[0;2;36m', 'Computer Wins', '\x1b[0m')
    elif player == "paper" and computer == "rock":
        print('\x1b[0;0;31m' + 'Match Result:', '\x1b[0;2;36m', 'Player Wins', '\x1b[0m')
    elif player == "scissors" and computer == "paper":
        print('\x1b[0;0;31m' + 'Match Result:', '\x1b[0;2;36m', 'Player Wins', '\x1b[0m')
    elif player == "scissors" and computer == "rock":
        print('\x1b[0;0;31m' + 'Match Result:', '\x1b[0;2;36m', 'Computer Wins', '\x1b[0m')
    game_round += 1
    print('\x1b[0;2;31m', '-'*50, '\x1b[0m')
    again = str(input(f'type "y" if you wanna play again :'))
    os.system('clear')

