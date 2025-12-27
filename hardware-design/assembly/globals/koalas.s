@ global constants
.section .rodata
prompt: .ascii "how many koalas do you have? \0"
input_fmt: .ascii "%d\0"
report: .ascii "that's %d thumbs!\n\0"

@ global variables
.section .data
num_koalas: .word 0

@ execution starts here
.section .text
.global main
main:
ldr r0, =prompt
bl printf

ldr r0, =input_fmt
ldr r1, =num_koalas
bl scanf

ldr r1, =num_koalas
ldr r1, [r1]
@ each koala has 6 thumbs
mov r2, #6
mul r3, r1, r2

ldr r0, =report
mov r1, r3
bl printf

mov r0, #0
b exit
