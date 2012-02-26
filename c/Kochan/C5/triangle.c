#include <stdio.h>

int main (void){
    int number;
    int i = 0;
    char asterisk = "*";
    while(1){
        printf("Enter number: ");
        scanf("%i", &number);
        if(number > 0){
            break;
        }
    }
    while (i < number){
        printf("%c\n", asterisk * i);
        i++;
    }

    return 0;
}
