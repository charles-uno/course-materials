.section .rodata
    output_str: .ascii "%d + %d = %d\n\0"

.section .text
.global main
main:
    ldr x0, =output_str
    mov x1, 2
    mov x2, 3
    add x3, x1, x2
    bl printf
    mov x0, 0
    b exit
