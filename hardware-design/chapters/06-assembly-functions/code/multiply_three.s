.section .rodata
    input_prompt: .ascii "please give an integer (number %d of 3) : \0"
    input_string: .ascii "%d\0"
    report_product: .ascii "the product of those numbers is %d\n\0"

.text
mul_three:
    sub sp, sp, 16
    str fp, [sp]
    str lr, [sp, 8]
    // three variables: x, y, z
    // return x*y*z
    mul x0, x0, x1
    mul x0, x0, x2
    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 16
    ret

.global main
main: 
    sub sp, sp, 48
    str fp, [sp]
    str lr, [sp, 8]
    add fp, sp, 40

	ldr x0, =input_prompt
    mov x1, 1
	bl printf
	ldr x0, =input_string
	add x1, sp, 16
	bl scanf

	ldr x0, =input_prompt
    mov x1, 2
	bl printf
	ldr x0, =input_string
	add x1, sp, 24
	bl scanf

	ldr x0, =input_prompt
    mov x1, 3
	bl printf
	ldr x0, =input_string
	add x1, sp, 32
	bl scanf

    ldr x0, [sp, 16]
    ldr x1, [sp, 24]
    ldr x2, [sp, 32]
    bl mul_three

    // store the result just in case we need to use r0
    str x0, [sp, 40]

    ldr x0, =report_product
    // oops we overwrote x0. better load the product
    ldr x1, [sp, 40]
    bl printf

    mov x0, 0
    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 48
    b exit

