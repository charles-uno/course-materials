# Assembly Globals

### Coding in Assembly

- We'll be doing some coding exercises in Assembly (specifically aarch64) on emulators and on a Raspberry Pi
- Assembly code can be super efficient. Ours won't be.
- We are not studying to become assembly developers. We are here for the core concepts

### Hello World in C

```C
#include <stdio.h>
int main() {
    printf("Hello world!\n");
    return 0;
}
```

Your local C compiler can turn this into an executable, which you can then run:

```bash
$ gcc hello.c
$ ./a.out
Hello world!
```

### Hello World in Python

```python
print('Hello world!')
```

You can run this using your local Python interpreter:
```bash
$ python3 hello.py
Hello world!
```

### Hello World in Assembly

```arm
.section .rodata
    greeting: .ascii "Hello world!\n\0"

.section .text
.global main
main:
    ldr x0, =greeting
    bl printf
    mov x0, 0
    b exit
```

You can assemble this into an executable and run it on your Raspberry Pi:
```bash
$ gcc hello.s
$ ./a.out
Hello world!
```

### What makes assembly special?

- It takes a lot of lines to do anything
- There is so much boilerplates
- Yikes

### What makes assembly special?

- An Intel CPU and an AMD CPU can both run the same logic, but they will do things in slightly different ways.
- When coding in C, you (mostly) don't have to worry about it. The compiler makes your logic work on the current hardware.
- Same for Python. The interpreter (itself compiled) figures it out.
- Assembly is not like that. Intel assembly is tied to the hardware specifics of the Intel CPU. ARM assembly is a different language.
- We study Assembly because we want to talk about what is happening on hardware.

## Assembly Program Structure

### Assembly Program Structure

Specifically Aarch64, sometimes called ARM v8

### Assembly Boilerplate

The Assembly programs we write in this course will look like this:
```arm
.section .rodata
    // global constants

.section .data
    // global variables

.section .text
.global main
main:
    // execution starts here

    // return 0 (normal exit status)
    mov x0, 0
    b exit
```

### Formatting Your Code

- Work in lowercase by convention, but uppercase mostly works too
- Indentation and line breaks can help with legibility
- Any line that starts with `//` is a comment
- Question: how many comments should your code include?

### Global Constants

```arm
.section .rodata
    prompt: .ascii "how many koalas do you have? \0"
    digits_per_hand: .word 5
```
- Value is allocated at the start of the program
- Use the variable name to load the *address*
- Value does not change
- Types we will use: `word` and `ascii`

### Main

```arm
.section .text
.global main
main:
    ldr x0, =message
    bl printf
    mov x0, 0
    b exit
```
- If using a different compiler, you may need to swap `main` to `_start` or similar
- We'll talk about instructions (`ldr`, `bl`, etc) next
- Return 0 unless you are trying to indicate a failure

## Assembly Commands

### Register Names

- The 64-bit registers in aarch64 are named `x0`, `x1`, etc
- If you see `w0`, that's the lower 32 bits of `x0`
- If you see `r0`, it's probably a typo left over from the previous version of this class

### Memory Diagrams

Just the registers for now

These will get more interesting when we start talking about local variables

### Don't Worry!

- We are just looking at these to get a feel for them
- You will have plenty of time to practice
- You do not need to worry about memorizing anything right now

### Basic Commands in Assembly

```arm
... // double slash for inline comments
add x0, x1, 5 // add x1 + 5, store in x0
add x0, x1, x7 // add x1 + x7, store in x0
mov x4, 5 // set x4 = 5 (literal number)
mov x4, x5 // set x4 = x5
mul x2, x8, x3 // multiply x8 * x3, store in x2
mul x2, x8, 12 // multiply x8 * 12, store in x2
sub x5, x4, 3 // subtract x4 - 3, store in x5
sub x5, x4, x3 // subtract x4 - x3, store in x5
```

### Reading from Memory

Load the *address* of global variable `fizz` to `x3`:
```arm
ldr x3, =fizz
```

Register `x2` holds an *address*. Load the *value* to `x3`:
```arm
ldr x3, [x2]
```

Register `x2` holds an *address*. Load the *value* from `x2-0x20` to `x3`:
```arm
ldr x3, [x2, -0x20]
```

Global variable `fizz` holds a number. Load the address, then load the value from that address:
```arm
ldr x3, =fizz
ldr x3, [x3] // yes it can be the same register
```

### Writing to Memory

Register `x5` holds an *address*. Store the *value* from `x7` to that address:
```arm
str x7, [x5]
```

Register `x5` holds an *address*. Store the *value* from `x8` to `x5+0x10`
```arm
str x7, [x5, 0x10]
```

### We'll talk more about these ones later

Call the function `printf`, which prints output to the terminal:
```arm
bl printf
```

Call the function `exit`, which exits the program:
```arm
b exit
```

`b` is "branch". `bl` is "branch and link". We'll get into these later

## Printf

### Printf in C

- We use `printf` to print output to the terminal in Assembly
- Let's look at C first. The functionality is the same and C is more legible

```C
const char* name = "charles";
printf("hello my name is %s\n", name);
```

```C
const int m = 2, n = 3;
int s = m + n;
printf("%d + %d = %d\n", m, n, s);
```

### What does it do?

- The first argument to `printf` must be a string
- The string can include format specifiers like `%d`
- Subsequent arguments are inserted into the string (in order) in place of the format specifiers

### Format Specifiers

- `%d` - interpret the value as an integer
- `%c` - interpret the value as an ASCII character
- `%s` - interpret the value as a *pointer* to a null-terminated string
- These values are just ones and zeroes! You can use whichever format speficier you want. But you might not like the results
- Why do we use a pointer to the string instead of the string itself?

### Calling Printf in Assembly

We'll get deeper into function calls later. For now:
- `printf` is a function
- `bl printf` is how we call it
- `printf` looks at `x0` for its first argument (the output string)
- If the output string includes a format identifier, it grabs the value from `x1`
- If the output string includes another format identifier, it grabs the value from `x2`, etc
- Format identifiers in Assembly are the same as those in C

### Assembly Printf Example 1

```arm
.section .rodata
    output: .ascii "hello my name is %s\n\0"
    name: .ascii "charles\0"

.section .text
.global main
main:
    ldr x0, =output
    ldr x1, =name
    bl printf
    mov x0, 0
    b exit
```

### Assembly Printf Example 2

```arm
.section .rodata
    output_str: .ascii "the current year is %d\n\0"
    current_year: .word 2026

.section .text
.global main
main:
    ldr x0, =output_str
    ldr x1, =current_year
    ldr x1, [x1]
    bl printf
    mov x0, 0
    b exit
```

### Assembly Printf Example 3

```arm
.section .rodata
    output_str: .ascii "%d + %d = %d\n\0"

.section .text
.global main
main:
    ldr x0, =output_str
    mov x1, 2
    mov x2, 3
    add x3, x1, x2
    bl printf
    mov x0, 0
    b exit
```

## Scanf

### Minimal Read

```arm
.section .rodata
    input_fmt: .ascii "%d\0"
.section .data
    input_val: .word 0
.section .text
.global main
main:
    ldr x0, =input_fmt
    ldr x1, =input_val
    bl scanf
    mov x0, 0
    b exit
```

### More Useful Read

```arm
.section .rodata
    prompt: .ascii "Please enter a number: \0"
    report: .ascii "You entered %d\n\0"
    input_fmt: .ascii "%d\0"
.section .data
    input_val: .word 0
.section .text
.global main
main:
    ldr x0, =prompt
    bl printf
    ldr x0, =input_fmt
    ldr x1, =input_val
    bl scanf
    ldr x1, =input_val
    ldr x1, [x1]
    ldr x0, =report
    bl printf
    mov x0, 0
    b exit
```

## Automated Testing

### Expectations on Assignments

- Every piece of code you turn in should come with a test
- Make sure it compiles
- Provide example input, check the output
- Tests will be shell scripts
- I will provide a template

### Why Test?

- Code is often modified by someone other than the original author
- Code is often modified long after the original context is forgotten
- Non-obvious program behavior may be (or become) important
- Documentation can easily be outdated and/or ignored
- Automated tests make noise before breaking changes are committed
- They also act as live documentation

### Why Shell?

- Many languages have built-in test frameworks. Assembly doesn't. We're improvising
- Shell scripting uses familiar syntax (ls, gcc)
- You are welcome to copy-paste from my example
- I tried Python last time. It was more work. You are welcome to try it again!

### Why Bash?

```bash
#!/usr/bin/bash
set -e

function run_and_check {
    local TEST_CASE_NAME="$1"
    local INPUT="$2"
    local EXPECTED_OUTPUT="$3"
    ACTUAL_OUTPUT=$(echo "$INPUT" | ./a.out) ||:
    if [[ "$EXPECTED_OUTPUT" != "$ACTUAL_OUTPUT" ]]; then
        echo "$TEST_CASE_NAME - expected \"$EXPECTED_OUTPUT\" but got \"$ACTUAL_OUTPUT\""
    else
        echo "$TEST_CASE_NAME - ok"
    fi
}


# Case 0: compile the code
CASE_NAME="compile"
rm a.out ||:
gcc add_two.s 
if [[ "$?" == "0" || -f a.out ]]; then 
    echo "$CASE_NAME - ok"
else
    echo "$CASE_NAME - build failed"
fi

# Case 1: small positive ints
CASE_NAME="positive"
INPUT="3
4"
EXPECTED_OUTPUT="Enter a number: Enter a number: Sum: 7"
run_and_check "$CASE_NAME" "$INPUT" "$EXPECTED_OUTPUT"

# Case 2: sum to zero
CASE_NAME="opposite"
INPUT="-3
3"
EXPECTED_OUTPUT="Enter a number: Enter a number: Sum: 0"
run_and_check "$CASE_NAME" "$INPUT" "$EXPECTED_OUTPUT"

# Case 3: negatives
CASE_NAME="negative"
INPUT="-3
-106"
EXPECTED_OUTPUT="Enter a number: Enter a number: Sum: -109"
run_and_check "$CASE_NAME" "$INPUT" "$EXPECTED_OUTPUT"
```