// NOTE: does not work yet

.section .rodata
    prompt: .ascii "Enter a number: \0"
    format: .ascii "%d\0"
    reply: .ascii "Sum: %d\n\0"

.text
.global main
main:
    // stack frame setup, two local variables
    sub sp, sp, 64
    str fp, [sp]
    str lr, [sp, 8]
    add fp, sp, 48

    ldr x0, =prompt
    bl printf
    ldr x0, =format
    add x1, sp, 16
    bl  scanf

    ldr x0, =prompt
    bl printf
    ldr x0, =format
    add x1, sp, 32
    bl  scanf

    ldr x0, [sp, 16]
    ldr x1, [sp, 32]
    add x1, x0, x1
    ldr x0, =reply
    bl printf

    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 64
    ret

