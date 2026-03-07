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

### Booting

The operating system is responsible for launching programs. Loading instructions into memory, initializing the CPU

But the OS is itself a program! How does it launch itself?

## Put Another Way

- After we run each instruction in a program, we fetch the next instruction from memory
- Sometimes it's the next instruction
- Sometimes we jump to another part of the program
- When we turn on the computer, how do we know where to start?

### Firmware and the Boot Loader

The operating system loads and initializes itself through a process called booting. When a computer is turned on:

- It starts running boot instructions from a hard-coded address (often 0x00000000)
- This is firmware, stored in non-volatile memory
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

### OS Responsibilities

Wait, what does the OS do again?


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




