@ Global constants
@ current_prompt: string prompting the user to enter the current year
@ birth_prompt: string prompting the user to enter their birth year
@ input_string: formatting string for reading the user’s input
@ print_age: formatting string for printing the age the user turns this year

@ function compute_age
	@ two parameters: birth_year and this_year
	@ returns this_year - birth_year; the age they will turn this year

@ main
	@ set up stack frame for main
	@ local variables: current_year, user_birth_year, age
	@ [fp, #-8] is current_year, an integer
	@ [fp, #-12] is user_birth_year, an integer
	@ [fp, #-16] is age, an integer


	@ prompt the user to enter the current year, and store input

	@ prompt the user to enter their birth year, and store the input

	@ call compute_age on user_birth_year and current_year

	@ store return value to age

	@ report the age the user turns this year

	@ return 0

	@ tear down stack frame for main


@ Pointers
@ pointers to strings
