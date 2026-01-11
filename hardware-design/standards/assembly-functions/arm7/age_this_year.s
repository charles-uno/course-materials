    .section .rodata
current_year_prompt: .ascii "what year is it? \0"
birth_year_prompt: .ascii "what year were you born? \0"
input_string: .ascii "%d\0"
print_age: .ascii "you will turn %d this year\n\0"

@ function compute_age

    .text
    .global compute_age
compute_age:
    @ set up stack frame, no local variables
    push {fp, lr}
    add fp, sp, #4
	@ two parameters: birth_year and this_year
	@ returns this_year - birth_year; the age they will turn this year
	sub r0, r1, r0
    @ stack frame teardown
    pop {fp, lr}
    bx lr

    .text
    .global main
main: 
    @ stack frame setup, three local variables
    push {fp, lr}
    add fp, sp, #4
    sub sp, sp, #12
    @ fp-8 is birth year. read it in
	ldr r0, birth_year_prompt_ptr
	bl printf
	ldr r0, input_string_ptr
	sub r1, fp, #8
	bl scanf
	@ fp-12 is current year. read it in
	ldr r0, current_year_prompt_ptr
	bl printf
	ldr r0, input_string_ptr
	sub r1, fp, #12
	bl scanf
	@ function expects current year in r0, birth year in r1
	ldr r0, [fp, #-8]
	ldr r1, [fp, #-12]
	bl compute_age
	@ result is in r0. store it in fp-16 in case we need it later
	sub r1, fp, #16
	str r0, [r1]
	@ report the result
	ldr r0, print_age_ptr
	@ oops we overwrote the age in r0, load it from memory
	ldr r1, [fp, #-16]
	bl printf
    @ stack frame teardown, return 0
    mov r0, #0
    sub sp, fp, #4
    pop {fp, pc}

current_year_prompt_ptr: .word current_year_prompt
birth_year_prompt_ptr: .word birth_year_prompt
input_string_ptr: .word input_string
print_age_ptr: .word print_age
