# Hardware Design (CSCI 241)

Taught by Prof Charles Fyfe (St Olaf College)

Adapted in part from materials by Prof Melissa Lynn (St Olaf College)

> TODO: check if ML wants an author credit on the slides

Course listing [here](https://catalog.stolaf.edu/academic-programs/computer-science)

## Repo Summary

- **code.** Source code for assignments. This includes benchmarking tools (eg `pthreads`) for exploring caching and ILP, as well as example code for Aarch64 exercises. Aarch64 is meant to be compiled on a 64-bit Raspberry Pi
- **doenet-assignments.**
- **exams.**
- **md2tex.** Script for converting Markdown files to LaTeX source. This is purely for convenience. Markdown is quicker to write and easier on the eyes
- **slides.**
- **syllabus.**

## Requirements

The syllabus, slides, and exams are typeset using LaTeX. LaTeX source is pretty ugly, so much of the content is written in Markdown then converted at build time. In order to produce PDFs you'll need:

- MikTex, MacTex, or similar. The big install
- Python 3
- Make
- Mistletoe (`pip3 install mistletoe`) - for converting Markdown to LaTeX
- Pyyaml (`pip3 install pyyaml`)
- Pygments (`pip3 install Pygments`) - for syntax highlighting via `minted`
- ARM syntax highlighting (`pip3 install pygments-arm`)

These requirements are for Mac OS. Linux is probably pretty much the same. If you need it to run on Windows, I'll bet an AI bot can figure it out

Circuit diagrams created using [this tool](https://www.circuit2tikz.tf.fau.de/designer/)

# TODO

For tests: explicitly say to turn in a SCAN not a PHOTO

Add a slide with example two's complement subtraction

Rewrite Pi setup. A few enumerated debugging tools. Also encourage use of AI tools for debugging! This is a great use case because (1) it's the sort of thing that lots of nerds argue about in the training data, (2) correctness is easily testable, (3) unlikely to break anything

Update AI use policy in the syllabus

Split warmups (Doenet) from assignments (PDF)

Update standards and calendar. Three tests with three standards each (plus overhead: pi setup, csgit setup)
1. **Data Representation.** Integers, hex, arithmetic, two's complement, floating point, ASCII, structured data
2. **Logic Representation.** Boolean logic, logic gates, logic circuits, control circuits, circuitverse simulations
3. **Assembly IO.** Global variables, global constants, printf, scanf, automated testing
4. **Electronic Circuits.** Resistors, transistors, breadboard labs
5. **Data Storage.** Memory hierarchy, caching, locality, physical storage mechanisms, redundancy, memory interleaving
6. **Control Flow.** Comparison, branching, if/else, loops
7. **The CPU.** Instruction cycle, clock-driven execution, instruction-level parallelization, booting(?)
8. **Stack Frames.** Local variables, functions, context switching
9. **OS Concepts.** Booting, user/kernel modes, system calls, traps/exceptions/interrupts, multithreading, multiprocessing, concurrency, hyperthreading

Build PDFs using GitHub actions? Then they can be readily accessed from the repo