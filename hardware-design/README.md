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

# TODO - Curriculum

Add dedicated DISCUSSION slides. not just a question in the middle of a list

Add BOARD WORK slides. Ideally one per section. Dedicaetd group work

Just do a quiz per standard. Have a handful of checkboxes. O(5) per standard. Make the expectations clear and also give us some granularity on the grading

Update standards:

1. **Data Representation.**
    - Positive integers and arithmetic
    - Hexadecimal
    - Two's complement
    - Floating point
    - ASCII, strings
    - Structured data (HTML, JSON)
2. **Logic Representation.**
    - Boolean logic
    - Logic gates
    - Logic circuits
    - Control circuits
    - Circuitverse simulations (or logic.ly?)
3. **Electronic Circuits.**
    - Resistors
    - Transistors
    - Building logic gates
    - Breadboard labs
4. **Assembly Programming.**
    - Assembly program structure
    - Global constants and variables
    - Printf and scanf
    - Automated testing
5. **Data Storage.**
    - Memory hierarchy
    - Cache and locality
    - Physical storage mechanisms
    - Redundancy, RAID
    - Memory interleaving, storage alignment
    - Erase before write, write endurance
    - MMIO
6. **Control Flow.**
    - Processor flags
    - Conditionals
    - Loops
    - Nested control flow
7. **Executing Instructions.**
    - Instruction cycle
    - Clock-driven execution
    - Instruction-level parallelism
    - Booting
8. **Stack Frames.**
    - Local variables
    - Functions
    - Context switching?
    - Recursion?
9. **Concurrency & Parallelism.**
    - User/kernel modes, system calls, traps, exceptions, interrupts
    - Concurrency
    - Multicore systems
    - Multiprocessing
    - Multithreading, hyperthreading
10. **Networking**
    - Network hardware
    - TCP/IP model
    - Security, encryption

Switch from `word` to `long`? Some weirdness around 64-bit comparisons on 32-bit values

Split out the FDEW quiz questions into smaller bits! "explain how fetch works" is too vague. Huge difference in detail between responses. What am I actually asking for?
- Explain what's happening on the data, instruction, and control buses during each step of FDEW
- What's happening in the ALU during each stage?
- Etc

Rewrite Pi setup. Encourage use of AI tools for debugging! This is a great use case because (1) it's the sort of thing that lots of nerds argue about in the training data, (2) correctness is easily testable, (3) unlikely to break anything. Also mention a few common issues

Update AI use policy in the syllabus

Get better ASCII table for tests (make sure null byte is visible)

Actually use `str` for local variables! In the current material we only ever use `scanf` to put data in memory

Add a slide with example two's complement subtraction

functions: add *recursion*. probably need to do functions after control flow then

talk about extra annotation in AP! do not wait until stack frames


# TODO - Tooling

Add `header.yaml` or similar. Handle it along with YAML headers in the markdown files. Start with the repo-level one, then course-level, then chapter-level. Ideally want to be able to have author and title info in there to be shared across files

Update exams to use markdown?

Figure out how to create tagged PDFs for accessibility


Pi setup -- ssh gen no longer does `id_rsa.pub`? It does a different type of key? might depend on if there is entropy in the system

circuitverse - clarify that the button is a different type of input
switch over to a different circuit simulator? logic.ly? 
add screenshots to help with testbench setup



Split warmups (Doenet) from assignments (PDF). Maybe get rid of Doenet entirely. Just have people check against their neighbors

Add makefile check to confirm that sections line up in the slides and the assignments

