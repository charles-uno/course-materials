beamer: true
---

# Assembly Conditionals

### Branch (and Sometimes Link)

Recall from before:

- We print with `bl printf`
- We exit the program with `b exit`
- The commands `b` and `bl` affect the program counter (PC) which holds the address of the next instruction
- `bl` also sets the link register (LR) so we know how to return

### Trees usually have more than once branch

- The logic we've looked at so far has been entirely linear
- What if we want different behavior on the fly?
- How do we write conditionals (`if`, `else`) and loops (`for`, `while`)?

## Comparison

### Comparison

- New instruction: `cmp` (aka compare)
- Updates processor flags NZCV

### Processor Flags

You don't need to know the details, but for the sake of completeness:
- N (Negative): Set if the result is negative (MSB is 1).
- Z (Zero): Set if the result is zero (the operands were equal).
- C (Carry): Set if the subtraction did not require a "borrow" (used for unsigned comparisons).
- V (oVerflow): Set if the result overflowed the signed integer range

### Conditional Branching

After setting the processor flags, how do we use them?

| Instruction | Description |
| ----------- | ----------- |
| `beq`       | Branch if equal |
| `bne`       | Branch if not equal |
| `blt`       | Branch if less than |
| `ble`       | Branch if less than or equal |
| `bgt`       | Branch if greater than |
| `bge`       | Branch if greater than or equal |

### Labels

Wait -- how are these different from functions?

### Vocabulary Reminder

- There are other commands too
- Example: `cbz` (compare and branch if zero)
- We are prioritizing small vocabulary

### Signed and Unsigned

The previous ones are meant for unsigned (aka two's complement) numbers. For unsigned we *should* use:

| Instruction | Description |
| ----------- | ----------- |
| `blo`       | Branch if lower than |
| `bls`       | Branch if lower or same |
| `bhi`       | Branch if higher than |
| `bhs`       | Branch if higher or same |

In this class we'll keep out numbers pretty small, so we don't need to worry about overflow

### Summary

- Use `cmp` to compare two values, set processor flags
- Use `beq` (etc) to execute logic based on those flags
- As long as we don't worry about huge numbers, we can pretend `bgt` is the same as `bhi`

## Conditional Logic

### If (Python)

```python
if x > 0:
    print("positive")
print("done")
```

### Breaking it Down

What, explicitly, is that code doing?
- Compare x to zero (aka subtract x-0)
- If x is greater than 0 (aka if the result is positive), print "positive"
- Either way, print "done"

### If (Assembly)

```arm
    cmp x0, 0
    ble nonpositive
positive:
    ldr x0, =reply_positive
    bl printf
nonpositive:
    ldr x0, =reply_done
    bl printf
    b exit
```

### If/Else (Python)

```python
if x % 2 == 0:
    print("even")
else:
    print("odd")
```

### If/Else (Assembly)

Note: `endif` is just a label. You can call it anything

```arm
    and x0, x0, 1
    cmp x0, 0
    bne odd
even:
    ldr x0, =reply_even
    b endif
odd:
    ldr x0, =reply_odd
    b endif
endif:
    bl printf
```

### Summary

- If: use a conditional branch to skip a line
- Else: conditional branch followed by an unconditional branch

## Loops

### While Loop (Python)

```python
i = 0
while i < 5:
    print(i)
    i += 1
print("done")
```

### Breaking it Down

Again, let's be explicit about what's happening:
- Initialize `i` to 0
- Perform the loop test: compute `i - 5` and check if it's negative
- If the loop test passes, perform the loop body: print, increment
- Go back to the loop test

### While Loop (Assembly)

```arm
    mov x3, 0
    b loop_test
loop_body:
    ldr x0, =print_int
    mov x1, x3
    bl printf
    add x3, x3, 1
loop_test:
    cmp x3, 5
    blt loop_body
    // done with loop
    ldr x0, =done
    bl printf
```

### Local Variables?

- The example above does everything in registers for brevity
- In "real" code, local variables live on the stack
- How would the code need to change to reflect that?

### For Loop (C)

Let's not worry about what `range(5)` is actually doing in Python

```C
for (int i = 0; i < 5; i++) {
    printf("%d\n");
}
printf("done\n");
```

### For Loop 

```arm
    mov x19, 0
loop_start:
    cmp x19, 5
    bge loop_done
    // loop body
    ldr x0, =print_int
    mov x1, x19
    bl printf
    // increment loop variable
    add x19, x19, 1
    b loop_start
loop_done:
    ldr x0, =done
    bl printf
```

### Summary

- While loop: body (may include increment), test
- For loop: test, body, increment

## Nested Comparisons

### Nested Comparisons

- There is only one set of processor flags (NZCV)
- We have to be very careful to do the conditional branch before overwriting

### Nested Example

```arm
.section .rodata
prompt: .ascii "Please say 5: \0"
input_fmt: .ascii "%d\0"
reply_no: .ascii "No.\n\0"
reply_yes: .ascii "Yes!\n\0"

.section .data
guess: .word 0

.text
.global main
main: 
begin_loop:
    // ask for input
    ldr x0, =prompt
    bl printf
    // read the guess
    ldr x0, =input_fmt
    ldr x1, =guess
    bl scanf
    // load guess from memory
    ldr x1, =guess
    ldr x1, [x1]
    // check the guess
    cmp x1, 5
    // if it's 5, we're done
    beq break
    // otherwise, try again
    ldr x0, =reply_no
    bl printf
    b begin_loop
break:
    ldr x0, =reply_yes
    bl printf
    // return zero
    mov x0, 0
    b exit
```

### Another Example

TODO: sum of odd numbers?

check if a number is prime?
