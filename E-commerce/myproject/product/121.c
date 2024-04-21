#include <stdio.h>

int main() {
    int i;

    printf("Printing odd numbers from 1 to 5:\n");

    for (i = 1; i <= 5; i++) {
        if (i % 2 == 0) {
            continue;  
        }
        printf("%d\n", i);  
    }

    return 0;
}
