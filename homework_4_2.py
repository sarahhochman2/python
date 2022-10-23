# FOR LOOPS EXERCISES

# Ex. 1
# Enter your name, save it in name variable and
# save in result_1 variable your name repeated 3 times (use loops)

name_1 = input("name? ")
result_1=""
for i in range (0,3):
    result_1=result_1+name_1
print(result_1)

# Ex. 2
# Modify your previous program so that it will enter your name
# (save it in variable  name_2) and a number
# (save in variable number) and then save in result_2 variable your name
# repeated as many times as number_1 is
# (use loops)
name_2 = input("name? ")
number_1 = int(input("number? "))
result_2=""
for i in range (0,number_1):
    result_2=result_2+name_2
print(result_2)

# Ex. 3
# Enter a random string, which includes only digits.
# Write code which find a sum of digits in this string and save it
# into result_3 variable

string_number_1 = input("enter a string of integers: ")
result_3=0
for i in range(0,len(string_number_1)):
    number=int(string_number_1[i])
    result_3= result_3+number
print(result_3)

# Ex. 4
# Create code which sums up all even numbers between 2 and 100
# (include 100) and save it in result_4 variable
result_4=0
for i in range (2,101):
    result_4 = result_4+i
print(result_4)
