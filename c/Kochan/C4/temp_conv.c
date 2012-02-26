/*
 * Convert Fahrenheit to celsius 
*/

#include <stdio.h>

int main (void) {
    int input_temp; // user input
    int minus_stuff = 32;
    float div_stuff = 1.8;
    
    printf("Enter fahrenheit number: ");
    scanf("%i", &input_temp);
    printf("%i F is %g C\n", input_temp, (input_temp - minus_stuff) / div_stuff);

    return 0;
}
