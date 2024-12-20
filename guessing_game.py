secret_number = 7

guess_count = 0

guess = 0

while guess != secret_number:
    guess_count += 1
    guess = int(input("Input a number that is between 1 and 10"))

print(f"You guessed {guess_count} times before arriving at correct value. Thank you for your patience.")


# This simple game prompts the user to guess a number equivalent to the secret number
# guess_count is the counter keeping record of the number of guesses a user tries.
