
### Hello World in Assembly

```arm
.section .rodata
    greeting: .ascii "Hello world!\n\0"

.section .text
.global main
main:
    ldr x0, =greeting
    bl printf
    mov x0, 0
    b exit
```