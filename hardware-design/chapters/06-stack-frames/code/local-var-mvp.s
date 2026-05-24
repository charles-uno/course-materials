.section .rodata
prompt: .ascii "int plz: \0"
input_fmt: .ascii "%d\0"
output: .ascii "%d+1=%d\n\0"
.align 2

.global main
main: 
sub sp, sp, 0x10
ldr x0, =prompt
bl printf
ldr x0, =input_fmt
mov x1, sp
bl scanf
ldr x0, =output
ldr x1, [sp]
add x2, x1, 1
bl printf
add sp, sp, 0x10
b exit
    