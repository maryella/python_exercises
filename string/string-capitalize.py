# Capitalize a string
# 1. Title
cap_string = string.title()
# 2. Split and Capitalize then move together
array = string.split(" ")
caparray = []
for i in array:
    caparray.append(i.capitalize())
cap_string = ' '.join(caparray)
