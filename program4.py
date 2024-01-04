# Write a program in python to demonstrate control statement break.
secret_number = 42
while True:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        # Break out of the loop if the guess is correct
        break
    elif guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
print("End of the program.")