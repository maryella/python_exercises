# De dup
strings = ["cat", "dog", "cat", "rabbit"]
unique = []
for i in strings:
    if i not in unique:
        unique.append(i)

print(unique)

# Dedup 2 -- set makes unordered list of unique items
unique = set(strings)
print(unique)
