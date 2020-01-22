# comment

dict = {'a': "A", 'b': "B", 'c': 'C'}
test = "ABC"
test = test.lower()
i = 0
converted = ""
for i in test:
    if i in dict:
        new_letter = dict[i]
        converted += new_letter

print(converted)
