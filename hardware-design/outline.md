Data Representation
- Positive Integers
    - Decimal, binary, conversions, arithmetic, overflow, hex?
    - **BOARD WORK:** conversions and arithmetic
- Negative Integers
    - Two's complement, subtraction
    - **BOARD WORK:** conversions and arithmetic
- Non-Integer Data
    - Fixed point, floating point, precision vs magnitude, representation errors, cancellation of significance
    - **BOARD WORK:** representation of non-exact values, subtraction with formulas
    - ASCII and unicode, sound, color, images, video, HTML, JSON, Thrift
    - **BOARD WORK:** convert a string to ASCII to ones and zeroes
- Data transformation
    - Hashing, checksums, compression, space-time complexity tradeoff, lossy vs lossless, encryption
    - **BOARD WORK:**
Logic Representation
- Truth tables
    - Boolean logic, operators
    - **BOARD WORK:** convert between boolean expressions, truth tables
- Logic circuits
    - Logic gates, functional completeness, multiple inputs/outputs
    - **BOARD WORK:**
- Math circuits
    - Addition, multiplication, comparison
    - **BOARD WORK:** truth table then circuit for two-bit multiplication
- Control circuits
    - Multiplexer, latch
    - **BOARD WORK:** truth table then circuit for a multiplexer
Computer Architecture
- Intro: Von Neumann Architecture
    - CPU, ALU, registers, memory, busses, IO
    - **BOARD WORK:**
- Execution cycle
    - Fetch, decode, execute, write, clock-driven execution
    - **BOARD WORK:**
- Instruction-Level Parallelism
    - Pipelining, data hazard, register renaming, control hazard, branch prediction, eager execution, superpipelining, superscalar execution, VLIW, SIMD
    - **BOARD WORK:**
- Storage Hierarchy
    - Book storage hierarchy, caching, temporal locality, spatial locality, physical storage mechanisms
    - Latches / flip-flops. SRAM, cache, registers
    - Capacitors. Leaky. DRAM. Leaky. must be refreshed. Write by row (~kB)
    - Charge traps. SSDs. Write endurance. Write by page (~kB), erase by block (~MB)
    - Magnetic domains. HDD. Write by sector (~kB)
    - **BOARD WORK:**
- Performance & Resiliency
    - Prefetching, write-back caching, hardware compression, block-level deduplication, log-structured filesystem, memory interleaving, storage alignment
    - Cosmic rays, hardware failure, power failure, journaling, ECC, CRC, Hamming codes, checksums, copy on write, mirroring, RAID, XOR parity
    - **BOARD WORK:**
Linux Shell
- VM setup?
- Shell commands?
- Piping?
- Conditionals and Loops?
Assembly Programming
- Registers, variable sizes. Scratch vs callee-saved. PC? 
    - **BOARD WORK:**
- Basic operations... ADD, SUB, AND, MUL, LSL... this is pretty awkward to test
    - **BOARD WORK:**
- Loading and storing data
    - **BOARD WORK:**
- IO using printf and scanf
    - **BOARD WORK:**
Control Flow
- Local variables
- Function calls (recursion?)
- Conditionals
- Loops
OS Concepts
- Booting, kernel, system calls
    - **BOARD WORK:**
- Process life cycle
    - **BOARD WORK:**
- Concurrency vs parallelism (generalize the idea of context switching)
    - **BOARD WORK:**
- Cores, processes, threads (and hyperthreading)
    - **BOARD WORK:** pthreads timing data
Breadboards
- Resistors
    - Water analogy, series, parallel
    - **BOARD WORK:** breadboard! look at LED brightness
- Capacitors
    - Water analogy, low-pass filter, high-pass filter
    - **BOARD WORK:** breadboard! make filters
- Transistors
    - Water analogy, logic gates
    - **BOARD WORK:** breadboard! make logic gates
Networking
- Network hardware
- Application Layer
- Transport Layer
- Internet Layer
- Link Layer
- Security (maybe mixed in)

