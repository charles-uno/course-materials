.section .rodata
prompt: .ascii "int plz: \0"
input_fmt: .ascii "%d\0"
output: .ascii "%d + 1 = %d\n\0"
.align 2

.global main
main: 
sub sp, sp, 0x30
str lr, [sp, 0x20]
str fp, [sp, 0x10]
add fp, sp, 0x20
ldr x0, =prompt
bl printf
ldr x0, =input_fmt
mov x1, sp
bl scanf
ldr x0, =output
ldr x1, [sp]
add x2, x1, 1
bl printf
ldr lr, [sp, 0x10]
ldr fp, [sp, 0x20]
add sp, sp, 0x30
b exit
    