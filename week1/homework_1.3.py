"""
Write a program that takes an integer as
user input and uses a while loop to generate a fibonacci
series (in which each number in the series is the sum of the previous two
numbers in the series (the series begins 1,
1, 2, 3, 5, 8, 13, etc.)) up to the user's number.
"""

def fibonacci_generator(user_input):
    counter = 1
    my_array = [1, 1]
    while (my_array[counter] < user_input):
        print my_array
        difference = my_array[counter] + my_array[counter - 1]
        my_array.append(difference)
        counter += 1


fibonacci_generator(100)
