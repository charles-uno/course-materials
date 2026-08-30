
Data Representation
- Positive Integers
    - Positive Integers in Decimal
    - Positive Integers in Binary
    - Converting from Decimal to Binary
    - Converting from Binary to Decimal
    - Addition in Binary
    - Multiplication in Binary (note: no division)
    - Overflow
- Negative Integers
    - Two's Complement
    - Subtraction in Binary
    - Side Note: Hexadecimal
    - Converting Between Binary and Hexadecimal
    - **BOARD WORK:** conversions and arithmetic
- Non-Integer Data
    - Fixed point vs floating point
    - Breaking down the standard
    - Precision vs magnitude
    - Representation errors (0.1 + 0.2 = ...)
    - Cancellation of significance
    - **BOARD WORK:** representation of non-exact values, subtraction with formulas
    - ASCII and unicode
    - Sound, color, images, video
    - HTML, JSON
    - Thrift
    - **BOARD WORK:** convert a string to ASCII to ones and zeroes
- Data transformation
    - Hashing
    - Checksums
    - Compression
    - Space-time complexity tradeoff
    - LLMs are good at compressing! Their whole deal is finding patterns
    - Lossy vs lossless
    - Encryption
    - **BOARD WORK:**
Logic Representation
- Truth tables
    - Boolean logic
    - Boolean operators
    - **BOARD WORK:** convert between boolean expressions, truth tables
- Logic circuits
    - Logic gates
    - Functional completeness
    - Multiple inputs/outputs
    - **BOARD WORK:**
- Math circuits
    - Addition
    - Multiplication
    - Comparison
    - **BOARD WORK:** truth table then circuit for two-bit multiplication
- Control circuits
    - Multiplexer
    - Latch
    - **BOARD WORK:** truth table then circuit for a multiplexer
Electronic Circuits
- Resistors
    - Water analogy
    - Series
    - Parallel
    - **BOARD WORK:** breadboard! look at LED brightness
- Capacitors
    - Water analogy
    - Low-pass filter
    - High-pass filter
    - **BOARD WORK:** breadboard! make filters
- Transistors
    - Water analogy
    - Logic gates
    - **BOARD WORK:** breadboard! make logic gates
Linux Shell
- VM setup?
    - **BOARD WORK:**
- Shell commands?
    - **BOARD WORK:**
- Piping?
    - **BOARD WORK:**
- Conditionals and Loops?
    - **BOARD WORK:**
Assembly Programming
- Registers, variable sizes. Scratch vs callee-saved. PC? 
    - **BOARD WORK:**
- Basic operations... ADD, SUB, AND, MUL, LSL... this is pretty awkward to test
    - **BOARD WORK:**
- Loading and storing data
    - **BOARD WORK:**
- IO using printf and scanf
    - **BOARD WORK:**

NOTE: do we want to pull control flow in here? If we can get away with it, then yes. let students use AI. writing this code by hand manually is pretty rough. give them more time to play. Might be a bit much. Alternatively, we could do functions and conditionals together? they are both control flow. then local variables go with AP





Instruction Cycles
- Von Neumann Architecture
    - CPU
    - ALU
    - Registers
    - Memory
    - Busses
    - IO
    - **BOARD WORK:**
- Execution cycle
    - Fetch
    - Decode
    - Execute
    - Write
    - Clock-driven execution
    - **BOARD WORK:**
- Pipelining and hazards
    - Data hazard
    - Register renaming
    - Control hazard
    - Branch prediction
    - Eager execution
    - Superpipelining. 15+ stages, not just the 4 from the textbook
    - **BOARD WORK:**
- Instruction-level parallelism
    - Superscalar execution
    - VLIW
    - SIMD
    - **BOARD WORK:**
- Storage Hierarchy
    - Book storage hierarchy
    - Caching
    - Temporal locality, spatial locality
    - **BOARD WORK:**
- Physical storage mechanisms
    - Latches / flip-flops. SRAM, cache, registers
    - Capacitors. Leaky. DRAM. Leaky. must be refreshed. Write by row (~kB)
    - Charge traps. SSDs. Write endurance. Write by page (~kB), erase by block (~MB)
    - Magnetic domains. HDD. Write by sector (~kB)
    - **BOARD WORK:**
- Performance
    - Prefetching
    - Write-back caching
    - Hardware compression
    - Block-level deduplication
    - Log-structured filesystem
    - memory interleaving
    - storage alignment
    - **BOARD WORK:**
- Resiliency
    - Cosmic rays, hardware failure, power failure
    - Journaling
    - ECC, CRC. Hamming codes, checksums
    - Copy on write. Never overwrite. do a new write and move the pointer
    - Mirroring, RAID, XOR parity
    - **BOARD WORK:**
Control Flow
- Conditionals
    - this is a whole day
    - **BOARD WORK:** identify lowercase letters
- Loops
    - this is a whole day
    - **BOARD WORK:**
Parallelism & Concurrency
- Booting, kernel, system calls
    - **BOARD WORK:**
- Process life cycle
    - **BOARD WORK:**
- Concurrency vs parallelism (generalize the idea of context switching)
    - **BOARD WORK:**
- Cores, processes, threads (and hyperthreading)
    - **BOARD WORK:** pthreads timing data
Stack Frames
- Stack and heap
    - **BOARD WORK:**
- Local variables
    - **BOARD WORK:**
- Function calls. BL, LR
    - **BOARD WORK:**
- Recursion
    - **BOARD WORK:**
Networking
- Network hardware
- Application Layer
- Transport Layer
- Internet Layer
- Link Layer
- Security (maybe mixed in)














Data Representation
- Positive Integers
- Negative Integers
- Non-Integer Data
- Data Transformation
Logic Representation
- Truth tables
- Logic circuits
- Math circuits
- Control circuits
Electronic Circuits
- Resistors
- Capacitors
- Transistors
Computer Architecture
- Von Neumann Architecture
- Execution cycle
- Pipelining and hazards, ILP
- Storage hierarchy, physical mechanisms, caching
- Performance & resiliency


Linux Shell
- VM setup?
- Shell commands?
- Piping?
- Conditionals and Loops?
Assembly Programming
- Basic operations
- Loading and storing data, global and local variables... stack vs heap?
- IO using printf and scanf
- Conditionals & loops
Parallelism & Concurrency
- Booting, kernel, system calls
- Process life cycle
- Concurrency vs parallelism (generalize the idea of context switching)
- Cores, processes, threads (and hyperthreading)
Networking
- Network hardware
- Application Layer
- Transport Layer
- Internet Layer
- Link Layer
- Security (maybe mixed in)

