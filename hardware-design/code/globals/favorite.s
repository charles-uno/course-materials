.section .rodata
output_str: .ascii "My favorite number is %d\n\0"
favorite_num: .word 123

.section .text
.global main
main:
ldr r0, =output_str
ldr r1, =favorite_num
ldr r1, [r1]
bl printf
mov r0, #0
b exit

