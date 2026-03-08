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

These all use the same mechanism. They trigger a handler in the kernel, which pauses the application so the OS can run the appropriate handler

Importantly: different platforms sometimes use different words! We will mostly use all these words interchangeably

% https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt
% https://pages.cs.wisc.edu/~gerald/cs537/Summer17/handouts/traps.pdf
% terminology is not consistent! 

## Process Management

### OS Responsibilities (Again)

- Launches and manages processes
- Handles scheduling of CPU resources
- That's a bit abstract. Can we be more concrete?



### Launching a Process




### Fork



### Process Life Cycle


### What Gets Tracked

For each process, the OS tracks:
- Process ID (PID): unique identifier for a process.
- Address space information
- Execution state (register values, stack location)
- Set of resources allocated to the process
- Current process state:
    - Ready: can run, but not currently scheduled
    - Running: scheduled on CPU, actively executing instructions
    - Blocked: waiting for event before can continue execution
    - Exited: done, but needs to be removed from system

### Address Space

- The OS keeps track of an **address space** for each process
- The process sees available memory as a contiguous block from 0x00000000 to 0xffffffff
- Physical location of that memory may be very different

$$$
\includegraphics[width=0.7\columnwidth]{images/os-concepts/address-space}
$$$

### Why??

- OS can move program data without causing problems
- Program data does not need to be contiguous
- One program cannot touch data belonging to another program
- Virtual memory. OS can pretend to have more memory than is physically present

### Multiprogramming

- Your web browser is an application
- VSCode is an application
- The part of your OS that draws the GUI is an application
- Whatever tracks mouse movement and draws the cursor too
- Only one of these can run on the CPU at a time
- Sure looks like all of them are running all the time

### Multiprogramming

$$$
\includegraphics[width=0.7\columnwidth]{images/os-concepts/multicore1}
$$$

### Taking Turns

There are a few different scheduling strategies:
- First In, First Out
- Round robin
- Shortest Job Next, Shortest Job Remaining. Sometimes with adjustments to prevent starvation
- Priority-based scheduling
- Multi-Level Feedback Queue (MLFQ). IO-limited vs CPU-limited applications




% memory-mapped IO
















% ## files and directories
% metadata: name, size, type, timestamp
% permissions
% directories
% journaling
% allocation. contiguous, linked, indexed

% ## parallelism
% multithreading
% multiprocessing
% concurrency, deadlock, race condition







## Parallelism






### Placeholder
$$$
\includegraphics[width=\columnwidth]{images/os-concepts/process-states}
$$$

### Placeholder
$$$
\includegraphics[width=\columnwidth]{images/os-concepts/starting-a-program}
$$$

### Placeholder
$$$
\includegraphics[width=\columnwidth]{images/os-concepts/xkcd-meltdown}
$$$









% meltdown attack




### Threads, Processes, and Cores





% multicore processors
% GPUs - fewer transistors, simpler instruction set
% memory wall - can't keep up with CPU speed increases
% power wall - can't dissipate heat fast enough
% threads. running on different cores, same memory
% wall time vs CPU time


% multithreading - one program using multiple cores. shared memory
% multiprocessing - different processes. possible to split one program into multiple processes (eg supercomputer weather models) but generally not. communication between processes is a lot of work
% hyperthreading - two cores per core. superscalar processing, context switching during idle times






% sleepy hello




