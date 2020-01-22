# 3 Letter counter
word = input("Enter a word: ")
count = {}
for i in word:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1
print(count)
