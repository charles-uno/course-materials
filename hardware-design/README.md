
> TODO: update the readme! this is way out of date
> include info about building the slides. dependencies, make
> include link to the course on doenet

> TODO: add ability to build the syllabus outside the slide deck? maybe each section is its own tex file. then we can just import in both places
> or maybe the course intro in the slides doesn't need to cover the whole syllabus... that's probably a better solution

syntax highlighting: `pip install pygments-arm`



# Hardware Design

Taught at St Olaf College, Spring 2024

Partial course. The curriculum was mostly set by [Melissa Lynn](https://wp.stolaf.edu/mscs/mscs-faculty-staff-listing/), but she was unable to complete the semester. 

Course listing for CS 241: https://catalog.stolaf.edu/academic-programs/computer-science




## Slides

Requires MikTex, MacTex, or similar. The big install. 

Tikz circuit diagrams created using this tool: https://www.circuit2tikz.tf.fau.de/designer/


## Labs

These labs are meant to be run on Raspberry Pi. No promises that you'll be able to compile this flavor of Assembly anywhere else. Example usage:
```
> cd labs/lab23/
> gcc char_flipper.s
> ./a.out
Enter a character: H
Flipped case: h
```

ARM tutorial: https://computerscience.chemeketa.edu/armTutorial/index.html

Emulator: https://cpulator.01xz.net/?sys=arm

## Standards

- Assembly 1: global variables and input/output
- Assembly 2: local variables and functions
- Assembly 3: conditionals and loops

## Standards-Based Grading

- Quiz 1: standards 1, 2
- Quiz 2: standards 3, 4
- Exam 1: standards 1-4
- Quiz 3: standards 5, 6
- Quiz 4: standards 7, 8
- Exam 2: standards 5-8
- Final: standards 1-8

Notably, you only have to demonstrate proficiency once! So if you get full credit on standard 1 on the quiz, you can skip that part of exam 1 and the final.

Grading scale:

- Proficiency. Full credit
- Almost. Half credit, submit a revision within a week for full credit
- Partial proficiency. Half credit. Try again
- No credit. Try again

