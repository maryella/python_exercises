# 4 Word summary: count number of times it was used
# this does not account for punctuation
sentence = input("Enter a sentence: ")
loweredsentence = sentence.lower()
print(loweredsentence)
breakdown = loweredsentence.split(" ")
count = {}
for i in breakdown:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

count2 =
print(count)
