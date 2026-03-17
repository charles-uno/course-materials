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

Write `add_one_twice.s` in assembly. This code should do the same thing as the above C code. You may refer to the compiled code as you work, but your code should stick to the vocabulary we use in class (eg no `stp`). Also make sure your code creates a stack frame for every function, even if the compiler left them out

## Mark it up!

Print the code out on paper. I recommend two colums

Mark it up. Explain what's happening:
- Every time we call a function or return from one
- Every time we load or store data from memory
- Every time we update the value in a register
- Every time we do input/output

You should have a lot of notes on your paper!

Also explain in words what the program will do


## Small Memory Diagram

put some break points in there

work through this individually, then compare your results with a neighbor. if they do not match *exactly*, talk it out until you reach agreement

$$$
\newpage
$$$

## Bigger Memory Diagrams

Put some break points in here. have them produce the memory diagram at that point

Throw another local variable or two in there too. An unnecessary str/ldr

Say SP=0x4010 at the start of main

When prompted for an int, assume the user enters 8

```arm
.section .rodata
prompt: .ascii "int plz: \0"
fmt: .ascii "%d\0"
output: .ascii "%d + 1 = %d\n\0"

.section .data
n: .word 0

.text
.global main

add_one:
sub sp, sp, 0x20
str fp, [sp]
str lr, [sp, 0x10]
add fp, sp, 0x10
bl add_one_impl
ldr lr, [sp, 0x10]
ldr fp, [sp]
add sp, sp, 0x20
ret

add_one_impl:
sub sp, sp, 0x20
str fp, [sp]
str lr, [sp, 0x10]
add fp, sp, 0x10
add x0, x0, 1
ldr lr, [sp, 0x10]
ldr fp, [sp]
add sp, sp, 0x20
ret

main: 
sub sp, sp, 0x20
str fp, [sp]
str lr, [sp, 0x10]
add fp, sp, 0x10
ldr x0, =prompt
bl printf
ldr x0, =fmt
ldr x1, =n
bl scanf
ldr x0, =n
ldr x0, [x0]
bl add_one
mov x2, x0
ldr x0, =output
ldr x1, =n
ldr x1, [x1]
bl printf
ldr lr, [sp, 0x10]
ldr fp, [sp]
add sp, sp, 0x20
mov x0, 0
b exit
```

$$$
\newpage
$$$

## Writing Assembly Without Reference

Below is the skeleton of an assembly program, with a bunch of comments. Fill in the missing code.

```arm
.section .rodata
// global constants (if any)




.section .data
// global variables (if any)


.text
get_n_thumbs:
// stack frame setup, no local variables



// compute the number of thumbs



// stack frame teardown



// return the result



.global main
main: 
// stack frame setup, one local variable



// ask the user how many koalas they have



// read their response into a local variable



// load the value from memory and pass it to get_n_thumbs



// report the number of thumbs to the user



// stack frame teardown



// exit (normal status code)



```