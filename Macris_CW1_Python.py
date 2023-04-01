# Constantine Macris
# Prof Ilias Hotzoglou
# March 26, 2021
# Programming Assignment #1 in Python

def cpSeries(n):  # fruitful function that returns the nth element of the produced series

    i = 1  # initiation of counter variable for while loop
    a = 0  # initiation of "a(n-2)" variable
    b = 1  # initiation of "a(n-1)" variable
    while i < n:  # while loop to compute the formula to the nth element
        x = 2 * b + 3 * a
        a = b  # reassigning the value of the second variable to the first variable
        b = x  # reassigning the value of equation to the second variable
        i += 1  # incrementing the count variable to terminate the loop
    return b  # returns the value calculated after 'n' loop iterations


print()
print(cpSeries(5))  # call and display the cpSeries function

