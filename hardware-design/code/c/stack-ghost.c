#include <stdio.h>

int* get_secret_address() {
    int secret = 42;
    printf("Setting secret at address: %p\n", (void*)&secret);
    return &secret; // DANGEROUS: Returning address of local stack variable
}

void noise_function() {
    int junk[10];
    for(int i = 0; i < 10; i++) {
        junk[i] = 0xDEADBEEF; // Overwriting the abandoned stack frame
    }
}

int main() {
    int* ptr = get_secret_address();
    printf("Value immediately after return: %d\n", *ptr);
    noise_function();
    printf("Value after calling noise_function: %d\n", *ptr);
    return 0;
}