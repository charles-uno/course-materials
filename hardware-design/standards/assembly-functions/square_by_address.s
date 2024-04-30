    .section .rodata
prompt: .ascii "Enter a number: \0"
input_format: .ascii "%d\0"
reply: .ascii "The square of that number is: %d\n\0"

    .text
    .global square_by_address
square_by_address:
    @ stack frame setup
    push {fp, lr}
    add fp, sp, #4
    @ load value from the input address
    ldr r0, [r0]
    @ compute the square and store the result
    mul r0, r0, r0
    str r0, [r1]
    mov r0, r1
    @ restore previous stack frame
    pop {fp, lr}
    bx lr

    .text
    .global main
main: 
    @ stack frame setup, two local variables
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #8
    @ get input from the terminal
    ldr r0, prompt_ptr
    bl printf
    ldr r0, input_format_ptr
    sub r1, fp, #8
    bl  scanf
    @ send variable addresses to function
    sub r0, fp, #8
    sub r1, fp, #12
    bl square_by_address
    @ load and print function result
    ldr r1, [r0]
    ldr r0, reply_ptr
    bl printf
    @ return 0, restore previous stack frame
    mov r0, #0
    sub sp, fp, #4
    pop {fp, lr}
    bx lr

prompt_ptr: .word prompt
input_format_ptr: .word input_format
reply_ptr: .word reply

