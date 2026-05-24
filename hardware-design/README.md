# Hardware Design (CSCI 241)

Course materials by Charles Fyfe. Adapted in part from materials by Melissa Lynn

Course listing [here](https://catalog.stolaf.edu/academic-programs/computer-science)

## Just The PDFs Please!

PDFs are built automatically using GitHub Actions. Check out the `Actions` tab up top. 

## Repo Summary

Heads up! Stuff is moving around right now. 

- `chapters` - This holds most of the actual content! Each chapter contains slides, homework, and a quiz
- `build` - Templates and scripts for building our Markdown source files into PDFs via LaTeX
- `syllabus` - The syllabus
- `project` - Document explaining the final project for the course
- `final` - The final exam. Also some tooling to generate personalized exams for each student based on what they need to reattempt

## Building Locally

Typesetting is done via LaTeX. Source code for LaTeX is pretty ugly, so much of the content is written in Markdown and converted over at build time. If you want to run that process locally, you'll need:

- MikTex, MacTex, or similar. The big install
- Python 3, plus the packages in `build/requirements.txt`
- Make

These requirements are for Mac OS. Linux is probably pretty much the same. If you need it to run on Windows, I'll bet an AI bot can figure it out

Circuit diagrams created using [this tool](https://www.circuit2tikz.tf.fau.de/designer/)

# TODO - Curriculum

Add dedicated DISCUSSION slides. not just a question in the middle of a list

Add BOARD WORK slides. Ideally one per section. Dedicated group work

- Data representation:
    - Converting positive integers between hex, binary, and decimal
    - Negation and arithmetic with two's complement
    - Floating point numbers (conceptual? math?)
    - ASCII and structured data (conceptual? math?)
- Logic Representation:
    - Converting between truth tables, logical expressions, and logic circuits
    - Building logic gates from transistors
    - Control circuits (conceptual?)
- Assembly Programming:
    - global constants and variables
    - basic instructions
    - Printf, scanf
- ...
- Networking
    - hardware
    - application layer
    - transport layer
    - internet layer
    - link layer
    - security

Update standards:

0. **Shell Scripting.** Shell command basics, shell control flow (conditionals, loops, functions), raspberry pi setup, csgit setup
1. **Data Representation.** Positive integers, arithmetic, hexadecimal, two's complement, floating point, ASCII, strings, structured data (HTML, JSON), compression, encryption
2. **Logic Representation.** Boolean logic, logic gates, logic circuits, control circuits, circuitverse simulations (or logic.ly?)
3. **Electronic Circuits.** resistors, transistors, building logic gates, breadboard labs -- not sure if this is its own section or if we should bundle it in with logic circuits
4. **Assembly Programming.** Assembly program structure, global constants and variables, printf and scanf, automated testing
5. **Data Storage.** Memory hierarchy, cache and locality, physical storage mechanisms, redundancy, RAID, memory interleaving, storage alignment, erase before write, write endurance, MMIO
6. **Control Flow.** Processor flags, conditionals, loops, nested control flow
7. **Executing Instructions.** Instruction cycle, clock-driven execution, instruction-level parallelism, booting
8. **Stack Frames.** Stack vs heap, local variables, functions, recursion
9. **Concurrency & Parallelism.** User/kernel modes, system calls, traps, exceptions, interrupts, context switching, concurrency, multicore systems, multiprocessing, multithreading, hyperthreading
10. **Networking.** Network hardware, TCP/IP model, security, encryption

Switch from `word` to `long`? Some weirdness around 64-bit comparisons on 32-bit values

circuitverse - clarify that the button is a different type of input
switch over to a different circuit simulator? logic.ly? 
add screenshots to help with testbench setup

# TODO - Repo

md2tex pending updates:
- handle links that start within a word, eg parentheses
- handle block quotes
- make sure we handle inline comments correctly

Add `header.yaml` or similar. Handle it along with YAML headers in the markdown files. Start with the repo-level one, then course-level, then chapter-level. Ideally want to be able to have author and title info in there to be shared across files

Figure out how to create tagged PDFs for accessibility


