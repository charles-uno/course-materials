#include <stdio.h>

int* get_address() {
    int value = 42;
    printf("Setting value at address: %p\n", (void*)&value);
    return &value;
}

void noise_function() {
    int junk[10];
    for(int i = 0; i < 10; i++) {
        junk[i] = 0xc0ffee;
    }
}

int main() {
    int* ptr = get_address();
    printf("Value immediately after return: %d\n", *ptr);
    noise_function();
    printf("Value after calling noise_function: %d\n", *ptr);
    return 0;
}