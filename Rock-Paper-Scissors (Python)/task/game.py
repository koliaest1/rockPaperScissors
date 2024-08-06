# Write your code here
import random


def sort_list(options_list, option):
    length = len(options_list)
    winning_options = length // 2
    if options_list.index(option) < winning_options:
        move = (winning_options - options_list.index(option))
        options_list = options_list[(-1) * move:] + options_list[:(-1) * move]
    elif options_list.index(option) > winning_options:
        move = (options_list.index(option) - winning_options)
        options_list = options_list[move:] + options_list[:move]
    return options_list


def winning_option(user_choice, computer_choice, game_options):
    score = 0
    sorted_options_list = sort_list(game_options, user_choice)
    if user_choice == computer_choice:
        score += 50
        print(f'There is a draw ({user_choice})')
    elif sorted_options_list.index(user_choice) > sorted_options_list.index(computer_choice):
        score += 100
        print(f'Well done. The computer chose {computer_choice} and failed')
    elif sorted_options_list.index(computer_choice) > sorted_options_list.index(user_choice):
        print(f'Sorry, but the computer chose {computer_choice}')
    return score


def get_score(user_name):
    file_name = open('rating.txt', 'r')
    for line in file_name:
        name, score = line.split()
        if name == user_name:
            return int(score)
        else:
            return 0


def main():
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    user_score = get_score(name)
    game_options = input()
    if game_options:
        game_options = game_options.split(',')
    else:
        game_options = ['rock', 'paper', 'scissors']
    print("Okay, let's start")
    while True:
        user_turn = input()
        computer_turn = random.choice(game_options)
        if user_turn == "!exit":
            print('Bye!')
            exit()
        elif user_turn == '!rating':
            print(f'Your rating: {user_score}')
        elif user_turn in game_options:
            user_score += winning_option(user_turn, computer_turn, game_options)
        else:
            print('Invalid input')


if __name__ == "__main__":
    main()
