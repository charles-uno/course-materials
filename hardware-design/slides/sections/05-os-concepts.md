beamer: true
---

# OS Concepts

### OS Concepts

- We have talked about executing instructions as part of a program
- How do we boot the machine so we can run the program in the first place?
- And how does the machine handle background stuff while the program runs?

## The OS Kernel

### The Operating System

First things first:

"OS" stands for "Operating System"

The OS is special software sits between applications and hardware (and allows them to communicate with one another)

$$$
\includegraphics[width=\columnwidth]{images/os-concepts/os-location}
$$$

### What does the OS do?

Big picture:

- The OS provides abstractions for applications to access hardware
- The OS manages hardware resources
- The OS also usually provides a GUI (graphical user interface)

In this course we are concerned with the OS **kernel** (not the GUI)

### The OS Kernel

Breaking it down a level further:

- When launching a program, the kernel loads the instructions into memory and initializes the CPU
- The kernel balances CPU time between processes
- It cleans up after processes that misbehave
- The kernel provides interfaces for programs to access hardware (eg read files)
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

### Process Hierarchy

$$$
\includegraphics[width=\columnwidth]{images/os-concepts/device-drivers}
$$$

### System Calls

- The kernel is allowed to write data to disk
- *Only* the kernel is allowed to write data to disk
- User applications are *not* allowed to write data to disk
- Whenever an application wants to write to disk, it makes a system call to the kernel

$$$
\includegraphics[width=\columnwidth]{images/os-concepts/call-to-os}
$$$

### Vectored Events

**Interrupt:** signal from an external device (eg mouse, keyboard)

**Exception:** signal from the application
- **Trap:** The program can resume after the instruction that triggered it. Eg divide by zero, system calls
- **Fault:** The program can reattempt the instruction that triggered it. Eg page fault
- **Abort:** Unable to pinpoint the failure. Not recoverable. Eg: hardware failures, corrupted data

These all use the same mechanism to get the kernel's attention. They trigger a handler in the kernel

This terminology is not universal! We are not going to be too strict about it

% https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt
% https://pages.cs.wisc.edu/~gerald/cs537/Summer17/handouts/traps.pdf
% terminology is not consistent! 




## Booting

### Booting

The operating system itself is software. 

To run, it needs to be loaded into RAM and the CPU needs to be initialized to start running the operating system.

How can this happen, if the operating system itself is responsible for this task?

### Firmware and Boot Loader

The operating system loads and initializes itself through a process called booting. When a computer is turned on:
- Code stored in firmware (nonvolatile memory in hardware) runs
- Examples: Basic Input/Output System (BIOS) and Unified Extensible Firmware Interface (UEFI)
- This code loads first chunk of operating system software (called the boot block) from disk to RAM
- It starts running boot block instructions on CPU
Then, operating system software loads the rest of itself from disk, initializes hardware resources, and initializes data structures and abstractions.

### Starting the Boot

- As soon as we start executing an instruction, we are already fetching the next one
- But how do we know where to start?
- The location of the "boot block" is hard-coded. Often 0x00000000
- This is firmware. Non-volatile memory (aka users are not allowed to modify it)
- Technically not part of the OS, but same ballpark










% what is the OS?

% ## the os kernel
% kernel responsibilities
% traps/interrupts
% system calls

% ## booting
% os is software!
% firmware
% boot loader

% ## multiprogramming
% CPU time sharing
% scheduling algorithms? (Round Robin, Priority, Multi-level Feedback Queues)
% virtual memory
% fork
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










## Task-Level Parallelism






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









% interrupts
% computer is idle until an interrupt wakes it up
% example system calls
% File I/O: open, read, write, close
% Process Management: fork, execve, exit
% Memory Management: mmap
% Networking: socket, connect, send, recv

% traps. another word for interrupt? comes from the opposite direction?

% bash system calls
% c system calls

% execution modes. user mode, kernel mode
% address space (OS is mapped into every space)

% meltdown attack


% process hierarchy. fork, child, parent


### Threads, Processes, and Cores






% multiprogramming. switching back and forth fast
% processes
% context switching


% multicore processors
% GPUs - fewer transistors, simpler instruction set
% memory wall - can't keep up with CPU speed increases
% power wall - can't dissipate heat fast enough
% threads. running on different cores, same memory
% wall time vs CPU time


% multithreading - one program using multiple cores. shared memory
% multiprocessing - different processes. possible to split one program into multiple processes (eg supercomputer weather models) but generally not. communication between processes is a lot of work
% hyperthreading - two cores per core. superscalar processing, context switching during idle times




