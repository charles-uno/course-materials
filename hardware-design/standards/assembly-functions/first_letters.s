    .section .rodata
prompt: .ascii "what is your name? \0"
output: .ascii "the first three letters of your name: %s\n\0"

    .text
    .global insert_null
insert_null:
    @ set up stack frame, no local variables
    push {fp, lr}
    add fp, sp, #4
    mov r1, #0
    str r1, [r0]
    @ stack frame teardown, return 0
    mov r0, #0
    pop {fp, lr}
    bx lr

    .text
    .global main
main: 
    @ stack frame setup, make room for a big string
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #400
    @ print prompt
    ldr r0, prompt_ptr
    bl printf



    @ fp-8 is n1, initialize to 4
    mov r4, #4
    str r4, [fp, #-8]
    @ fp-12 is n2, initialize to 7
    mov r5, #7
    str r5, [fp, #-12]
    @ fp-16 is n1_plus
    mov r0, r4
    bl add_one
    str r0, [fp, #-16]
    @ fp-20 is n2_plus
    mov r0, r5
    bl add_one
    str r0, [fp, #-20]
    @ Load and print n1, n1_plus
    ldr r0, output_ptr
    ldr r1, [fp, #-8]
    ldr r2, [fp, #-16]
    bl printf
    @ Load and print n2, n2_plus
    ldr r0, output_ptr
    ldr r1, [fp, #-12]
    ldr r2, [fp, #-20]
    bl printf
    @ stack frame teardown, return 0
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

prompt_ptr: .word prompt
output_ptr: .word output

