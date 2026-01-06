@ NOTE: this one does not work. not sure why we seem to be unable to overwrite a char in the middle of a string. also sed faults

    .section .rodata
prompt: .ascii "what is your name? \0"
string_format: .ascii "%s\0"
output: .ascii "the first three letters of your name: %s\n\0"

    .text
    .global insert_null
insert_null:
    @ set up stack frame, no local variables
    push {fp, lr}
    add fp, sp, #4
    mov r1, #'X'
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
    @ read in value, hope it doesn't overflow
    ldr r0, string_format_ptr
    sub r1, fp, #8
    bl scanf
    @ insert a null byte so we only print the first characters
    sub r0, fp, #16
    bl insert_null
    @ print the string. it'll stop when it hits the null
    ldr r0, output_ptr
    sub r1, fp, #8
    bl printf
    @ stack frame teardown, return 0
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

prompt_ptr: .word prompt
output_ptr: .word output
string_format_ptr: .word string_format

