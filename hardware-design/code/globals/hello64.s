; https://www.deusinmachina.net/p/the-basics-of-arm64-assembly

.global main

.section .text

main:
    ldr x0, =message
    bl printf
    mov x0, #0
    b exit

.section .rodata
    message: .ascii "Hello World\n"

