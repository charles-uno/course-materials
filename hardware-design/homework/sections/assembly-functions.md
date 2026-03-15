---
---

# Assembly Functions

## Function Calls

```c
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
```

Compile this code and run it. Does it do what you expect?

Compile to assembly with no optimization. Look at the result

Compile to assembly with highest optimization. Look at the result

Write equivalent logic in assembly. Keep to the limited vocabulary we have used in class (eg `str` rather than `stp`)



## Nested Function Calls

```c
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
```

Compile to an executable. Run it. Does it do what you expect?
```bash
gcc func.c
./a.out
```

Compile to Assembly with no optimization:
```bash
gcc -O0 func.c -S
```

Compile with highest optimization:
```bash
gcc -O3 func.c -S
```