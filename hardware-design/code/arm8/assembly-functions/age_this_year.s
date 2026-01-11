.section .rodata
    current_year_prompt: .ascii "what year is it? \0"
    birth_year_prompt: .ascii "what year were you born? \0"
    input_string: .ascii "%d\0"
    print_age: .ascii "at the end of this year you will be %d years old\n\0"

.text
compute_age:
    sub sp, sp, 16
    str fp, [sp]
    str lr, [sp, 8]
    add fp, sp, 8
	// two parameters: birth_year and this_year
	sub x0, x1, x0
    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 16
    ret

.global main
main: 
    sub sp, sp, 48
    str fp, [sp]
    str lr, [sp, 8]
    add fp, sp, 32

	ldr x0, =birth_year_prompt
	bl printf
	ldr x0, =input_string
	add x1, sp, 16
	bl scanf

	ldr x0, =current_year_prompt
	bl printf
	ldr x0, =input_string
	add x1, sp, 24
	bl scanf

	// function expects current year then birth year
	ldr x0, [sp, 16]
	ldr x1, [sp, 24]
	bl compute_age

	// result is in x0. store in a local variable just in case we need it later
	str x0, [sp, 32]
	// report the result
	ldr x0, =print_age
	// oops we overwrote the age in x0, load it from memory
	ldr x1, [sp, 32]
	bl printf

    mov x0, 0
    ldr lr, [sp, 8]
    ldr fp, [sp]
    add sp, sp, 48
    ret

