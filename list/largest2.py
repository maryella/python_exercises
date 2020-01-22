num_list = [1, 2, 3, 4, 5]

# Largest other options
# 1
largest = max(num_list)
# 2
sorted_list = sorted(num_list, reverse=True)
largest = sorted_list[0]
print(largest)
# 2.5
sorted_list = sorted(num_list)
sorted_list.reverse()
largest = sorted_list[0]
print(largest)
