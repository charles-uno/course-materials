@ global constants
.section .rodata
greeting: .ascii "Hello World!\n\0"

@ execution starts here
.section .text
.global main

main:

ldr r0, =greeting
bl printf

mov r0, #0
bl exit

