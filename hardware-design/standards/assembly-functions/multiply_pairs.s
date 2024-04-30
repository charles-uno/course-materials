    .section .rodata
output: .ascii "%d * %d = %d\12\0"

    .text
    .global mul_two
mul_two:
    @ set up stack frame, no local variables
    push {fp, lr}
    add fp, sp, #4
    @ return x*y
    mul r0, r0, r1
    @ stack frame teardown
    pop {fp, lr}
    bx lr

    .text
    .global main
main: 
    @ stack frame setup, six local variables
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #24
    @ fp-8 is a, initialize to 4
    mov r0, #4
    str r0, [fp, #-8]
    @ fp-12 is b, initialize to 9
    mov r0, #9
    str r0, [fp, #-12]
    @ fp-16 is c, initialize to 7
    mov r0, #7
    str r0, [fp, #-16]
    @ fp-20 is a*b
    ldr r0, [fp, #-8]
    ldr r1, [fp, #-12]
    bl mul_two
    str r0, [fp, #-20]
    @ fp-24 is b*c
    ldr r0, [fp, #-12]
    ldr r1, [fp, #-16]
    bl mul_two
    str r0, [fp, #-24]
    @ fp-28 is c*a
    ldr r0, [fp, #-16]
    ldr r1, [fp, #-8]
    bl mul_two
    str r0, [fp, #-28]

    @ Load and print a, b, a*b
    ldr r0, output_ptr
    ldr r1, [fp, #-8]
    ldr r2, [fp, #-12]
    ldr r3, [fp, #-20]
    bl printf
    @ Load and print b, c, b*c
    ldr r0, output_ptr
    ldr r1, [fp, #-12]
    ldr r2, [fp, #-16]
    ldr r3, [fp, #-24]
    bl printf
    @ Load and print c, a, c*a
    ldr r0, output_ptr
    ldr r1, [fp, #-16]
    ldr r2, [fp, #-8]
    ldr r3, [fp, #-28]
    bl printf
    @ stack frame teardown, return 0
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

output_ptr: .word output

