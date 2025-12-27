@ ascii globals go here
    .section .rodata
running_tally: .ascii "The first %d odd numbers add to: %d\n\0"

    .text
    .global main
main: 
    @ stack frame setup, no local variables
    push {fp, lr}
    @ init loop counter and running sum
    mov r4, #0
    mov r5, #0
begin_loop:
    @ increment loop counter
    add r4, r4, #1
    @ the nth odd number is 2n-1. add that to the running sum
    add r5, r5, r4
    add r5, r5, r4
    sub r5, r5, #1
    @ print the running sum
    ldr r0, running_tally_ptr
    mov r1, r4
    mov r2, r5
    bl printf
    @ check break condition
    cmp r4, #10
    blt begin_loop
    @ return 0, stack frame teardown
    mov r0, #0
    pop {fp, lr}
    bx lr

@ pointers to ascii globals
running_tally_ptr: .word running_tally
