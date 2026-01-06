.section .rodata
    prompt: .ascii "please provide an integer: \0"
    input_fmt: .ascii "%d\0"
    output: .ascii "%d + 1 = %d\n\0"

.section .data
    n: .word 0

// https://stackoverflow.com/questions/78404268/how-to-use-stack-in-arm64-assembly

.text
add_one:
    str lr, [sp, -16]!
    str fp, [sp, -16]!
    add fp, sp, 16
    add x0, x0, 1
    ldr fp, [sp], 16
    ldr lr, [sp], 16
    ret

.global main
main: 
    str lr, [sp, -16]!
    str fp, [sp, -16]!
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
    ldr fp, [sp], 16
    ldr lr, [sp], 16
    ret
    