#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>

int* init_array(int array_size, int max_value) {
    int* arr = malloc(array_size * sizeof(int));
    for (int i = 0; i < array_size; i++) {
        if (max_value == 0) {
            arr[i] = 0;
        } else {
            arr[i] = 1 + rand() % max_value;
        }
    }
    return arr;
}

double compute_average(int* arr, int array_size, int num_subtotals) {
    int* subtotals = init_array(num_subtotals, 0);
    for (int i = 0; i < array_size; i++) {
        subtotals[i % num_subtotals] += arr[i];
    }
    int total = 0;
    for (int i = 0; i < num_subtotals; i++) {
        total += subtotals[i];
    }
    return (double)total/array_size;
}

void report_average_and_timer(int* arr, int array_size, int num_subtotals) {
    srand(time(NULL));
    struct timeval tstart, tend;
    gettimeofday(&tstart, NULL);
    double avg = compute_average(arr, array_size, num_subtotals);
    gettimeofday(&tend, NULL);
    double dt = tend.tv_sec - tstart.tv_sec + (tend.tv_usec - tstart.tv_usec)/1.e6;
    printf("average: %.2f; array_size: %d; n_subtotals: %d; time: %g sec\n", avg, array_size, num_subtotals, dt);
}

int main(int argc, char** argv) {
    if (argc != 3) {
        fprintf(stderr, "usage: %s SA NS\n", argv[0]);
        fprintf(stderr, "where SA is the size of the array and NS is the number of subtotals to compute\n");
        return 1;
    }
    int array_size = strtol(argv[1], NULL, 10);
    int num_subtotals = strtol(argv[2], NULL, 10);
    int* arr = init_array(array_size, 100);

    report_average_and_timer(arr, array_size, num_subtotals);

    free(arr);
    return 0;
}

