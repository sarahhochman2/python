# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1,
# then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is
# included in your string.
# Save result to result_1 variable

string_1 = input("enter a sentence: ")
char_1 = input("enter a character: ")
i=0
result_1=0
while i < len(string_1):
   if string_1[i]==char_1:
       result_1=result_1+1
   i=i+1
print(f"There are {result_1} {char_1} in the string {string_1}")

# Enter a random number and save it in variable number_1.
# Then create code to multiply all the digits together
# and save result in the result_2 variable.

number_1 = input("Enter a multi-digit number: ")
i = 0
result_2=1
while i < len(number_1):
    result_2= result_2 * int(number_1[i])
    i=i+1
print(f"{result_2}= the digits of {number_1} multiplied together")

# Enter a random number and save it in variable number_2.
# Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = input("Enter a long random number: ")
i=0
result_3=""
while i<len(number_2):
    result_3=number_2[i]+result_3
    i=i+1
print(result_3)