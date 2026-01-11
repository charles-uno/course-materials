    .section .rodata
prompt_str:
    .ascii "Enter a number: \0"
format_str:
    .ascii "%d\0"
reply_str:
    .ascii "Sum: %d\n\0"

    .text
    .global main
main:
    @ set up stack frame, two local variables
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #8

    ldr r0, prompt_ptr
    bl printf
    ldr r0, format_ptr
    sub r1, fp, #8
    bl  scanf

    ldr r0, prompt_ptr
    bl printf
    ldr r0, format_ptr
    sub r1, fp, #12
    bl  scanf

    ldr r0, [fp, #-8]
    ldr r1, [fp, #-12]
    add r1, r0, r1
    ldr r0, reply_ptr
    bl printf

    sub sp, fp, #4
    pop {fp, pc}

prompt_ptr:
    .word prompt_str
format_ptr:
    .word  format_str
reply_ptr:
    .word  reply_str
