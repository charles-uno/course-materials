    .section .rodata
input_prompt: .ascii "please give an integer (number %d of 3) : \0"
input_string: .ascii "%d\0"
report_product: .ascii "the product of those numbers is %d\n\0"

    .text
    .global mul_three
mul_three:
    @ set up stack frame, no local variables
    push {fp, lr}
    add fp, sp, #4
    @ three variables: x, y, z
    @ return x*y*z
    mul r0, r0, r1
    mul r0, r0, r2
    @ stack frame teardown
    pop {fp, lr}
    bx lr

    .text
    .global main
main: 
    @ stack frame setup, four local variables
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #16
    @ read a value to fp-8
	ldr r0, input_prompt_ptr
    mov r1, #1
	bl printf
	ldr r0, input_string_ptr
	sub r1, fp, #8
	bl scanf
    @ read a value to fp-12
	ldr r0, input_prompt_ptr
    mov r1, #2
	bl printf
	ldr r0, input_string_ptr
	sub r1, fp, #12
	bl scanf
    @ read a value to fp-16
	ldr r0, input_prompt_ptr
    mov r1, #3
	bl printf
	ldr r0, input_string_ptr
	sub r1, fp, #16
	bl scanf
    @ load those three values to pass to the function
    ldr r0, [fp, #-8]
    ldr r1, [fp, #-12]
    ldr r2, [fp, #-16]
    bl mul_three
    @ store the result just in case we need to use r0
    sub r1, fp, #20
    str r0, [r1]
    @ report the result
    ldr r0, report_product_ptr
    @ oops we overwrote r0. better load the product
    ldr r1, [fp, #-20]
    bl printf
    @ stack frame teardown, return 0
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

input_prompt_ptr: .word input_prompt
input_string_ptr: .word input_string
report_product_ptr: .word report_product
