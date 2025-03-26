@ Global constants
@ prompt: string asking the user to enter a number
.section .rodata
prompt:
.ascii "enter a number: \0"
.align 2

@ input string: formatting string for reading the user’s input
input_string:
.ascii "%d\0"
.align 2

@ print report: formatting string for reporting the square of the user’s number
print_report:
.ascii "the square of %d is %d \n\0"
.align 2

.section .data

@ Global variables
@ num: integer, the number entered by the user
num:
.word 0

.section .text
.global main

@ main
@ set up stack frame for main
@ one local variable, square
main:
push {fp, lr}
mov fp, sp
sub sp, sp, #8  @ Allocate space for local variable (square)

@ ask the user to enter a number
ldr r0, =prompt
bl printf

@ store the response in num
ldr r0, =input_string
ldr r1, =num
bl scanf

@ load the value of num from memory
ldr r1, =num
ldr r1, [r1]

@ multiply the value by itself, store the result in square
mul r2, r1, r1
str r2, [fp, #-8]   @ Store square in stack

@ load the values of num and square from memory
ldr r1, =num
ldr r1, [r1]         @ Load num
ldr r2, [fp, #-8]    @ Load square

@ print a sentence saying what the square of number is
ldr r0, =print_report
mov r1, r1   @ First argument (num)
mov r2, r2   @ Second argument (square)
bl printf

@ return 0
@ tear down stack frame for main
mov r0, #0
add sp, sp, #8
pop {fp, lr}
bx lr

@ Pointers
@ pointers to strings

prompt_ptr:
.word prompt

input_ptr:
.word input_string

print_ptr:
.word print_report
