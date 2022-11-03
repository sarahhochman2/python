# Enter a country and save it to variable your_choice_country.
# Write find_index_by_value function which will check
# if the tuple countries contains a country of your choice.
# If your_choice_country is in the tuple, return its
# index, otherwise return a -1 value

countries = ('USA', 'Canada', 'United Kingdom', 'Mexico', 'Brazil', 'Argentina', 'Chili', 'South Africa', 'Egypt',
             'Morocco', 'India', 'China', 'Ukraine', 'Spain', 'France', 'Russia')
your_choice_country = 'Canada'


def find_index_by_value(value1, tuple1):
    if value1 in tuple1:
        return tuple1.index(value1)
    else:
        return -1


print(f"index of {your_choice_country} in {countries}\n"
      f" is {find_index_by_value(your_choice_country, countries)}")
print("\n\n\n")
# Change the previous exercise.
# Enter a random number and save it to variable your_choice_number. Write
# find_value_by_index function which will check if the tuple countries
# contains a country with this index.
# If there is a value with this index your_choice_number in the tuple,
# return this value,
# otherwise return a 'No such index' text

your_choice_number = 7


def find_value_by_index(index, tuple1):
    if index < len(tuple1):
        return tuple1[index]
    else:
        return "no such index"

print(f"The country at index {your_choice_number}\n"
      f" in tuple {countries}\n"
      f" is {find_value_by_index(your_choice_number,countries)}")
print("\n\n\n")

# Enter a pair of values in variables new_team_name, new_team_city.
# Then write add_your_own_team function
# to add them to nhl_hockey_teams dictionary, where the name will be the key.


nhl_hockey_teams = {
    "Canadiens": "Montreal",
    "Maple Leafs": "Toronto",
    "Red Wings": "Detroit",
    "Bruins": "Boston",
    "Blackhawks": "Chicago",
    "Oilers": "Edmonton",
    "Penguins": "Pittsburgh",
    "Islanders": "New York",
    "Rangers": "New York",
    "Devils": "New Jersey",
    "Avalanche": "Colorado",
    "Kings": "Los Angeles",
    "Flyers": "Philadelphia",
    "Ducks": "Anaheim",
    "Flames": "Calgary",
    "Hurricanes": "Carolina",
    "Stars": "Dallas",
    "Blues": "St. Louis",
    "Lightning": "Tampa Bay",
    "Capitals": "Washington"
}


def add_your_own_team(team_name, team_city, team_dict):
    team_dict[team_name] = team_city
    return team_dict


new_team_name = input("new team name: ")
new_team_city = input("new team city: ")
add_your_own_team(new_team_name, new_team_city, nhl_hockey_teams)
for key, value in nhl_hockey_teams.items():
    print(key, ' : ', value)
print("\n\n\n")

# Create two dictionaries in dict_1, dict_2 variables.
# Write a join_dicts function to concatenate the following
# dictionaries to create a new one.

dict_1 = {}
dict_2 = {}


def join_dicts(dict1, dict2):
    new_dict = dict1.copy()
    new_dict.update(dict2)
    return new_dict


number_1 = int(input("How many keys do you want in dict 1? "))
number_2 = int(input("How many keys do you want in dict 2? "))
print("for dictionary 1")
for x in range(0, number_1):
    key = input("key: ")
    dict_1[key] = input("value: ")
print("for dictionary 2")
for y in range(0, number_2):
    key = input("key: ")
    dict_2[key] = input("value: ")
print(f"dictionary 1: {dict_1}")
print(f"dictionary 2: {dict_2}")
dict_3 = join_dicts(dict_1, dict_2)
print(f"joined dictionaries: {dict_3}")
print("\n\n\n")

# # Enter a random number and save it to number_1 variable.
# Then write create_numbers_dict function to generate
# a dictionary that contains items with keys from 1 to number_1 and
# values in format "x": "x**2".


def create_numbers_dict(number1):
    dictionary = {}
    for i in range(1, number1+1):
        dictionary[i] = i**2
    return dictionary


number_1 = int(input("enter a random number: "))
number_to_the_power = create_numbers_dict(number_1)
for key, value in number_to_the_power.items():
    print(key, ' : ', value)
print("\n\n\n")

# Write sum_up_hockey_cups functions to sum all values in a dictionary dict_3.

dict_3 = {
    "Montreal Canadiens": 24,
    "Toronto Maple Leafs": 13,
    "Detroit Red Wings": 11,
    "Boston Bruins": 6,
    "Chicago Blackhawks": 6,
    "Edmonton Oilers": 5,
    "Pittsburgh Penguins": 5,
    "New York Islanders": 4,
    "New York Rangers": 4,
    "New Jersey Devils": 3,
    "Colorado Avalanche": 2,
    "Los Angeles Kings": 2,
    "Philadelphia Flyers": 2,
    "Anaheim Ducks": 1,
    "Calgary Flames": 1,
    "Carolina Hurricanes": 1,
    "Dallas Stars": 1,
    "St. Louis Blues": 1,
    "Tampa Bay Lightning": 1,
    "Washington Capitals": 1
}


def sum_up_hockey_cups(teams_dict):
    numbers = teams_dict.values()
    result = 0
    for items in numbers:
        result = result + items
    return result


print(f"The sum of all the hockey cups is {sum_up_hockey_cups(dict_3)}")
print("\n\n\n")

# Write remove_item_by_key function to remove a key True from dict_4 dictionary.

dict_4 = {
    "a": 231,
    "b": 'hello',
    True: False,
    42: 'answer'
}


def remove_item_by_key(dict1, key1):
    key_list = list(dict1.keys())
    for p in range(0, len(key_list)):
        key_list[p] = str(key_list[p])
    if key1 not in key_list:
        return "not in dictionary"
    else:
        where = key_list.index(key1)
        values_list = list(dict1.values())
        answer = values_list[where]
        for key4, value4 in dict(dict1).items():
            if value4 == answer:
                del dict1[key4]
        return answer


look_for = input("What word would you like to look for? ")
print(dict_4)
print(f"We looked for {look_for} in {dict_4} and here it is {remove_item_by_key(dict_4, look_for)}")
print(dict_4)
print("\n\n\n")

dict_5 = {
    "Cyprus": 1207359,
    "Czechia": 10708981,
    "Democratic Republic of the Congo": 89561403,
    "Denmark": 5792202,
    "Djibouti": 988000,
    "Dominica": 71986,
    "Dominican Republic": 10847910,
    "Ecuador": 17643054,
    "Egypt": 102334404,
    "El Salvador": 6486205,
    "Equatorial Guinea": 1402985,
    "Eritrea": 3546421,
    "Estonia": 1326535,
    "Eswatini": 1160164,
    "Ethiopia": 114963588,
    "Fiji": 896445,
}


def find_min_max(dict1):
    list_values = list(dict1.values())
    minimum = list_values[0]
    for number in list_values:
        if number < minimum:
            minimum = number
    maximum = list_values[0]
    for number in list_values:
        if number > maximum:
            maximum = number
    min_key = 0
    max_key = 0
    for key9, value9 in dict1.items():
        if minimum == value9:
            min_key = key9
        if maximum == value9:
            max_key = key9
    min_max = (minimum, maximum, min_key, max_key)
    return min_max


min_max_list = find_min_max(dict_5)
print(f"In the dictionary of countries and IDs,\n "
      f"the minimum ID number is {min_max_list[0]} \n"
      f"which is the country {min_max_list[2]}\n"
      f"and the maximum ID number is {min_max_list[1]}\n"
      f"which is the country {min_max_list[3]}")
print("\n\n\n")

# Write remove_duplicates functions to remove duplicates from dictionary dict_6.

dict_6 = {
    "Lessie": "collie",
    "Marlie": "labrador",
    "Spike": "boxer",
    "Buddy": "labrador",
    "Milo": "labrador",
    "Archie": "corgi",
    "Tobby": "pit bull",
    "Jack": "poodle",
    "Lucy": "german shepherd",
    "Bailey": "labrador"
}


def remove_duplicates(dictionary):
    # key_list = list(dictionary.keys())
    # name = ""
    # new_list = ()
    # for x in range(0,len(key_list)):
    #    name = key_list.pop(key_list[x])
    #    if name not in key_list:
    #        new_list = new_list + name
    # new_dict = {}
    # for x in range(0,len(new_list)):
    #    new_dict[new_list[x]]=dictionary.get(new_list[x])
    #
    # values_list = list(dictionary.values())
    # name = ""
    # new_list = []
    # for y in range(len(values_list)-1, -1, -1):
    #     name = values_list.pop(y)
    #     if (name not in values_list) and (name not in new_list):
    #         new_list.append(name)
    # new_dict = {}
    # ##find values_list[x] in dictionary
    # ##add key and value to new_dict
    # for x in range(0, len(new_list)):
    #     for key, value in dict(dictionary).items():
    #         if new_list[x] == value:
    #             new_dict[key] = new_list[x]
    #     continue
    # return new_dict
    # dictionary2 = dictionary.copy()

    # for key, value in dict(dictionary).items():
    #     for key2, value2 in dict(dictionary2).items():
    #
    #         if value == value2:
    #             dictionary2.pop(key2)
    #
    #     break
    # return dictionary2

    list_of_values = dictionary.values()
    no_dups_values = list(set(list_of_values))
    # find keys to match values in dictionary
    new_dict = {}
    for key7, value7 in dictionary.items():
        if value7 in no_dups_values:
            no_dups_values.remove(value7)
            new_dict[key7] = value7
    return new_dict


for key, value in dict_6.items():
    print(key, ' : ', value)

print("removing duplicates")
dict_7 = remove_duplicates(dict_6)
for key, value in dict_7.items():
    print(key, ' : ', value)
