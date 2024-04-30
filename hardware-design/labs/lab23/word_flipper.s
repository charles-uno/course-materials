    .section .rodata
input_prompt:
    .ascii "Enter a word: \0"
char_format:
    .ascii "%c\0"

    .text
    .global flip_char_case
flip_char_case:
    @ set up stack frame, no local variables
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #0
    @ input r0 is an ascii char
    @ for uppercase letter (65-90) return the corresponding lowercase ascii value
    @ for lowercase letter (97-122) return the corresponding uppercase ascii value
    @ anything else return the input unchanged
    cmp r0, #65
    blt return
    cmp r0, #90
    ble upper_to_lower
    cmp r0, #97
    blt return
    cmp r0, #122
    ble lower_to_upper
    b return
upper_to_lower:
    add r0, r0, #32
    b return
lower_to_upper:
    sub r0, r0, #32
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

begin_loop:
    ldr r0, char_format_ptr
    sub r1, fp, #8
    bl  scanf

    @ input char is at fp-8. load to r0 for input, r3 for comparison
    ldr r0, [fp, #-8]
    mov r3, r0
    bl flip_char_case

    @ r3 is the input. r0 is flipped. so r3 != r0 indicates a letter
    cmp r3, r0
    beq end_loop

    mov r1, r0
    ldr r0, char_format_ptr
    bl printf
    b begin_loop
    
end_loop:
    @ print newline
    ldr r0, char_format_ptr
    mov r1, #'\n'
    bl printf

    @ return 0, restore stack frame
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

input_prompt_ptr:
    .word input_prompt
char_format_ptr:
    .word  char_format
