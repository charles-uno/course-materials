.section .rodata
    prompt: .ascii "please provide an integer: \0"
    input_fmt: .ascii "%d\0"
    output: .ascii "%d + 1 = %d\n\0"

.text
add_one:
    sub sp, sp, 16
    str fp, [sp]
    str lr, [sp, 8]
    add fp, sp, 8
    add x0, x0, 1
    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 16
    ret

.global main
main: 
    sub sp, sp, 32
    str fp, [sp]
    str lr, [sp, 8]
    add fp, sp, 24
    ldr x0, =prompt
    bl printf
    ldr x0, =input_fmt
    mov x1, fp
    bl scanf
    ldr x0, [fp]
    bl add_one
    mov x2, x0
    ldr x0, =output
    ldr x1, [fp]
    bl printf
    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 32
    ret
    