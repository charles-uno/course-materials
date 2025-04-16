    .section .rodata
prompt: .ascii "Enter a number: \0"
input_format: .ascii "%d\0"
reply: .ascii "The square of that number is: %d\n\0"

    .text
square_by_address:
    @ stack frame setup, no local variables
    push {fp, lr}
    add fp, sp, #4
    @ load the value of x from its address
    @ two input variables
    @ the first is the address of the input value
    @ the second is the address to hold the result
    ldr r0, [r0]
    @ compute the square
    mul r0, r0, r0
    @ store the result in the given address
    str r0, [r1]
    @ return that address
    mov r0, r1
    @ restore previous stack frame
    pop {fp, lr}
    bx lr

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
    @ address of the value
    @ empty local variable to hold the result
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

