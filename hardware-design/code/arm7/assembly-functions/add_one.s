    .section .rodata
output: .ascii "%d + 1 = %d\12\0"

    .text
add_one:
    @ set up stack frame, no local variables
    push {fp, lr}
    add fp, sp, #4
    @ input is x, return x+1
    add r0, r0, #1
    @ stack frame teardown
    pop {fp, pc}

    .global main
main: 
    @ stack frame setup, four local variables
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #16
    @ fp-8 is n1, initialize to 4
    mov r0, #4
    str r0, [fp, #-8]
    @ fp-12 is n2, initialize to 7
    mov r0, #7
    str r0, [fp, #-12]
    @ fp-16 is n1_plus
    ldr r0, [fp, #-8]
    bl add_one
    str r0, [fp, #-16]
    @ fp-20 is n2_plus
    ldr r0, [fp, #-12]
    bl add_one
    str r0, [fp, #-20]
    @ Load and print n1, n1_plus
    ldr r0, output_ptr
    ldr r1, [fp, #-8]
    ldr r2, [fp, #-16]
    bl printf
    @ Load and print n2, n2_plus
    ldr r0, output_ptr
    ldr r1, [fp, #-12]
    ldr r2, [fp, #-20]
    bl printf
    @ stack frame teardown, return 0
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

output_ptr: .word output

