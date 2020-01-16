# Guess the number
solution = '5'
playing = True
print("I am thinking of a number between 1 and 10.")
while playing:
    guess = input("What's the number? ")
    if guess == solution:
        print("Yes, you win")
        playing = False
    else:
        print("No, try again")
