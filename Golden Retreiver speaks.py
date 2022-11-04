# Create a GoldenRetriever class that inherits from the Dog class.
# Give the sound argument of GoldenRetriever.speak()
# a default value of "Bark".
# Use the following code for your parent Dog class:

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class Golden_Retreiver(Dog):
    def speak(self, sound="bark"):
        return super().speak(sound)
class Collie(Dog):
    def speak(self, sound="bark bark"):
        return super().speak(sound)

my_dog = Golden_Retreiver("Sarah", 23)
my_dog2 = Collie("Esther", 54)
print(my_dog)
print(my_dog.speak())
print(my_dog2)
print(my_dog2.speak())