
---

# OS Concepts

## Reading

Read the Introduction to Chapter 13, and Sections 13.1 and 13.2 of the textbook [Dive Into Systems](https://diveintosystems.org), before starting this assignment. 

## Operating System Basics

1. Describe the role of the Operating System. Which of the following are true?
    - The operating system is software.
    - The operating system is hardware.
    - The operating system manages hardware components to run programs.
    - The operating system is available whenever the computer is on.
    - The operating system can start programs in response to user interaction.
2. Which of the following are true about multiprogramming?
    - Multiprogramming allows more than one program to run at a time
    - In multiprogramming, all programs are simultaneous running on CPU cores
    - We can never have more programs running than our computer has CPU cores
    - Programs cannot share hardware resources
3. Which of the following are true about the operating system kernel? 
	- The kernel manages the hardware layer to run programs
	- The kernel implements the interfaces to the user applications layer
	- The kernel implements policies for which process runs next on the CPU
	- The kernel implements the system call interface and the device interface

## Booting and Running

1. Number the following steps 1 through 4, giving the order in which the operating system performs the tasks to start running a program.
    - Load the program's binary executable from disk to RAM
    - Allocate a portion of RAM
    - Initializes the CPU to start running the program
    - Create and initialize process for running the program
2. What is booting?
    - The process of the operating system loading and initializing itself on the computer
    - The process of removing stale data from the cache
    - The processes between pressing the power button on a computer and when the CPU is provided with power
3. What is an interrupt-driven system?
    - The OS sleeps until it receives a request.
    - The latest program to start interrupts previously run programs to use the CPU
    - The OS interrupts other processes to access the resources that it needs
    - After booting and initializing, the OS runs until it is interrupted by and input/output device
4. What is a system call?
    - A request from a program to the OS to access protected resources
    - A command executed by the CPU
    - An instruction from the operating system
    - Data retrieval from secondary storage
5. What is a trap?
    - An interrupt coming from the software layer
    - An interrupt coming from the hardware layer
    - An interrupt from a malicious program
    - An interrupt from a network interface card (NIC)
6. Number the following steps 1 through 4, giving the order of steps in a system call.
    - The trap handler reads the identification number.
    - The identification number of the system call is placed and a trap instruction is issued to the OS.
    - The trap handler executes the system call.
    - The CPU stops executing program instructions, and starts executing OS instructions.
7. Number the following steps 1 through 3, giving the order of steps in a hardware interrupt.
    - The interrupting device puts a signal on the CPU's interrupt bus.
    - The OS interrupt handler executes the instructions.
    - The CPU stops executing program instructions, and starts executing OS instructions.
8. What is user mode?
    - An execution mode where only user-level instructions are executed, and the CPU is prevented from accessing OS instructions and data, as well as some hardware components.
    - An execution mode where the CPU can execute any instructions, access any memory location, and directly access hardware components.
    - An execution mode where all instructions are issued by the current user.
    - An executing mode where the user specifies which hardware components and memory locations the CPU can access.
9. What is kernel mode?
    - An execution mode where only the OS software is running.
    - An execution mode where the CPU can execute any instructions, access any memory location, and directly access hardware components.
    - An execution mode where the CPU debugs issues in the OS.
    - An executing mode where the computer has booted in safe mode, so that malicious software and data leaks can be resolved.

## Processes

1. What is a process?
    - An instance of a program running in the system.
    - A sequence of instructions executed by the CPU.
    - The steps that the CPU follows in order to execute an instruction.
    - A sequence of instructions initiated by the OS.
2. In multiprogramming, what handles switching between multiple processes running on the CPU?
    - The OS
    - The control unit
    - The CPU
    - The load balancer
3. What is timesharing?
    - The OS schedules processes to execute for short time intervals, taking turns
    - The CPU alternates between executing instructions from different processes
    - While a process is accessing memory, it pauses to allow another process to execute
    - Memory accesses from multiple processes are grouped together for efficiency
4. What does the OS save from the current process when context switching? Select all.
    - Register values
    - Memory state
    - Values in secondary storage
    - The time needed to finish the process
5. What information does the OS maintain for each process? Select all.
    - A unique identifier for the process
    - Address space information
    - Execution state
    - Register values
    - Stack location
    - Resources allocated to the process
    - Current process state
6. What are possible process execution states? Select all.
    - Ready
    - Running
    - Blocked
    - Exited
    - Paused
    - Idle
    - Stalled
    - Active
7. In Unix, what system call create a new process?
    - fork
    - new
    - branch
    - execute
8. In the diagram below, what are the relationships between the processes? Select all true statements.
    - A is the parent of B
    - B is the parent of E
    - C is a child of A
    - D and E are siblings
    - B has made two calls to fork
    - E is the parent of B
    - A is the parent of E
    - D and C are siblings
    - B is a child of E
    - F is a child of B
    - E has made one call to fork

$$$
\begin{tikzpicture}[transform shape]
	% Paths, nodes and wires:
	\node[shape=circle, draw, line width=1pt, minimum width=1.215cm](N1) at (6, 6){} node[anchor=center] at (N1.text){$A$};
	\node[shape=circle, draw, line width=1pt, minimum width=1.215cm](N2) at (5, 4){} node[anchor=center] at (N2.text){$B$};
	\node[shape=circle, draw, line width=1pt, minimum width=1.215cm](N3) at (7, 4){} node[anchor=center] at (N3.text){$C$};
	\node[shape=circle, draw, line width=1pt, minimum width=1.215cm](N4) at (4, 2){} node[anchor=center] at (N4.text){$D$};
	\node[shape=circle, draw, line width=1pt, minimum width=1.215cm](N5) at (6, 2){} node[anchor=center] at (N5.text){$E$};
	\node[shape=circle, draw, line width=1pt, minimum width=1.215cm](N6) at (8, 2){} node[anchor=center] at (N6.text){$F$};
	\draw[-latex] (5.558, 5.558) -- (5, 4.625);
	\draw[-latex] (6.442, 5.558) -- (7, 4.625);
	\draw[-latex] (4.558, 3.558) -- (4, 2.625);
	\draw[-latex] (5.442, 3.558) -- (6, 2.625);
	\draw[-latex] (7.442, 3.558) -- (8, 2.625);
\end{tikzpicture}
$$$

## Raspberry Pi Cores

In this section, you will investigate the CPU of your Raspberry Pi.

In the terminal on your Raspberry Pi, enter the following command.

```
lscpu
```

You should see information on the architecture of your Raspberry Pi.

1. What is listed for thread(s) per core?
2. What is listed for cores per socket? (Note: sometimes called clusters)
3. What is listed for sockets?

## Raspberry Pi Multithreading

For this exercise, you will investigate how the number of threads impacts the run time of a process. Review sections 13.2, 14.1, and 14.2 of [Dive Into Systems](https://diveintosystems.org)

- Login to your Pi as the appropriate user
- Create a directory for this assignment called `instructions-on-hardware`
- Create a new Google Doc for your discussion and screenshots. Make sure to give it a clear title and put your name on it.
- Download the file `pthreads1.c` from Moodle and copy it into your new directory
- Compile the code: `gcc pthreads1.c -o pthreads1 -lpthread -lm`
- Run it: `./pthreads1 1`
- Copy-paste the output into your doc. Make sure to label it clearly
- Now run it again with the `time` command: `time ./pthreads1 1`
- Paste the output in your doc. What did `time` do? Why might that be useful?

The CPU time of the process is the sum of the user-CPU-time and the system-CPU-time:

- "real" indicates the elapsed time for the entire computation (wall-clock time).
- "user" indicates how much time is spent executing the program code (user-CPU-time).
- sys indicates how much time was spent executing operating system code (system-CPU-time).
- Real time is not always exactly the same as user time plus system time. Why not? Put some thoughts in your doc
		
Find at least three other people to work with. Each person should run the following:

```
time ./pthreads1 1
time ./pthreads1 2
time ./pthreads1 3
time ./pthreads1 4
time ./pthreads1 5
time ./pthreads1 6
time ./pthreads1 7
time ./pthreads1 8
time ./pthreads1 9
time ./pthreads1 10
time ./pthreads1 11
time ./pthreads1 12
```

Use a spreadsheet to record user, system, and real time for each run. You can all share the same spreadsheet. Just be careful not to accidentally overwrite each others' data.

Make three graphs:

1. User time vs number of cores
2. CPU time vs number of cores
3. Real time vs number of cores

For the time values, use the average of your data points. Also compute the standard deviation for each data point. Add that to the graph as error bars.

**Add a screenshot of each graph to your doc.**

Based on your graphs, answer the following questions in your doc:

1. What happens to the wall-clock time as we increase the number of threads? Why does this happen?
2. What happens to the CPU time? Why?
3. How about the system time?



