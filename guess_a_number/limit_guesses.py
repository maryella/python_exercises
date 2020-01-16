# 4 Limit guess
solution = random.randint(1, 10)
playing = True
guesses = 5
print("I am thinking of a number between 1 and 10. You have %d chances to guess!" % guesses)
while playing:
    guess = int(input("What's the number? "))
    if guess == solution:
        print("Yes, you win")
        playing = False
    elif guesses == 0:
        print("You ran out of guesses")
        playing = False
    elif guess > solution:
        guesses -= 1
        print("%d is too high. You have %d guesses left." % (guess, guesses))
    else:
        guesses -= 1
        print("%d is too low. You have %d guesses left." % (guess, guesses))
