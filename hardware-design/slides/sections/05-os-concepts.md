beamer: true
---

# OS Concepts

### OS Concepts

- We have talked about executing instructions as part of a program
- How do we boot the machine so we can run the program in the first place?
- And how does the machine handle background stuff while the program runs?

## The Operating System

### The Operating System

First things first:

"OS" stands for "Operating System"

% The OS is special software sits between applications and hardware (and allows them to communicate with one another)

$$$
\includegraphics[width=\columnwidth]{images/os-location}
$$$

### What does the OS do?

The operating system manages the use of hardware components:

- Manages workloads to run programs efficiently
- Resource management
- Makes the computer easy to use, from the perspective of the user
- Easy-to-use abstractions of the underlying system 

The core OS functionality is called the **kernel**

### The OS Kernel

- The kernel implements **mechanisms** to enable hardware to run programs. Example: initializing the CPU to run instructions
- It implements program abstractions as **processes**. This is how the OS keeps track of everything that runs on the CPU
- It implements **policies** for managing the hardware and processes. Example: allocating CPU time between processes

### System Calls

Programs use **system calls** to interface with the OS kernel. 

Only the kernel is allowed to talk to hardware components outside the CPU and main memory. Each of these actions requires a system call to the kernel:

- Reading data from the SSD (such as reading a file)
- Writing data to the SSD (such as writing a file)
- Getting updates from a keyboard or mouse
- Interfacing with the wifi card to connect to the internet
- Etc




### OS Concepts

We've talked about running instructions within a program

But how do we get to that point?

Before we can run the program, we need to boot the computer

We generally also want to fire up an operating system

The OS handles:

- memory allocation
- CPU time allocation
- device interfaces
- context switching (computer can juggle multiple tasks)

% firmware initializes hardware, finds the boot loader (eg GRUB, Windows Boot Manager)

## Booting

### Starting the Boot

- As soon as we start executing an instruction, we are already fetching the next one
- But how do we know where to start?
- The location of the "boot block" is hard-coded. Often 0x00000000
- This is firmware. Non-volatile memory (aka users are not allowed to modify it)
- Technically not part of the OS, but same ballpark

### Placeholder
$$$
\includegraphics[width=\columnwidth]{images/device-drivers}
$$$

### Placeholder
$$$
\includegraphics[width=\columnwidth]{images/call-to-os}
$$$

### Placeholder
$$$
\includegraphics[width=\columnwidth]{images/os-location}
$$$

### Placeholder
$$$
\includegraphics[width=\columnwidth]{images/process-states}
$$$

### Placeholder
$$$
\includegraphics[width=\columnwidth]{images/starting-a-program}
$$$

### Placeholder
$$$
\includegraphics[width=\columnwidth]{images/xkcd-meltdown}
$$$

### Placeholder
$$$
\includegraphics[width=\columnwidth]{images/xkcd-meltdown-cropped}
$$$


## The Operating System

% what is the OS?

% OS kernel

% device interface - allows devices to talk to the kernel

% system call interface - OS allows users to talk to the kernel

% running a program




% vectored events - interrupts and exceptions (fault, trap, abort) - intel x86 terminology

% Per April 2016 version of the Intel Software Developer Manual

% vectored events cause the processor jump to an interrupt handler
% it saves as much context as it can, so execution can later resume

% exceptions/interrupts have an ID (called a vector) that determines which handler

% interrupts are from hardware signals. external devices

% exceptions are from the execution of a program. divide by zero, illegal memory access, page fault

% example: page fault
% try to access something in memory, but it's been swapped out. suspend execution to load it

% trap - program can resume after the instruction that triggered it. example: divide by zero
% fault - program can reattempt the instruction that triggered it. example: page fault. try to access something from memory, but it's been swapped. suspend execution, load it, then try again
% abort - unable to pinpoint the failure. not recoverable. example: hardware failures, corrupted data

% trap is like a precursor to try/catch

% you can also do intentional traps to pass control to the kernel mode. example: file io
% program makes a system call, which the processor turns into a trap

% https://stackoverflow.com/questions/3149175/what-is-the-difference-between-trap-and-interrupt

% terminology is not consistent! 
% https://pages.cs.wisc.edu/~gerald/cs537/Summer17/handouts/traps.pdf
% traps come from the current process, interrupts come from devices. same hardware mechanism






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




