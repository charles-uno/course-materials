beamer: true
template: slides.tex
---

# Logic Representation

### What does boolean mean?
	
- Boolean logic uses two values: true and false
- This is convenient for computers that can only store 1 (on) and 0 (off).
- Complex logic becomes possible when multiple boolean values are used togather.


# Boolean Functions

### Truth Tables

A boolean function takes boolean input(s) and produces a boolean output. In order to see all the inputs and outputs, we can write a truth table. For example:

| A | not A |
|:-:|-------|
| 1 | 0     |
| 0 | 1     |

### Boolean Functions

Fundamental boolean functions include AND, OR, and XOR:

| A | B | A and B | A or B | A xor B |
|:-:|:-:|:--------:|:------:|:-------:|
| 1 | 1 | 1       | 1      | 0       |
| 1 | 0 | 0       | 1      | 1       |
| 0 | 1 | 0       | 1      | 1       |
| 0 | 0 | 0       | 0      | 0       |

### Boolean Functions

We also have opposite functions NAND, NOR, and XNOR. These are just the previous gates but flipped:

| A | B | A nand B | A nor B | A xnor B |
|:-:|:-:|:--------:|:-------:|:--------:|
| 1 | 1 | 0        | 0       | 1        |
| 1 | 0 | 1        | 0       | 0        |
| 0 | 1 | 1        | 0       | 0        |
| 0 | 0 | 1        | 1       | 1        |

### Boolean Function Shorthand

We are going to be writing these over and over. To save some ink:

- Not A is written $\LogicNot{A}$
- A and B is written $\LogicAnd{A}{B}$
- A or B is written $\LogicOr{A}{B}$
- A xor B is $\LogicXor{A}{B}$
- A nand B is written $\LogicNand{A}{B}$
- A nor B is written $\LogicNor{A}{B}$
- A xnor B is written $\LogicXnor{A}{B}$
	
Heads up: you may see different symbols elsewhere!

% ### Group Exercises
% TODO: this

# Boolean Expressions

### Putting Boolean Functions Together

We can chain multiple boolean functions together. This is called a boolean expression.

For example, let's define the function $f$ with two inputs:
$$$
\begin{align*}
	f(A, B) & = \text{(A or B) and not (A and B)}               \\
			& = \LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})} \\
\end{align*}
$$$

### Parsing Boolean Expressions

At face value, it's hard to understand. Let's break out some helper functions:
$$$
\begin{align*}
	f(A, B) & = \LogicAnd{\underbrace{(\LogicOr{A}{B})}}{(\underbrace{\LogicNand{A}{B})}} \\
\end{align*}
$$$

### Parsing Boolean Expressions
$$$
\begin{align*}
	f(A, B) & = \LogicAnd{\underbrace{(\LogicOr{A}{B})}}{(\underbrace{\LogicNand{A}{B})}} \\
\end{align*}
$$$
Then we can write out a truth table for those helper functions:

| A | B | $\LogicOr{A}{B}$ | $\LogicNand{A}{B}$ |
|:-:|:-:|----------------:|------------------:|
| 1 | 1 | 1               | 0                 |
| 1 | 0 | 1               | 1                 |
| 0 | 1 | 1               | 1                 |
| 0 | 0 | 0               | 1 |

### Putting Boolean Functions Together
$$$
\begin{align*}
	f(A, B) & = \LogicAnd{\underbrace{(\LogicOr{A}{B})}}{(\underbrace{\LogicNand{A}{B})}} \\
\end{align*}
$$$

Then finally we can write the truth table for the whole expression:

| A | B | $\LogicOr{A}{B}$ | $\LogicNand{A}{B}$ | $f(A, B)$ |
|:-:|:-:|-----------------:|-------------------:|-----------|
| 1 | 1 | 1               | 0                 | 0         |
| 1 | 0 | 1               | 1                 | 1         |
| 0 | 1 | 1               | 1                 | 1         |
| 0 | 0 | 0               | 1                 | 0         |

% ### Group Exercises
% TODO: this

# Logic Gates

### Logic Gates
Logic gates are the same thing as boolean functions. But instead of writing them as a word or symbol, we draw them like a flow chart.

### Boolean Operators: NOT

The NOT gate looks like this:
$$$
\begin{tikzpicture}
	% Paths, nodes and wires:
	\node[ieeestd not port] at (12.877, 10.375){};
	\node[shape=rectangle, minimum width=0.354cm, minimum height=0.59cm] at (11.555, 10.437){} node[anchor=north west, align=left, text width=-0.034cm, inner sep=6pt] at (11.36, 10.75){A};
	\node[shape=rectangle, minimum width=0.744cm, minimum height=0.59cm] at (14.36, 10.563){} node[anchor=north west, align=left, text width=0.356cm, inner sep=6pt] at (13.971, 10.875){\LogicNot{A}};
\end{tikzpicture}
$$$

Truth table:

| A | $\LogicNot{A}$ |
|:-:|:--------------:|
| 0 |  1             |
| 1 |  0             |

### Boolean Operators: AND, NAND
$$$
\begin{tikzpicture}
	% Paths, nodes and wires:
	\node[ieeestd and port] at (4.919, 6.5){};
	\node[ieeestd nand port] at (9.419, 6.5){};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (3.5, 6.875){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (3.125, 7.25){A};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (8, 6.875){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (7.625, 7.25){A};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (3.5, 6.125){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (3.125, 6.5){B};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (8, 6.125){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (7.625, 6.5){B};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (6.25, 6.5){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (5.875, 6.875){\LogicAnd{A}{B}};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (10.75, 6.5){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (10.375, 6.875){\LogicNand{A}{B}};
\end{tikzpicture}
$$$

Truth table:

| A | B | $\LogicAnd{A}{B}$ | $\LogicNand{A}{B}$ |
|:-:|:-:|-------------------:|--------------------:|
| 0 | 0 |       0            |       1            |
| 0 | 1 |       0            |       1            |
| 1 | 0 |       0            |       1            |
| 1 | 1 |       1            |       0            |

### Boolean Operators: OR, NOR
$$$
\begin{tikzpicture}
	% Paths, nodes and wires:
	\node[ieeestd or port] at (4.919, 6.5){};
	\node[ieeestd nor port] at (9.419, 6.5){};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (3.5, 6.875){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (3.125, 7.25){A};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (8, 6.875){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (7.625, 7.25){A};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (3.5, 6.125){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (3.125, 6.5){B};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (8, 6.125){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (7.625, 6.5){B};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (6.25, 6.5){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (5.875, 6.875){\LogicOr{A}{B}};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (10.75, 6.5){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (10.375, 6.875){\LogicNor{A}{B}};
\end{tikzpicture}
$$$

Truth table:

| A | B | $\LogicOr{A}{B}$ | $\LogicNor{A}{B}$  |
|:-:|:-:|------------------:|-------------------:|
| 0 | 0 |       0            |       1            |
| 0 | 1 |       1            |       0            |
| 1 | 0 |       1            |       0            |
| 1 | 1 |       1            |       0            |

### Boolean Operators: XOR, XNOR
$$$
\begin{tikzpicture}
	% Paths, nodes and wires:
	\node[ieeestd xor port] at (4.919, 6.5){};
	\node[ieeestd xnor port] at (9.419, 6.5){};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (3.5, 6.875){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (3.125, 7.25){A};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (8, 6.875){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (7.625, 7.25){A};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (3.5, 6.125){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (3.125, 6.5){B};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (8, 6.125){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (7.625, 6.5){B};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (6.25, 6.5){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (5.875, 6.875){\LogicOr{A}{B}};
	\node[shape=rectangle, minimum width=0.715cm, minimum height=0.715cm] at (10.75, 6.5){} node[anchor=north west, align=left, text width=0.327cm, inner sep=6pt] at (10.375, 6.875){\LogicNor{A}{B}};
\end{tikzpicture}
$$$

Truth table:

| A | B | $\LogicXor{A}{B}$ | $\LogicXnor{A}{B}$ |
|:-:|:-:|--------------------:|--------------------:|
| 0 | 0 |       0            |       1            |
| 0 | 1 |       1            |       0            |
| 1 | 0 |       1            |       0            |
| 1 | 1 |       0            |       1            |

% ### Group Exercises
% TODO: this

# Logic Circuits

### Multiple Gates Together

When we chain multiple boolean functions together, we get a boolean expression.

Similarly, when we chain multiple logic gates together, we get a logic circuit.
$$$
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (1.571, 3.973){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (1.259, 4.286){B};
		\node[ieeestd and port] at (7.205, 5.286){};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (1.545, 4.741){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (1.232, 5.054){A};
		\node[ieeestd or port] at (4.919, 6.143){};
		\node[ieeestd nand port] at (4.919, 4.429){};
		\draw (6, 6.143) -- (6, 5.571) -- (6.143, 5.571);
		\draw (6, 4.429) -- (6, 5) -- (6.123, 5.006);
		\node[jump crossing] at (3.429, 4.717){};
		\draw (3.838, 4.709) -- (3.571, 4.714);
		\draw (3.838, 4.149) -- (2, 4.143);
		\draw (3.429, 4.577) -- (3.429, 4.143);
		\draw (3.429, 4.857) -- (3.429, 5.857) -- (3.838, 5.863);
		\draw (3.286, 4.714) -- (2, 4.714);
		\draw (3.838, 6.423) -- (2.857, 6.429) -- (2.857, 4.714);
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (8.741, 5.312){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (8.429, 5.625){??};
	\end{tikzpicture}
$$$
What does this one do?

### Understanding a Logic Circuit

We can work from left to right, making note of what each gate does
$$$
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (1.571, 3.973){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (1.259, 4.286){B};
		\node[ieeestd and port] at (7.205, 5.286){};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (1.545, 4.741){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (1.232, 5.054){A};
		\node[ieeestd or port] at (4.919, 6.143){};
		\node[ieeestd nand port] at (4.919, 4.429){};
		\draw (6, 6.143) -- (6, 5.571) -- (6.143, 5.571);
		\draw (6, 4.429) -- (6, 5) -- (6.123, 5.006);
		\node[jump crossing] at (3.429, 4.717){};
		\draw (3.838, 4.709) -- (3.571, 4.714);
		\draw (3.838, 4.149) -- (2, 4.143);
		\draw (3.429, 4.577) -- (3.429, 4.143);
		\draw (3.429, 4.857) -- (3.429, 5.857) -- (3.838, 5.863);
		\draw (3.286, 4.714) -- (2, 4.714);
		\draw (3.838, 6.423) -- (2.857, 6.429) -- (2.857, 4.714);
		\node[shape=rectangle, minimum width=1.447cm, minimum height=0.59cm] at (6, 6.714){} node[anchor=north west, align=left, text width=1.059cm, inner sep=6pt] at (5.259, 7.027){\LogicOr{A}{B}};
		\node[shape=rectangle, minimum width=1.25cm, minimum height=0.59cm] at (6.357, 4.143){} node[anchor=north west, align=left, text width=0.862cm, inner sep=6pt] at (5.714, 4.455){\LogicNand{A}{B}};
		\node[shape=rectangle, minimum width=3.108cm, minimum height=0.59cm] at (9.714, 5.402){} node[anchor=north west, align=left, text width=2.72cm, inner sep=6pt] at (8.143, 5.714){??};
	\end{tikzpicture}
$$$

### Understanding a Logic Circuit
We can work from left to right, making note of what each gate does
$$$
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (1.571, 3.973){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (1.259, 4.286){B};
		\node[ieeestd and port] at (7.205, 5.286){};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (1.545, 4.741){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (1.232, 5.054){A};
		\node[ieeestd or port] at (4.919, 6.143){};
		\node[ieeestd nand port] at (4.919, 4.429){};
		\draw (6, 6.143) -- (6, 5.571) -- (6.143, 5.571);
		\draw (6, 4.429) -- (6, 5) -- (6.123, 5.006);
		\node[jump crossing] at (3.429, 4.717){};
		\draw (3.838, 4.709) -- (3.571, 4.714);
		\draw (3.838, 4.149) -- (2, 4.143);
		\draw (3.429, 4.577) -- (3.429, 4.143);
		\draw (3.429, 4.857) -- (3.429, 5.857) -- (3.838, 5.863);
		\draw (3.286, 4.714) -- (2, 4.714);
		\draw (3.838, 6.423) -- (2.857, 6.429) -- (2.857, 4.714);
		\node[shape=rectangle, minimum width=1.447cm, minimum height=0.59cm] at (6, 6.714){} node[anchor=north west, align=left, text width=1.059cm, inner sep=6pt] at (5.259, 7.027){\LogicOr{A}{B}};
		\node[shape=rectangle, minimum width=1.25cm, minimum height=0.59cm] at (6.357, 4.143){} node[anchor=north west, align=left, text width=0.862cm, inner sep=6pt] at (5.714, 4.455){\LogicNand{A}{B}};
		\node[shape=rectangle, minimum width=3.108cm, minimum height=0.59cm] at (9.714, 5.402){} node[anchor=north west, align=left, text width=2.72cm, inner sep=6pt] at (8.143, 5.714){\LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})}};
	\end{tikzpicture}
$$$

### Understanding a Logic Circuit

Then we can write the corresponding truth table

$$$
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (1.571, 3.973){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (1.259, 4.286){B};
		\node[ieeestd and port] at (7.205, 5.286){};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (1.545, 4.741){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (1.232, 5.054){A};
		\node[ieeestd or port] at (4.919, 6.143){};
		\node[ieeestd nand port] at (4.919, 4.429){};
		\draw (6, 6.143) -- (6, 5.571) -- (6.143, 5.571);
		\draw (6, 4.429) -- (6, 5) -- (6.123, 5.006);
		\node[jump crossing] at (3.429, 4.717){};
		\draw (3.838, 4.709) -- (3.571, 4.714);
		\draw (3.838, 4.149) -- (2, 4.143);
		\draw (3.429, 4.577) -- (3.429, 4.143);
		\draw (3.429, 4.857) -- (3.429, 5.857) -- (3.838, 5.863);
		\draw (3.286, 4.714) -- (2, 4.714);
		\draw (3.838, 6.423) -- (2.857, 6.429) -- (2.857, 4.714);
		\node[shape=rectangle, minimum width=1.447cm, minimum height=0.59cm] at (6, 6.714){} node[anchor=north west, align=left, text width=1.059cm, inner sep=6pt] at (5.259, 7.027){\LogicOr{A}{B}};
		\node[shape=rectangle, minimum width=1.25cm, minimum height=0.59cm] at (6.357, 4.143){} node[anchor=north west, align=left, text width=0.862cm, inner sep=6pt] at (5.714, 4.455){\LogicNand{A}{B}};
		\node[shape=rectangle, minimum width=3.108cm, minimum height=0.59cm] at (9.714, 5.402){} node[anchor=north west, align=left, text width=2.72cm, inner sep=6pt] at (8.143, 5.714){\LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})}};
	\end{tikzpicture}
$$$

| A | B | $\LogicOr{A}{B}$ | $\LogicNand{A}{B}$ | $\LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})}$ |
|:-:|:-:|-----------------:|-------------------:|--------------------------------------------------:|
| 1 | 1 | 1               | 0                 | 0                                                |
| 1 | 0 | 1               | 1                 | 1                                                |
| 0 | 1 | 1               | 1                 | 1                                                |
| 0 | 0 | 0               | 1                 | 0 |

### Drawing a Logic Circuit
Similarly, if we have a logical expression, we can draw it as a diagram from right to left.
$$$
\begin{tikzpicture}
	% Paths, nodes and wires:
	\node[ieeestd and port] at (7.205, 5.286){};
	\node[shape=rectangle, minimum width=1.447cm, minimum height=0.59cm] at (5.598, 5.741){} node[anchor=north west, align=left, text width=1.059cm, inner sep=6pt] at (4.857, 6.054){\LogicOr{A}{B}};
	\node[shape=rectangle, minimum width=1.25cm, minimum height=0.59cm] at (5.5, 4.884){} node[anchor=north west, align=left, text width=0.862cm, inner sep=6pt] at (4.857, 5.196){\LogicNand{A}{B}};
	\node[shape=rectangle, minimum width=3.108cm, minimum height=0.59cm] at (9.714, 5.402){} node[anchor=north west, align=left, text width=2.72cm, inner sep=6pt] at (8.143, 5.714){\LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})}};
\end{tikzpicture}
$$$

### Drawing a Logic Circuit
$$$
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (3.402, 5.741){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (3.089, 6.054){B};
		\node[ieeestd and port] at (7.205, 5.286){};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (3.375, 6.509){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (3.062, 6.821){A};
		\node[ieeestd or port] at (4.919, 6.143){};
		\draw (6, 6.143) -- (6, 5.571) -- (6.143, 5.571);
		\node[shape=rectangle, minimum width=1.447cm, minimum height=0.59cm] at (6, 6.714){} node[anchor=north west, align=left, text width=1.059cm, inner sep=6pt] at (5.259, 7.027){\LogicOr{A}{B}};
		\node[shape=rectangle, minimum width=1.25cm, minimum height=0.59cm] at (5.357, 4.857){} node[anchor=north west, align=left, text width=0.862cm, inner sep=6pt] at (4.714, 5.17){\LogicNand{A}{B}};
		\node[shape=rectangle, minimum width=3.108cm, minimum height=0.59cm] at (9.714, 5.402){} node[anchor=north west, align=left, text width=2.72cm, inner sep=6pt] at (8.143, 5.714){\LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})}};
	\end{tikzpicture}
$$$

### Drawing a Logic Circuit
$$$
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (3.402, 5.741){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (3.089, 6.054){B};
		\node[ieeestd and port] at (7.205, 5.286){};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (3.375, 6.509){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (3.062, 6.821){A};
		\node[ieeestd or port] at (4.919, 6.143){};
		\node[ieeestd nand port] at (4.919, 4.429){};
		\draw (6, 6.143) -- (6, 5.571) -- (6.143, 5.571);
		\draw (6, 4.429) -- (6, 5) -- (6.123, 5.006);
		\node[shape=rectangle, minimum width=1.447cm, minimum height=0.59cm] at (6, 6.714){} node[anchor=north west, align=left, text width=1.059cm, inner sep=6pt] at (5.259, 7.027){\LogicOr{A}{B}};
		\node[shape=rectangle, minimum width=1.25cm, minimum height=0.59cm] at (6.357, 4.143){} node[anchor=north west, align=left, text width=0.862cm, inner sep=6pt] at (5.714, 4.455){\LogicNand{A}{B}};
		\node[shape=rectangle, minimum width=3.108cm, minimum height=0.59cm] at (9.714, 5.402){} node[anchor=north west, align=left, text width=2.72cm, inner sep=6pt] at (8.143, 5.714){\LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})}};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (3.402, 3.973){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (3.089, 4.286){B};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (3.375, 4.741){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (3.062, 5.054){A};
	\end{tikzpicture}
$$$

### Drawing a Logic Circuit
$$$
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (1.571, 3.973){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (1.259, 4.286){B};
		\node[ieeestd and port] at (7.205, 5.286){};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (1.545, 4.741){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (1.232, 5.054){A};
		\node[ieeestd or port] at (4.919, 6.143){};
		\node[ieeestd nand port] at (4.919, 4.429){};
		\draw (6, 6.143) -- (6, 5.571) -- (6.143, 5.571);
		\draw (6, 4.429) -- (6, 5) -- (6.123, 5.006);
		\node[jump crossing] at (3.429, 4.717){};
		\draw (3.838, 4.709) -- (3.571, 4.714);
		\draw (3.838, 4.149) -- (2, 4.143);
		\draw (3.429, 4.577) -- (3.429, 4.143);
		\draw (3.429, 4.857) -- (3.429, 5.857) -- (3.838, 5.863);
		\draw (3.286, 4.714) -- (2, 4.714);
		\draw (3.838, 6.423) -- (2.857, 6.429) -- (2.857, 4.714);
		\node[shape=rectangle, minimum width=1.447cm, minimum height=0.59cm] at (6, 6.714){} node[anchor=north west, align=left, text width=1.059cm, inner sep=6pt] at (5.259, 7.027){\LogicOr{A}{B}};
		\node[shape=rectangle, minimum width=1.25cm, minimum height=0.59cm] at (6.357, 4.143){} node[anchor=north west, align=left, text width=0.862cm, inner sep=6pt] at (5.714, 4.455){\LogicNand{A}{B}};
		\node[shape=rectangle, minimum width=3.108cm, minimum height=0.59cm] at (9.714, 5.402){} node[anchor=north west, align=left, text width=2.72cm, inner sep=6pt] at (8.143, 5.714){\LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})}};
	\end{tikzpicture}
$$$

### Functional Completeness

|||

- Logic gates are not independent!
- There are many ways to build gates from other gates.
- It's even possible to build all gates using only NAND. This is called functional completeness.
- Why might functional completeness be useful?

$$$
\includegraphics[width=\columnwidth]{images/functional-completeness.png}
$$$

|||

% ### Group Exercises
% TODO: this

# Control Circuits

### Control Circuits

OK, so we have circuits that can do logic. Now what?

### Multiplexers

|||
$$$
\includegraphics[width=\columnwidth]{images/multiplexer}
$$$			
- When S=1, out=A
- When S=0, out=B
- Why might this be useful?
- Can we build this out of logic gates?
|||

### Latches (aka Flip-Flops)
What do you suppose this does?
$$$
\resizebox{0.8\columnwidth}{!}{
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[jump crossing] at (5.997, 5.857){};
		\draw (8.162, 6.709) -- (9, 6.714);
		\draw (8.162, 4.28) -- (9, 4.286);
		\draw (6, 4) -- (5, 4);
		\draw (6, 6.989) -- (5, 7);
		\draw (8.162, 6.709) -- (8.143, 5.857) -- (6.143, 5.857);
		\draw (8.162, 4.28) -- (8.143, 5.143) -- (6, 5.143) -- (5.997, 5.717);
		\draw (6, 6) -- (6, 6.429);
		\draw (5.857, 5.857) -- (5.571, 5.857) -- (5.571, 4.571) -- (6, 4.56);
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (4.714, 7){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (4.429, 7.286){S};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (4.714, 4.143){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (4.429, 4.429){R};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (9.143, 6.857){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (8.857, 7.143){Q};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (9.286, 4.429){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (9, 4.714){$\overline{Q}$};
		\node[ieeestd nor port] at (7.081, 4.28){};
		\node[ieeestd nor port] at (7.081, 6.709){};
	\end{tikzpicture}
}
$$$

### Baseline State
$$$
\resizebox{0.8\columnwidth}{!}{
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[jump crossing] at (5.997, 5.857){};
		\draw (8.162, 6.709) -- (9, 6.714);
		\draw (8.162, 4.28) -- (9, 4.286);
		\draw (6, 4) -- (5, 4);
		\draw (6, 6.989) -- (5, 7);
		\draw (8.162, 6.709) -- (8.143, 5.857) -- (6.143, 5.857);
		\draw (8.162, 4.28) -- (8.143, 5.143) -- (6, 5.143) -- (5.997, 5.717);
		\draw (6, 6) -- (6, 6.429);
		\draw (5.857, 5.857) -- (5.571, 5.857) -- (5.571, 4.571) -- (6, 4.56);
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (4.714, 7){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (4.429, 7.286){0};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (4.714, 4.143){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (4.429, 4.429){0};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (9.143, 6.857){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (8.857, 7.143){0};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (9.286, 4.429){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (9, 4.714){1};
		\node[ieeestd nor port] at (7.081, 4.28){};
		\node[ieeestd nor port] at (7.081, 6.709){};
	\end{tikzpicture}
}
$$$

### Send a Signal...
$$$
\resizebox{0.8\columnwidth}{!}{
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[jump crossing] at (5.997, 5.857){};
		\draw (8.162, 6.709) -- (9, 6.714);
		\draw (8.162, 4.28) -- (9, 4.286);
		\draw (6, 4) -- (5, 4);
		\draw (6, 6.989) -- (5, 7);
		\draw (8.162, 6.709) -- (8.143, 5.857) -- (6.143, 5.857);
		\draw (8.162, 4.28) -- (8.143, 5.143) -- (6, 5.143) -- (5.997, 5.717);
		\draw (6, 6) -- (6, 6.429);
		\draw (5.857, 5.857) -- (5.571, 5.857) -- (5.571, 4.571) -- (6, 4.56);
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (4.714, 7){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (4.429, 7.286){0};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (4.714, 4.143){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (4.429, 4.429){1};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (9.143, 6.857){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (8.857, 7.143){1};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (9.286, 4.429){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (9, 4.714){0};
		\node[ieeestd nor port] at (7.081, 4.28){};
		\node[ieeestd nor port] at (7.081, 6.709){};
	\end{tikzpicture}
}
$$$

### Remove the Signal
$$$
\resizebox{0.8\columnwidth}{!}{
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[jump crossing] at (5.997, 5.857){};
		\draw (8.162, 6.709) -- (9, 6.714);
		\draw (8.162, 4.28) -- (9, 4.286);
		\draw (6, 4) -- (5, 4);
		\draw (6, 6.989) -- (5, 7);
		\draw (8.162, 6.709) -- (8.143, 5.857) -- (6.143, 5.857);
		\draw (8.162, 4.28) -- (8.143, 5.143) -- (6, 5.143) -- (5.997, 5.717);
		\draw (6, 6) -- (6, 6.429);
		\draw (5.857, 5.857) -- (5.571, 5.857) -- (5.571, 4.571) -- (6, 4.56);
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (4.714, 7){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (4.429, 7.286){0};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (4.714, 4.143){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (4.429, 4.429){0};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (9.143, 6.857){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (8.857, 7.143){1};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (9.286, 4.429){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (9, 4.714){0};
		\node[ieeestd nor port] at (7.081, 4.28){};
		\node[ieeestd nor port] at (7.081, 6.709){};
	\end{tikzpicture}
}
$$$

### Latch Behavior

- Baseline is S=0, R=0
- When we set R=1, the result is Q=1
- When we return to baseline, the latch "remembers" Q=1
- What happens if we set S=1 instead?
- Why might this behavior be useful?
- What happens if we set S=1 and R=1 at the same time?


% ### Group Exercises
% TODO: this
% group warmup in Circuitverse. Use the testbench

# Arithmetic with Circuits

### Why bother with circuits over expressions?

Multiple outputs!

### Arithmetic with Circuits
	
- Let's say A and B are a pair of one-bit binary numbers
- Can we build a circuit to add them?
- Let's start with a truth table
	
### Arithmetic with Circuits

The four possible cases are:

- `0b0 + 0b0 = 0b00`
- `0b1 + 0b0 = 0b01`
- `0b0 + 0b1 = 0b01`
- `0b1 + 0b1 = 0b10`
	
Which we can write as a truth table:

| A | B | C | D |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Where A and B are the input bits, C and D are the digits of the result

### Arithmetic with Circuits

The four possible cases are:
	
- `0b0 + 0b0 = 0b00`
- `0b1 + 0b0 = 0b01`
- `0b0 + 0b1 = 0b01`
- `0b1 + 0b1 = 0b10`
	
Which we can write as a truth table:

| A | B | C | D |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 1 | 0 | 1 |

What is the logical expression for C? How about D?

Let's draw the expression

### The Half Adder

Why might this be called a "half" adder?
$$$
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[ieeestd and port] at (5.205, 5){};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (2.571, 3.688){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (2.259, 4){A};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.465cm] at (2.598, 2.964){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (2.286, 3.214){B};
		\node[ieeestd xor port] at (5.205, 3.286){};
		\node[jump crossing] at (3.854, 3.571){};
		\draw (3.994, 3.571) -- (4.123, 3.566);
		\draw (4.123, 3.006) -- (3, 3);
		\draw (3.714, 3.571) -- (3, 3.571);
		\draw (4.123, 4.72) -- (3.857, 4.714) -- (3.854, 3.711);
		\draw (3.857, 3.429) -- (3.857, 3);
		\draw (4.123, 5.28) -- (3.429, 5.286) -- (3.429, 3.571);
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (6.688, 5.027){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (6.375, 5.339){C};
		\node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (6.688, 3.286){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (6.375, 3.598){D};
	\end{tikzpicture}
$$$

### Full Adder

What's special about a full adder?
$$$
\begin{tikzpicture}
	% Paths, nodes and wires:
	\node[american xor port] at (6, 5.571){};
	\node[american xor port] at (7.815, 5.006){};
	\node[american and port] at (7.714, 3.571){};
	\node[jump crossing] at (4.286, 4.711){};
	\node[jump crossing] at (3.717, 4.714){};
	\node[jump crossing] at (3.711, 5.286){};
	\draw (4.614, 5.851) -- (3, 5.857);
	\draw (4.614, 5.291) -- (3.857, 5.286);
	\draw (3.571, 5.286) -- (3, 5.286);
	\draw (3.714, 5.429) -- (3.714, 5.857);
	\draw (3.714, 5.143) -- (3.714, 4.857);
	\draw (3.571, 4.714) -- (3, 4.714);
	\draw (3.857, 4.714) -- (4.143, 4.714);
	\node[jump crossing] at (6.143, 4.717){};
	\draw (6.143, 5.571) -- (6.143, 4.857);
	\draw (6.429, 5.286) -- (6.143, 5.286);
	\draw (6.283, 4.717) -- (6.429, 4.726);
	\draw (4.429, 4.714) -- (6.003, 4.717);
	\draw (4.286, 4.857) -- (4.286, 5.286);
	\node[american and port] at (7.714, 2.286){};
	\draw (6.143, 4.571) -- (6.143, 3.857) -- (6.328, 3.851);
	\draw (5.571, 4.714) -- (5.571, 3.286) -- (6.328, 3.291);
	\draw (6.328, 2.006) -- (3.714, 2) -- (3.714, 4.571);
	\draw (4.286, 4.571) -- (4.286, 2.571) -- (6.328, 2.566);
	\node[american or port] at (9.417, 3){};
	\draw (7.868, 3.571) -- (7.857, 3.286) -- (8.031, 3.28);
	\draw (7.868, 2.286) -- (7.857, 2.714) -- (8.031, 2.72);
	\draw (7.969, 5.006) -- (10, 5);
	\draw (9.571, 3) -- (10, 3);
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (2.571, 6){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (2.286, 6.286){A};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (2.571, 5.429){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (2.286, 5.714){B};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (2.571, 4.714){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (2.286, 5){$\text{C}_{\text{in}}$};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (10.429, 3){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (10.143, 3.286){$\text{C}_{\text{out}}$};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (10.429, 5){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (10.143, 5.286){S};
\end{tikzpicture}
$$$

% ### Group Exercises
% TODO: group warmup in Circuitverse
