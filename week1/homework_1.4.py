from __future__ import division

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
    multiples = range(2,10)
    print "multiples: ", multiples
    my_range = range(2, user_input + 1)
    for term in my_range:
        divisors_of_term = []
        for multiple in multiples:
            divisor = int(term) / int(multiple)
            print str(term) + "/" + str(multiple) + " = "
            print "divisor: ", divisor
            divisors_of_term.append(divisor)
        for value in divisors_of_term:
            if(value > 1):
                print "value: " + str(value) + "---" + " is greater than 1"

find_primes_in_range(10)
