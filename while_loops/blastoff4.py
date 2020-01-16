# Blastoff 4
loopthru = True
num = int(input("Start the countdown at: "))
while loopthru:
    if num >= 20:
        print("Less than 20 please")
        num = int(input("Start the countdown at: "))
    else:
        if num > 0:
            print(num)
        else:
            print("Blast Off!")
            loopthru = False
        num -= 1
