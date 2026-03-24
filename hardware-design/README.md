# Hardware Design (CSCI 241)

Taught by Prof Charles Fyfe (St Olaf College)

Adapted in part from materials by Prof Melissa Lynn (St Olaf College)

> TODO: check if ML wants an author credit on the slides

Course listing [here](https://catalog.stolaf.edu/academic-programs/computer-science)

## Just The PDFs Please!

PDFs are built automatically using GitHub Actions. Check out the `Actions` tab up top. 

## Repo Summary

Heads up! Stuff is moving around right now. 

- `chapters` - This holds most of the actual content! Split up by chapter (aka unit, aka standard). Each directory contains `slides.md`, maybe some homework, maybe some support files
- `slides.tex` - build target for the whole slide deck. Pulls content from `chapters/*/slides.md`
- `homework.tex` - build target for the big bundle of homework. Pulls content from `chapters/*/homework.md`. Probably want to split this up into multiple files actually
- `build` - Templates and scripts for building our Markdown source files into PDFs via LaTeX
- `syllabus` - The syllabus
- `exams` - Quizzes and final. A bit of a mishmash from multiple semesters. Need to get this cleaned up

## Building Locally

Typesetting is done via LaTeX. Source code for LaTeX is pretty ugly, so much of the content is written in Markdown and converted over at build time. If you want to run that process locally, you'll need:

- MikTex, MacTex, or similar. The big install
- Python 3, plus the packages in `requirements.txt`
- Make

These requirements are for Mac OS. Linux is probably pretty much the same. If you need it to run on Windows, I'll bet an AI bot can figure it out

Circuit diagrams created using [this tool](https://www.circuit2tikz.tf.fau.de/designer/)

# TODO

Update exams to use markdown?

Figure out how to create tagged PDFs for accessibility

Add a slide with example two's complement subtraction

Add a slide with `concurrent` block when talking about multiprogramming. you can do multiprogramming within a program!


Pi setup -- ssh gen no longer does `id_rsa.pub`? It does a different type of key?

circuitverse - clarify that the button is a different type of input
switch over to a different circuit simulator? logic.ly? 
add screenshots to help with testbench setup

Rewrite Pi setup. Encourage use of AI tools for debugging! This is a great use case because (1) it's the sort of thing that lots of nerds argue about in the training data, (2) correctness is easily testable, (3) unlikely to break anything. Also mention a few common issues:

Update AI use policy in the syllabus

Write a script to create the stack frame walkthrough? It's super tedious and error prone when done manually

talk about extra annotation in AP! do not wait until stack frames

Get better ASCII table for tests (make sure null byte is visible)

Split warmups (Doenet) from assignments (PDF). Maybe get rid of Doenet entirely. Just have people check against their neighbors

Add makefile check to confirm that sections line up in the slides and the assignments

Update standards:
1. **Data Representation.** Integers, hex, arithmetic, two's complement, floating point, ASCII, structured data
2. **Logic Representation.** Boolean logic, logic gates, logic circuits, control circuits, circuitverse simulations
3. **Assembly Programming.** Global variables, global constants, printf, scanf, automated testing
4. **Electronic Circuits.** Resistors, transistors, breadboard labs
5. **Data Storage.** Memory hierarchy, caching, locality, physical storage mechanisms, redundancy, memory interleaving, RAID, virtual memory, erase before write, MMIO, 4kB storage alignment, write endurance, memory-mapped IO
6. **Control Flow.** Comparison, branching, if/else, loops
7. **The CPU.** Instruction cycle, clock-driven execution, instruction-level parallelization
8. **Stack Frames.** Local variables, functions, context switching
9. **OS Concepts.** Booting, user/kernel modes, system calls, traps/exceptions/interrupts, multithreading, multiprocessing, concurrency, hyperthreading
10. **Networking**? 

Maybe three quizzes with three standards each. OR MAYBE just have a quiz after every standard? Don't even clump them together? I like the idea of touching base on the standard a week later. Make sure it sinks in deeper than just short term memory. 

ALSO MAYBE: instead of O(10) standards, maybe have O(10) units, with a handful of standard each? That gives more granularity on what students got right and wrong. Might make homework grading easier, since each section is worth the same. Might also help stratify the grade distribution. Biggest downside is a *lot* of new columns in the Moodle gradebook