@ ascii globals go here
    .section .rodata
result: .ascii "The sum from 0 to 100 is: %d\n\0"

    .text
    .global main
main: 
    @ stack frame setup, no local variables
    push {fp, lr}
    @ init loop counter and sum
    mov r4, #0
    mov r5, #0
begin_loop:
    @ increment loop counter
    add r4, r4, #1
    @ increase running sum
    add r5, r5, r4
    @ check break condition
    cmp r4, #100
    blt begin_loop
    @ report result
    ldr r0, result_ptr
    mov r1, r5
    bl printf
    @ return 0, stack frame teardown
    mov r0, #0
    pop {fp, lr}
    bx lr

@ pointers to ascii globals
result_ptr: .word result
