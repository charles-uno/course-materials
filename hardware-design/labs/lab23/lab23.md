# Lab 23 - Loops in Assembly

Start in class on Wednesday, 4/24

Due Friday, 4/26, by 10pm

## Setup  

### For Code

Log into your personal account on your Raspberry Pi, and create a subdirectory for this lab
```
cd HD
mkdir lab23
cd lab23
```

### For Google Doc Submission

Make a copy of this doc (using the File menu) and share it with `hd-tas@stolaf.edu`, then enter all your work in your shared copy. Please use your St. Olaf email account (`@stolaf.edu`). Please use the default document name "Copy of Lab ...", so we can find your work. We don't need your name in the document name

Enter your username here: 
|----------|
|          |
|----------|







OPTIONAL: notes to grader
For example, "Could you comment on my answers to problems A3 and B2?"




A.	Reading
Recall that the textbook “Diving Into Systems” has chapters on Assembly Programming, but it does not cover the exact variety of assembly that we will use on the Raspberry Pis. There are many varieties of assembly languages, sharing similar structures, but with somewhat different syntax.

We will be programming in ARM v7 Assembly, which is covered in the tutorial here. 

The reading for this lab is Sections 4.5 and 4.6 from the ARM tutorial. Take notes as you read through these sections. You may choose to write your notes in the text box below, or write your notes on paper, take a picture, and upload the picture in the box below.





After completing the reading - What makes sense, what doesn't?  Are there things you want to ask in class, on Moodle, in office hours, or a help session, etc.?  
If you understand everything, write Understood.





NOTE: this lab is tricky! Please work in groups of ~4 to make sure nobody gets left behind. You may even want to have some people start with B, others start with C, then come together at the end. Just make sure the work you turn in at the end reflects your own personal understanding. Also remember that Friday is a catch-up day
B. Review: Branching in Assembly
In your lab23 subdirectory, create a new file char_flipper.s
This program accepts a single character, then prints back that same character in the opposite case. For example, “a” gives “A”, and “R” gives “r”. For non-letter input, return the same value unchanged. A skeleton of the program is included below, with comments. Please fill in the missing logic and answer the questions as you go.

In the past, we have always used numbers as input. How might we accept a character instead? Hint: “printf” exists in many languages, including Python and C. Try Google.




Once you have the value in memory, what’s the difference between an ASCII value and the corresponding unsigned int? (For example, “A” vs 65)




In C or Python, you can perform multiple comparisons on the same line (eg n >= 65 && n <= 90). Assembly doesn’t do that. What’s your strategy for handling all these cases without spaghetti code?




Did your code work? Did it get close? Put a screenshot in here for your own satisfaction




char_flipper.s
   .section .rodata
@ strings go here for input and output


   .text
   .global flip_char_case
flip_char_case:
   @ set up stack frame


   @ input r0 is an ascii char


   @ for uppercase letter (65-90) return the corresponding lowercase value


   @ for lowercase letter (97-122) return the corresponding uppercase value


   @ anything else return the input unchanged


   @ tear down the stack frame


   .text
   .global main
main:  
   @ set up the stack frame


   @ use printf to print the prompt


   @ use scanf to put the input in memory


   @ load the input from memory


   @ call flip_char_case


   @ use printf to announce the result


   @ return 0, stack frame cleanup


@ pointers to globals go here






To submit your work in this part: carry these steps out on your Pi.
cd ~/HD/lab23
git add char_flipper.s
git commit -m "lab23: Part B complete"
git pull origin main
git push origin main


Note: if your work is not yet complete, use a different commit message indicating what you have done, e.g., "lab23: Part B started only"
C. Looping with Static Values
In your lab23 subdirectory, create a new file count_to_ten.s
This program counts to ten. No input, no functions. Just practice writing a loop. 

The tutorial (link) shows a basic loop, then also shows a loop that is more efficient (but maybe less legible). Which style will you use? Why?




You may accidentally write a loop that never breaks. If that happens, use ctrl-C to stop the process. Approximately how many times did you run into this issue?




Did your code work? Did it get close? Put a screenshot in here for your own satisfaction




count_to_ten.s
   .section .rodata
@ strings go here for input and output


   .text
   .global main
main:
   @ set up the stack frame


   @ initialize counter


   @ top of loop


   @ do the thing


   @ maybe break from the loop


   @ return 0, stack frame cleanup


@ pointers to globals go here







To submit your work in this part: carry these steps out on your Pi.
cd ~/HD/lab23
git add char_flipper.s
git commit -m "lab23: Part C complete"
git pull origin main
git push origin main


Note: if your work is not yet complete, use a different commit message indicating what you have done, e.g., "lab23: Part C started only"
D. Looping with Dynamic Values

In your lab23 subdirectory, create a new file char_counter.s
This program accepts a series of characters. It counts the length of the first word then reports that length. No spell-checking necessary – just count how many lowercase letters you see in a row, starting with the first one. A skeleton of the program is included below, with comments. Please fill in the missing logic and answer the questions as you go.

In this program, we accept characters one at a time. If we wanted, we could accept input all at once as a string. Which seems easier in this situation? Why? Hint: think about allocating stack space for local variables




How many local variables does your function need? Do you have any values that would make sense to store in longer-term registers r4-r9?




Did your code work? Did it get close? Put a screenshot in here for your own satisfaction




char_counter.s
   .section .rodata
@ strings go here for input and output


   .text
   .global is_lowercase_letter
is_lowercase_letter:
   @ set up stack frame


   @ input r0 is an ascii char


   @ for lowercase letter (97-122) return 1


   @ anything else return 0


   @ tear down the stack frame


   .text
   .global main
main:
   @ set up the stack frame


   @ initialize length counter


   @ use printf to print the prompt


   @ top of loop


   @ read one char into memory


   @ is this a lowercase letter?


   @ maybe increment the counter and repeat


   @ maybe break from the loop


   @ use printf to announce the result


   @ return 0, stack frame cleanup


@ pointers to globals go here






To submit your work in this part: carry these steps out on your Pi.
cd ~/HD/lab23
git add char_flipper.s
git commit -m "lab23: Part D complete"
git pull origin main
git push origin main


Note: if your work is not yet complete, use a different commit message indicating what you have done, e.g., "lab23: Part D started only"
E. Bringing it All Together
For our final program, we will bring together elements of sections B and C. Make sure you have a good understanding of both. If you don’t, work through your questions with your group, or even the next table over! You can also ask for help from the professor and/or TAs of course
In your lab23 subdirectory, open a new file word_flipper.s
This program accepts a word and prints that word back with the case flipped. No spell-checking necessary. Just process each letter (uppercase and/or lowercase) until you run into the end of the word (and non-letter character). A skeleton of the program is included below, with comments. Please fill in the missing logic and answer the questions as you go.

How many local variables do you need in main? Hint: you can read, process, and write characters one at a time. No need to worry about your input and output stepping on each others’ toes. The operating system makes this possible by buffering the input until the program is ready for it




You can reuse your function flip_char_case from section B to process a single character. Can you also use this function to judge if the current character is a letter or not? If so, how?




How would you modify this program to process multiple words? Explain below




Do you think the functions flip_char_case or is_lowercase_letter ever looked at a null byte during your work? Why or why not?




Did your code work? Did it get close? Put a screenshot in here for your own satisfaction




word_flipper.c
   .section .rodata
@ strings go here for input and output


   .text
   .global flip_char_case
flip_char_case:
   @ same as part B


   .text
   .global main
main:  
   @ set up stack frame


   @ print the prompt


   @ top of loop


   @ read one character


   @ flip the case


   @ was it a letter?


   @ maybe print and keep going


   @ maybe break from the loop


   @ do you need to print a newline here?


   @ return 0, stack frame cleanup


@ pointers to globals go here






To submit your work in this part: carry these steps out on your Pi.
cd ~/HD/lab23
git add char_flipper.s
git commit -m "lab23: Part E complete"
git pull origin main
git push origin main


Note: if your work is not yet complete, use a different commit message indicating what you have done, e.g., "lab23: Part E started only"

F. 	Submission
On a scale of 1 to 10, how difficult was this lab for you?
On a scale of 1 to 10, how satisfied are you with your work?




In the text box below, write a brief summary of the information covered in this lab. Indicate what topics you understand well, and which topics you will need to spend some more time on.




Did you work on this lab with other students? If so, list their names in the box below.





Finally, verify that you have shared your Google Doc with hd-tas@stolaf.edu. Also log in to csgit.stolaf.edu, to double check that the files char_flipper.s, char_counter.s, and word_flipper.s appear in your lab23 subdirectory.

