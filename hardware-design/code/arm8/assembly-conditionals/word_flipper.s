.section .rodata
    prompt: .ascii "Enter a word: \0"
    char_format: .ascii "%c\0"
    newline: .ascii "\n\0"

.text
flip_char_case:
    // stack frame setup, no local variables
    sub sp, sp, 0x20
    str fp, [sp]
    str lr, [sp, 0x10]
    // for uppercase letter (65-90) return the corresponding lowercase ascii value
    // for lowercase letter (97-122) return the corresponding uppercase ascii value
    // anything else return the input unchanged
    cmp x0, 'A'
    blt return
    cmp x0, 'Z'
    ble upper_to_lower
    cmp x0, 'a'
    blt return
    cmp x0, 'z'
    ble lower_to_upper
    b return
upper_to_lower:
    add x0, x0, 32
    b return
lower_to_upper:
    sub x0, x0, 32
    b return
return:
    ldr lr, [sp, 0x10]
    ldr fp, [sp]
    add sp, sp, 0x20
    ret

.global main
main:
    // stack frame setup, one local variable
    sub sp, sp, 0x30
    str fp, [sp]
    str lr, [sp, 0x10]
    add fp, sp, 0x20
    // display the prompt
    ldr x0, =prompt
    bl printf
    // use scanf to process characters one at a time. this works because the
    // os buffers the input and only feeds it in as we ask for it
begin_loop:
    ldr x0, =char_format
    add x1, sp, 0x20
    bl  scanf
    ldr x0, [sp, 0x20]
    // we only care about the bottom 8 bits. clear out anything else
    and x0, x0, 0xff
    bl flip_char_case
    // reload the original. if the char did not change, it's not a letter
    ldr x1, [sp, 0x20]
    and x1, x1, 0xff
    cmp x0, x1
    beq end_loop
    mov x1, x0
    ldr x0, =char_format
    bl printf
    b begin_loop
    
end_loop:
    ldr x0, =newline
    bl printf
    // return 0, restore stack frame
    ldr lr, [sp, 0x10]
    ldr fp, [sp]
    add sp, sp, 0x30
    ret
