// arm7 had push and pop. arm64 does not. more info about the switch
// https://stackoverflow.com/questions/64638627/explain-arm64-instruction-stp
// https://developer.arm.com/documentation/ddi0602/2025-12/Base-Instructions/STR--immediate---Store-register--immediate--?lang=en

.section .rodata
    prompt: .ascii "please provide an integer: \0"
    input_fmt: .ascii "%d\0"
    output: .ascii "%d + 1 = %d\n\0"

.section .data
    n: .word 0

.text
.global main

add_one:
    // stack frame setup, no local variables
    sub sp, sp, 16
    str fp, [sp, -8]
    str lr, [sp]
    add fp, sp, 16
    // call nested function
    bl add_one_impl
    // stack frame teardown
    ldr lr, [sp]
    ldr fp, [sp, -8]
    add sp, sp, 16
    // pass along nested return
    ret

add_one_impl:
    // stack frame setup, no local variables
    sub sp, sp, 16
    str fp, [sp, -8]
    str lr, [sp]
    add fp, sp, 16
    // return input +1
    add x0, x0, 1
    // stack frame teardown
    ldr lr, [sp]
    ldr fp, [sp, -8]
    add sp, sp, 16
    ret

main: 
    // stack frame setup, no local variables
    sub sp, sp, 16
    str fp, [sp, -8]
    str lr, [sp]
    add fp, sp, 16
    // prompt for input
    ldr x0, =prompt
    bl printf
    // store input to global variable
    ldr x0, =input_fmt
    ldr x1, =n
    bl scanf
    // load input from memory and pass to add_one
    ldr x0, =n
    ldr x0, [x0]
    bl add_one
    // report input and output
    mov x2, x0
    ldr x0, =output
    ldr x1, =n
    ldr x1, [x1]
    bl printf
    // stack frame teardown
    ldr lr, [sp]
    ldr fp, [sp, -8]
    add sp, sp, 16
    // return 0
    mov x0, 0
    ret 
    