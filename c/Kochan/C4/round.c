/* Write a program to find the next largest even multiple for the following
 * values of i and j:
 *
*/

#include <stdio.h>

int main (void) {
    int i;
    int j;
    while(1){
        printf("Enter values of i and j: ");
        scanf("%i %i", &i, &j);
        if(i > 0 && j > 0){
            break;
        }
    }
    printf("Here: %i\n", i + j - i % j);

    return 0;
}
