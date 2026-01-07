.section .rodata
    output_str: .ascii "who has %d thumbs and wrote this code? %s\n\0"
    name: .ascii "charles\0"
    n_thumbs: .word 2

.section .text
.global main
main:
    ldr x0, =output_str
    ldr x1, =n_thumbs
    ldr x1, [x1]
    ldr x2, =name
    bl printf
    mov x0, 0
    b exit
