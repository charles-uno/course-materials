.section .rodata
    prompt: .ascii "please provide an integer: \0"
    input_fmt: .ascii "%d\0"
    output: .ascii "%d + 1 = %d\n\0"

.section .data
    n: .word 0


// https://developer.arm.com/documentation/ddi0602/2025-12/Base-Instructions/STR--immediate---Store-register--immediate--?lang=en
// https://stackoverflow.com/questions/64638627/explain-arm64-instruction-stp

.text
add_one:
    sub sp, sp, 16
    str fp, [sp, -8]
    str lr, [sp]
    add fp, sp, 16

    bl add_one_impl

    ldr lr, [sp]
    ldr fp, [sp, -8]
    add sp, sp, 16
    ret


add_one_impl:
    sub sp, sp, 16
    str fp, [sp, -8]
    str lr, [sp]
    add fp, sp, 16

    add x0, x0, 1

    ldr lr, [sp]
    ldr fp, [sp, -8]
    add sp, sp, 16
    ret


.global main
main: 
    sub sp, sp, 16
    str fp, [sp, -8]
    str lr, [sp]
    add fp, sp, 16

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

    ldr lr, [sp]
    ldr fp, [sp, -8]
    add sp, sp, 16

    ret
    