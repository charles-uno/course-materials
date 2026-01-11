@ ascii globals go here
    .section .rodata
prompt: .ascii "Please input a character: \0"
char_format: .ascii "%c\0"
reply_uppercase: .ascii "Input is an uppercase letter\n\0"
reply_lowercase: .ascii "Input is a lowercase letter\n\0"
reply_number: .ascii "Input is a number\n\0"
reply_other: .ascii "Input is something else\n\0"

    .text
    .global main
main: 
    @ stack frame setup, one local variable
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #4
    @ print the prompt
    ldr r0, prompt_ptr
    bl printf
    @ read the value and load it
    ldr r0, char_format_ptr
    sub r1, fp, #8
    bl scanf
    ldr r4, [fp, #-8]
    @ numbers is 48-57
    @ uppercase is ascii 65-90
    @ lowercase is ascii 97-122
    cmp r4, #48
    blt other
    cmp r4, #57
    ble number
    cmp r4, #65
    blt other
    cmp r4, #90
    ble uppercase
    cmp r4, #97
    blt other
    cmp r4, #122
    ble lowercase
    b other
uppercase:
    ldr r0, reply_uppercase_ptr
    b print_and_return
lowercase:
    ldr r0, reply_lowercase_ptr
    b print_and_return
number:
    ldr r0, reply_number_ptr
    b print_and_return
other:
    ldr r0, reply_other_ptr
print_and_return:
    bl printf
    @ return 0, stack frame teardown
    mov r0, #0
    sub sp, fp, #4
    pop {fp, lr}
    bx lr

@ pointers to ascii globals
prompt_ptr: .word prompt
char_format_ptr: .word char_format
reply_uppercase_ptr: .word reply_uppercase
reply_lowercase_ptr: .word reply_lowercase
reply_number_ptr: .word reply_number
reply_other_ptr: .word reply_other
