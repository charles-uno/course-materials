.section .rodata
    // global constants

.section .data
    // global variables

// execution starts here
.section .text
.global main
main:
    // execution starts here

    // return 0 (normal exit status)
    mov x0, 0
    b exit
