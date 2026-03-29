
---

# Assembly Functions

Submit code via csgit. Submit notes, screenshots, and scans via Moodle.

Please work on your own, then compare your results with at least two of your peers. If you find nontrivial differences, talk them out until everyone is on the same page.

When printing code to mark it up, I recommend formatting the text with multiple columns or printing multiple pages per sheet. Marked-up code should be scanned and submitted via Moodle.

When parsing C code, you may reference whatever people and resources you like. You do not need to be able to reproduce it, but I would like you to generally understand it when you look at it. 

When writing Assembly code, you may reference whatever people and materials you like. But make sure the code you turn in reflects your own understanding. 

For memory diagrams, it is convenient (but not required) to start with SP=0x4010 and FP=0x5000. You do *not* need to track PC. For LR, you can use words (eg "caller LR", "main LR", etc). 

## The Stack

Download `stack-vs-heap.c` from Moodle. 

Connect to your Pi using VSCode. Create a new directory `HD/assembly-functions`. Copy `stack-vs-heap.c` into that directory.

1. Print out the C code. What do you think it does? Mark up the code to explain what it does. Submit a scan of your marked-up code.
2. Compile the C code to Assembly with `gcc -S`. How does it allocate memory on the stack? How does it allocate memory on the heap?
3. Compile the code to an executable. Run it with `-s`. Run it with `-h`. What do you notice?
4. The constant `N_LOOPS` starts at 1 million. Try modifying it to be bigger or smaller, recompile, and run again. What happens? Why?
5. The constant `ARRAY_SIZE` starts at 64. Does this mean 64 bits, 64 bytes, or something else?
6. Modify `ARRAY_SIZE` to be very large. What happens? Why?

## Local Variables

1. Write an Assembly program `koala-thumbs.s`. It should do the following:
    - Ask the user how many koalas they have
    - Read the response (an integer) into a local variable
    - Load the value from memory
    - Compute and return the total number of thumbs
    - Report the total number of thumbs
2. Write a unit test to exercise `koala-thumbs.s`. Make sure the code compiles and runs correctly for a few test cases. 
2. Draw out the memory diagram for `koala-thumbs.s`. Start at the top of `main` and show each update to memory and registers. Assume the user has 45 koalas.
3. Write an Assembly program `multiply-three.s`. It should do the following:
    - Ask the user for three integers (repeating the same prompt is ok)
    - Store the inputs into local variables
    - Load the values from memory
    - Compute the product
    - Report the product
4. Write a unit test. Make sure the code compiles and runs correctly for a few test cases. You may want to see the earlier example `add-two-test.sh` for an example of how to handle multiple inputs.
4. Draw out the memory diagram for `multiply-three.s`. Start at the top of `main` and show each update. Assume the user inputs the numbers `5`, `12`, and `100`. 

## Stack Frames

Download `stack-ghost.c` from Moodle. Copy it over to your Pi.

1. Print out the C code. What do you think it does? Mark up the code to explain what it does. 
3. Compile the code to an executable. Run it a few times. What happens?
2. Compile the C code to Assembly with `gcc -S`. Print it out. Can you explain the behavior?

## Function Calls

Create a new file `add-one-twice.c`. Paste the following code into it:

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

1. Compile this code and run it. Does it do what you expect?
2. Compile this code to Assembly using `gcc -O0 -S`. Print it out. Mark it up to explain what the code does.
3. Compile it to Assembly again, but this time use `gcc -O3 -S`. Print out. Mark it up to explain the differences. 
4. What does the `-O` flag do? What's a situation where you would prefer `-O0`? What's a situation where you would prefer `-O3`?
5. Write `add-one-twice.s` in Assembly. This code should do the same thing as the C code above. Keep to the limited vocabulary we have covered in class (eg `str` rather than `stp`). Also make sure you include stack frames for each function (even if `gcc` skipped them). 
6. Write a unit test for `add-one-twice.s` to make sure it compiles and runs for a few different inputs. 
7. Draw out the memory diagram for `add-one-twice.s`. Start at the top of `main` and show each update.

## Optimization with Functions

Download `mystery.c` from Moodle. Copy it over to your Pi.

1. What does this code do? No need to print it out. NOTE: don't worry if you haven't seen these sorting algorithms before.
2. Compile this code and run it. Does it do what you expect?
3. Compile it again using Gprof. This is the code profiler built into `gcc`.
```bash
  gcc -pg mystery.c -o mystery
  ./mystery
  gprof mystery gmon.out
```
4. Look at the profile. Which algorithm is more efficient? How can you tell?
5. Compile to Assembly with and without instrumentation:
```bash
  gcc -pg mystery.c -S -o mystery-instrumented.s
  gcc mystery.c -S -o mystery-regular.s
```
  Look at the two outputs. Can you find the difference?

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