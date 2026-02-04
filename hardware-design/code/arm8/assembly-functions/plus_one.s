.section .rodata
    prompt: .ascii "please provide an integer: \0"
    input_fmt: .ascii "%d\0"
    output: .ascii "%d + 1 = %d\n\0"

.section .data
    n: .word 0

.text
add_one:
    sub sp, sp, 0x20
    str fp, [sp]
    str lr, [sp, 0x10]
    add fp, sp, 0x10
    add x0, x0, 1
    ldr lr, [sp, 0x10]
    ldr fp, [sp]
    add sp, sp, 0x20
    ret

.global main
main: 
    sub sp, sp, 0x20
    str fp, [sp]
    str lr, [sp, 0x10]
    add fp, sp, 0x10
    ldr x0, =prompt
    bl printf
    ldr x0, =input_fmt
    ldr x1, =n
    bl scanf
    ldr x0, =n
    ldr x0, [x0]
    bl add_one
    mov x2, x0
    ldr x0, =output
    ldr x1, =n
    ldr x1, [x1]
    bl printf
    ldr lr, [sp, 0x10]
    ldr fp, [sp]
    add sp, sp, 0x20
    b exit
    