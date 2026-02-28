.section .rodata
prompt: .ascii "int plz: \0"
input_fmt: .ascii "%d\0"
output: .ascii "%d+1=%d\n\0"
.align 2

.text
add_one:
sub sp, sp, 0x20
str fp, [sp]
str lr, [sp, 0x10]
add fp, sp, 0x10
add x0, x0, 1
ldr lr, [sp, 0x10]
ldr fp, [sp]
add sp, sp, 0x20
ret

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
ldr x0, [sp]
bl add_one
mov x2, x0
ldr x0, =output
ldr x1, [sp]
bl printf
ldr lr, [sp, 0x10]
ldr fp, [sp, 0x20]
add sp, sp, 0x30
b exit
