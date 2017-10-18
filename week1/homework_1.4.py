"""
(Extra credit, from Introduction to Python) Find prime numbers in a range of numbers.
Ask the user for an integer, and display all prime numbers (i.e., numbers that have no
even divisor above 1) between 2 and the user's number.
Sample program runs (user input in bold):
$ python homework1.3.py
* Prime Numbers *
Please enter max integer: 5
2
3
5
$ pyt
"""

def find_primes_in_range(user_input):
    my_range = (1, user_input)
    for i, term in my_range:
        print "i: ", i
        print "term: ", term

find_primes_in_range(10)
