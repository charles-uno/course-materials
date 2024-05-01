    .section .rodata
input_prompt: .ascii "please give integer %c: \0"
input_string: .ascii "%d\0"
report_product: .ascii "x*(y+z) = %d\n\0"

    .text
    .global do_math
do_math:
    @ set up stack frame, no local variables
    push {fp, lr}
    add fp, sp, #4
    @ three variables: x, y, z
    @ return x*(y+z)
    add r1, r1, r2
    mul r0, r0, r1
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
    @ read x to fp-8
	ldr r0, input_prompt_ptr
    mov r1, #'x'
	bl printf
	ldr r0, input_string_ptr
	sub r1, fp, #8
	bl scanf
    @ read y to fp-12
	ldr r0, input_prompt_ptr
    mov r1, #'y'
	bl printf
	ldr r0, input_string_ptr
	sub r1, fp, #12
	bl scanf
    @ read z to fp-16
	ldr r0, input_prompt_ptr
    mov r1, #'z'
	bl printf
	ldr r0, input_string_ptr
	sub r1, fp, #16
	bl scanf
    @ load those three values to pass to the function
    ldr r0, [fp, #-8]
    ldr r1, [fp, #-12]
    ldr r2, [fp, #-16]
    bl do_math
    @ store the result just in case we need to use r0
    sub r1, fp, #20
    str r0, [r1]
    @ report the result
    ldr r0, report_product_ptr
    @ oops we overwrote r0. better load it from memory
    ldr r1, [fp, #-20]
    bl printf
    @ stack frame teardown, return 0
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

input_prompt_ptr: .word input_prompt
input_string_ptr: .word input_string
report_product_ptr: .word report_product


@ function do_math
	@ three parameters: x, y, z
	@ returns x*(y+z)

@ main
	@ set up stack frame for main
	@ local variables: num1, num2, num3, result

	@ initialize num1 to 3

	@ initialize num2 to 7

	@ initialize num3 to 8

	@ call do_math on x, y, and z, and store the returned value to result

	@ return 0

	@ tear down stack frame for main
