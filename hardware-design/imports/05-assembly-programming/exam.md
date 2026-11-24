
---


Write an assembly program called `koalas.s` that does the following:
- Ask the user how many koalas they have
- Store their input in a global variable named `num_koalas`.
- Load the value from memory
- Compute the number of thumbs. Note: each koala has 6 thumbs
- Report the result

For example, if the user has 4 koalas, the report should say:
```
That's 24 thumbs!
```

The next page outline the structure of the program with comments. You may write your assembly code between the comments, or on a separate sheet of paper. If you write on a separate sheet of paper, you do not need to rewrite the comments.

$$$
\standardsfooter
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



# Assembly Functions

1. What is one use case where we should store data on the stack? Why?
2. What is one use case where we should store data on the heap? Why?
1. In class, we discussed a few strategies that compilers use to improve the efficiency of function calls (tail call optimization, inlining, etc). Choose one. Explain how it works.
2. There is an Assembly program `spider-legs.s` on the next page. Explain in words what this code does. Make a guess about what the output looks like. Briefly explain any assumptions you have made. 
3. Draw a memory diagram for `spider-legs.s`. Start at the beginning of `main` and stop after line `0x08`. If you need the memory address of an instruction, use the line number. Make sure to include the special registers `sp`, `fp`, `pc`, and `lr`. Briefly explain any assumptions. 

TODO: add starting values for sp and fp. maybe add starting values for lr and pc also actually


$$$
\standardsfooter
\newpage
$$$

```arm,linenos=true
// ... global constants etc omitted for brevity
get_n_legs:
    sub sp, sp, 0x20
    str fp, [sp]
    str lr, [sp, 0x10]
    add fp, sp, 0x10
    mov x4, 8
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
    bl get_n_legs
    mov x1, x0
    ldr x0, =report
    bl printf
    ldr lr, [sp, 0x10]
    ldr fp, [sp]
    mov x0, 0
    b exit
```



