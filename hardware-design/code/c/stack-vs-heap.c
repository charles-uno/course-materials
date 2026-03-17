#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define ARRAY_SIZE 64

void run_stack_test(long loops) {
    for (long i = 0; i < loops; i++) {
        // Allocated by moving the Stack Pointer (SP)
        volatile char buffer[ARRAY_SIZE]; 
        buffer[0] = (char)(i % 255);
    }
}

void run_heap_test(long loops) {
    for (long i = 0; i < loops; i++) {
        // Allocated by the memory manager (malloc/free)
        char *buffer = (char *)malloc(ARRAY_SIZE * sizeof(char));
        if (!buffer) return;
        buffer[0] = (char)(i % 255);
        free(buffer);
    }
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <num_loops> [-s|--stack|-h|--heap]\n", argv[0]);
        return 1;
    }

    long loops = atol(argv[1]);
    char *mode = argv[2];
    clock_t start, end;

    if (strcmp(mode, "-s") == 0 || strcmp(mode, "--stack") == 0) {
        printf("Testing STACK with %ld loops...\n", loops);
        start = clock();
        run_stack_test(loops);
        end = clock();
    } 
    else if (strcmp(mode, "-h") == 0 || strcmp(mode, "--heap") == 0) {
        printf("Testing HEAP with %ld loops...\n", loops);
        start = clock();
        run_heap_test(loops);
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
