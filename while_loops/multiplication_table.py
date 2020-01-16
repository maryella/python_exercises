# 9. Multiplication table
x = 1
while x <= 10:
    y = 1
    while y <= 10:
        result = x * y
        print(str(x) + " X " + str(y) + " = " + str(result))
        y += 1
    x += 1
