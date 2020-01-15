# 10. How many coins?
coins = 0
asking = True
while asking:
    answer = input("You have %d coins. Do you want another?" % coins)
    if answer == "yes":
        coins += 1
    else:
        asking = False
        print("Bye")
