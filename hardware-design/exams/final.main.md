title: Final Exam
date: May 15, 2026
template: ../build/final-template.tex
new_page_for_section: true
---

%BEGIN_DR

# Data Representation

1. Convert the unsigned binary number `0b00100001` to decimal.
1. Convert the decimal integer `-23` to 8-bit two's complement binary.
1. Compute the following subtraction of two's complement binary integers: `0b00111000 - 0b00010111`. Do the math in binary. Convert everything to decimal to check your result.
1. Convert the hexadecimal number `0x05FE` directly to unsigned binary.
1. Choose one: website, audio, or image. Explain (using words) how we take that information and turn it into ones and zeroes.

$$$
\standardsfooterNoRevision
$$$

% ![ascii table](wikimedia-ascii-table)

%END_DR

%BEGIN_LR
# Logic Representation

1. Let `f(A,B,C)=(A NAND B) XOR (NOT C)`. Write out the truth table for `f`
1. Draw a logic circuit for `f`
1. Let `g(A, B, C)` be true if at least two of the inputs (`A`, `B`, `C`) are false. Write `g` in terms of the basic boolean functions `AND`, `OR`, `NOT`, `NAND`, `NOR`, and/or `XOR`. 
1. Draw a logic circuit representing the sum of two one-bit unsigned binary numbers: `0bA + 0bB = 0bCD`. There should be two input bits (`A` and `B`) and two output bits (`C` and `D`). 

$$$
\standardsfooterNoRevision
$$$
%END_LR

%BEGIN_IH
# Instructions on Hardware

1. What is the role of the CPU in a computer?
1. What is the role of main memory in a computer?
1. What are temporal locality and spatial locality? How are they used by the cache to run programs more efficiently?
1. Explain what happens in the ALU for each step of the instruction cycle: fetch, decode, execute, write
1. Explain how data moves between registers and memory during each step of the instruction cycle. You may assume the instruction is `ADD`
1. Choose one type of instruction-level parallelism (eg pipelining, VLIW, SIMD, superscalar execution). Explain how it works. What's the best-case performance improvement? Does it require specialized hardware? Does code need to be written in a certain way to take advantage of it? 

$$$
\standardsfooterNoRevision
$$$
%END_IH

%BEGIN_AG
# Assembly Globals

TODO: make sure the comments in the code line up with the instructions! specifically: storing n_thumbs

Write an assembly program called `koalas.s` that does the following:
- Ask the user how many koalas they have
- Store their input in a global variable named `num_koalas`
- Load the value from memory
- Compute the number of thumbs. Note: each koala has 6 thumbs
- Store the number of thumbs in a global variable named `num_thumbs`
- Report the result

For example:
```
How many koalas do you have? 4
That's 24 thumbs!
```

The next page outline the structure of the program with comments. You may write your assembly code between the comments, or on a separate sheet of paper. If you write on a separate sheet of paper, you do not need to rewrite the comments.

$$$
\standardsfooterNoRevision
\newpage
$$$


```arm
// global constants: prompt, input format, report
.section .rodata



.align 2
// global variable: num_koalas
.section .data



.section .text
.global main
main:
// prompt the user for input



// store their response in num_koalas



// load num_koalas from memory



// compute the number of thumbs



// report the result



// return 0 (normal exit status)
mov x0, 0
b exit
```
%END_AG


%BEGIN_OS
# OS Concepts

1. When you turn on a computer, how does it know which instruction to run first? What do the first instructions do?
1. Explain context switching. What is it? When and why does it happen?
1. Your Raspberry Pi has four cores. What does this mean? Give an example of a situation where a computer with multiple cores is preferrable to a computer with a single core.
1. Would you rather have a computer with 100 CPU cores and a 1GHz clock, or 1 CPU core and a 100GHz clock? Why? Which do you suppose would be easier to manufacture? Why?
1. Briefly explain concurrency and parallelism. Give one way they are the same. Give one way they are different.
1. What are processes and threads? Give one way they are the same. Give one way they are different.


$$$
\standardsfooterNoRevision
$$$
%END_OS

%BEGIN_AF
# Assembly Functions

1. What are the stack and the heap used for? Why do we need both?
1. In class, we discussed a few strategies that compilers use to improve the efficiency of function calls (tail call optimization, inlining, etc). Choose one. Explain how it works.
2. There is an Assembly program `get-n-seconds.s` on the next page. Explain in words what this code does. Make a guess about what the output looks like. Briefly explain any assumptions you have made. 
3. Draw a memory diagram for `get-n-seconds.s`. Start with `sp=0x4000`, `fp=0x5000`, `lr=0x6000`, and `pc=0x0e`. Proceed step-by-step until you have executed line `0x08` *twice*. Draw the memory diagram as it appears at that moment. If you need the memory address of an instruction, use the line number. Briefly explain any assumptions. 
   
   Note: As you go, you may find it helpful to write down intermediate values for registers and memory. Grading is based only on the final values, not their history.

$$$
\standardsfooterNoRevision
\newpage
$$$

```arm,linenos=true
// ... global constants etc omitted for brevity
times_sixty:
    sub sp, sp, 0x20
    str fp, [sp]
    str lr, [sp, 0x10]
    add fp, sp, 0x10
    mov x4, 60
    mul x3, x0, x4
    mov x0, x3
    ldr lr, [sp, 0x10]
    ldr fp, [sp]
    add sp, sp, 0x20
    ret
main:
    sub sp, sp, 0x30
    str fp, [sp]
    str lr, [sp, 0x10]
    add fp, sp, 0x20
    ldr x0, =prompt
    bl printf
    ldr x0, =fmt
    mov x1, fp
    bl scanf
    ldr x0, [fp]
    bl times_sixty
    bl times_sixty
    mov x1, x0
    ldr x0, =report
    bl printf
    ldr lr, [sp, 0x10]
    ldr fp, [sp]
    mov x0, 0
    b exit
```

$$$
\standardsfooterNoRevision
$$$
%END_AF

%BEGIN_CF
# Control Flow

Write code in Aarch64 to do the following:
  - Initialize sum to 0
  - Loop from 0 to 100
  - If a number is odd, skip it
  - If a number is even, add it to the sum

% Do not use a formula to compute the sum. Write the loop.

Don't worry about code sections, global constants, stack frames, input, output, etc. 

$$$
\standardsfooterNoRevision
$$$
%END_CF

%BEGIN_NW
# Networking

1. Give a one-sentence summary of each layer in the TCP/IP model: Application, Transport, Internet, Link.
2. Briefly explain DNS.
3. Briefly explain the TCP and UDP transport protocols. Give one example of a case where TCP is more appropriate. Give one example of a case where UDP is more appropriate.
4. Briefly explain public and private IP addresses. Why is the distinction necessary? Does one request ever use both public and private IP addresses?
5. What is a MAC address? Why is it important?
6. We discussed several network-related attack vectors in class (DDoS, SYN flooding, BGP hijacking, ARP spoofing, etc). Pick one of them. Describe how it works. Explain one precaution that can be taken against it. 

$$$
\standardsfooterNoRevision
$$$
%END_NW







