    .section .rodata
prompt: .ascii "Enter an integer: \0"
input_format: .ascii "%d\0"
plus_one_reply: .ascii "That number squared is: %d\n\0"

    .text
get_square:
    @ stack frame setup, no local variables
    push {fp, lr}
    add fp, sp, #4
    @ input is x. return x*x
    mul r0, r0, r0
    @ restore previous stack frame
    pop {fp, pc}

    .global main
main: 
    @ stack frame setup, two local variables
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #12
    @ print the prompt
    ldr r0, prompt_ptr
    bl printf
    @ read the input to memory
    ldr r0, input_format_ptr
    sub r1, fp, #8
    bl  scanf
    @ load x from memory
    ldr r0, [fp, #-8]
    @ call get_square, store the result


    @ compute y = x+1, store to a local variable
    bl plus_one
    str r0, [fp, #-12]
    @ compute z = y+1, store to a local variable
    bl plus_one
    str r0, [fp, #-16]
    @ load and report x+1 = y
    ldr r0, plus_one_reply_ptr
    ldr r1, [fp, #-8]
    ldr r2, [fp, #-12]
    bl printf
    @ load and print y+1 = z
    ldr r0, plus_one_reply_ptr
    ldr r1, [fp, #-12]
    ldr r2, [fp, #-16]
    bl printf
    @ return 0, restore previous stack frame
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

prompt_ptr: .word prompt
input_format_ptr: .word input_format
plus_one_reply_ptr: .word plus_one_reply

