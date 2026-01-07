.section .rodata
    input_prompt: .ascii "Enter a character: \0"
    char_format: .ascii "%c\0"
    reply: .ascii "Flipped case: %c\12\0"

.text
flip_char_case:
    // stack frame setup, no local variables
    sub sp, sp, 16
    str fp, [sp]
    str lr, [sp, 8]
    // we only care about the last 8 bits. ignore the rest
    and x0, x0, 0xff
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
    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 16
    ret

.text
.global main
main: 
    sub sp, sp, 32
    str fp, [sp]
    str lr, [sp, 8]
    add fp, sp, 24

    ldr x0, =input_prompt
    bl printf
    ldr x0, =char_format
    add x1, sp, 16
    bl scanf

    ldr x0, [sp, 16]
    bl flip_char_case

    mov x1, x0
    ldr x0, =reply
    bl printf

    // return 0, stack frame teardown
    mov x0, 0
    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 32
    ret
