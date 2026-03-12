beamer: true
---

# OS Concepts

### OS Concepts

- We have talked about executing instructions as part of a program
- How do we boot the machine so we can run the program in the first place?
- And how does the machine handle background stuff while the program runs?

### First Things First

The operating system is special software sits between applications and hardware (and allows them to communicate with one another)

$$$
\includegraphics[width=\columnwidth]{images/os-concepts/os-location}
$$$

### What does the OS do?

Big picture:

- The OS launches applications. Loads instructions, initializes CPU
- The OS manages applications while they run. Scheduling, cleanup
- The OS allows applications to access hardware. SSD, mouse, keyboard, network, etc
- The OS also usually provides a GUI (graphical user interface)

## Booting

### Booting

The operating system is responsible for launching programs. Loading instructions into memory, initializing the CPU

But the OS is itself a program! How does it launch itself?

### Put Another Way

- After we run each instruction in a program, we fetch the next instruction from memory
- Sometimes it's the next instruction
- Sometimes we jump to another part of the program
- When we turn on the computer, how do we know where to start?

### Firmware and the Boot Loader

The operating system loads and initializes itself through a process called booting. When a computer is turned on:

- It starts running instructions from a hard-coded address (often 0x00000000)
- This is non-volatile memory, aka firmware
- First stage boot loader: BIOS, UEFI, etc. Initializes CPU, memory, IO
- Second stage boot loader: GRUB, BOOTMGR, etc. Loads the first chunk of the OS
- From there the OS loads the rest of itself and initializes data structures and abstractions

### Don't @ Me

The boot loader is not technically part of the OS. But it's doing similar work:
- Interfacing with hardware
- Loading process instructions to memory
- Initializing the CPU

% ### Summary
% TODO: this

% ### Exercises
% TODO: this

## The OS Kernel

### What does the OS do?

- The visible part of the OS is the graphical user interface (GUI)
- We are more interested in what's happening under the hood
- Launching and managing applications
- Interfacing with hardware
- That's all managed by the OS **kernel**

### What Does the Kernel Do?

To be a bit more specific:

- When launching a program, the kernel loads the instructions into memory and initializes the CPU
- The kernel allocates CPU time between processes
- It cleans up after processes that finish or misbehave
- It provides interfaces for programs to access hardware (eg files access, keyboard input)
- The kernel enforces policies for which processes are allowed to access what

### Kernel Responsibilities

Yes:
- Reading a file from disk as binary
- Enforcing which processes have access to which memory addresses
- Receiving keystrokes from the keyboard
- Sending and receiving network traffic

No:
- Turning binary data into documents, images, videos, etc
- User accounts and passwords
- Keyboard shortcuts, entering text in forms
- Interpreting data from the network as HTML, messages, etc

### Computers are like onions. They have layers

$$$
\includegraphics[width=\columnwidth]{images/os-concepts/device-drivers}
$$$

### System Calls

- The kernel is allowed to write data to disk
- *Only* the kernel is allowed to write data to disk
- User applications are *not* allowed to write data to disk
- Whenever an application wants to write to disk, it has to delegate that action to the kernel
- It does so by making a **system call**

### Interrupt-Driven Systems

- The OS is idle until a system call "wakes it up"
- The CPU stops running the application and switches over to the system call handler
- System calls are just one type of **vectored event**

$$$
\includegraphics[width=\columnwidth]{images/os-concepts/call-to-os}
$$$

### Vectored Events

**Interrupt:** signal from an external device (eg mouse, keyboard)

**Exception:** signal from the application
- **Trap:** The program can resume after the instruction that triggered it. Eg divide by zero, system calls
- **Fault:** The program can reattempt the instruction that triggered it. Eg page fault
- **Abort:** Unable to pinpoint the failure. Not recoverable. Eg: hardware failures, corrupted data

Different platforms use different words. These all use the same mechanism

% https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt
% https://pages.cs.wisc.edu/~gerald/cs537/Summer17/handouts/traps.pdf
% terminology is not consistent! 

### Pausing and Resuming an Application

What happens to the running process when the kernel takes over?

- Save context from the current process: registers (including special registers), memory state
- Loads context for the other process (the interrupt handler)
- This is called **context switching**

## Managing a Process

### OS Responsibilities (Again)

- Launches and manages processes
- Handles scheduling of CPU resources
- That's a bit abstract. Can we be more concrete?

### Process Launch Process

Initiating program execution:
- OS assigns the process a PID (process ID)
- OS allocates part of RAM for running the program
- OS loads program from disk to RAM
- OS allocates an address space for the process
- OS initializes CPU to start running program instructions

### Launching a Process
$$$
\includegraphics[width=\columnwidth]{images/os-concepts/starting-a-program}
$$$

### Address Space

- The OS keeps track of an address space for each process
- The process sees available memory as a contiguous block from 0x00000000 to 0xffffffff
- Physical location of that memory may be very different

$$$
\includegraphics[width=0.7\columnwidth]{images/os-concepts/address-space}
$$$

### Address Spaces -- Why??

- OS can move program data without causing problems
- Program data does not need to be contiguous
- One program cannot touch data belonging to another program
- Virtual memory. OS can pretend to have more memory than is physically present

### Forking

Processes can create additional processes (called children). 

% For example: running a command in the terminal in VSCode

$$$
\begin{center}
\includegraphics[width=0.5\columnwidth]{images/os-concepts/forks}
\end{center}
$$$

### Process Life Cycle

$$$
\includegraphics[width=\columnwidth]{images/os-concepts/process-states}
$$$

### Process Life Cycle

- OS keeps track of process status
- Exited processes get cleaned up
- Blocked processes get sidelined (aka we use context switching to let the CPU work on something else)

## Multiprogramming

### Multiple Programs

- Your web browser is an application
- VSCode is an application
- The part of your OS that draws the GUI is an application
- Whatever tracks mouse movement and draws the cursor too
- Only one of these can run on the CPU at a time
- Sure *looks* like all of them are running all the time

### Multiple Programs

In fact, just run `top` (on Mac or Linux)

### Multiple Programs

- The OS can put a process on hold to step in and handle interrupts
- It can also put a process on hold to give another process time on the CPU
- It does so constantly!

### Taking Turns

- OS decides how long the current process is allowed to run
- OS decides which process gets the next turn
- OS handles context switching
- OS cleans up processes that finish/crash

### Taking Turns

There are a few different scheduling strategies:

- First In, First Out
- Round robin
- Shortest Job Next, Shortest Job Remaining. Sometimes with adjustments to prevent starvation
- Priority-based scheduling
- Multi-Level Feedback Queue (MLFQ). IO-limited vs CPU-limited applications

### AKA Concurrency

- The OS switches back and forth between processes many times per second
- To a human user, it looks like the CPU is doing many things at once

### AKA Concurrency

$$$
\includegraphics[width=\columnwidth]{images/os-concepts/multicore1}
$$$

## Parallelism

### Concurrent vs Parallel

- Multiprogramming (aka concurrency) is when multiple processes take turns on the CPU. This gives the *appearance* that multiple things are happening simultaneously
- Parallelism is when we actually *do* multiple things simultaneously

### Concurrent vs Parallel

$$$
\includegraphics[width=0.5\columnwidth]{images/os-concepts/multicore1}
$$$

$$$
\includegraphics[width=0.5\columnwidth]{images/os-concepts/multicore2}
$$$

### Why Parallelism?

We can do multiple things on a single CPU. Why add more?

### Multicore Processors

Barriers to improvements of processor speed:

- Memory wall: memory access speeds can't keep pace with CPU speed
- Power wall: more transistors on a processor increases temperature and power use

Instead adding more transistors to a single CPU increase speed of processor, add more compute cores to CPU (simpler, fewer transistors).

### Parallel Terminology: Core

- A **core** is a complete unit (ALU, registers, cache) within the CPU
- Modern CPUs typically have multiple cores
- High-performance machines may have *many* cores
- Multiple cores allow the computer to run instructions on multiple ALUs at the same time

### Parallel Terminology: Threads

A process may break itself up into multiple **threads** to take advantage of multiple cores. For example:

- Word processor: one thread for showing updates, one for spell check, etc
- Browser: manage multiple downloads at the same time
- Media players: playback is one thread, search/UI is another

### Parallel Terminology: Process

We previously talked about each application as its own **process**. Sometimes an application delgates work to additional child processes:

- Chrome runs each tab as a child process
- Running a command in the VSCode terminal spawns a new child process
- Coordination between sibling processes is tricky since they may run at different speeds

### Process vs Thread

An application may be broken into multiple threads and/or multiple processes. So what's the difference?

- Threads are fast and efficient. They use the same address space in memory. They have access to the same variables (sorta). Switching context between threads is easy
- Processes are safe and isolated. If one process crashes or becomes compromised, its siblings are not affected
- Processes can be split across multiple CPUs (unlike threads). Example: *big* weather models running on a supercomputer. Multiprocessing across CPUs, then multithreading within each CPU

### Processes and Threads

Also worth noting: parallelism within an application is coded in explicitly! The OS (usually) does not figure it out on the fly. 

### More Parallelism, More Problems

Sometimes threads and processes can step on each others' toes:

- Data corruption. One thread/process is reading a file while another is modifying it
- Deadlock. Two processes, each waiting for the other to release a locked resource
- Race conditions. Two threads both set `x = x + 1` at the same time

% GPUs -- we talked about these for instruction-level parallelism




% ## files and directories
% metadata: name, size, type, timestamp
% permissions
% directories
% journaling
% allocation. contiguous, linked, indexed


% meltdown attack

% sleepy hello

