
# Long long vowels
string = "Good"
vowels = "aeiou"
i = 0
new_string = ""

while i < len(string):
    if string[i] in vowels and (i + 1) < len(string):
        if string[i] == string[i+1]:
            new_string = new_string + (string[i] * 5)
        else:
            new_string += string[i]
    else:
        new_string += string[i]
    i += 1

print(new_string)
