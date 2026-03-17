#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


const size_t ARRAY_SIZE = 64;
const long N_LOOPS = 10000000;


void run_stack_test() {
    for (long i = 0; i < N_LOOPS; i++) {
        // Allocated by moving the Stack Pointer (SP)
        volatile char buffer[ARRAY_SIZE]; 
        buffer[0] = (char)(i % 255);
    }
}

void run_heap_test() {
    for (long i = 0; i < N_LOOPS; i++) {
        // Allocated by the memory manager (malloc/free)
        char *buffer = (char *)malloc(ARRAY_SIZE * sizeof(char));
        if (!buffer) return;
        buffer[0] = (char)(i % 255);
        free(buffer);
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s [-s|--stack|-h|--heap]\n", argv[0]);
        return 1;
    }

    char *mode = argv[1];
    clock_t start, end;

    if (strcmp(mode, "-s") == 0 || strcmp(mode, "--stack") == 0) {
        printf("Testing STACK with %ld loops...\n", N_LOOPS);
        start = clock();
        run_stack_test();
        end = clock();
    } 
    else if (strcmp(mode, "-h") == 0 || strcmp(mode, "--heap") == 0) {
        printf("Testing HEAP with %ld loops...\n", N_LOOPS);
        start = clock();
        run_heap_test();
        end = clock();
    } 
    else {
        printf("Unknown flag: %s\n", mode);
        return 1;
    }

    double cpu_time = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Time taken: %f seconds\n", cpu_time);

    return 0;
}
