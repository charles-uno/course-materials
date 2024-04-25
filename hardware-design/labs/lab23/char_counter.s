    .section .rodata
input_prompt:
    .ascii "Enter a word: \0"
char_format:
    .ascii "%c\0"
report_length:
    .ascii "word length is %d\12\0"

    .text
    .global is_lowercase_letter
is_lowercase_letter:
    @ set up stack frame, no local variables
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #0
    @ input r0 is an ascii char
    @ return 1 if its value is a lowercase letter (97-122) return the corresponding uppercase ascii value
    @ return 0 otherwise
    cmp r0, #65
    blt return_zero
    cmp r0, #90
    blt return_zero
    b return_one
return_zero:
    mov r0, #0
    b return
return_one:
    mov r0, #1
    b return
return:
    pop {fp, lr}
    bx lr

    .text
    .global main
main: 
    push {fp, lr}
    @ stack frame, one local variables
    add fp, sp, #4
    sub sp, sp, #4
    @ fp-8 is where we read the char from input

    ldr r0, input_prompt_ptr
    bl printf

    @ initialize the length counter
    mov r4, #0

begin_loop:
    ldr r0, char_format_ptr
    sub r1, fp, #8
    bl  scanf

    @ input char is at fp-8. load to r0
    ldr r0, [fp, #-8]
    bl is_lowercase_letter

    @ if it's a letter, increment the counter and loop again
    cmp r0, #1
    beq letter
    bne end_loop

letter:
    add r4, r4, #1
    b begin_loop
end_loop:
    ldr r0, report_length_ptr
    mov r1, r4
    bl printf

    @ return 0, restore stack frame
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

input_prompt_ptr:
    .word input_prompt
char_format_ptr:
    .word  char_format
report_length_ptr:
    .word   report_length
