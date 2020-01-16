# 5 Play Again
solution = 5
playing = "yes"
guesses = 2
print("I am thinking of a number between 1 and 10. You have %d chances to guess!" % guesses)
while playing == "yes":
    playagain = ""
    if guesses == 0:
        print("You ran out of guesses")
        playagain = input("Would you like to play again? ")
        if playagain == "yes":
            guesses = 2
        else:
            playing = "no"
    else:
        guess = int(input("What's the number? "))
        if guess == solution:
            print("Yes, you win")
            playagain = input("Would you like to play again? ")
            if playagain == "yes":
                guesses = 2
            else:
                playing = "no"
        elif guess > solution:
            guesses -= 1
            print("%d is too high. You have %d guesses left." %
                  (guess, guesses))
        else:
            guesses -= 1
            print("%d is too low. You have %d guesses left." %
                  (guess, guesses))
