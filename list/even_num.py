num_list = [1, 2, 3, 4, 5]

# Even Num
evens = []
for i in num_list:
    if i % 2 == 0:
        evens += str(i)
    i += 1
print(evens)
