import random

def play_round():
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"Your number: {player_number}")
    guess = input("Do you think your number is higher or lower than the computer's number? (type 'higher' or 'lower'): ").strip().lower()

    if guess not in ['higher', 'lower']:
        print("Invalid input. Please type 'higher' or 'lower'.")
        return 0, 0  # No points awarded for invalid input

    if player_number == computer_number:
        print(f"It's a tie! The computer's number was also {computer_number}. The computer wins this round!")
        return 0, 1  # Computer wins a point in case of a tie
    elif (guess == 'higher' and player_number > computer_number) or \
         (guess == 'lower' and player_number < computer_number):
        print(f"The computer's number is {computer_number}")
        print(f"The player number is {player_number}")
        print(f"Correct! The computer's number was {computer_number}.")
        return 1, 0  # Player gets a point, computer gets none
    else:
        print(f"The computer's number is {computer_number}")
        print(f"The player number is {player_number}")
        print(f"Wrong! The computer's number was {computer_number}.")
        return 0, 1  # Computer gets a point, player gets none

def play_game(rounds):
    player_score = 0
    computer_score = 0

    for i in range(rounds):
        print(f"\nRound {i+1}")
        player_points, computer_points = play_round()
        player_score += player_points
        computer_score += computer_points

    print(f"\nGame over! Your final score is {player_score}/{rounds}.")
    print(f"Computer's final score is {computer_score}/{rounds}.")

total_rounds = int(input("How many rounds do you want to play? "))
play_game(total_rounds)
