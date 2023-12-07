import random
import time
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def guide():
    print("\tCricket Match Simulation")
    print('Guide to play:')
    print('''First is Tossing
    If won the Toss user gets to choose Batting or Bowling.
    If you lose the Toss Computer decides it
    If user is batting user has to enter Number from 1 to 6
    Computer Generates a random value from 1 to 6
    User plays until he is Out
    After batting the computer bats and user bowls in the same manner''')


possible_actions = [1,2,3,4,5,6]
choices = ['batting','bowling']
user_score = 0
computer_score = 0
user_number = 0
computer_number = 0
innings = 0
user_is = ''

guide()

user_selection = int(input("For odd type 1 or For even type 0: "))
if user_selection not in ['1','0']:
    print('Invalid Number')
time.sleep(0.25)
user_action = int(input("Enter a number from (1 to 6) for toss: "))
computer_action = random.choice(possible_actions)
time.sleep(0.5)
print(f'computer number is {computer_action}')

if user_selection == 1:
    if (user_action + computer_action) % 2 == 1:
        print('you won the toss')
        user_is = input('batting or bowling: ')
    else:
        user_is = random.choice(choices)
        print('Computer won the toss')
elif user_selection == 0:
    if (user_action + computer_action) % 2 == 0:
        print('you won the toss')
        user_is = input('batting or bowling: ')
    else:
        user_is = random.choice(choices)
        print('Computer won the toss')

time.sleep(0.5)
print(f'congratulations you choose {user_is} first')
time.sleep(0.5)
clear_screen()

for _ in range(3):
    print('.',end='')
    time.sleep(0.45)
print('🏏')
time.sleep(0.45)
print('Match Starts')

while innings != 2:
    if user_is.lower() == 'batting':
        user_number = int(input('Enter number from 1 to 6 to Bat: '))
        time.sleep(0.5)
        computer_number = random.choice(possible_actions)
        print(f'Computer choice: {computer_number}')
        if user_number != computer_number:
            user_score += user_number
            time.sleep(0.5)
            print(f'Total Runs = {user_score}')
        else:
            print("it's an out")
            time.sleep(0.5)
            print(f'Total run = {user_score}')
            user_is = 'bowling'
            innings += 1
            if innings == 1:
                print(f'you are {user_is}')
        if innings == 1 and computer_score > user_score:
            break
    else:
        user_number = int(input('Enter number from 1 to 6 to Bowl: '))
        computer_number = random.choice(possible_actions)
        time.sleep(0.5)
        print(f'Computer choice: {computer_number}')
        if user_number != computer_number:
            computer_score += computer_number
            time.sleep(0.5)
            print(f'Total Runs = {computer_score}')
        else:
            print("it's an out")
            time.sleep(0.5)
            print(f'Total run = {computer_score}')
            user_is = 'batting'
            innings += 1
            if innings == 1:
                print(f'you are {user_is}')

        if innings == 1 and computer_score > user_score:
            break

if computer_score > user_score:
    print('Computer won the match')
else:
    print('yay you won the match')
