# Logic Representation

### What does boolean mean?

- Boolean logic uses two values: true and false
- This is convenient for computers that can only store 1 (on) and 0 (off).
- Complex logic becomes possible when multiple boolean values are used togather.

## Boolean Functions

### Truth Tables

A boolean function takes boolean input(s) and produces a boolean output. In order to see all the inputs and outputs, we can write a truth table. For example:

\begin{tabular}{c c}
		A & not A \\
		\hline
		1 & 0     \\
		0 & 1
\end{tabular}

### Boolean Functions

Fundamental boolean functions include AND, OR, and XOR:

\begin{tabular}{c c c c c}
    A & B & A and B & A or B & A xor B \\
    \hline
    1 & 1 & 1       & 1      & 0       \\
    1 & 0 & 0       & 1      & 1       \\
    0 & 1 & 0       & 1      & 1       \\
    0 & 0 & 0       & 0      & 0
\end{tabular}

### Boolean Functions

We also have opposite functions NAND, NOR, and XNOR. These are just the previous gates but flipped:

\begin{tabular}{c c c c c}
    A & B & A nand B & A nor B & A xnor B \\
    \hline
    1 & 1 & 0        & 0       & 1        \\
    1 & 0 & 1        & 0       & 0        \\
    0 & 1 & 1        & 0       & 0        \\
    0 & 0 & 1        & 1       & 1
\end{tabular}

### Boolean Function Shorthand

We are going to be writing these over and over. To save some ink:

\begin{itemize}
    \item Not A is written \LogicNot{A}
    \item A and B is written \LogicAnd{A}{B}
    \item A or B is written \LogicOr{A}{B}
    \item A xor B is \LogicXor{A}{B}
    \item A nand B is written \LogicNand{A}{B}
    \item A nor B is written \LogicNor{A}{B}
    \item A xor B is written \LogicXnor{A}{B}
\end{itemize}

Heads up: you may see different symbols elsewhere!

## Boolean Expressions

### Putting Boolean Functions Together

We can chain multiple boolean functions together. This is called a boolean expression.

For example, let's define the function $f$ with two inputs:

\begin{align*}
    f(A, B) & = \text{(A or B) and not (A and B)}               \\
            & = \LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})} \\
\end{align*}

### Parsing Boolean Expressions

At face value, it's hard to understand. Let's break out some helper functions:

\begin{align*}
    f(A, B) & = \LogicAnd{\underbrace{(\LogicOr{A}{B})}}{(\underbrace{\LogicNand{A}{B})}} \\
\end{align*}

### Parsing Boolean Expressions

\begin{align*}
    f(A, B) & = \LogicAnd{\underbrace{(\LogicOr{A}{B})}}{(\underbrace{\LogicNand{A}{B})}} \\
\end{align*}

Then we can write out a truth table for those helper functions:

\begin{tabular}{c c c c}
    A & B & \LogicOr{A}{B} & \LogicNand{A}{B} \\
    \hline
    1 & 1 & 1              & 0                \\
    1 & 0 & 1              & 1                \\
    0 & 1 & 1              & 1                \\
    0 & 0 & 0              & 1
\end{tabular}

### Putting Boolean Functions Together

\begin{align*}
    f(A, B) & = \LogicAnd{\underbrace{(\LogicOr{A}{B})}}{(\underbrace{\LogicNand{A}{B})}} \\
\end{align*}

Then finally we can write the truth table for the whole expression:

\begin{tabular}{c c c c c}
    A & B & \LogicOr{A}{B} & \LogicNand{A}{B} & f(A, B) \\
    \hline
    1 & 1 & 1              & 0                & 0       \\
    1 & 0 & 1              & 1                & 1       \\
    0 & 1 & 1              & 1                & 1       \\
    0 & 0 & 0              & 1                & 0
\end{tabular}

## Logic Gates

### Logic Gates

Logic gates are the same thing as boolean functions. But instead of writing them as a word or symbol, we draw them like a flow chart.

### Boolean Operators: NOT

\begin{columns}
    \begin{column}{0.5\textwidth}
        The NOT gate looks like this:
        \bigskip

        \begin{tikzpicture}
            % Paths, nodes and wires:
            \node[ieeestd not port] at (12.877, 10.375){};
            \node[shape=rectangle, minimum width=0.354cm, minimum height=0.59cm] at (11.555, 10.437){} node[anchor=north west, align=left, text width=-0.034cm, inner sep=6pt] at (11.36, 10.75){A};
            \node[shape=rectangle, minimum width=0.744cm, minimum height=0.59cm] at (14.36, 10.563){} node[anchor=north west, align=left, text width=0.356cm, inner sep=6pt] at (13.971, 10.875){\LogicNot{A}};
        \end{tikzpicture}
    \end{column}
    \begin{column}{0.5\textwidth}
        Truth table:
        \bigskip

        \begin{center}
            \begin{tabular}{c c}
                A & \LogicNot{A} \\
                \hline
                1 & 0            \\
                0 & 1
            \end{tabular}
        \end{center}
    \end{column}
\end{columns}

### Boolean Operators: AND, NAND

\begin{columns}
    \begin{column}{0.5\textwidth}
        \begin{tikzpicture}
            % Paths, nodes and wires:
            \node[ieeestd and port] at (1.11, 10.22){};
            \node[ieeestd nand port] at (1.081, 7.47){};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.59cm] at (-0.375, 10.563){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.5, 10.875){A};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.465cm] at (-0.375, 10){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.5, 10.25){B};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.59cm] at (-0.404, 7.813){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.529, 8.125){A};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.465cm] at (-0.404, 7.25){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.529, 7.5){B};
            \node[shape=rectangle, minimum width=0.744cm, minimum height=0.59cm] at (2.61, 10.25){} node[anchor=north west, align=left, text width=0.356cm, inner sep=6pt] at (2.221, 10.563){\LogicAnd{A}{B}};
            \node[shape=rectangle, minimum width=0.744cm, minimum height=0.59cm] at (2.581, 7.563){} node[anchor=north west, align=left, text width=0.356cm, inner sep=6pt] at (2.192, 7.875){\LogicNand{A}{B}};
        \end{tikzpicture}
    \end{column}
    \begin{column}{0.5\textwidth}
        \begin{center}
            \begin{tabular}{c c c c}
                A & B & \LogicAnd{A}{B} & \LogicNand{A}{B} \\
                \hline
                1 & 1 & 1               & 0                \\
                1 & 0 & 0               & 1                \\
                0 & 1 & 0               & 1                \\
                0 & 0 & 0               & 1
            \end{tabular}
        \end{center}
    \end{column}
\end{columns}

### Boolean Operators: OR, NOR

\begin{columns}
    \begin{column}{0.5\textwidth}
        \begin{tikzpicture}
            % Paths, nodes and wires:
            \node[ieeestd or port] at (1.11, 10.22){};
            \node[ieeestd nor port] at (1.081, 7.47){};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.59cm] at (-0.375, 10.563){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.5, 10.875){A};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.465cm] at (-0.375, 10){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.5, 10.25){B};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.59cm] at (-0.404, 7.813){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.529, 8.125){A};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.465cm] at (-0.404, 7.25){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.529, 7.5){B};
            \node[shape=rectangle, minimum width=0.744cm, minimum height=0.59cm] at (2.61, 10.25){} node[anchor=north west, align=left, text width=0.356cm, inner sep=6pt] at (2.221, 10.563){\LogicOr{A}{B}};
            \node[shape=rectangle, minimum width=0.744cm, minimum height=0.59cm] at (2.581, 7.563){} node[anchor=north west, align=left, text width=0.356cm, inner sep=6pt] at (2.192, 7.875){\LogicNor{A}{B}};
        \end{tikzpicture}
    \end{column}
    \begin{column}{0.5\textwidth}
        \begin{center}
            \begin{tabular}{c c c c}
                A & B & \LogicOr{A}{B} & \LogicNor{A}{B} \\
                \hline
                1 & 1 & 1              & 0               \\
                1 & 0 & 1              & 0               \\
                0 & 1 & 1              & 0               \\
                0 & 0 & 0              & 1
            \end{tabular}
        \end{center}
    \end{column}
\end{columns}

### Boolean Operators: XOR, XNOR

\begin{columns}
    \begin{column}{0.5\textwidth}
        \begin{tikzpicture}
            % Paths, nodes and wires:
            \node[ieeestd xor port] at (1.11, 10.22){};
            \node[ieeestd xnor port] at (1.081, 7.47){};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.59cm] at (-0.375, 10.563){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.5, 10.875){A};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.465cm] at (-0.375, 10){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.5, 10.25){B};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.59cm] at (-0.404, 7.813){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.529, 8.125){A};
            \node[shape=rectangle, minimum width=0.215cm, minimum height=0.465cm] at (-0.404, 7.25){} node[anchor=north west, align=left, text width=-0.173cm, inner sep=6pt] at (-0.529, 7.5){B};
            \node[shape=rectangle, minimum width=0.744cm, minimum height=0.59cm] at (2.61, 10.25){} node[anchor=north west, align=left, text width=0.356cm, inner sep=6pt] at (2.221, 10.563){\LogicXor{A}{B}};
            \node[shape=rectangle, minimum width=0.744cm, minimum height=0.59cm] at (2.581, 7.563){} node[anchor=north west, align=left, text width=0.356cm, inner sep=6pt] at (2.192, 7.875){\LogicXnor{A}{B}};
        \end{tikzpicture}
    \end{column}
    \begin{column}{0.5\textwidth}
        \begin{center}
            \begin{tabular}{c c c c}
                A & B & \LogicXor{A}{B} & \LogicXnor{A}{B} \\
                \hline
                1 & 1 & 0               & 1                \\
                1 & 0 & 1               & 0                \\
                0 & 1 & 1               & 0                \\
                0 & 0 & 0               & 1
            \end{tabular}
        \end{center}
    \end{column}
\end{columns}

## Logic Circuits

### Multiple Gates Together

When we chain multiple boolean functions together, we get a boolean expression.

Similarly, when we chain multiple logic gates together, we get a logic circuit.

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

What does this one do?

### Understanding a Logic Circuit

We can work from left to right, making note of what each gate does

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

### Understanding a Logic Circuit

We can work from left to right, making note of what each gate does

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

### Understanding a Logic Circuit

Then we can write the corresponding truth table

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

\begin{center}
    \begin{tabular}{c c c c c}
        A & B & \LogicOr{A}{B} & \LogicNand{A}{B} & \LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})} \\
        \hline
        1 & 1 & 1              & 0                & 0                                               \\
        1 & 0 & 1              & 1                & 1                                               \\
        0 & 1 & 1              & 1                & 1                                               \\
        0 & 0 & 0              & 1                & 0
    \end{tabular}
\end{center}

### Drawing a Logic Circuit

Similarly, if we have a logical expression, we can draw it as a diagram from right to left.

\begin{tikzpicture}
    % Paths, nodes and wires:
    \node[ieeestd and port] at (7.205, 5.286){};
    \node[shape=rectangle, minimum width=1.447cm, minimum height=0.59cm] at (5.598, 5.741){} node[anchor=north west, align=left, text width=1.059cm, inner sep=6pt] at (4.857, 6.054){\LogicOr{A}{B}};
    \node[shape=rectangle, minimum width=1.25cm, minimum height=0.59cm] at (5.5, 4.884){} node[anchor=north west, align=left, text width=0.862cm, inner sep=6pt] at (4.857, 5.196){\LogicNand{A}{B}};
    \node[shape=rectangle, minimum width=3.108cm, minimum height=0.59cm] at (9.714, 5.402){} node[anchor=north west, align=left, text width=2.72cm, inner sep=6pt] at (8.143, 5.714){\LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})}};
\end{tikzpicture}

### Drawing a Logic Circuit

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

### Drawing a Logic Circuit

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

### Drawing a Logic Circuit

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

### Functional Completeness

\begin{columns}
    \begin{column}{0.5\textwidth}
        \begin{itemize}
            \item Logic gates are not independent!
            \item There are many ways to build gates from other gates.
            \item It's even possible to build all gates using only NAND. This is called functional completeness.
            \item Why might functional completeness be useful?
        \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
        \includegraphics[width=\columnwidth]{images/functional-completeness.png}
    \end{column}
\end{columns}

## Control Circuits

### Control Circuits

OK, so we have circuits that can do logic. Now what?

### Multiplexers

\begin{columns}
    \begin{column}{0.5\textwidth}
        \includegraphics[width=\columnwidth]{images/multiplexer}
    \end{column}
    \begin{column}{0.5\textwidth}
        \begin{itemize}
            \item When S=1, out=A
            \item When S=0, out=B
            \item Why might this be useful?
            \item Can we build this out of logic gates?
        \end{itemize}
    \end{column}
\end{columns}

### Latches (aka Flip-Flops)

What do you suppose this does?

\begin{center}
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
\end{center}

### Baseline State

\begin{center}
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
\end{center}

### Send a Signal...

\begin{center}
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
\end{center}

### Remove the Signal

\begin{center}
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
\end{center}

### Latch Behavior

- Baseline is S=0, R=0
- When we set R=1, the result is Q=1
- When we return to baseline, the latch "remembers" Q=1
- What happens if we set S=1 instead?
- Why might this behavior be useful?
- What happens if we set S=1 and R=1 at the same time?

## Arithmetic with Circuits

### Why bother with logic circuits?

- Multiple outputs
- Looks like circuitry

### Arithmetic with Circuits

- Let's say A and B are a pair of one-bit binary numbers
- Can we build a circuit to add them?
- Let's start with a truth table

### Arithmetic with Circuits

The four possible cases are:

- $0b0 + 0b0 = 0b00$
- $0b1 + 0b0 = 0b01$
- $0b0 + 0b1 = 0b01$
- $0b1 + 0b1 = 0b10$

Which we can write as a truth table:

\begin{center}
    \begin{tabular}{c c c c}
        A & B & C & D \\
        \hline
        1 & 1 & 0 & 0 \\
        1 & 0 & 1 & 0 \\
        0 & 1 & 1 & 0 \\
        0 & 0 & 0 & 1
    \end{tabular}
\end{center}

Where A and B are the input bits, C and D are the digits of the result

### Arithmetic with Circuits

The four possible cases are:

- $0b0 + 0b0 = 0b00$
- $0b1 + 0b0 = 0b01$
- $0b0 + 0b1 = 0b01$
- $0b1 + 0b1 = 0b10$

Which we can write as a truth table:

\begin{center}
    \begin{tabular}{c c c c}
        A & B & C & D \\
        \hline
        1 & 1 & 0 & 0 \\
        1 & 0 & 1 & 0 \\
        0 & 1 & 1 & 0 \\
        0 & 0 & 0 & 1
    \end{tabular}
\end{center}

What is the logical expression for C? How about D?

Let's draw the expression

### The Half Adder

Full adders can be chained together. Carry in as well as carry out.

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

### Bigger Adder with Carry

\begin{tikzpicture}
    % Paths, nodes and wires:
    \node[ieeestd and port] at (5.205, 5){};
    \node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (2.571, 3.688){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (2.259, 4){B};
    \node[shape=rectangle, minimum width=0.59cm, minimum height=0.465cm] at (2.598, 2.964){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (2.286, 3.214){C};
    \node[ieeestd xor port] at (5.205, 3.286){};
    \node[jump crossing] at (3.854, 3.571){};
    \draw (3.994, 3.571) -- (4.123, 3.566);
    \draw (4.123, 3.006) -- (3, 3);
    \draw (3.714, 3.571) -- (3, 3.571);
    \draw (4.123, 4.72) -- (3.857, 4.714) -- (3.854, 3.711);
    \draw (3.857, 3.429) -- (3.857, 3);
    \draw (4.123, 5.28) -- (3.429, 5.286) -- (3.429, 3.571);
    \node[ieeestd xor port] at (7.776, 6){};
    \node[ieeestd and port] at (7.776, 7.714){};
    \node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (2.598, 6.402){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (2.286, 6.714){A};
    \node[jump crossing] at (6.429, 6.283){};
    \draw (6.571, 6.286) -- (6.714, 6.286);
    \draw (6.695, 7.434) -- (6.429, 7.429) -- (6.429, 6.429);
    \draw (6.695, 5.72) -- (6.429, 5.714);
    \draw (6.429, 6.143) -- (6.429, 5.714) -- (6.429, 5) -- (6.286, 5);
    \draw (6.695, 7.994) -- (6, 8) -- (6, 6.286) -- (6.286, 6.286);
    \draw (6, 6.286) -- (3, 6.286);
    \draw (6.286, 3.286) -- (8.857, 3.286);
    \node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (9.402, 7.741){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (9.089, 8.054){D};
    \node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (9.429, 6.027){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (9.116, 6.339){E};
    \node[shape=rectangle, minimum width=0.59cm, minimum height=0.59cm] at (9.402, 3.402){} node[anchor=north west, align=left, text width=0.202cm, inner sep=6pt] at (9.089, 3.714){F};
\end{tikzpicture}

## Electrical Circuits

### The Setup

\begin{tikzpicture}
    % Paths, nodes and wires:
    \node[ground] at (2.571, 5.659){};
    \node[sground, yscale=-1] at (2.571, 8.484){};
    \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (3.473, 8.857){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (2.857, 9.214){V>0};
    \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (3.107, 5.429){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (2.786, 5.714){V=0};
    \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (0.536, 7.143){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (0.214, 7.429){input};
    \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (2.429, 7.143){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (2.107, 7.429){logic};
    \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (3.821, 7.143){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (3.5, 7.429){output};
\end{tikzpicture}

### For Example

\begin{columns}
    \begin{column}{0.5\textwidth}
        \begin{itemize}
            \item Input A can be true (V>0) or false (V=0)
            \item Same for input B
            \item Output may be true or false depending on inputs
        \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
        \begin{tikzpicture}
            % Paths, nodes and wires:
            \node[ground] at (1, 4.286){};
            \node[sground, yscale=-1] at (1, 9){};
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (1.812, 9.429){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (1.196, 9.786){V>0};
            \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (1.464, 3.857){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (1.143, 4.143){V=0};
            \node[npn] at (1, 8.143){};
            \node[npn] at (1, 6.429){};
            \draw (1, 5.571) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (1, 4.429);
            \draw (1, 9) -- (1, 8.913);
            \draw (1, 7.373) -- (1, 7.199);
            \draw (1, 5.659) -- (1, 5.571);
            \draw (1, 4.429) -- (1, 4.286);
            \draw (1, 5.571) -- (2, 5.571);
            \draw (0.16, 6.429) -- (0, 6.429);
            \draw (0.16, 8.143) -- (0, 8.143);
            \node[shape=rectangle, minimum width=0.679cm, minimum height=0.679cm] at (-0.214, 8.071){} node[anchor=north west, align=left, text width=0.291cm, inner sep=6pt] at (-0.571, 8.429){A};
            \node[shape=rectangle, minimum width=0.679cm, minimum height=0.679cm] at (-0.214, 6.429){} node[anchor=north west, align=left, text width=0.291cm, inner sep=6pt] at (-0.571, 6.786){B};
            \node[shape=rectangle, minimum width=0.679cm, minimum height=0.679cm] at (2.286, 5.571){} node[anchor=north west, align=left, text width=0.291cm, inner sep=6pt] at (1.929, 5.929){??};
        \end{tikzpicture}
    \end{column}
\end{columns}

### What is a resistor?

- light bulb
- ceramic
- the coils in your toaster
- if you run electric current through it and it gets hot, it's a resistor (or at least has resistance)

### Voltage Drops in the Resistor

\begin{tikzpicture}
    % Paths, nodes and wires:
    \node[ground] at (2.571, 5.659){};
    \draw (2.571, 8.484) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (2.571, 7.199);
    \node[sground, yscale=-1] at (2.571, 8.484){};
    \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (1.964, 8.571){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (1.643, 8.857){3V};
    \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (1.107, 6.143){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (0.786, 6.429){0V};
    \draw[-latex] (1.571, 6.286) -- (2.286, 6.857);
    \draw[-latex] (1.571, 6) -- (2.286, 5.571);
    \draw (2.571, 7.199) -- (2.571, 5.659);
\end{tikzpicture}

### Voltage only drops if it has somewhere to go

Voltage drop only happens if electricity is flowing. Otherwise the voltage is the same everywhere

\begin{tikzpicture}
    % Paths, nodes and wires:
    \node[ground] at (2.571, 5.659){};
    \draw (2.571, 8.484) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (2.571, 7.199);
    \node[sground, yscale=-1] at (2.571, 8.484){};
    \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (0.893, 7.857){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (0.571, 8.143){3V};
    \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (0.857, 5.429){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (0.536, 5.714){0V};
    \draw[-latex] (1.286, 8.143) -- (2.286, 8.571);
    \draw[-latex] (1.429, 7.714) -- (2.286, 7.286);
    \draw[-latex] (1.571, 5.429) -- (2.286, 5.571);
\end{tikzpicture}

### NOT ALLOWED

\begin{columns}
    \begin{column}{0.5\textwidth}
        We assume:
        \begin{itemize}
            \item Top rail fixed at V>0
            \item Bottom rail fixed at 0V
            \item Wires have zero resistance
        \end{itemize}
    \end{column}
    \begin{column}{0.5\textwidth}
        \begin{tikzpicture}
            % Paths, nodes and wires:
            \node[ground] at (1, 8){};
            \node[sground, yscale=-1] at (1, 9){};
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (1.813, 9.429){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (1.196, 9.786){V>0};
            \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (1.679, 7.714){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (1.357, 8){V=0};
            \draw (1, 9) -- (1, 8);
        \end{tikzpicture}		\end{column}
\end{columns}

If you try to build this, one of those assumptions will fail. What might that look like?

### Historical Transistors

\includegraphics[width=0.5\columnwidth]{images/tube-transistor-wiki}

### Modern Transistors

\includegraphics[width=\columnwidth]{images/semiconductor-transistor-overkill}

### Transistor Behavior

% https://www.101computing.net/creating-logic-gates-using-transistors/

\begin{tikzpicture}
    % Paths, nodes and wires:
    \node[ground] at (1, 6.286){};
    \node[sground, yscale=-1] at (1, 9){};
    \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (1.813, 9.429){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (1.196, 9.786){V>0};
    \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (1.429, 5.857){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (1.107, 6.143){V=0};
    \draw (1, 8.857) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (1, 7.714);
    \draw (1, 9) -- (1, 8.857);
    \draw (1, 7.714) -- (2, 7.714);
    \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (2.67, 7.714){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (2.054, 8.071){output};
    \draw (-0.857, 7) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (0.143, 7);
    \draw (0.286, 7) -- (0.408, 7);
    \node[npn] at (1, 7){};
    \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (-1.714, 7){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (-2.33, 7.357){input};
\end{tikzpicture}

### Transistor Behavior

\begin{columns}
    \begin{column}{0.5\textwidth}
        \usetikzlibrary{shapes.geometric}
        \begin{tikzpicture}
            % Paths, nodes and wires:
            \node[ground] at (1, 6.286){};
            \node[sground, yscale=-1] at (1, 9){};
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (1.813, 9.429){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (1.196, 9.786){V>0};
            \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (1.429, 5.857){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (1.107, 6.143){V=0};
            \draw (1, 8.857) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (1, 7.714);
            \node[shape=ellipse, draw, line width=1pt, dash pattern={on 1pt off 2pt}, minimum width=1.149cm, minimum height=1.108cm] at (1, 7){};
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.965cm] at (-1.33, 7.143){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (-1.946, 7.643){input\\V>0};
            \draw (1, 6.571) to[cute closed switch] (1, 7.429);
            \draw (1, 9) -- (1, 8.857);
            \draw (1, 7.714) -- (1, 7.429);
            \draw (1, 6.571) -- (1, 6.286);
            \draw (1, 7.714) -- (2, 7.714);
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (2.67, 7.714){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (2.054, 8.071){??};
            \draw (-0.714, 7) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (0.286, 7);
            \draw (0.286, 7) -- (0.408, 7);
        \end{tikzpicture}
    \end{column}
    \begin{column}{0.5\textwidth}
        \usetikzlibrary{shapes.geometric}
        \begin{tikzpicture}
            % Paths, nodes and wires:
            \node[ground] at (1, 6.286){};
            \node[sground, yscale=-1] at (1, 9){};
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (1.813, 9.429){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (1.196, 9.786){V>0};
            \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (1.429, 5.857){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (1.107, 6.143){V=0};
            \draw (1, 8.857) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (1, 7.714);
            \node[shape=ellipse, draw, line width=1pt, dash pattern={on 1pt off 2pt}, minimum width=1.149cm, minimum height=1.108cm] at (1, 7){};
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.965cm] at (-1.33, 7.143){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (-1.946, 7.643){input\\V=0};
            \draw (1, 6.571) to[cute open switch] (1, 7.429);
            \draw (1, 9) -- (1, 8.857);
            \draw (1, 7.714) -- (1, 7.429);
            \draw (1, 6.571) -- (1, 6.286);
            \draw (1, 7.714) -- (2, 7.714);
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (2.67, 7.714){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (2.054, 8.071){??};
            \draw (-0.714, 7) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (0.286, 7);
            \draw (0.286, 7) -- (0.408, 7);
        \end{tikzpicture}
    \end{column}
\end{columns}

### Transistor Behavior

\begin{columns}
    \begin{column}{0.5\textwidth}
        \usetikzlibrary{shapes.geometric}
        \begin{tikzpicture}
            % Paths, nodes and wires:
            \node[ground] at (1, 6.286){};
            \node[sground, yscale=-1] at (1, 9){};
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (1.813, 9.429){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (1.196, 9.786){V>0};
            \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (1.429, 5.857){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (1.107, 6.143){V=0};
            \draw (1, 8.857) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (1, 7.714);
            \node[shape=ellipse, draw, line width=1pt, dash pattern={on 1pt off 2pt}, minimum width=1.149cm, minimum height=1.108cm] at (1, 7){};
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.965cm] at (-1.33, 7.143){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (-1.946, 7.643){input\\V>0};
            \draw (1, 6.571) to[cute closed switch] (1, 7.429);
            \draw (1, 9) -- (1, 8.857);
            \draw (1, 7.714) -- (1, 7.429);
            \draw (1, 6.571) -- (1, 6.286);
            \draw (1, 7.714) -- (2, 7.714);
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (2.67, 7.714){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (2.054, 8.071){output\\V=0};
            \draw (-0.714, 7) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (0.286, 7);
            \draw (0.286, 7) -- (0.408, 7);
        \end{tikzpicture}
    \end{column}
    \begin{column}{0.5\textwidth}
        \usetikzlibrary{shapes.geometric}
        \begin{tikzpicture}
            % Paths, nodes and wires:
            \node[ground] at (1, 6.286){};
            \node[sground, yscale=-1] at (1, 9){};
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (1.813, 9.429){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (1.196, 9.786){V>0};
            \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (1.429, 5.857){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (1.107, 6.143){V=0};
            \draw (1, 8.857) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (1, 7.714);
            \node[shape=ellipse, draw, line width=1pt, dash pattern={on 1pt off 2pt}, minimum width=1.149cm, minimum height=1.108cm] at (1, 7){};
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.965cm] at (-1.33, 7.143){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (-1.946, 7.643){input\\V=0};
            \draw (1, 6.571) to[cute open switch] (1, 7.429);
            \draw (1, 9) -- (1, 8.857);
            \draw (1, 7.714) -- (1, 7.429);
            \draw (1, 6.571) -- (1, 6.286);
            \draw (1, 7.714) -- (2, 7.714);
            \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (2.67, 7.714){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (2.054, 8.071){output\\V>0};
            \draw (-0.714, 7) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (0.286, 7);
            \draw (0.286, 7) -- (0.408, 7);
        \end{tikzpicture}
    \end{column}
\end{columns}

### Why two resistors?

In many cases, we can get away with just one resistor. The previous example had two. Why?

Always need a resistor between a voltage source and ground. Transistors have internal resistance but it's very small. Easy to burn them out

### More Complex Example

\begin{tikzpicture}
    % Paths, nodes and wires:
    \node[ground] at (1, 4.286){};
    \node[sground, yscale=-1] at (1, 9){};
    \node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (1.813, 9.429){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (1.196, 9.786){V>0};
    \node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (1.679, 4){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (1.357, 4.286){V=0};
    \draw (1, 5.571) to[american resistor, /tikz/circuitikz/bipoles/length=1.12cm] (1, 4.429);
    \node[npn] at (1, 8.143){};
    \node[npn] at (1, 6.429){};
    \draw (1, 9) -- (1, 8.913);
    \draw (1, 7.373) -- (1, 7.199);
    \draw (1, 5.659) -- (1, 5.571);
    \draw (1, 5.571) -- (2, 5.571);
    \draw (0.16, 8.143) -- (0, 8.143);
    \draw (0.16, 6.429) -- (0, 6.429);
    \draw (1, 4.429) -- (1, 4.286);
    \node[shape=rectangle, minimum width=0.668cm, minimum height=0.65cm] at (-0.22, 8.143){} node[anchor=north west, align=left, text width=0.28cm, inner sep=6pt] at (-0.571, 8.485){A};
    \node[shape=rectangle, minimum width=0.668cm, minimum height=0.65cm] at (-0.286, 6.429){} node[anchor=north west, align=left, text width=0.28cm, inner sep=6pt] at (-0.637, 6.771){B};
    \node[shape=rectangle, minimum width=0.668cm, minimum height=0.65cm] at (2.286, 5.628){} node[anchor=north west, align=left, text width=0.28cm, inner sep=6pt] at (1.934, 5.971){??};
\end{tikzpicture}




