# OS Concepts

We've talked about running instructions within a program

But how do we get to that point?

Before we can run the program, we need to boot the computer

We generally also want to fire up an operating system

The OS handles:
- memory allocation
- CPU time allocation
- device interfaces
- context switching (computer can juggle multiple tasks)


## Booting

### Starting the Boot

- As soon as we start executing an instruction, we are already fetching the next one
- But how do we know where to start?
- The location of the "boot block" is hard-coded. Often 0x00000000
- This is firmware. Non-volatile memory (aka users are not allowed to modify it)



### placeholder

![foo](images/device-drivers)

### placeholder

![foo](images/call-to-os)


### placeholder

![foo](images/address-space)


### placeholder

![foo](images/address-space)


### placeholder

![foo](images/address-space)

\includegraphics[width=\columnwidth]{images/ascii-table}



## The Operating System


% what is the OS?

% OS kernel

% device interface - allows devices to talk to the kernel

% system call interface - OS allows users to talk to the kernel

% running a program


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



## Multiprogramming






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



### Group Exercises

TODO: this