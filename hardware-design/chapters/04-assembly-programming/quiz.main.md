template: quiz.tex
title: Assembly Programming
date: March 14, 2026
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
