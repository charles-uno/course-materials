@ global constants
.section .rodata
prompt: .ascii "How many koalas do you have? \0"
input_format: .ascii "%d\0"
reply: .ascii "That's %d thumbs!\n\0"

num_thumbs:
    @ stack frame setup, no local variables
    push {fp, lr}
    add fp, sp, #4
    @ ----------> DIAGRAM 2 STOP HERE
    @ multiply the number of koalas by 6, return result
    mov r2, #6
    mul r0, r0, r2
    @ stack frame teardown
    pop {fp, pc}

.text
.global main
main: 
    @ set up stack frame for main, one local variable
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #4
    @ ask the user how many koalas they have
    ldr r0, prompt_ptr
    bl printf
    @ store response to local variable
    sub r1, fp, #8
    ldr r0, input_format_ptr
    bl scanf
    @ ----------> DIAGRAM 1 STOP HERE
    @ load local variable, pass it into num_thumbs
    ldr r0, [fp, #-8]
    bl num_thumbs    
    @ ----------> DIAGRAM 3 STOP HERE
    @ print the results
    mov r1, r0
    ldr r0, reply_ptr
    bl printf
    @ return 0, stack frame teardown
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

@ pointers
prompt_ptr: .word prompt
input_format_ptr: .word input_format
reply_ptr: .word reply