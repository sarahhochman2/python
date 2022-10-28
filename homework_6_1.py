# You are given a list in list_1 variable, write a swap_first_last
# function to return a new list with
# the first and the last elements of the list swapped.
# Return this list


def swap_first_last(array_1):
    array_1[0], array_1[len(array_1)-1] = array_1[len(array_1)-1], array_1[0]
    return array_1


list_1 = [1, 'asdasd', True, 2, False, 4, 'Hello world', None, range(1, 11), 100]
print("switch first and last")
print(list_1)
print(swap_first_last(list_1))


# You are given a list in list_2 variable, write a reverse_list function
# which creates a new list in reversed order.
# Return this list


def reverse_list(array_2):
    return array_2[::-1]


list_2 = [1, 'asdasd', True, 2, False, 4, 'Hello world', None, range(1, 11), 100]
print("reverse the list")
print(list_2)
print(reverse_list(list_2))


# Create a list which contains only number items and
# save it to the list_3 variable.
# Then write multiply_list_items
# function to multiply all the items in a list. Return result of multiplication


def multiply_list_items(array_3):
    product = 1
    for number in array_3:
        product = product * number
    return product


list_3 = []
count = int(input("How many numbers would you like in your list? "))
for x in range(0, count):
    list_number = int(input("number: "))
    list_3.append(list_number)
print("multiply input list")
print(list_3)
print(multiply_list_items(list_3))


# Create a list which contains only number items and save it to the list_4 variable.
# Then write smallest_item_list
# function to get the smallest number from a list. Return smallest element


def smallest_item_list(array_4):
    return min(array_4)


list_4 = []
count = int(input("How many numbers would you like in your list? "))
for x in range(0, count):
    list_number = int(input("random number: "))
    list_4.append(list_number)
print("smallest item")
print(list_4)
print(smallest_item_list(list_4))


# Given a list in list_5 variable,
# write a remove_duplicates_list function to remove duplicates from a list.
# Return new list without duplicates

list_5 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 'hello', 1, 2, 3, 4, 'hello', 'hello', 1]


def remove_duplicates_list(array_5):
    for i in range(0, len(array_5)):
        y = i + 1
        while y < len(array_5):
            if array_5[i] == array_5[x]:
                array_5.pop(x)
                y = y - 1
            y = y + 1
    return array_5


print("remove duplicates")
print(list_5)
print(remove_duplicates_list(list_5))


# You are given a list in list_6 variable.
# Enter an integer number and save it to number_1 variable,
# write a longer_words_list function which will return the list of words
# that are longer than number_1
# from a given list of words.

def longer_words_list(array_6, number1):
    new_array = []
    for item in array_6:
        if len(item) < number1:
            pass
        else:
            new_array.append(item)
    return new_array


list_6 = ['On', 'it', 'differed', 'repeated', 'wandered', 'required', 'in.', 'Then', 'girl', 'neat', 'why', 'yet',
          'knew', 'rose', 'spot.', 'Moreover', 'property', 'we', 'he', 'kindness', 'greatest', 'be', 'oh', 'striking',
          'laughter.', 'In', 'me', 'he', 'at', 'collecting', 'affronting', 'principles', 'apartments.', 'Has', 'visitor',
          'law', 'attacks', 'pretend', 'you', 'calling', 'own', 'excited', 'painted.', 'Contented', 'attending',
          'smallness', 'it', 'oh', 'ye', 'unwilling.', 'Turned', 'favour', 'man', 'two', 'but', 'lovers.', 'Suffer',
          'should', 'if', 'waited', 'common', 'person', 'little', 'oh.', 'Improved', 'civility', 'graceful', 'few',
          'smallest', 'screened', 'settling.', 'Likely', 'active', 'her', 'warmly', 'has.']
number_1 = int(input("What is the shortest word you would like? "))
print("long words")
print(longer_words_list(list_6, number_1))


# Given two lists in list_7 and list_8 variables.
# Write a function find_item_lists that takes two lists and returns
# True if they have at least one common member.


def find_item_lists(array_7, array_8):
    for item in array_7:
        if item in array_8:
            return True
    return False


list_7 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 'hello', 1, 2, 3, 4, 'hello', 'hello', 1]
list_8 = ['asdasd', True, 8, False, 94, 'Hello world', None, range(1, 11), 100, 1]
print("does each list contain something the same?")
print(list_7)
print(list_8)
print(find_item_lists(list_7, list_8))


# You are given a list in list_9 variable.
# Write a function list_to_string to convert a list of
# characters into a string.


def list_to_string(list9):
    return "".join(list9)


list_9 = ['I', ' ', 'l', 'i', 'k', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n']
print("turn the list to a string")
print(list_9)
print(list_to_string(list_9))


# Given a list of numbers in list_10 and a number number_2,
# write count_items_list function which will count number of
# occurrences of number_2 in the given list
list_10 = [1, 2, 3, 1, 1, 1, 2, 3, 4]
number_2 = 3


def count_items_list(array_10, number2):
    counter = 0
    for item in array_10:
        if number2 in array_10:
            counter += 1
            array_10.remove(number2)
    return counter


print(f"How many times does {number_2} appear in {list_10}")
print(count_items_list(list_10, number_2))


# Given a list of numbers, write a function even_items_list
# to return new list which include all even numbers in
# given list.
list_11 = [1, 2, 3, 1, 1, 1, 2, 3, 4]


def even_items_list(array_11):
    new_array = []
    for item in array_11:
        if item % 2 == 0:
            new_array.append(item)
    return new_array


print(f"make even array from {list_11}")
print(even_items_list(list_11))
