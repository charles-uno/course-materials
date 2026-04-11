
---

# Assembly Conditionals

Submit code via `csgit`. Submit notes, screenshots, and scans via Moodle.

Please work on your own, then compare your results with at least two of your peers. If you find nontrivial differences, talk them out until everyone is on the same page.

When printing code to mark it up, I recommend formatting the text with multiple columns or printing multiple pages per sheet. Marked-up code should be scanned and submitted via Moodle.

When parsing C code, you may reference whatever people and resources you like. You do not need to be able to reproduce it, but I would like you to generally understand it when you look at it. 

When writing Assembly code, you may reference whatever people and materials you like. But make sure the code you turn in reflects your own understanding. 

## Reading

Read [Dive Into Systems](https://diveintosystems.org) 9.4.

## Understanding Conditional Code

TODO: provide some C code here. Have them print it out and mark it up.

## Fizzbuzz

Write an Assembly program `fizzbuzz.s`. It should do the following:

- Prompt the user to enter an integer between 1 and 100
- Make sure the entry is valid. Otherwise, print an error message and prompt them again. Loop this until they enter an appropriate number
- Loop from 1 to the number entered. If the number is a multiple of 2, print `fizz`. If it's a multiple of 3, print `buzz`. If it's a multiple of both, print `fizzbuzz`. Otherwise, print the number. 
- Note: you are not required to use functions, but you may find them helpful as you organize your code.

For example, if the user enters 8, the output should be:
```
1
fizz
buzz
fizz
5
fizzbuzz
7
fizz
```

This is a complex program with multiple nested comparisons! I strongly encourage you to start small and work your way up. Commit your progress to `csgit` every time you make progress. For example, you could do:

1. Write a program that prompts the user for a number and prints it back out. 
2. Update it to ensure the input is positive. If the number is zero or negative, print an error message and exit.
3. Update it to ensure the input isn't too big. If it's over 100, print an error message and exit.
4. Update it to loop instead of exiting. It should keep prompting and checking until the user provides good input.
5. Instead of just printing the input, update the program to print everything from 1 to that number.
6. Add handling to print "fizz" for even numbers.
7. Etc...

Make sure to include a test with your code! It should include coverage for corner cases. 

## Word flipper?

