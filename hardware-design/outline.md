# Data Representation
- Positive Integers
    - Decimal, binary, conversions, arithmetic, overflow, hex?
    - *BOARD WORK:* conversions and arithmetic
- Negative Integers
    - Two's complement, subtraction
    - *GROUP WORK:* conversions and arithmetic
- Non-Integer Data
    - Fixed point, floating point, precision vs magnitude, representation errors, cancellation of significance
    - *GROUP WORK:* representation of non-exact values, subtraction with formulas
    - ASCII and unicode, sound, color, images, video, HTML, JSON, Thrift
    - *GROUP WORK:* convert a string to ASCII to ones and zeroes
- Data transformation
    - Hashing, checksums, compression, space-time complexity tradeoff, lossy vs lossless, encryption
    - *GROUP WORK:*
## Logic Representation
- Truth tables
    - Boolean logic, operators
    - *GROUP WORK:* convert between boolean expressions, truth tables
- Logic circuits
    - Logic gates, functional completeness, multiple inputs/outputs
    - *GROUP WORK:*
- Math circuits
    - Addition, multiplication, comparison
    - *GROUP WORK:* truth table then circuit for two-bit multiplication
- Control circuits
    - Multiplexer, latch
    - *GROUP WORK:* truth table then circuit for a multiplexer
## Computer Architecture
- Intro: Von Neumann Architecture
    - CPU, ALU, registers, memory, busses, IO
    - *GROUP WORK:*
- Execution cycle
    - Fetch, decode, execute, write, clock-driven execution
    - *GROUP WORK:*
- Instruction-Level Parallelism
    - Pipelining, data hazard, register renaming, control hazard, branch prediction, eager execution, superpipelining, superscalar execution, VLIW, SIMD
    - *GROUP WORK:*
- Storage Hierarchy
    - Book storage hierarchy, caching, temporal locality, spatial locality, physical storage mechanisms
    - Latches / flip-flops. SRAM, cache, registers
    - Capacitors. Leaky. DRAM. Leaky. must be refreshed. Write by row (~kB)
    - Charge traps. SSDs. Write endurance. Write by page (~kB), erase by block (~MB)
    - Magnetic domains. HDD. Write by sector (~kB)
    - *GROUP WORK:*
- Performance & Resiliency
    - Prefetching, write-back caching, hardware compression, block-level deduplication, log-structured filesystem, memory interleaving, storage alignment
    - Cosmic rays, hardware failure, power failure, journaling, ECC, CRC, Hamming codes, checksums, copy on write, mirroring, RAID, XOR parity
    - *GROUP WORK:*
## Linux Shell
- VM setup?
- Shell commands?
- Piping?
- Conditionals and Loops?
## Assembly Programming
- Registers, variable sizes. Scratch vs callee-saved. PC? 
    - *GROUP WORK:*
- Basic operations... ADD, SUB, AND, MUL, LSL... this is pretty awkward to test
    - *GROUP WORK:*
- Loading and storing data
    - global variables
    - local variables
    - *GROUP WORK:*
- IO using printf and scanf
    - *GROUP WORK:*

- Assembly program structure (incl global variables)
- Basic commands (includes STR, LDR)
- IO using Printf and Scanf
- Automated Testing?

## Control Flow
- Comparison & Conditionals
- Loops
- Function Calls
- Local variables (incl stack frames)


## OS Concepts
- Booting, kernel, system calls
    - *GROUP WORK:*
- Process life cycle
    - *GROUP WORK:*
- Concurrency vs parallelism (generalize the idea of context switching)
    - *GROUP WORK:*
- Cores, processes, threads (and hyperthreading)
    - *GROUP WORK:* pthreads timing data
## Breadboards
- Resistors
    - Water analogy, series, parallel
    - *GROUP WORK:* breadboard! look at LED brightness
- Capacitors
    - Water analogy, low-pass filter, high-pass filter
    - *GROUP WORK:* breadboard! make filters
- Transistors
    - Water analogy, logic gates
    - *GROUP WORK:* breadboard! make logic gates
## Networking
- Network hardware
- Application Layer
- Transport Layer
- Internet Layer
- Link Layer
- Security (maybe mixed in)

