beamer: true
template: slides.tex
---

# Storage

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
