# Introduction

### Course Overview 

![dune robot hbo](images/dune-robot-hbo)

\begin{center}
Thou shalt not make a machine in the likeness of a human mind
\end{center}
\begin{flushright}
Dune, Frank Herbert
\end{flushright}

## Grading

### Peer Reviews

- Participation score (10\% of your total grade) is mostly based on peer reviews
- Reviews will be short. Less than one page. They should include *specific examples* of ways your peers helped you succeed
- You can get full credit here without too much trouble. Show up. Work together. Make it easy for your peers to write nice things about you
- I recommend keeping notes over the course of the semester when someone is particularly helpful, insightful, etc

### Important Links

- Dive Into Systems: https://diveintosystems.org/book/index.html
- Doenet: https://www.doenet.org/course?tool=dashboard&courseId=_GnqAk2zB64CHKPeZY9Ren
- ARM Tutorial: https://diveintosystems.org/book/C9-ARM64/index.html
- ARM Simulator: http://163.238.35.161/~zhangs/arm64simulator/
- Circuitverse: https://circuitverse.org/simulator


### Hello World

```C
#include <stdio.h>

int main() {
    printf("Hello world!\n");
    return 0;
}
```


### Align Example

\begin{align*}
    f(A, B) & = \text{(A or B) and not (A and B)}               \\
            & = \LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})} \\
\end{align*}





### Tabular Example

	Fundamental boolean functions include AND, OR, and XOR:

	\begin{tabular}{c c c c c}
		A & B & A and B & A or B & A xor B \\
		\hline
		1 & 1 & 1       & 1      & 0       \\
		1 & 0 & 0       & 1      & 1       \\
		0 & 1 & 0       & 1      & 1       \\
		0 & 0 & 0       & 0      & 0
	\end{tabular}




### Columns and Tikz

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


