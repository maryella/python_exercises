# # 8. Print a Triangle
height = int(input("How tall should triangle be? "))
i = 0

while i < height:
    stars = ((i * 2) + 1) * "*"
    whitespace = int(height - 1 - i) * " "
    print(whitespace + stars)
    i += 1
