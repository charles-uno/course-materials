    .section .rodata
plus_one_output: .ascii "%d + 1 = %d\n\0"

    .text
plus_one:
    @ stack frame setup, no local variables
    push {fp, lr}
    add fp, sp, #4
    @ input is x. return x+1
    add r0, r0, #1
    @ restore previous stack frame
    pop {fp, pc}

    .global main
main: 
    @ stack frame setup, three local variables
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #12
    @ set initial value, store it
    mov r0, #5
    str r0, [fp, #-8]
    @ call add_one, store result
    bl plus_one
    str r0, [fp, #-12]
    @ load both values and print them
    ldr r0, plus_one_output_ptr
    ldr r1, [fp, #-8]
    ldr r2, [fp, #-12]
    bl printf
    @ return 0, restore previous stack frame
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

plus_one_output_ptr: .word plus_one_output

