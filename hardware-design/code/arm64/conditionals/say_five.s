.section .rodata
    prompt: .ascii "Please enter 5: \0"
    input_fmt: .ascii "%d\0"
    reply_incorrect: .ascii "Incorrect! %d is not 5\n\0"
    reply_correct: .ascii "Correct!\n\0"

.section .data
    guess: .word 0

.text
.global main
main: 
    // stack frame setup, no local variables
    sub sp, sp, 16
    str fp, [sp]
    str lr, [sp, 8]
    add fp, sp, 24
begin_loop:
    // ask for input
    ldr x0, =prompt
    bl printf
    // read the guess to memory
    ldr x0, =input_fmt
    ldr x1, =guess
    bl scanf
    // load the guess from memory
    ldr x1, =guess
    ldr x1, [x1]
    // check if the guess is correct
    cmp x1, 5
    // if the guess is correct, we're done
    beq break
    // otherwise, try again
    ldr x0, =reply_incorrect
    bl printf
    b begin_loop
break:
    ldr x0, =reply_correct
    bl printf
    // stack frame teardown, return zero
    mov x0, 0
    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 16
    ret
