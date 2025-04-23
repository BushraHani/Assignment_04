#Control Flow for Console


import random

def play_round():
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"\nYour number is: {player_number}")
    guess = input("Do you think your number is higher or lower than the computer's? (type 'higher' or 'lower'): ").strip().lower()

    if guess not in ['higher', 'lower']:
        print("Invalid input! You lose this round.")
        return 0

    print("The computer's number was:", computer_number)

    if guess == 'higher' and player_number > computer_number:
        print("You guessed right! +1 point")
        return 1
    elif guess == 'lower' and player_number < computer_number:
        print("You guessed right! +1 point")
        return 1
    elif player_number == computer_number:
        print("It's a tie! No points awarded.")
        return 0
    else:
        print("Wrong guess. No points this round.")
        return 0

def play_game():
    print("Welcome to the High-Low Game!")
    rounds = int(input("How many rounds would you like to play? "))

    score = 0
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        score += play_round()

    print(f"\nGame over! Your final score is: {score} out of {rounds}")

if __name__ == "__main__":
    play_game()
