# Hardware Design (CSCI 241)

Taught by Prof Charles Fyfe (St Olaf College)

Adapted in part from materials by Prof Melissa Lynn (St Olaf College)

> TODO: check if ML wants an author credit on the slides

Course listing [here](https://catalog.stolaf.edu/academic-programs/computer-science)

## Just The PDFs Please!

PDFs are built automatically using GitHub Actions. Check out the `Actions` tab up top. 

## Repo Summary

- **code.** Source code for assignments. This includes benchmarking tools (eg `pthreads`) for exploring caching and ILP, as well as example code for Aarch64 exercises. Aarch64 is meant to be compiled on a 64-bit Raspberry Pi
- **doenet-assignments.** Auto-graded warmups. Also includes prompts for circuitverse work, coding exercises, etc. Decent chance we should split the warmups from the "real" work (see TODOs at the bottom)
- **exams.**
- **md2tex.** Script for converting Markdown files to LaTeX source. This is purely for convenience. Markdown is quicker to write and easier on the eyes
- **slides.**
- **syllabus.**

## Building Locally

Typesetting is done via LaTeX. Source code for LaTeX is pretty ugly, so much of the content is written in Markdown and converted over at build time. If you want to run that process locally, you'll need:

- MikTex, MacTex, or similar. The big install
- Python 3, plus the packages in `requirements.txt`
- Make

These requirements are for Mac OS. Linux is probably pretty much the same. If you need it to run on Windows, I'll bet an AI bot can figure it out

Circuit diagrams created using [this tool](https://www.circuit2tikz.tf.fau.de/designer/)

# TODO

Update syllabus to use markdown. Maybe exams too

Figure out how to create tagged PDFs for accessibility

For tests: explicitly say to turn in a SCAN not a PHOTO

Add a slide with example two's complement subtraction

Pi setup -- ssh gen no longer does `id_rsa.pub`? It does a different type of key?

Add image flashing to coding setup

circuitverse - clarify that the button is a different type of input

Rewrite Pi setup. Encourage use of AI tools for debugging! This is a great use case because (1) it's the sort of thing that lots of nerds argue about in the training data, (2) correctness is easily testable, (3) unlikely to break anything. Also mention a few common issues:
- SSH setting didn't stick when the card was flashed
- Local network permissions (Mac)
- Internet sharing (Mac) (may require St Olaf Guest network)
- Get the IP address from network settings
- Pi may not be allowed on wifi

Update AI use policy in the syllabus

Get better ASCII table for tests (make sure null byte is visible)

Split warmups (Doenet) from assignments (PDF). Maybe get rid of Doenet entirely. Just have people check against their neighbors

Add makefile check to confirm that sections line up in the slides and the assignments

Update standards and calendar. Three tests with three standards each (plus overhead: pi setup, csgit setup)
1. **Data Representation.** Integers, hex, arithmetic, two's complement, floating point, ASCII, structured data
2. **Logic Representation.** Boolean logic, logic gates, logic circuits, control circuits, circuitverse simulations
3. **Assembly Programming.** Global variables, global constants, printf, scanf, automated testing
4. **Electronic Circuits.** Resistors, transistors, breadboard labs
5. **Data Storage.** Memory hierarchy, caching, locality, physical storage mechanisms, redundancy, memory interleaving, RAID, virtual memory, erase before write, MMIO, 4kB storage alignment, write endurance, memory-mapped IO
6. **Control Flow.** Comparison, branching, if/else, loops
7. **The CPU.** Instruction cycle, clock-driven execution, instruction-level parallelization
8. **Stack Frames.** Local variables, functions, context switching
9. **OS Concepts.** Booting, user/kernel modes, system calls, traps/exceptions/interrupts, multithreading, multiprocessing, concurrency, hyperthreading

Build PDFs using GitHub actions? Then they can be readily accessed from the repo