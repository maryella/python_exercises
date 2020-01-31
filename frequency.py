# Frequency Pattern

# Exercise #1: Given two lists of numbers, write a function to find out if two lists have the same frequency of digits.
a = [1, 2, 3, 4]
b = [1, 4, 5, 6]
c = [1, 4, 4, 2]
d = [1, 4, 3, 2]
e = [1, 2, 3, 4, 5]


def function1(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        letter_count1 = {}
        for i in list1:
            if i not in letter_count1:
                letter_count1[i] = 1
            else:
                letter_count1[i] += int(1)
        letter_count2 = {}
        for i in list2:
            if i not in letter_count2:
                letter_count2[i] = 1
            else:
                letter_count2[i] += int(1)
        if letter_count1 != letter_count2:
            return False
        else:
            return True


print(function1(a, a))
print(function1(a, b))
print(function1(a, c))
print(function1(a, d))
print(function1(e, a))

# Exercise2: Given two Lists write a function to determine if each value in our first List contains a corrsponding value to the second power in the second List.

a = [1, 2, 3, 4]
b = [1, 4, 9, 16]
c = [1, 4, 5, 6]
d = [1, 4, 4, 2]
e = [1, 16, 9, 4]
f = [1, 2, 3, 4, 5]


# def function2(list1, list2):
#     if len(list1) != len(list2):
#         return False
#     else:
#         test_array = []
#         for x in list1:
#             for y in list2:
#                 if y == x * x:
#                     test_array.append(y)
#         if len(list1) == len(test_array):
#             return True
#         else:
#             return False


# print(function2(a, b))
# print(function2(a, c))
# print(function2(a, d))
# print(function2(a, e))
# print(function2(f, a))

# dictionary version


# def function2(list1, list2):
#     if len(list1) != len(list2):
#         return False
#     else:
#         test_dictionary = {}
#         for x in list1:
#             for y in list2:
#                 if y == x * x:
#                     test_dictionary[x] = y
#         if len(list1) == len(test_dictionary):
#             return True
#         else:
#             return False


# print(function2(a, b))
# print(function2(a, c))
# print(function2(a, d))
# print(function2(a, e))
# print(function2(f, a))


# Exercise 3 Create a function that accepts two strings and checks if they are valid anagrams.
a = "pie"
b = "eip"
c = "pies"
d = "pwe"


# def anagram(first, second):
#     if len(first) != len(second):
#         return False
#     else:
#         first_dictionary = {}
#         for i in first:
#             if i not in first_dictionary:
#                 first_dictionary[i] = 1
#             else:
#                 first_dictionary[i] += int(1)
#         second_dictionary = {}
#         for i in second:
#             if i not in second_dictionary:
#                 second_dictionary[i] = 1
#             else:
#                 second_dictionary[i] += int(1)
#         if first_dictionary != second_dictionary:
#             return False
#         else:
#             return True
#         # attempt to hard code dictionary compare
#         # x = len(first_dictionary)
#         # while x < 0:
#         #     if first_dictionary[x] == second_dictionary[x]:
#         #         return True
#         #     x -= 1


# print(anagram(a, b))
# print(anagram(a, c))
# print(anagram(a, d))

# Exercise 4: : Given a string return the letter that is used the most in the string.
# a = "hello"
# b = "sprinkle slurps"
# c = "car cat cuts crinckles"


# def letter_counter(string):
#     counted = {}
#     for i in string:
#         if i not in counted:
#             counted[i] = 1
#         else:
#             counted[i] += int(1)
#     sort_count = sorted([(value, key)
#                          for (key, value) in counted.items()], reverse=True)
#     return sort_count[0][1]


# print(letter_counter(c))
