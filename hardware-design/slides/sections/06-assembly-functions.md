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

### The Stack

- The stack is a region of memory that the OS has reserved for this process
- We can assign local variables there
- We have the special registers SP (stack pointer) and FP (frame pointer) to keep track

### Memory Diagram

We can draw a **memory diagram** to keep track of registers and memory for our process:
$$$
\bigskip
\begin{columns}
\begin{column}{0.4\textwidth}
$$$

| Register | Value |
| --- | --- |
| x0 | ... |
| x1 | ... |
| x2 | ... |
| x3 | ... |
| sp | 0x4010 |
| fp | 0x5000 |
| pc | ... |
| lr | ... |

$$$
\end{column}
\begin{column}{0.6\textwidth}
$$$

| Address | Value |
| --- | --- |
| 0x3f90 | ... |
| 0x3fa0 | ... |
| 0x3fb0 | ... |
| 0x3fc0 | ... |
| 0x3fd0 | ... |
| 0x3fe0 | ... |
| 0x3ff0 | ... |
| 0x4000 | ... |

$$$
\end{column}
\end{columns}
$$$

### Stack Numbering

- We usually start the stack at 0x4000 or 0x5000. This is arbitrary
- The stack builds *up*
- Higher on the stack is *decreasing* memory address
- Increment by 0x10 bytes (more on this later)

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
- This is why it's called a stack. We're stacking

### Example Local Variable in Assembly

$$$
\begin{multicols}{2}{\small
$$$
```arm
.section .rodata
prompt: .ascii "int plz: \0"
input_fmt: .ascii "%d\0"
output: .ascii "%d+1=%d\n\0"
.align 2

.global main
main: 
sub sp, sp, 0x10
ldr x0, =prompt
bl printf
ldr x0, =input_fmt
mov x1, sp
bl scanf
ldr x0, =output
ldr x1, [sp]
add x2, x1, 1
bl printf
add sp, sp, 0x10
b exit
```
$$$
}\end{multicols}
$$$

### Exercise

Let's work through this on the board

## Stack Frames

### Utterly Deranged

$$$
\begin{center}
\includegraphics[width=0.8\columnwidth]{images/assembly-functions/sure-grandma}
\end{center}
$$$

### Initial State

At the start of the program, our memory diagram looks like this:

$$$
\bigskip
\begin{columns}
\begin{column}{0.4\textwidth}
$$$

| Register | Value |
| --- | --- |
| x0 | ... |
| x1 | ... |
| x2 | ... |
| x3 | ... |
| sp | 0x4010 |
| fp | 0x5000 |
| pc | ... |
| lr | ... |

$$$
\end{column}
\begin{column}{0.6\textwidth}
$$$

| Address | Value |
| --- | --- |
| 0x3fc0 | ... |
| 0x3fd0 | ... |
| 0x3fe0 | ... |
| 0x3ff0 | ... |
| 0x4000 | ... |
| 0x4010 | ... $\rdelim\}{3}{3mm}[parent stack frame]$ |
| ... | ... |
| 0x5000 | ... |

$$$
\end{column}
\end{columns}
$$$

The existing stack frame goes from `0x5000` (FP) to `0x4010` (SP)

### Stacking Frames

After calling into `main`, we update SP and FP to add a new frame to the stack:

$$$
\bigskip
\begin{columns}
\begin{column}{0.4\textwidth}
$$$

| Register | Value |
| --- | --- |
| x0 | ... |
| x1 | ... |
| x2 | ... |
| x3 | ... |
| sp | 0x3fe0 |
| fp | 0x4000 |
| pc | ... |
| lr | ... |

$$$
\end{column}
\begin{column}{0.6\textwidth}
$$$

| Address | Value |
| --- | --- |
| 0x3fc0 | ... |
| 0x3fd0 | ... |
| 0x3fe0 | ... $\rdelim\}{3}{3mm}[main stack frame]$ |
| 0x3ff0 | ... |
| 0x4000 | ... |
| 0x4010 | ... $\rdelim\}{3}{3mm}[parent stack frame]$ |
| ... | ... |
| 0x5000 | ... |

$$$
\end{column}
\end{columns}
$$$

### Tracking Stacked Frames

Wait a sec:

- When we move into a new function, we update SP and FP to define our new stack frame
- But registers do not "remember" past values
- When the function is done and we want to return, how do we go back to the previous frame?

### Stack Frame Overhead

- At the start of a function, when creating the new stack frame, also store the previous FP
- At the end of the function, when returning to the previous stack frame, restore FP
- SP does not need to be stored explicitly. Why not?

### Example Time

So what does this look like in Assembly?

### Example Stack Frame

$$$
\begin{multicols}{2}{\small
$$$
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
$$$
}\end{multicols}
$$$

### What's LR?

LR is the **link register**. It keeps track of the return address from a function

Recall we use `bl printf` for output, and `b exit` for exiting the program





### Back to the Board

Let's work through this one together on the board

## Function Calls




% also need to store LR


### Example Function

$$$
\begin{multicols}{2}{\small
$$$
```arm
.section .rodata
prompt: .ascii "int plz: \0"
input_fmt: .ascii "%d\0"
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
ldr x0, =input_fmt
mov x1, sp
bl scanf
ldr x0, [sp]
bl add_one
mov x2, x0
ldr x0, =output
ldr x1, [sp]
bl printf
ldr lr, [sp, 0x10]
ldr fp, [sp, 0x20]
add sp, sp, 0x30
b exit
```
$$$
}\end{multicols}
$$$








% we have talked about global constants and global variables
% those ones have to be declared at implementation time
% what if you want to declare variables on the fly?

% the stack is a region of memory that the OS has set aside for your program
% we use special register sp to keep track of our location in that memory

% sp always points to the top of the stack
% if we need more memory, we can move sp up
% when we're done with that memory, we can move sp back down

% SIMD
% an ascii char is 1 byte
% we store numbers as words (4 bytes)
% when updating the stack pointer sp, we work in increments of 0x10 bytes (16 bytes)
% in practice, we are just wasting a bunch of memory in order to worry about less stuff


% FP is not strictly necessary
% some compilers even let you skip it
% FP is useful for debugging. code is easier to read. integration with debugging tools
% https://stackoverflow.com/questions/46797915/what-are-the-advantages-of-a-frame-pointer


## Calling a Function

### Branch and Link

New command: BL

Branch and Link

Branch = modify PC. Recall: PC tells us what to do next. Usually we just do the next line. In this case, we will jump to some other part of the program. This is how we call a function.

Link = set LR to the PC of the next line. Once we're done with the function, this is how we return to the parent context.



### SIMD

- SIMD - single instruction, multiple data
- 64 bit architecture (8 bytes)
- there are cases where it works in chunks of 16 bytes
- I don't have time to worry about that, and neither do you. For the purposes of this class, everything is 16 bytes.
- This is wasteful! We are using double the memory we need, sometimes more
- That's ok. We are not trying to become assembly developers. We are getting exposure to important concepts

