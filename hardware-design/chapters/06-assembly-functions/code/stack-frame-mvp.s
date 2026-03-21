.section .rodata
output: .ascii "%d+1=%d\n\0"
.align 2

.text
.global main
main: 
sub sp, sp, 0x20
str lr, [sp, 0x10]
str fp, [sp]
add fp, sp, 0x20
ldr x0, [sp]
ldr x0, =output
mov x1, 5
add x2, x1, 1
bl printf
ldr lr, [sp, 0x10]
ldr fp, [sp]
add sp, sp, 0x20
b exit
