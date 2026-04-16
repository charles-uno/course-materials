
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






















