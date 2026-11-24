#include <stdio.h>

int add_one(int x) {
  x += 1;
  return x;
}

int add_two(int x) {
    int p = add_one(x);
    int q = add_one(p);
    return q;
}

int main() {
  int a = 7;
  int b = add_two(a);
  printf("%d + 1 + 1 = %d\n", a, b);
  return 0;
}

