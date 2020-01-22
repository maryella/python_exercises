hotel = {
    '1': {
        '101': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}

answer = input("Would you like to check in or check out? ")
floor_num = input("What floor? ")
room_num = input("Which room? ")
i = floor_num
print(i)
for x in hotel[i]:
    if room_num == x:
        print("Sorry, choose another room")
# if answer == 'check in':
