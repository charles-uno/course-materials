    .section .rodata

    .text
func:
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #8
    @ ...
    sub sp, fp, #4
    pop {fp, pc}

    .global main
main: 
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #16
    @ ...
    bl func
    @ ...
    sub sp, fp, #4
    pop {fp, pc}


