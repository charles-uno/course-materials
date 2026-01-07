// NOTE: does not quite work yet


.section .rodata
    prompt: .ascii "Enter a word: \0"
    char_format: .ascii "%c\0"
    newline: .ascii "\n\0"

    debug: .ascii "%c -> %c\n\0"

.text
flip_char_case:
    // stack frame setup, no local variables
    sub sp, sp, 16
    str fp, [sp]
    str lr, [sp, 8]

    mov x1, x0
    
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

    mov x2, x0
    ldr x0, =debug
    bl printf
    mov x0, x2

    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 16
    ret

.text
.global main
main:
    // stack frame setup, one local variable
    sub sp, sp, 32
    str fp, [sp]
    str lr, [sp, 8]
    add fp, sp, 24
    // display the prompt
    ldr x0, =prompt
    bl printf
    // loop over the input characters one by one
begin_loop:
    ldr x0, =char_format
    add x1, sp, 24
    bl  scanf
    // load input character from memory
    ldr x0, [sp, 24]
    // we only care about the last 8 bits. ignore the rest
    and x0, x0, 0xff

    mov x4, x0

    // flip the character in x0
    bl flip_char_case
    // compare original to flipped. if it changed, it's a letter

    cmp x0, x4
    beq end_loop

    mov x1, x0
    ldr x0, =char_format
    bl printf
    b begin_loop
    
end_loop:
    // print newline
    ldr x0, =newline
//    mov x1, '\n'
    bl printf

    // return 0, restore stack frame
    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 32
    ret
