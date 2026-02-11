
# Logic Representation


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
