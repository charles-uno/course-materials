    .section .rodata
intro: .ascii "I'm thinking of a number 0 to 127\n\0"
prompt: .ascii "Guess #%d: \0"
input_format: .ascii "%d\0"
too_high_reply: .ascii "Too high!\n\0"
too_low_reply: .ascii "Too low!\n\0"
correct_reply: .ascii "Correct!\n\0"
no_more_tries: .ascii "No more tries. Better luck next time!\n\0"

    .text
    .global main
main: 
    @ stack frame setup
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #4
    @ use current time to generate "random" number in r4
    sub r0, fp, #8      @ no errors
    bl time             @ in these
    ldr r4, [fp, #-8]   @ four lines
    and r4, r4, #0x7f   @ i promise
    @ init guess counter
    mov r5, #0
    @ print game intro
    ldr r0, intro_ptr
    bl printf
begin_loop:
    @ increment guess counter, break if max
    add r5, r5, #1
    cmp r5, #10
    bgt break_failure
    @ print the numbered prompt
    mov r1, r5
    ldr r0, prompt_ptr
    bl printf
    @ read in the guess
    sub r1, fp, #8
    ldr r0, input_format_ptr
    bl scanf
    ldr r6, [fp, #-8]
    @ compare the guess to the solution
    cmp r6, r4
    beq break_success
    blt too_low
    bgt too_high
    @ handle cases
too_low:
    ldr r0, too_low_reply_ptr
    bl printf
    b begin_loop
too_high:
    ldr r0, too_high_reply_ptr
    bl printf
    b begin_loop
break_success:
    ldr r0, correct_reply_ptr
    bl printf
    b return
break_failure:
    ldr r0, no_more_tries_ptr
    bl printf
    b return
return:
    @ stack frame teardown
    add sp, sp, #4
    pop {fp, lr}
    bx lr

intro_ptr: .word intro
prompt_ptr: .word prompt
input_format_ptr: .word input_format
too_high_reply_ptr: .word too_high_reply
too_low_reply_ptr: .word too_low_reply
correct_reply_ptr: .word correct_reply
no_more_tries_ptr: .word no_more_tries
