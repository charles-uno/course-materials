
---

# Control Flow

Do all coding for this assignment in the directory `HD/control-flow`. Submit via `csgit`. Submit notes, screenshots, and scans via Moodle.

Please work on your own, then compare your results with at least two of your peers. If you find nontrivial differences, talk them out until everyone is on the same page.

When printing code to mark it up, I recommend formatting the text with multiple columns or printing multiple pages per sheet. Marked-up code should be scanned and submitted via Moodle.

When parsing C code, you may reference whatever people and resources you like. You do not need to be able to reproduce it, but I would like you to generally understand it when you look at it. 

When writing Assembly code, you may reference whatever people and materials you like. But make sure the code you turn in reflects your own understanding. You may need to reproduce this on a test!

## Reading

Read [Dive Into Systems](https://diveintosystems.org) 9.4.

## Absolute Value

Write an Assembly program `absolute-value.s` that does the following:

- Prompt the user to enter an integer
- If the input is positive or zero, print it back
- Otherwise, multiply by -1 and print the result


## Leap Year Checker

Write an Assembly program `leap-year-checker.s` which does the following:

- Prompt the user to enter a year between 0 and 9999
- If they enter a number that is too small or too big, print an error message and exit
- Print whether or not the number is a leap year

Note: X is a leap year if it is divisible by 4, but not divisible by 100, unless divisible by 400. For example:

- 1900: not a leap year (multiple of 100)
- 1992: leap year (multiple of 4)
- 1993: not a leap year (not a multiple of 4)
- 2000: leap year (multiple of 400)

You may use `UDIV` and `MSUB` for division. You may also implement your own logic to check division and remainder. For example, something like the following:
```python
def is_divisible_by(numerator, denominator):
    remainder = numerator
    while remainder > 0:
        remainder = remainder - denominator
    return remainder == 0
```




## Character Flipper

Write an Assembly program `char-flipper.s` that does the following:

- Prompt the user to enter a character
- If the input is a lowercase letter, print the same letter as uppercase
- If the input is an uppercase letter, print it flipped to lowercase
- Otherwise, print the same character back

Be sure to include a test, and make sure your test covers corner cases

## Understanding Conditional Code

Copy this code into `say-five.c`. Compile to an executable. Run it. Does it do what you expect?

Now compile the C code to Assembly:

```bash
gcc -S say-five.c
```

Print out both versions of the code. Mark them up. Explain as much as you can. Indicate which part of the Assembly code corresponds to which part of the C.

```c
#include <stdio.h>

int main() {
    int is_valid, number;
    while (1) {
        printf("Please enter 5: ");
        is_valid = scanf("%d", &number);
        if (is_valid == 1 && number == 5) {
            printf("Correct!\n");
            break; 
        } else {
            printf("Incorrect.\n");
            // Clear the input buffer to prevent accidental infinite loop
            while (getchar() != '\n') {}
        }
    }
    return 0;
}
```

## Fizzbuzz

Write an Assembly program `fizzbuzz.s`. It should do the following:

- Prompt the user to enter an integer between 1 and 100
- Make sure the entry is valid. Otherwise, print an error message and prompt them again. Loop this until they enter an appropriate number
- Loop from 1 to the number entered. If the number is a multiple of 2, print `fizz`. If it's a multiple of 3, print `buzz`. If it's a multiple of both, print `fizzbuzz`. Otherwise, print the number. 
- Note: you are not required to use functions, but you may find them helpful as you organize your code.

For example, if the user enters 8, the output should be:
```
1
fizz
buzz
fizz
5
fizzbuzz
7
fizz
```

This is a complex program with multiple nested comparisons! I strongly encourage you to start small and work your way up. Commit your progress to `csgit` every time you make progress. For example, you could do:

1. Write a program that prompts the user for a number and prints it back out. 
2. Update it to ensure the input is positive. If the number is zero or negative, print an error message and exit.
3. Update it to ensure the input isn't too big. If it's over 100, print an error message and exit.
4. Update it to loop instead of exiting. It should keep prompting and checking until the user provides good input.
5. Instead of just printing the input, update the program to print everything from 1 to that number.
6. Add handling to print "fizz" for even numbers.
7. Etc...

Make sure to include a test with your code! It should include coverage for corner cases. 

## Prime Checker

Write an Assembly program `prime-checker.s` that prompts the user for a positive integer, then reports whether or not the number is prime.

This is a tricky one! I suggest you start small and build one step at a time. For example, you could do:

1. Write a program with a global constant `N` that you set manually. It checks whether `N` is divisible by 3 and reports the result
2. Update the program to switch `N` to a global variable. Prompt the user for its value at runtime.
3. Update the program to prompt the user for two numbers, `N` and `D`. Check if `N` is divisible by `D` (aka check if `N/D` has remainder zero)
4. Update the program to loop over all values of `D` from 2 to `N-1`. If `N` is not divisible by any of them, it's prime
5. Update the program to be more efficient! As soon as you find a divisor, you know `N` is not prime, so you can break out of the loop

You are not required to use functions. However, you may find them useful to organize your code. 




# Stack Frames


TODO: add coverage for RECURSION!




% reading: Dive into Systems 9.5 (functions), 9.6 (recursion)

Submit code via `csgit`. Submit notes, screenshots, and scans via Moodle.

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


















