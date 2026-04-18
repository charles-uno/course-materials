beamer: true
---

# Instructions on Hardware

### Von Neumann Architecture

- What are the fundamental parts of a computer?
- How do they work together to execute instructions?

$$$
\includegraphics[width=\columnwidth]{images/von-neumann-architecture.png}
$$$

## Hardware Components

### What's Where?
$$$
\begin{center}
    \includegraphics[width=0.7\columnwidth]{images/pi-part-labels}
\end{center}
$$$

### CPU

Control unit drives execution.

- Instruction register (IR) holds the current instruction
- Program counter (PC) holds the address of the next instruction
- Clock management happens here too (more on this later)

Processing unit performs execution.

- ALU (arithmetic logic unit) does work
- General purpose registers store program data.


### CPU

It's all boolean logic!
$$$
\includegraphics[width=\columnwidth]{images/example-alu}
$$$


### CPU

It's all boolean logic!
$$$
\includegraphics[width=\columnwidth]{images/register-file}
$$$

### CPU

It's all boolean logic!
$$$
\includegraphics[width=\columnwidth]{images/full-cpu}
$$$

### Main Memory

Stores program data and instructions

Physical mechanism: little tiny capacitors holding electric charges

We'll talk more about storage later

% https://en.wikipedia.org/wiki/Flash_memory#NAND_flash

### Busses

- Address bus: what address in memory are we working with?
- Control bus: what are we doing with that address? Eg read or write
- Data bus: carries data between registers and memory

### Input and Output

- Input unit(s) load program data and instructions on the computer and initiate program execution.
- Output unit(s) store or receive program results.
- What are some examples of input/output hardware?


% ### Group Exercises
% TODO: this

## Executing an Instruction

### Execution Steps
There are four steps to executing an instruction:
- Fetch
- Decode
- Execute
- Write

### Fetch

$$$
\includegraphics[width=\columnwidth]{images/fdew-add-fetch}
$$$
- Special register PC holds the address of the instruction
- Read instruction from memory, store to IR
- Increment PC to point to the next instruction

### Decode

$$$
\begin{center}
    \includegraphics[width=0.7\columnwidth]{images/fdew-add-decode}
\end{center}
$$$
- The CPU breaks down the instruction bits from IR into its component parts
- Opcode is sent to the ALU, arguments to the registers
- Basically a bunch of multiplexers

### Walkthrough: Execute
$$$
\begin{center}
    \includegraphics[width=0.7\columnwidth]{images/fdew-add-execute}
\end{center}
$$$

- ALU performs the operation on the operands
- ALU outputs result and condition code values associated with the result value.

### Walkthrough: Write(back)
$$$
\begin{center}
    \includegraphics[width=0.7\columnwidth]{images/fdew-add-write}
\end{center}
$$$

- Result from ALU is stored in destination register

### Von Neumann Bottleneck

- Suppose you have an array of a billion integers in memory. You want to add 1 to each of them. How do you do it?

### Von Neumann Bottleneck

- Suppose you have an array of a billion integers in memory. You want to add 1 to each of them. How do you do it?
- You have to load each value from memory, store it in a register, run it through the CPU, and write it back to memory
- This is a lot of work!

% ### Group Exercises
% TODO: this

## Clock-Driven Execution

### Clock-Driven Execution

- Electrical signals move within the CPU, between CPU and memory, etc
- Different paths, different lengths, different amounts of time for signals to get where they're going
- How do we keep everything coordinated?

### What does a clock mean?

- The CPU has a clock
- Clock signal flips true/false at a very consistent rate
- Execution advances one step every tick of the clock
- System status in between ticks does not matter
- Physical mechanism: quartz. Electricity causes consistent predictable vibration

### Clock Speed

- 1 Hz (Hertz) = 1 cycle per second
- 1 kHz = 1,000 Hz = 1,000 cycles per second
- 1 MHz = 1,000,000 Hz = 1,000,000 cycles per second
- 1 GHz = 1,000,000,000 Hz = 1,000,000,000 cycles per second
- $10^9$ cycles per second means each cycle lasts $\frac{1}{10^9}$ seconds

### Why not just make the clock run faster?

- Electricity moves at approximately the speed of light
- Speed of light is about one foot per nanosecond
- If the computer runs at 1 GHz, that's one cycle every nanosecond
- Wires in the CPU are twisted and packed very tightly. How long do you suppose they would be if straightened?

% ### Group Exercises
% TODO: this

## Memory Hierarchy

### Size vs Speed

- How many books can you have in your hands at a time?
- How many books can you store on your bookshelf?
- How many books are there in the library?
- For each case, how accessible are those books?

### Book Storage Hierarchy
$$$
\includegraphics[width=\columnwidth]{images/memory-hierarchy-books.png}
$$$

### Books and Bytes

- Data works the same way
- Registers are super close to the CPU, but can only hold a few bytes of data
- Memory holds more, but you have to load it before you can use it
- Remote storage is even bigger and even slower

### Data Storage Hierarchy
$$$
\includegraphics[width=\columnwidth]{images/memory-hierarchy.png}
$$$

### Wait a Sec

- We fetch instructions from memory one at a time
- It takes ~100 CPU cycles to get data from memory
- Does that mean we spend 99\% of our time waiting??
- TLDR: the cache does a lot of work here

### Primary Storage

- Primary storage can be accessed directly by the CPU
- Registers, cache, main memory
- Physical mechanism: SRAM (static RAM). Data is stored in electric circuits, such as latches. Fastest type of storage. Used for registers
- Another physical mechanism: DRAM (dynamic RAM). Data is stored in capacitors holding electric charge. Slower, cheaper, denser. Used for main memory

### Secondary Storage

- Secondary storage must be copied into primary storage before it can be accessed
- HDD (hard disk drives). Magnetic storage on a spinning circular platter. Read/write arm hovers just a few atoms away from the disk surface. Moving pieces. Ask your parents if you want to make them feel old.
- SSD (solid state drives). No moving parts. Thousands of transistors chained together.
- Remote storage. Physical mechanism doesn't matter much since latency and transfer rate are due to the network

### Quantifying Storage

- Latency: how long to get data (measured in nanoseconds)
- Capacity: how much data (measured in bytes)
- Transfer rate (aka throughput): how fast we can read or write (measured in bytes/second)

% ### Group Exercises
% TODO: this

## Locality \& Cache

### Wait -- what's a cache?

- Cache is in between registers and main memory (in every way)
- Physically closer to the ALU than memory, but not as close as the registers
- Stores more data than the registers, but not as much as memory
- Why might this be useful?

### Temporal Locality

- When you load a value from memory, there's a decent chance you'll use that same value again soon
- The computer stores that value in the cache
- When you try to load the value next time, the cache intercepts your request and returns the data much faster
- This is called temporal locality (similar in time)

### Spatial Locality

- When you load one value from an array, there's a decent chance you'll be back for the rest soon
- The computer stores "nearby" data in the cache
- When you try to load that data from memory, the cache intercepts your request and returns the data much faster
- This is called spatial locality (similar in space)

### Hits and Misses

- Cache hit: you try to load data from memory. It's already in the cache! You get your data faster that you expected
- Cache miss: you try to load data from memory. It's not in the cache. You have to wait for the data to be loaded from memory (about 10x slower)

### Cache Eviction

- Caches hold only a small amount of data compared to memory
- If the computer wants to store something in the cache, but the cache is full, existing data has to be deleted to make room
- This is called a cache eviction

### Caching Applications

- The cache is a hardware component in between the CPU and main memory
- Caches can also be implemented in software!
- For example: your browser caches images from websites you visit. If you visit the same site later, the browser can find the image locally. This is much faster than pulling it across the network

### Caching in Software

You can even use the idea of a cache within your code!

What happens here if you call `fibonacci(1000)`?
```python
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-1) + fibonacci(n-2)
```

### Caching in Software

How about now?
```python
CACHE = {}

def fibonacci(n):
	if n not in CACHE:
		if n < 2:
			CACHE[n] = n
		else:
			CACHE[n] = fibonacci(n-1) + fibonacci(n-2)
	return CACHE[n]
```

% ### Group Exercises
% TODO: this

## Instruction-Level Parallelism

% out of order execution

% very large instruction word

% SIMD

% superscalar execution


### Remember Execution Steps

- Fetch
- Decode
- Execute
- Write

Which of these stages do actual work? Which are overhead?


### Time is Money
$$$
\includegraphics[width=\columnwidth]{images/fdew-before-pipelining}
$$$

- The execute step is the only step that uses the CPU. The rest are just moving values around
- That means the CPU is sitting idle 75\% of the time at least!
- Is there any way to be more efficient?

### Pipelining

- After the fetch stage is done for an instruction, its circuitry doesn't do anything until the next instruction starts
- Same for decode
- What if we start the next instruction as soon as the circuitry is available?

### Behold the Pipeline
$$$
\begin{center}
    %	\includegraphics[\columnwidth]{images/pipelining}
    \includegraphics[width=0.6\columnwidth]{images/pipelining-wiki}
\end{center}
$$$

### Please explain that busy diagram

1. Fetch instruction 1
2. Decode instruction 1, fetch instruction 2
3. Execute instruction 1, decode instruction 2, fetch instruction 3
4. Write instruction 1, execute instruction 2, decode instruction 3, fetch instruction 4
5. Done with instruction 1, write instruction 2, execute instruction 3, decode instruction 4, fetch instruction 5
6. Etc

### Pipelining Upsides

- Code runs faster
- One instruction takes 4 cycles (same as before)
- Two pipelined instructions take 5 cycles (previously: 8)
- Three pipelined instructions take 6 cycles (previously: 12)
- This is a pretty big improvement


% Instructions are cached. Often a bunch of them are pre-loaded into the cache as the program starts
% Typical numbers:
% L1 cache access is 1-4 CPU cycles
% L1 cache can hold thousands of instructions


### Pipelining Downsides

Can you think of any downsides of pipelining?

Hint: we will be using the terms "data hazard" and "control hazard"

### Hazards

- Data hazard: we want to do two steps simultaneously, but we can't because they want to touch the same register
- Control hazard: we don't know what instruction to fetch next because it depends on the result of the result of an instruction that's still running

### Data Hazards

```python
x = y + 5
z = x + 7
```
Do you see the problem?

### Data Hazards
```python
x = y + 5
z = x + 7
```

- Instruction 1 is writing data to `x` (write stage)
- Instruction 2 is reading data from `x` (execute stage)
- Those stages are supposed to happen at the same time
- Race condition. Different outcome based on which happens first
- Not good
- What can we do?

### Mitigating Data Hazards

- Out of order execution (OoO). Sometimes `gcc` can figure out a way to reorder the instructions to avoid the hazard
- Operand forwarding. Pass the value right back into the CPU to avoid the dangerous register read
- Pipeling stall. Add a "bubble" to the pipeline. Wait until the operation is safe

### Pipelining with a Bubble
$$$
\includegraphics[width=0.66\columnwidth]{images/pipelining-wiki-with-bubble}
$$$

### Control Hazards
```python
if r1 == 0:
    fizz()
else:
    buzz()
```
Which instruction should we load into the pipeline after the `if`?

### Mitigating Control Hazards

- Pipeling stall. Add a "bubble" to the pipeline. Wait until we know the result of the conditional
- Branch prediction. Guess. If we guess wrong, go back and do it right
- Eager execution. Try them both. Once we get the result, throw away the moot one

### Eager Execution Gone Wrong
$$$
\includegraphics[width=\columnwidth]{images/xkcd-meltdown-cropped.png}
$$$
Source: xkcd

### Additional ILP Strategies

Pipelining is an important way to accomplish instruction-level parallelism (aka executing more than one instruction at a time)

There are other ways too

### Superscalar Processing

The ALU contains circuitry to do a bunch of different operations. We use multiplexers to keep the results we want

$$$
\includegraphics[width=\columnwidth]{images/example-alu}
$$$

### Superscalar Processing

What if, as we're running a program, we see that our next two instructions use all different circuitry?

### Superscalar Processing

If two consecutive instructions use all different circuitry, we can run them at the same time

% in principle, we expect this to work for different instructions
% in practice, ALUs contain duplicate logic for common operations

It's like flipping burgers with one hand and slicing tomatoes with the other

What are some upsides and downsides of this approach?

### Superscalar Pros and Cons

Pro: your code runs faster!

Con: it takes a lot of logic to figure out which instructions can be run together. And this needs to happen at the hardware level. If you spend a CPU cycle figuring it out, you're not gaining anything

### Very Long Instruction Word

- Superscalar Processing seems pretty slick, but it's also a lot of work for the processor
- You need extra circuitry to figure out when it's safe to run instructions together
- What if we pushed that responsibility up to the compiler?

### Very Long Instruction Word

- Programming language specifies bundles of instructions that are safe to run together
- The compiler can guarantee correctness
- No extra logic in the ALU
- Just need to be able to fetch and store multiple instructions at a time

### Single Instruction, Multiple Data

Another common use case: what if we want to do the same thing to multiple pieces of data?

- Load two adjacent values from memory
- Store two registers to adjacent memory addresses
- Addition on multiple values

### Single Instruction, Multiple Data

SIMD is a big part of what makes GPUs work!

A very fancy CPU might be able to pass 512 bits through its ALU at a time (16 32-bit numbers)

A GPU can have hundreds of ALU "lanes" which all execute instructions based on a single fetch and decode


### Simultaneous Multi-Threading

- AKA hyperthreading, the proprietary Intel term
- Just tell the CPU to pretend that it is two CPUs
- When one thread is idle (eg waiting for data from memory) it switches to the other one
- When switching between threads, all register values are moved to the cache

### Instruction-Level Parallelism Wrapup

Modern systems generally use a combination of ILP strategies:

- Pipelining: fetch the next instruction while this one is decoding
- OoO Execution: reorder instructions to avoid stalling the pipeline
- Superscalar processing: processor dynamically identifies instructions that are safe to run together (requires specific hardware)
- VLIW: compiler identifies batches of instructions that are safe to run together
- SIMD: one fetch+decode for multiple simultaneous execute+write
- SMT: the CPU runs two "hyperthreads". Switches between them when the active one is idle

% ### Group Exercises
% TODO: this

% EPIC: explicitly parallel instruction computing. like the next level past VLIW?

% memory-mapped IO


% register spilling. ILP means we want to have as many registers active at a time as possible. more independent things to parallelize. but eventually we run out of registers. when that happens, we have to "spill" values to memory. we load those values back later when we need them. in many cases, the values will get cached and we never actually hit main memory. if we do have to go to memory we'll take a performance hit

% stack and heap. both are ostensibly in memory. stack is generally small enough and contiguous enough that it lives in the cache