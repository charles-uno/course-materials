    .section .rodata
intro: .ascii "I'm thinking of a number 0 to 100\n\0"
prompt: .ascii "Guess: \0"
input_format: .ascii "%d\0"
incorrect_reply: .ascii "Nope!\n\0"
correct_reply: .ascii "Correct!\n\0"

    .text
    .global main
main: 
    @ stack frame setup
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #4
    @ print game intro
    ldr r0, intro_ptr
    bl printf
    @ set the answer to be your favorite number
    mov r4, #36
begin_loop:
    @ print the prompt
    ldr r0, prompt_ptr
    bl printf
    @ read in the guess
    sub r1, fp, #8
    ldr r0, input_format_ptr
    bl scanf
    ldr r6, [fp, #-8]
    @ compare the guess to the solution
    cmp r6, r4
    beq handle_correct_guess
    ldr r0, incorrect_reply_ptr
    bl printf
    b begin_loop
handle_correct_guess:
    ldr r0, correct_reply_ptr
    bl printf
    @ stack frame teardown
    add sp, sp, #4
    pop {fp, lr}
    bx lr

intro_ptr: .word intro
prompt_ptr: .word prompt
input_format_ptr: .word input_format
incorrect_reply_ptr: .word incorrect_reply
correct_reply_ptr: .word correct_reply
