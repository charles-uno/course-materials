.section .rodata
prompt: .ascii "how many koalas do you have? \0"
fmt: .ascii "%d\0"
report: .ascii "that's %d thumbs!\n\0"
.align 2
.section .text
.global main
get_n_thumbs:
    sub sp, sp, 0x20
    str fp, [sp]
    str lr, [sp, 0x10]
    add fp, sp, 0x10
    mov x4, 6
    mul x3, x0, x4
    mov x0, x3
    ldr lr, [sp, 0x10]
    ldr fp, [sp]
    add sp, sp, 0x20
    ret
main:
    sub sp, sp, 0x30
    str fp, [sp]
    str lr, [sp, 0x10]
    add fp, sp, 0x20
    ldr x0, =prompt
    bl printf
    ldr x0, =fmt
    mov x1, fp
    bl scanf
    ldr x0, [fp]
    bl get_n_thumbs
    mov x1, x0
    ldr x0, =report
    bl printf
    ldr lr, [sp, 0x10]
    ldr fp, [sp]
    mov x0, 0
    b exit
