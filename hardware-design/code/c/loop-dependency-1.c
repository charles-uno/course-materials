#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <time.h>

int* init_array(int size, int max) {
    int* arr = malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
            arr[i] = 1 + rand() % max;
        }
    return arr;
}

double compute_average_v1(int* arr, int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        total += arr[i];
    }
    return (double)total/size;
}

int main(int argc, char** argv) {
   /* Validate command line parameters. */
   if (argc != 2) {
       fprintf(stderr, "usage: %s <n>\n", argv[0]);
       fprintf(stderr, "where <n> is the size of the array\n");
       return 1;
   }
   int i;
   double avg, timer;
   int n = strtol(argv[1], NULL, 10);
   srand(time(NULL));
   struct timeval tstart, tend;
   int* arr = init_array(n, 100);

   gettimeofday(&tstart, NULL);
   avg = compute_average_v1(arr, n);
   gettimeofday(&tend, NULL);
   timer = tend.tv_sec - tstart.tv_sec + (tend.tv_usec - tstart.tv_usec)/1.e6;
   printf("v1 average is: %.2f; time is %g\n", avg, timer);

   free(arr);
   return 0;
}

