# L33tspeak
string = "Totally rad leet"
string = string.upper()
i = 0
new_string = ""

while i < len(string):
    if string[i] == 'A':
        new_string += '4'
    elif string[i] == 'E':
        new_string += '3'
    elif string[i] == 'G':
        new_string += '6'
    elif string[i] == 'I':
        new_string += '1'
    elif string[i] == 'O':
        new_string += '0'
    elif string[i] == 'S':
        new_string += '5'
    elif string[i] == 'T':
        new_string += '7'
    else:
        new_string += string[i]
    i += 1

print(new_string)
