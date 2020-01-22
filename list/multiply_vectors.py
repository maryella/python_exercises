num_list = [1, 2, 3, 4, 5]

# Multiply Vectors: multiply two equally long lists to make a new list
vector1 = [2, 4, 5]
vector2 = [2, 3, 6]
result = []
i = 0
while i < len(vector1):
    new_num = vector1[i] * vector2[i]
    result.append(new_num)
    i += 1

print(result)
