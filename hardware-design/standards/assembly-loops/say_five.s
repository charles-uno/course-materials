    .section .rodata
prompt: .ascii "Please enter 5: \0"
input_format: .ascii "%d\0"
reply_incorrect: .ascii "Incorrect!\n\0"
reply_correct: .ascii "Correct!\n\0"

    .text
    .global main
main: 
    @ stack frame setup
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #4
begin_loop:
    @ print the prompt
    ldr r0, prompt_ptr
    bl printf
    @ read in the guess
    sub r1, fp, #8
    ldr r0, input_format_ptr
    bl scanf
    ldr r2, [fp, #-8]
    @ compare the guess to the solution
    cmp r2, #5
    beq break
    ldr r0, reply_incorrect_ptr
    bl printf
    b begin_loop
break:
    ldr r0, reply_correct_ptr
    bl printf
    @ stack frame teardown
    sub sp, fp, #4
    pop {fp, pc}

prompt_ptr: .word prompt
input_format_ptr: .word input_format
reply_correct_ptr: .word reply_correct
reply_incorrect_ptr: .word reply_incorrect
