#include <stdio.h>

int main() {
    int is_valid, number;
    while (1) {
        printf("Please enter 5: ");
        is_valid = scanf("%d", &number);
        if (is_valid == 1 && number == 5) {
            printf("Correct!\n");
            break; 
        } else {
            printf("Incorrect.\n");
            // Clear the input buffer to prevent accidental infinite loop
            while (getchar() != '\n') {}
        }
    }
    return 0;
}
