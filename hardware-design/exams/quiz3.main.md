title: Test 3
date: April 24, 2026
template: ../build/quiz-template.tex
new_page_for_section: true
---

# OS Concepts

- Foo
- Bar
- Fizz
- Buzz

$$$
\standardsfooter
$$$

# Assembly Functions

1. What is one use case where we should store data on the stack? Why?
2. What is one use case where we should store data on the heap? Why?
1. In class, we discussed a few strategies that compilers use to improve the efficiency of function calls (tail call optimization, inlining, etc). Choose one. Explain how it works.
2. There is an Assembly program `koala-thumbs.s` on the next page. Explain in words what this code does. Make a guess about what the output looks like. Briefly explain any assumptions you have made. 
3. Draw a memory diagram for `koala-thumbs.s`. Start at the beginning of `main` and stop after line `0x0d`. If you need the memory address of an instruction, use the line number. Make sure to include the special registers `sp`, `fp`, `pc`, and `lr`. Briefly explain any assumptions. 

$$$
\standardsfooter
\newpage
$$$

```arm,linenos=true
// ... global constants etc omitted for brevity
get_n_thumbs:
    sub sp, sp, 0x20
    str fp, [sp]
    str lr, [sp, 0x10]
    add fp, sp, 0x10
    mov x4, 6
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
    bl get_n_thumbs
    mov x1, x0
    ldr x0, =report
    bl printf
    ldr lr, [sp, 0x10]
    ldr fp, [sp]
    mov x0, 0
    b exit
```


