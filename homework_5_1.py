# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers

def difference(num_1, num_2):
    return num_1-num_2


num_1a = int(input("what is your first number? "))
num_2a = int(input("what is your second number? "))
print(f"difference: {difference(num_1a,num_2a)}")


# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    return num_1/num_2


print(f"division: {division(num_1a,num_2a)}")


# Function gets random number. If this number is more than ten,
# return the difference between 100 and this number,
# otherwise return this number multiplied by 10

def function_1(number):
    if number > 10:
        return 100-number
    else:
        return number * 10


numbera = int(input("What is a random number? "))
print(f"thought about random number is {function_1(numbera)}")

# Your function temperature_convertor gets the temperature in Fahrenheit,
# convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C


def temperature_convertor(fahrenheit_degree):
    return (fahrenheit_degree-32) * (5/9)


fahrenheit_degreea = int(input("What is the temp in F? "))
print(f"If outside the F temp is {fahrenheit_degreea} then it is "
      f"{temperature_convertor(fahrenheit_degreea)} in C")


# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a
# base fare of $4.00,
# plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers)
# as its only parameter and returns the total fare
# as its only result rounded by 2 digits.
# Write a program that demonstrates the function.

def taxi_fare(distance):
    distance = (distance * 100)/140
    fare = round(4.00 + (0.25 * distance), 2)
    return fare


ride_length = int(input("How long was your taxi ride in Kilometers? "))
print(f"the taxi ride costs ${taxi_fare(ride_length)}")
