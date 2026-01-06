// global constants
.section .rodata
prompt: .ascii "how many koalas do you have? \0"
input_fmt: .ascii "%d\0"
report: .ascii "that's %d thumbs!\n\0"

// global variables
.section .data
num_koalas: .word 0

// execution starts here
.section .text
.global main
main:
ldr x0, =prompt
bl printf

ldr x0, =input_fmt
ldr x1, =num_koalas
bl scanf

ldr x1, =num_koalas
ldr x1, [x1]
// each koala has 6 thumbs
mov r2, 6
mul r3, r1, r2

ldr x0, =report
mov x1, x3
bl printf

mov x0, 0
b exit
