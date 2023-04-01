// Constantine Macris
// Prof Ilias Hotzoglou
// March 26, 2021
// ITC 2088
// Programming Assignment #1 in C

#include <stdio.h>

int cpSeries(n) // fruitful function that returns the nth element of the produced series
{
    int i = 1; // initiation of counter variable for while loop
    int a = 0; // initiation of "a(n-2)" variable
    int b = 1; // initiation of "a(n-1)" variable
    while (i < n){ // while loop to compute the formula to the nth element
        int x = 2 * b + 3 * a;
        a = b; // reassigning the value of the second variable to the first variable
        b = x; // reassigning the value of equation to the second variable
        i++; // incrementing the count variable to terminate the loop
    }
    return b; // returns the value calculated after 'n' loop iterations
}

int main() // main function to call the cpSeries function
{
    printf("\n%d\n", cpSeries(5)); // displayed in 'int' data type
}
