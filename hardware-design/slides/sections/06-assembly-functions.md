beamer: true
---

# Assembly Functions

## The Stack

### Process Memory

When launching a process:

- The OS loads program instructions into memory
- It initializes the CPU
- And it allocates an address space for that process

Part of that address space is **the stack**

### Remember From Before

The heap is a disorganized pool of memory available to the entire program:
- Lots of space!
- You have to "find" space before using it, and manually free it when done
- Big files might be broken up, causing slower access

The stack is structured:
- Not as much space
- Fast access (often cached)
- Always build on top of the existing stack

### The Stack

- The stack is a region of memory that the OS has reserved for this process
- We can assign local variables there
- We have the special registers SP (stack pointer) and FP (frame pointer) to keep track

% local variables. scope is good for code complexity. 
% also we can allocate space dynamically, unlike global variables which must be set at compile time

### Memory Diagram

We can draw a **memory diagram** to keep track of registers and memory for our process:

|||

| Register | Value |
| --- | --- |
| x0 | ? |
| x1 | ? |
| x2 | ? |
| x3 | ? |
| sp | ? |
| fp | ? |
| pc | ? |
| lr | ? |

| Address | Value |
| --- | --- |
| 0x3f90 | ? |
| 0x3fa0 | ? |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | ? |
| 0x3fe0 | ? |
| 0x3ff0 | ? |
| 0x4000 | ? |

|||

### Stack Numbering

- We usually start the stack at 0x4000 or 0x5000. This is arbitrary
- The stack builds *up*
- Higher on the stack is *decreasing* memory address
- Increment by 0x10 bytes (more on this later)

### The Stack is a Convention!

- We will be talking about how the stack is used in *principle*
- There are lots of cases where the code may break these rules for better efficiency
- We will talk about a few of those cases too

## Local Variables

### Variable Scope

Local variables are visible only within that function. Other functions cannot touch those variables. The names can be reused.

```python
def fizz(x):
	y = x + 5
	a = y/2
	return a*y

def buzz(x):
	y = 2
	b = 14 + x
	return fizz(b) + y

def main():
	y = 12
	print(buzz(y))
```

### Variable Scope on the Stack

Here's how we keep track of those variables:

- We put the local variables for `main` at the bottom of the stack
- Then we put the local variables for `buzz` on top of that
- Then we put the local variables for `fizz` on top of that
- Etc
- To allocate more space on the stack, just change SP

### Stack Overflow

- The OS allocates a certain amount of memory for the stack when it starts the process
- What happens if the process tries to grow its stack larger than that?

### Stack Overflow

- If you try to read or write data past the top of your stack, the OS will terminate your program
- Some languages limit call depth to reduce the risk of stack overflow (eg `RecursionError` in Python)
- Some languages (eg Rust, Go) start with a small stack and grow it as needed. This adds overhead
- When allocating a large variable, we usually store the *address* on the stack, but the data in the heap

### Example Local Variable in Assembly

```arm
.section .rodata
prompt: .ascii "int plz: \0"
fmt: .ascii "%d\0"
output: .ascii "%d+1=%d\n\0"
.align 2

.global main
main: 
sub sp, sp, 0x10
ldr x0, =prompt
bl printf
ldr x0, =fmt
mov x1, sp
bl scanf
ldr x0, =output
ldr x1, [sp]
add x2, x1, 1
bl printf
add sp, sp, 0x10
b exit
```

### Local Variable Walkthrough (0)

Initial state:

|||
| Register | Value |
| --- | --- |
| x0 | ? |
| x1 | ? |
| x2 | ? |
| x3 | ? |
| sp | 0x4000 |
| fp | ? |
| pc | ? |
| lr | ? |

| Address | Value |
| --- | --- |
| 0x3f90 | ? |
| 0x3fa0 | ? |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | ? |
| 0x3fe0 | ? |
| 0x3ff0 | ? |
| 0x4000 | (in use) |
|||

### Local Variable Walkthrough (1)

```arm
sub sp, sp, 0x10
```

|||
| Register | Value |
| --- | --- |
| x0 | ? |
| x1 | ? |
| x2 | ? |
| x3 | ? |
| sp | $\cancel{0x4000}$ 0x3ff0 |
| fp | ? |
| pc | ? |
| lr | ? |

| Address | Value |
| --- | --- |
| 0x3f90 | ? |
| 0x3fa0 | ? |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | ? |
| 0x3fe0 | ? |
| 0x3ff0 | (reserved) |
| 0x4000 | (in use) |
|||

### Local Variable Walkthrough (2)

```arm
ldr x0, =prompt
bl printf
```

|||
| Register | Value |
| --- | --- |
| x0 | =prompt |
| x1 | ? |
| x2 | ? |
| x3 | ? |
| sp | $\cancel{0x4000}$ 0x3ff0 |
| fp | ? |
| pc | ? |
| lr | ? |

| Address | Value |
| --- | --- |
| 0x3f90 | ? |
| 0x3fa0 | ? |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | ? |
| 0x3fe0 | ? |
| 0x3ff0 | (reserved) |
| 0x4000 | (in use) |
|||

Prints: `int plz: `

### Local Variable Walkthrough (3)

```arm
ldr x0, =fmt
mov x1, sp
```

|||
| Register | Value |
| --- | --- |
| x0 | $\cancel{=prompt}$ =fmt |
| x1 | 0x3ff0 |
| x2 | ? |
| x3 | ? |
| sp | $\cancel{0x4000}$ 0x3ff0 |
| fp | ? |
| pc | ? |
| lr | ? |

| Address | Value |
| --- | --- |
| 0x3f90 | ? |
| 0x3fa0 | ? |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | ? |
| 0x3fe0 | ? |
| 0x3ff0 | (reserved) |
| 0x4000 | (in use) |
|||

### Local Variable Walkthrough (4)

```arm
bl scanf
```
Waits for user input. Let's say the user enters `86400`

|||
| Register | Value |
| --- | --- |
| x0 | $\cancel{=prompt}$ =fmt |
| x1 | 0x3ff0 |
| x2 | ? |
| x3 | ? |
| sp | $\cancel{0x4000}$ 0x3ff0 |
| fp | ? |
| pc | ? |
| lr | ? |

| Address | Value |
| --- | --- |
| 0x3f90 | ? |
| 0x3fa0 | ? |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | ? |
| 0x3fe0 | ? |
| 0x3ff0 | 86400 |
| 0x4000 | (in use) |
|||

### Local Variable Walkthrough (5)

```arm
ldr x0, =output
ldr x1, [sp]
add x2, x1, 1
```

|||
| Register | Value |
| --- | --- |
| x0 | $\cancel{=prompt}$ $\cancel{=fmt}$ =output |
| x1 | $\cancel{0x3ff0}$ 86400 |
| x2 | 86401 |
| x3 | ? |
| sp | $\cancel{0x4000}$ 0x3ff0 |
| fp | ? |
| pc | ? |
| lr | ? |

| Address | Value |
| --- | --- |
| 0x3f90 | ? |
| 0x3fa0 | ? |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | ? |
| 0x3fe0 | ? |
| 0x3ff0 | 86400 |
| 0x4000 | (in use) |
|||

### Local Variable Walkthrough (6)

```arm
bl printf
add sp, sp, 0x10
b exit
```

|||
| Register | Value |
| --- | --- |
| x0 | $\cancel{=prompt}$ $\cancel{=fmt}$ =output |
| x1 | $\cancel{0x3ff0}$ 86400 |
| x2 | 86401 |
| x3 | ? |
| sp | $\cancel{0x4000}$ $\cancel{0x3ff0}$ 0x4000 |
| fp | ? |
| pc | ? |
| lr | ? |

| Address | Value |
| --- | --- |
| 0x3f90 | ? |
| 0x3fa0 | ? |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | ? |
| 0x3fe0 | ? |
| 0x3ff0 | (freed) |
| 0x4000 | (in use) |
|||

Prints: `86400+1=86401` then exits

### Summary

- We can store local variables on the stack
- To allocate space on the stack, move SP up
- To free that space, move SP back down
- This is much faster than using the (unstructured) heap

## Stack Frames

### Utterly Deranged

$$$
\begin{center}
\includegraphics[width=0.8\columnwidth]{images/assembly-functions/sure-grandma}
\end{center}
$$$

### The Frame Pointer

In the previous example, we stored a local variable to the stack:
- Move SP up to reserve space
- Put input there using `scanf` (or store data with `str`)
- Load data with `ldr`
- Move SP back down to free the space

But what if we want to know how much of the stack belongs to the current function?

### The Frame Pointer

- SP always points to the top of the stack
- FP (the frame pointer) points to the bottom of the **stack frame**
- A stack frame is the portion of the stack used by a function
- Tracking FP is not strictly necessary! But debugging is harder without it

% https://stackoverflow.com/questions/46797915/what-are-the-advantages-of-a-frame-pointer

### Initial State

At the start of the program, our memory diagram looks like this:

|||
| Register | Value |
| --- | --- |
| x0 | ? |
| x1 | ? |
| x2 | ? |
| x3 | ? |
| sp | 0x4000 |
| fp | 0x5000 |
| pc | ? |
| lr | ? |

| Address | Value |
| --- | --- |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | ? |
| 0x3fe0 | ? |
| 0x3ff0 | ? |
| 0x4000 | ? |
| ... | ? |
| 0x5000 | ? $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

The existing stack frame goes from `0x5000` (FP) to `0x4000` (SP)

### Stacking Frames

After calling into `main`, we update SP and FP to add a new frame to the stack:

|||
| Register | Value |
| --- | --- |
| x0 | ? |
| x1 | ? |
| x2 | ? |
| x3 | ? |
| sp | 0x3fd0 |
| fp | 0x3ff0 |
| pc | ? |
| lr | ? |

| Address | Value |
| --- | --- |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | ? |
| 0x3fe0 | ? |
| 0x3ff0 | ? $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | ? |
| ... | ? |
| 0x5000 | ? $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Tracking Stacked Frames

Wait a sec:

- When we move into a new function, we update SP and FP to define our new stack frame
- But registers do not "remember" past values
- When the function is done and we want to return, how do we go back to the previous frame?

### Stack Frame Overhead

- At the start of a function, when creating the new stack frame, also store the previous FP
- At the end of the function, when returning to the previous stack frame, restore FP
- SP does not need to be stored explicitly. Why not?

### SIMD? More like PITA

- Recall SIMD: Single Instruction, Multiple Data
- Fetch and decode once, execute in parallel
- Aarch64 is a 64-bit architecture. Instructions process 8 bytes at a time
- Sometimes it does 128 bits (16 bytes) instead
- I don't have time to worry about that, and neither do you. For the purposes of this class, everything is 16 bytes.
- This is wasteful! We are using double the memory we need, sometimes more
- We are not trying to become assembly developers. We're here for the concepts

### For the sake of completeness

- `stp` (store pair) is the SIMD version of `str`
- `ldp` (load pair) is the SIMD version of `ldr`
- That's how "real" code handles stack frames
- Those commands even allow SP to be updated at the same time!
- We are choosing to prioritize a small vocabulary

### Example Time

So what does this look like in Assembly?

### Example Stack Frame

```arm
.section .rodata
output: .ascii "%d+1=%d\n\0"
.align 2

.text
.global main
main: 
sub sp, sp, 0x20
str lr, [sp, 0x10]
str fp, [sp]
add fp, sp, 0x20
ldr x0, [sp]
ldr x0, =output
mov x1, 5
add x2, x1, 1
bl printf
ldr lr, [sp, 0x10]
ldr fp, [sp]
add sp, sp, 0x20
b exit
```

### What's LR?

Hold that thought

Let's work through this together

## Function Calls

### Branch and Link

- We use `bl` to call functions, like `bl printf`
- `bl` updates the program counter (PC). Instead of executing the next address in memory, we "jump" to some other part of the program
- Once we're done with the function, we want to get back to the call site
- That's what the link register (LR) is for

% NOTE: x0, x1, ... are input args
% x0, x1, ... are also the return values

### Step by Step

When we execute `bl printf`:
- Increment PC to point to whatever instruction comes next
- Set LR = PC
- Update PC to point to the address of `printf`

At the end of `printf`, we run `ret`:
- Set PC = LR
- This means the next instruction we execute will be the one right after `bl printf`

### Example Function

```arm,linenos=true,xleftmargin=1em
.section .rodata
prompt: .ascii "int plz: \0"
fmt: .ascii "%d\0"
output: .ascii "%d+1=%d\n\0"
.align 2

.text
add_one:
sub sp, sp, 0x20
str fp, [sp]
str lr, [sp, 0x10]
add fp, sp, 0x10
add x0, x0, 1
ldr lr, [sp, 0x10]
ldr fp, [sp]
add sp, sp, 0x20
ret

.global main
main: 
sub sp, sp, 0x30
str lr, [sp, 0x20]
str fp, [sp, 0x10]
add fp, sp, 0x20
ldr x0, =prompt
bl printf
ldr x0, =fmt
mov x1, sp
bl scanf
ldr x0, [sp]
bl add_one
mov x2, x0
ldr x0, =output
ldr x1, [sp]
bl printf
ldr lr, [sp, 0x20]
ldr fp, [sp, 0x10]
add sp, sp, 0x30
mov x0, 0
b exit
```

### Function Call Walkthrough (0)

Initial state:

|||
| Register | Value |
| --- | --- |
| x0 | ? |
| x1 | ? |
| x2 | ? |
| x3 | ? |
| sp | 0x4000 |
| fp | 0x5000 |
| pc | 0x15 |
| lr | (caller lr) |

| Address | Value |
| --- | --- |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | ? |
| 0x3fe0 | ? |
| 0x3ff0 | ? |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (1)

```arm,linenos=true,xleftmargin=1em,firstnumber=21
sub sp, sp, 0x30
```

|||
| Register | Value |
| --- | --- |
| x0 | ? |
| x1 | ? |
| x2 | ? |
| x3 | ? |
| sp | $\cancel{0x4000}$ 0x3fd0 |
| fp | 0x5000 |
| pc | $\cancel{...}$ 0x16 |
| lr | (caller lr) |

| Address | Value |
| --- | --- |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | (reserved) |
| 0x3fe0 | (reserved) |
| 0x3ff0 | (reserved) |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (2)

```arm,linenos=true,xleftmargin=1em,firstnumber=22
str lr, [sp, 0x20]
str fp, [sp, 0x10]
add fp, sp, 0x20
```

|||
| Register | Value |
| --- | --- |
| x0 | ? |
| x1 | ? |
| x2 | ? |
| x3 | ? |
| sp | 0x3fd0 |
| fp | $\cancel{0x5000}$ 0x3ff0 |
| pc | $\cancel{...}$ 0x19 |
| lr | (caller lr) |

| Address | Value |
| --- | --- |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | (reserved) |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (3)

```arm,linenos=true,xleftmargin=1em,firstnumber=25
ldr x0, =prompt
bl printf
```

|||
| Register | Value |
| --- | --- |
| x0 | =prompt |
| x1 | ? |
| x2 | ? |
| x3 | ? |
| sp | 0x3fd0 |
| fp | 0x3ff0 |
| pc | $\cancel{...}$ 0x1b |
| lr | (caller lr) |

| Address | Value |
| --- | --- |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | (reserved) |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

Prints: `int plz:`

### Stack Frames for Built-In Functions?

- `bl printf` is a function call
- `printf` has its own stack frame
- Same for `scanf`
- For the sake of convenience, let's just worry about `add_one`

### Function Call Walkthrough (4)

```arm,linenos=true,xleftmargin=1em,firstnumber=27
ldr x0, =fmt
mov x1, sp
```

|||
| Register | Value |
| --- | --- |
| x0 | $\cancel{=prompt}$ =fmt |
| x1 | 0x3fd0 |
| x2 | ? |
| x3 | ? |
| sp | 0x3fd0 |
| fp | 0x3ff0 |
| pc | $\cancel{...}$ 0x1d |
| lr | (caller lr) |

| Address | Value |
| --- | --- |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | (reserved) |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (5)

```arm,linenos=true,xleftmargin=1em,firstnumber=29
bl scanf
```

Reads user input. Let's say they enter `86400`

|||
| Register | Value |
| --- | --- |
| x0 | =fmt |
| x1 | 0x3fd0 |
| x2 | ? |
| x3 | ? |
| sp | 0x3fd0 |
| fp | 0x3ff0 |
| pc | 0x1e |
| lr | (caller lr) |

| Address | Value |
| --- | --- |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | 86400 |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (6)

```arm,linenos=true,xleftmargin=1em,firstnumber=30
ldr x0, [sp]
```

|||
| Register | Value |
| --- | --- |
| x0 | $\cancel{=fmt}$ 86400 |
| x1 | 0x3fd0 |
| x2 | ? |
| x3 | ? |
| sp | 0x3fd0 |
| fp | 0x3ff0 |
| pc | 0x1f |
| lr | (caller lr) |

| Address | Value |
| --- | --- |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | 86400 |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (7)

```arm,linenos=true,xleftmargin=1em,firstnumber=31
bl add_one
```

|||
| Register | Value |
| --- | --- |
| x0 | 86400 |
| x1 | 0x3fd0 |
| x2 | ? |
| x3 | ? |
| sp | 0x3fd0 |
| fp | 0x3ff0 |
| pc | $\cancel{0x1f}$ 0x09 |
| lr | $\cancel{(caller lr)}$ 0x20 |

| Address | Value |
| --- | --- |
| 0x3fb0 | ? |
| 0x3fc0 | ? |
| 0x3fd0 | 86400 |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (8)

```arm,linenos=true,xleftmargin=1em,firstnumber=9
sub sp, sp, 0x20
str fp, [sp]
str lr, [sp, 0x10]
add fp, sp, 0x10
```

|||
| Register | Value |
| --- | --- |
| x0 | 86400 |
| x1 | 0x3fd0 |
| x2 | ? |
| x3 | ? |
| sp | $\cancel{0x3fd0}$ 0x3fb0 |
| fp | $\cancel{0x3ff0}$ 0x3fc0 |
| pc | $\cancel{...}$ 0x0d |
| lr | 0x20 |

| Address | Value |
| --- | --- |
| 0x3fb0 | 0x3fc0 |
| 0x3fc0 | 0x20 $\rdelim\}{-2}{3mm}[add\_one frame]$ |
| 0x3fd0 | 86400 |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (9)

```arm,linenos=true,xleftmargin=1em,firstnumber=13
add x0, x0, 1
```

|||
| Register | Value |
| --- | --- |
| x0 | $\cancel{86400}$ 86401 |
| x1 | 0x3fd0 |
| x2 | ? |
| x3 | ? |
| sp | 0x3fb0 |
| fp | 0x3fc0 |
| pc | $\cancel{...}$ 0x0e |
| lr | 0x20 |

| Address | Value |
| --- | --- |
| 0x3fb0 | 0x3fc0 |
| 0x3fc0 | 0x20 $\rdelim\}{-2}{3mm}[add\_one frame]$ |
| 0x3fd0 | 86400 |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (10)

```arm,linenos=true,xleftmargin=1em,firstnumber=14
ldr lr, [sp, 0x10]
ldr fp, [sp]
add sp, sp, 0x20
```

|||
| Register | Value |
| --- | --- |
| x0 | 86401 |
| x1 | 0x3fd0 |
| x2 | ? |
| x3 | ? |
| sp | $\cancel{0x3fb0}$ 0x3fd0 |
| fp | $\cancel{0x3fc0}$ 0x3ff0 |
| pc | $\cancel{...}$ 0x0d |
| lr | $\cancel{0x20}$ 0x20 |

| Address | Value |
| --- | --- |
| 0x3fb0 | (freed) |
| 0x3fc0 | (freed) |
| 0x3fd0 | 86400 |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (11)

```arm,linenos=true,xleftmargin=1em,firstnumber=17
ret
```

|||
| Register | Value |
| --- | --- |
| x0 | 86401 |
| x1 | 0x3fd0 |
| x2 | ? |
| x3 | ? |
| sp | 0x3fd0 |
| fp | 0x3ff0 |
| pc | $\cancel{0x12}$ 0x20 |
| lr | 0x20 |

| Address | Value |
| --- | --- |
| 0x3fb0 | (freed) |
| 0x3fc0 | (freed) |
| 0x3fd0 | 86400 |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (12)

```arm,linenos=true,xleftmargin=1em,firstnumber=32
mov x2, x0
ldr x0, =output
ldr x1, [sp]
bl printf
```

|||
| Register | Value |
| --- | --- |
| x0 | $\cancel{86401}$ =output |
| x1 | $\cancel{0x3fd0}$ 86400 |
| x2 | 86401 |
| x3 | ? |
| sp | 0x3fd0 |
| fp | 0x3ff0 |
| pc | $\cancel{...}$ 0x24 |
| lr | 0x20 |

| Address | Value |
| --- | --- |
| 0x3fb0 | (freed) |
| 0x3fc0 | (freed) |
| 0x3fd0 | 86400 |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

Prints: `86400+1=86401`

### Function Call Walkthrough (13)

```arm,linenos=true,xleftmargin=1em,firstnumber=36
ldr lr, [sp, 0x20]
ldr fp, [sp, 0x10]
```

|||
| Register | Value |
| --- | --- |
| x0 | =output |
| x1 | 86400 |
| x2 | 86401 |
| x3 | ? |
| sp | 0x3fd0 |
| fp | $\cancel{0x3ff0}$ 0x5000 |
| pc | $\cancel{...}$ 0x26 |
| lr | $\cancel{0x20}$ (caller lr) |

| Address | Value |
| --- | --- |
| 0x3fb0 | (freed) |
| 0x3fc0 | (freed) |
| 0x3fd0 | 86400 |
| 0x3fe0 | 0x5000 |
| 0x3ff0 | (caller lr) $\rdelim\}{-3}{3mm}[main frame]$ |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (14)

```arm,linenos=true,xleftmargin=1em,firstnumber=38
add sp, sp, 0x30
```

|||
| Register | Value |
| --- | --- |
| x0 | =output |
| x1 | 86400 |
| x2 | 86401 |
| x3 | ? |
| sp | $\cancel{0x3fd0}$ 0x4000 |
| fp | 0x5000 |
| pc | $\cancel{...}$ 0x27 |
| lr | $\cancel{0x20}$ (caller lr) |

| Address | Value |
| --- | --- |
| 0x3fb0 | (freed) |
| 0x3fc0 | (freed) |
| 0x3fd0 | (freed) |
| 0x3fe0 | (freed) |
| 0x3ff0 | (freed) |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

### Function Call Walkthrough (15)

```arm,linenos=true,xleftmargin=1em,firstnumber=39
mov x0, 0
b exit
```

|||
| Register | Value |
| --- | --- |
| x0 | $\cancel{=output}$ 0 |
| x1 | $\cancel{0x3fd0}$ 86400 |
| x2 | 86401 |
| x3 | ? |
| sp | 0x4000 |
| fp | 0x5000 |
| pc | $\cancel{...}$ 0x28 |
| lr | $\cancel{0x20}$ (caller lr) |

| Address | Value |
| --- | --- |
| 0x3fb0 | (freed) |
| 0x3fc0 | (freed) |
| 0x3fd0 | (freed) |
| 0x3fe0 | (freed) |
| 0x3ff0 | (freed) |
| 0x4000 | (in use) |
| ... | (in use) |
| 0x5000 | (in use) $\rdelim\}{-3}{3mm}[caller frame]$ |
|||

Exit status 0 (normal)

### Summary

- At the start of every function, move SP to allocate space
- Make room for FP, LR, and any local variables
- Update FP to track the bottom of the new frame
- Maybe call functions, which overwrite LR
- Stack frame teardown: restore previous FP, LR, SP

### Discussion

- In `main`, we had SP=0x3fd0 and FP=0x3ff0
- When we called `bl add_one`, we set SP=0x3fb0 and FP=0x3fc0
- What would SP and FP have been for `scanf`?
- How about `printf`?
- Hint: these functions were calles from `main` 

## Optimization with Functions

### tldr

- In real code, you can get deep call stacks. frequently 10+ functions deep
- we have ~6 instructions of overhead for every function call
- this can be significant in small functions, especially if called many times
- there are a few strategies for reducing this cost

### Tail Call Optimization

When the last thing a function does is call another function, the compiler can "reuse" the current stack frame instead of creating a new one

Just call `b` to jump straight into the nested function, instead of `bl`

At the end of the nested function, `ret` goes back to LR from the last time we called `bl` (parent function call)

### Function Inlining

|||
Before:
```python
def plus_one(x):
	return x + 1

def main():
	total = 0
	for i in range(100):
		total = plus_one(total)
	return total
```

After:
```python
def main():
	total = 0
	for i in range(100):
		total = total + 1
	return total
```
|||

### So Much Annotation!

```arm
.arch armv8-a
.file "function-mvp.c"
.text
.align  2
.p2align 5,,15
.global add_one
.type add_one, %function
add_one:
.LFB11:
.cfi_startproc
add w0, w0, 1
ret
.cfi_endproc
.LFE11:
.size add_one, .-add_one
.section .rodata.str1.8,"aMS",@progbits,1
.align 3
.LC0:
.string "%d + 1 = %d\n"
.section .text.startup,"ax",@progbits
.align 2
.p2align 5,,15
.global main
.type main, %function
main:
.LFB12:
.cfi_startproc
stp x29, x30, [sp, -16]!
.cfi_def_cfa_offset 16
.cfi_offset 29, -16
.cfi_offset 30, -8
mov w2, 8
mov w1, 7
mov x29, sp
adrp x0, .LC0
add x0, x0, :lo12:.LC0
bl printf
mov w0, 0
ldp x29, x30, [sp], 16
.cfi_restore 30
.cfi_restore 29
.cfi_def_cfa_offset 0
ret
.cfi_endproc
.LFE12:
.size main, .-main
.ident "GCC: (Debian 14.2.0-19) 14.2.0"
.section .note.GNU-stack,"",@progbits
```

### So Much Annotation!



### Performance Instrumentation

For performance-critical applications, we can compile with 





### Example Nested Function

```arm,linenos=true,xleftmargin=1em
.section .rodata
prompt: .ascii "int plz: \0"
fmt: .ascii "%d\0"
output: .ascii "%d + 1 = %d\n\0"

.section .data
n: .word 0

.text
.global main

add_one:
// stack frame setup, no local vars
sub sp, sp, 0x20
str fp, [sp]
str lr, [sp, 0x10]
add fp, sp, 0x10
// call nested function
bl add_one_impl
// stack frame teardown
ldr lr, [sp, 0x10]
ldr fp, [sp]
add sp, sp, 0x20
// pass along nested return
ret

add_one_impl:
// stack frame setup, no local vars
sub sp, sp, 0x20
str fp, [sp]
str lr, [sp, 0x10]
add fp, sp, 0x10
// return input +1
add x0, x0, 1
// stack frame teardown
ldr lr, [sp, 0x10]
ldr fp, [sp]
add sp, sp, 0x20
ret

main: 
// stack frame setup, no local vars
sub sp, sp, 0x20
str fp, [sp]
str lr, [sp, 0x10]
add fp, sp, 0x10
// prompt for input
ldr x0, =prompt
bl printf
// store input to global variable
ldr x0, =fmt
ldr x1, =n
bl scanf
// load input and pass to add_one
ldr x0, =n
ldr x0, [x0]
bl add_one
// report input and output
mov x2, x0
ldr x0, =output
ldr x1, =n
ldr x1, [x1]
bl printf
// stack frame teardown
ldr lr, [sp, 0x10]
ldr fp, [sp]
add sp, sp, 0x20
// return 0
mov x0, 0
b exit
```

### Board Time

Let's work through it together

### Return-Oriented Programming Attacks

- LR is stored on the stack
- Local variables are stored on the stack too
- What happens if user input overflows the local variable and overwrites LR?




## Advanced Topics

### TODO

should this stuff be tucked into the above content, or together at the end? probably tucked in

- function inlining. too much can cause binary bloat, cache misses
- tail-call optimization
- ROP attacks
- performance instrumentation
- stack overflow

