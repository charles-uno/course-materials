    .section .rodata
prompt_1:
    .ascii "Enter a number: \0"
prompt_2:
    .ascii "Enter another number: \0"
input_format:
    .ascii "%d\0"
reply:
    .ascii "The sum of those numbers is: %d\n\0"

    .text
    .global add_two_numbers
add_two_numbers_by_address:
    @ stack frame setup
    push {fp, lr}
    add fp, sp, #4
    @ load values from the input addresses
    ldr r4, [r0]
    ldr r5, [r1]
    @ compute the sum and store the result
    add r6, r4, r5
    str r6, [r2]
    mov r0, r2
    @ restore previous stack frame
    pop {fp, lr}
    bx lr

    .text
    .global main
main: 
    @ stack frame setup
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #12
    @ get input values from the terminal
    ldr r0, prompt_1_ptr
    bl printf
    ldr r0, input_format_ptr
    sub r1, fp, #8
    bl  scanf
    ldr r0, prompt_2_ptr
    bl printf
    ldr r0, input_format_ptr
    sub r1, fp, #12
    bl  scanf
    @ send variable addresses to function
    sub r0, fp, #8
    sub r1, fp, #12
    sub r2, fp, #16
    bl add_two_numbers_by_address
    @ load and print function result
    ldr r1, [r0]
    ldr r0, reply_ptr
    bl printf
    @ return 0, restore previous stack frame
    mov r0, #0
    sub sp, fp, #4
    pop {fp, lr}
    bx lr

prompt_1_ptr:
    .word prompt_1
prompt_2_ptr:
    .word prompt_2
input_format_ptr:
    .word input_format
reply_ptr:
    .word reply

