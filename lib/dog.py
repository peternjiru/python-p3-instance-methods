#!/usr/bin/env python3

class Dog:
    # Class body goes here

    # Instance method definition
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")    

# Note the use of the self keyword in our instance method definition above. 
# We will explore the concept of self in depth in the next module- just know 
# for now that it allows methods to access the other methods and attributes. 
# self is required in instance method definitions, though you don't actually 
# need to pass it in when you call the method.

fido = Dog()
fido.bark()

snoopy = Dog()
snoopy.bark()

# instance methods, the methods that belong to particular instances of particular 
# classes, cannot be used globally like procedural methods. They cannot be called without an instance.