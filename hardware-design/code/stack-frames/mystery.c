#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int ARRAY_SIZE = 10000;

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// bubble Sort
void bubble_sort(int *arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

// quick Sort
void quick_sort(int *arr, int low, int high) {
    if (low < high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(&arr[i], &arr[j]);
            }
        }
        int pi = i + 1;
        swap(&arr[pi], &arr[high]);
        quick_sort(arr, low, pi - 1);
        quick_sort(arr, pi + 1, high);
    }
}

int main() {
    int *original = malloc(ARRAY_SIZE * sizeof(int));
    int *work_copy = malloc(ARRAY_SIZE * sizeof(int));
    // Seed with random data
    for (int i = 0; i < ARRAY_SIZE; i++) {
        original[i] = rand() % 10000;
    }

    printf("Running Bubble Sort (N=%d)...\n", ARRAY_SIZE);
    memcpy(work_copy, original, ARRAY_SIZE * sizeof(int));
    bubble_sort(work_copy, ARRAY_SIZE);

    printf("Running Quick Sort (N=%d)...\n", ARRAY_SIZE);
    memcpy(work_copy, original, ARRAY_SIZE * sizeof(int));
    quick_sort(work_copy, 0, ARRAY_SIZE - 1);

    free(original);
    free(work_copy);
    return 0;
}
