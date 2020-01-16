# 7. Print a Box
width = int(input("Width? "))
whitespace = width - 2
height = int(input("Height? "))
i = 1

while i <= height:
    if i == 1 or i == height:
        print("* " * width)
    else:
        print("* " + ("  " * whitespace) + "*")
    i += 1
