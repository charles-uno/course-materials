.section .rodata
output_str: .ascii "who has %d thumbs and wrote this code? %s\n\0"
name: .ascii "charles\0"
n_thumbs: .word 2

.section .text
.global main
main:
ldr r0, =output_str
ldr r1, =n_thumbs
ldr r1, [r1]
ldr r2, =name
bl printf
mov r0, #0
b exit

