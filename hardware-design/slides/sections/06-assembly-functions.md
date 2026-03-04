beamer: true
---

# Assembly Functions

% SIMD!
% similar to having .align all over the place


## The Stack

% we have talked about global constants and global variables
% those ones have to be declared at implementation time
% what if you want to declare variables on the fly?

% the stack is a region of memory that the OS has set aside for your program
% we use special register sp to keep track of our location in that memory

% sp always points to the top of the stack
% if we need more memory, we can move sp up
% when we're done with that memory, we can move sp back down

% "down" is higher numbered addresses
% for exercises we put the bottom of the stack at 0x5000 by convention
% above 0x5000 is 0x4ff0, then 0x4fe0, etc

% SIMD
% an ascii char is 1 byte
% we store numbers as words (4 bytes)
% when updating the stack pointer sp, we work in increments of 0x10 bytes (16 bytes)
% in practice, we are just wasting a bunch of memory in order to worry about less stuff




### local variable mvp
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


### stack frame mvp
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

### function mvp
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

### Working Memory
$$$
	\begin{columns}
		\begin{column}{0.4\textwidth}
			\begin{alltt}
				\begin{tabular}{ r | l }
					x0 & ... \\
					x1 & ... \\
					x2 & ... \\
					x3 & ... \\
					sp & ... \\
					fp & ... \\
					pc & ... \\
					lr & ... \\
				\end{tabular}
			\end{alltt}
		\end{column}
		\begin{column}{0.6\textwidth}
			\begin{alltt}
				\begin{tabular}{ r | l }
					0x4f90 & apple \\
					0x4fa0 & banana \\
					0x4fb0 & carrot \rdelim\}{2}{3mm}[two rows] \\
					0x4fc0 & dolphin \\
					0x4fd0 & echidna \rdelim\}{4}{3mm}[four rows] \\
					0x4fe0 & flower \\
					0x4ff0 & grape \\
					0x5000 & hobbit \\
				\end{tabular}
			\end{alltt}
		\end{column}
	\end{columns}
$$$

### Push and Pop

When a program starts running, the OS loads the instructions into memory.

It also allocates memory for the program to use during execution

There is a special register called the stack pointer which provides the location of that memory

### Working Memory
$$$
	\begin{columns}
		\begin{column}{0.5\textwidth}

			we do not know what piece of memory the OS will provide

			arbitrarily say it starts at 0x5000

			stack pointer points to the "bottom" of our available memory. we work our way "up" by subtracting from the stack pointer

			The rules are the same when we call a function. It looks at SP to know the "bottom" of its available memory, then works up from there

		\end{column}
		\begin{column}{0.5\textwidth}
			\begin{alltt}
				\begin{tabular}{ r | l }
					0x4fe0 & \vdots           \\
					0x4ff0 & available        \\
					0x5000 & available        \\
					0x5010 & in use by parent \\
					0x5020 & in use by parent \\
					0x5030 & \vdots           \\
				\end{tabular}
			\end{alltt}
		\end{column}
	\end{columns}
$$$

## Calling a Function

### Branch and Link

New command: BL

Branch and Link

Branch = modify PC. Recall: PC tells us what to do next. Usually we just do the next line. In this case, we will jump to some other part of the program. This is how we call a function.

Link = set LR to the PC of the next line. Once we're done with the function, this is how we return to the parent context.

## Stack Frames

### Frame Pointer

- Not strictly necessary
- Code is easier to read
- Integration with debugging tools
- Stack pointer can move during the function
- Skipping the frame pointer can be skipped by some compilers

% https://stackoverflow.com/questions/46797915/what-are-the-advantages-of-a-frame-pointer

### SIMD

- SIMD - single instruction, multiple data
- 64 bit architecture (8 bytes)
- there are cases where it works in chunks of 16 bytes
- I don't have time to worry about that, and neither do you. For the purposes of this class, everything is 16 bytes.
- This is wasteful! We are using double the memory we need, sometimes more
- That's ok. We are not trying to become assembly developers. We are getting exposure to important concepts

## Local Variables

### Local Variables

- LDR from an address
- STR to an address
- Offsets from SP and FP

### Hello World in Assembly

$$$
{\Huge TODO: don't worry about PC yet? they haven't done the von neumann arch section yet}
$$$

