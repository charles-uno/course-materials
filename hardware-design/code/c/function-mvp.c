#include <stdio.h>

int add_one(int x) {
  x += 1;
  return x;
}

int main() {
  int a = 7;
  int b = add_one(a);
  printf("%d + 1 = %d\n", a, b);
  return 0;
}

