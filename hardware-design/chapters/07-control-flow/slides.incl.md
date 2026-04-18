beamer: true
---

# Control Flow

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

New instruction:
```arm
cmp x0, 5
cmp x0, x1
```

Compares the two inputs. Sets processor flags accordingly

### Processor Flags

```arm
cmp x0, x1
```

This sets the NZCV processor flags:

- Negative - `x0-x1` is negative (when interpreted as a *signed* int)
- Zero - `x0-x1` is zero
- Carry - `x0-x1` is positive (when interpreted as an *unsigned* int)
- oVerflow - `x0-x1` overflows (when interpreted as a *signed* int)

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

### Signed and Unsigned

Importantly: `cmp` is just comparing binary data! It does not know what the data represents

```arm
cmp 0xffffffff, 0x1
```

- Unsigned 0xffffffff is 4.3 billion
- Signed 0xffffffff is -1
- So which is bigger? 0xFFFFFFFF or 0x1?

### Don't Worry About It

The conditional branch instructions before are meant for signed numbers (aka two's complement). For unsigned we *should* use:

| Instruction | Description |
| ----------- | ----------- |
| `blo`       | Branch if lower than |
| `bls`       | Branch if lower or same |
| `bhi`       | Branch if higher than |
| `bhs`       | Branch if higher or same |

In this class, we will be dealing with small numbers. You can just use `bgt` and forget about `bhi`

### Labels

Conditional branch instructions update PC to "jump" execution to the given label. For example:

```arm
cmp x0, 5
bgt logic_for_handling_six_plus
```

This looks just like what we did for functions! How are function labels different from conditional labels?

### It's All The Same

- Labels allow us to jump within the code
- Aarch64 doesn't know about functions, conditionals, loops. It just knows PC
- Recall: we manually handle function input, output, local variables

### Summary

- Use `cmp` to compare two values, set processor flags
- Use `beq` (etc) to execute logic based on those flags

## If

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

We can do this by conditionally *skipping* the print:

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

### If V2 (Assembly)

The previous slide showed how to get this behavior by skipping code. We can also do it by running the extra code. This reads more like the Python:


```arm
    cmp x0, 0
    ble positive
endif:
    ldr x0, =reply_done
    bl printf
    b exit

positive:
    ldr x0, =reply_positive
    bl printf
    b endif
```

### Summary

- Conditionally skip the code that would be in the `if` block
- This means your conditional should be the opposite of what you would write in the `if`

## If/Else

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

### If/Elif/Else (Python)

In other languages this may use a `switch` statement

```python
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")
```



### If/Elif/Else (Assembly)

```arm
    cmp x0, 0
    beq zero
    blt negative
positive:
    ldr x0, =reply_positive
    b endif
zero:
    ldr x0, =reply_zero
    b endif
negative:
    ldr x0, =reply_negative
    b endif
endif:
    bl printf
```

### Summary

- If/else: conditional branch followed by an unconditional branch
- The two are mutually exclusive. Always want to execute one, never both

## While Loop

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

### Summary

- Jump forward to the loop test
- Maybe jump back to the loop body
- At the end of the loop body, we get back to the test
- Don't forget to increment or you'll go forever

## For Loop

### For Loop (C)

Note: `range(5)` is actually pretty weird in Python. Back to the classic:

```C
for (int i = 0; i < 5; i++) {
    printf("%d\n");
}
printf("done\n");
```

### For Loop Breakdown

- Initialize `i=0`
- Perform the loop test (`i<5`)
- If it passes, perform the loop body (print)
- Increment `i`
- Back up to the loop test

### For Loop (Assembly)

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

- Loop test first
- Maybe bail from the loop
- Loop body
- Increment
- Unconditionally back to the top

## Nested Logic

### Use Flags Promptly

Any concerns here?

```arm
cmp x4, 100
bl printf
// branch based on the value of x4
beq handle_large_value
```

### Use Flags Promptly

- The processor has only one set of flags (NZCV)
- It's very likely that there are more `cmp` calls within `printf`
- That `beq` is not going to work as intended

### Writing Nested Logic

Be careful to use your processor flags before you overwrite them!

### Nested Logic Example

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

### Summary

- `cmp` sets the processor flags
- There is only one set of flags
- If you call `b`, `bl`, etc, generally assume they have been overwritten
- Don't accidentally overwrite them before you use them!