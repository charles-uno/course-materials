.section .rodata
    report: .ascii "The sum from 0 to 100 is: %d\n\0"

.text
.global main
main: 
    // stack frame setup
    sub sp, sp, 16
    str fp, [sp]
    str lr, [sp, 8]
    add fp, sp, 24
    // initialize x4: loop counter
    // initialize x5: sum
    mov x4, 0
    mov x5, 0
begin_loop:
    // increment loop counter
    add x4, x4, 1
    // increase running sum
    add x5, x5, x4
    // check break condition
    cmp x4, 100
    // if not done, back to the top of the loop
    blt begin_loop
    // report result
    ldr x0, =report
    mov x1, x5
    bl printf
    // stack frame teardown, return zero
    mov x0, 0
    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 16
    ret

