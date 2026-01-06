// NOTE: does not work yet

.section .rodata
    prompt: .ascii "Enter a number: \0"
    format: .ascii "%d\0"
    reply: .ascii "Sum: %d\n\0"

.text
.global main
main:
    // stack frame setup, two local variables
    sub sp, sp, 32
    str fp, [sp, -8]
    str lr, [sp]
    add fp, sp, 24

    ldr x0, =prompt
    bl printf
    ldr x0, =format
    mov x1, fp
    bl  scanf

    ldr x0, =prompt
    bl printf
    ldr x0, =format
    sub x1, fp, 8
    bl  scanf

    ldr x0, [fp]
    ldr x1, [fp, 8]
    add x1, x0, x1
    ldr x0, =reply
    bl printf

    ldr lr, [sp]
    ldr fp, [sp, -8]
    add sp, sp, 32
    ret

