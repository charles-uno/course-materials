.section .rodata
    input_prompt: .ascii "Enter a character: \0"
    char_format: .ascii "%c\0"
    reply: .ascii "Flipped case: %c\12\0"

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

    // NOTE: options here
    // 1. use ldrb to read just one byte, then zero out the rest with uxtb
    // 2. use the 32-bit register w0?
    // 3. use a bit mask to manually clear the register
    ldr x0, [sp, 16]
    and x0, x0, 0xff
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
