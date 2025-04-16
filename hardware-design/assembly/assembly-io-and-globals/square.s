@ global constants
.section .rodata
prompt: .ascii "enter a number: \0"
input_string: .ascii "%d\0"
print_report: .ascii "the square of %d is %d \n\0"

@ global variables
.section .data
num: .word 0

@ execution starts here
.section .text
.global main

main:

@ ask the user to enter a number
main: ldr r0, =prompt
bl printf

@ store the response in num
ldr r0, =input_string
ldr r1, =num
bl scanf

@ load the value of num from memory
ldr r1, =num
ldr r1, [r1]

@ multiply the value by itself
mul r2, r1, r1

@ print the result
ldr r0, =print_report
mov r1, r1
mov r2, r2
bl printf

mov r0, #0
bl exit

