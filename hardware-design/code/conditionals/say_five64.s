    .section .rodata
prompt: .ascii "Please enter 5: \0"
input_format: .ascii "%d\0"
reply_incorrect: .ascii "Incorrect!\n\0"
reply_correct: .ascii "Correct!\n\0"

    .text
    .global main
main: 
    // stack frame setup
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #4
begin_loop:
    // print the prompt
    ldr x0, =prompt
    bl printf
    // read in the guess
    sub x1, fp, #8
    ldr x0, =input_format
    bl scanf
    ldr x2, [fp, #-8]
    // compare the guess to the solution
    cmp x2, #5
    beq break
    ldr x0, =reply_incorrect
    bl printf
    b begin_loop
break:
    ldr x0, =reply_correct
    bl printf
    // stack frame teardown
    sub sp, fp, #4
    pop {fp, pc}
