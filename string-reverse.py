# Reverse a string
string = "abcdefg"
new_string = ""
i = len(string)
while i > 0:
    new_string += string[i - 1]
    i -= 1
print(new_string)
