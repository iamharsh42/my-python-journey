import random

print("Get ready to guess numbers!")

range = input('Enter the last number: ')

if range.isdigit():
    range = int(range)
else:
    print('Enter a number next time!')
    quit()

random_number = random.randint(0, range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess == random_number:
            print("You guessed it correct!")
            break
        elif user_guess > random_number:
            print("Try a smaller number.")
        else:
            print("Try a larger number.")
    
    else:
        print("Enter a number next time.")

print("You guessed it in " + str(guesses) + " attempts")
