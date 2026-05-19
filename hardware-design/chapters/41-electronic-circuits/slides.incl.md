beamer: true
---

# Electronic Circuits

% resistors in parallel and in series

% need to talk about capacitors?

% Low-pass filter. Every wire has a little bit of resistance. two wires close together have capacitance. so the chip is full of accidental low-pass filters. This is a limit on how fast you can make the clock speed

% high-pass filter. edge detection. gives you a sharp edge on your clock ticks



## Electrical Circuits

### The Components
$$$
\begin{tikzpicture}
	% Paths, nodes and wires:
	\node[npn] at (3.269, 7.143){};
	\draw (7.857, 7.286) to[american resistor] (6.714, 7.286);
	\node[shape=rectangle, minimum width=1.696cm, minimum height=0.536cm] at (3.134, 5.913){} node[anchor=north west, align=left, text width=1.308cm, inner sep=6pt] at (2.269, 6.199){transistor};
	\node[shape=rectangle, minimum width=1.679cm, minimum height=0.536cm] at (7.429, 6.143){} node[anchor=north west, align=left, text width=1.291cm, inner sep=6pt] at (6.571, 6.429){resistor};
	\node[sground, yscale=-1] at (5.071, 3.714){};
	\node[ground] at (9.071, 4.429){};
	\node[shape=rectangle, minimum width=2.679cm, minimum height=0.536cm] at (5.071, 3.286){} node[anchor=north, align=center, text width=2.291cm, inner sep=6pt] at (5.071, 3.571){voltage source (fixed V>0)};
	\node[shape=rectangle, minimum width=3.679cm, minimum height=0.536cm] at (8.929, 3.429){} node[anchor=north, align=center, text width=3.291cm, inner sep=6pt] at (8.929, 3.714){ground\\(fixed V=0)};
	\draw (9.571, 7.286) -- (10.857, 7.286);
	\node[shape=rectangle, minimum width=1.679cm, minimum height=0.536cm] at (10.571, 6.143){} node[anchor=north west, align=left, text width=1.291cm, inner sep=6pt] at (9.714, 6.429){wire};
\end{tikzpicture}
$$$

### The Setup
$$$
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
$$$

### For Example
|||
- Input A can be true (V>0) or false (V=0)
- Same for input B
- Output may be true or false depending on inputs
- Let's discuss how these components behave
$$$
\begin{tikzpicture}
	% Paths, nodes and wires:
	\node[ground] at (5, 1.143){};
	\node[npn] at (5, 5){};
	\draw (2.857, 5) to[american resistor] (4, 5);
	\node[sground, yscale=-1] at (5, 5.857){};
	\node[npn] at (5, 3.286){};
	\draw (2.857, 3.286) to[american resistor] (4, 3.286);
	\draw (5, 2.429) to[american resistor] (5, 1.286);
	\draw (5, 2.714) -- (6, 2.714);
	\draw (5, 2.516) -- (5, 2.429);
	\draw (5, 1.286) -- (5, 1.143);
	\draw (5, 4.23) -- (5, 4.056);
	\draw (5, 5.857) -- (5, 5.77);
	\draw (4, 5) -- (4.16, 5);
	\draw (4, 3.286) -- (4.16, 3.286);
	\draw (2.857, 3.286) -- (2.571, 3.286);
	\draw (2.857, 5) -- (2.571, 5);
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (2.143, 5){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (1.857, 5.286){A};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (2.143, 3.286){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (1.857, 3.571){B};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (6.429, 2.714){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (6.143, 3){??};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (5.571, 6.429){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (5.286, 6.714){V>0};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (5.571, 0.857){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (5.286, 1.143){V=0};
\end{tikzpicture}
$$$
|||

### What is voltage?
	
- A measure of eletromagnetic potential energy
- Electricity "wants" to flow from high voltage to low voltage
- Similar to how a ball "wants" to roll down a slide

### Wires

- Perfectly conductive
- Voltage at one end of a wire is the same as the other
- Any shape you want, any number of connections

### Resistors
	
- A resistor has two ends
- If the voltage is different between the two ends, current flows
- As current flows through the resistor, it dissipates energy
- Examples: light bulb filament, toaster coils

### Water Slide Analogy
	
- Voltage source: top of the water slide
- Ground: pool at the bottom
- Wires: platform where you wait
- Resistors: the slide
- Transistors: lifeguards?
	
Let's come back to this in a minute

### Voltage Drops in the Resistor

Let's say this resistor is a light bulb. Does it light up?

$$$
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
$$$

### Voltage only drops if it has somewhere to go

Voltage drop only happens if electricity is flowing from source to ground. If the circuit is broken, resistors act like wires
$$$
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
$$$

### NOT ALLOWED

|||

We assume:
- Top rail fixed at V>0
- Bottom rail fixed at 0V
- Wires have zero resistance

$$$
\begin{tikzpicture}
	% Paths, nodes and wires:
	\node[ground] at (1, 8){};
	\node[sground, yscale=-1] at (1, 9){};
	\node[shape=rectangle, minimum width=1.197cm, minimum height=0.679cm] at (1.813, 9.429){} node[anchor=north west, align=left, text width=0.809cm, inner sep=6pt] at (1.196, 9.786){V>0};
	\node[shape=rectangle, minimum width=0.608cm, minimum height=0.536cm] at (1.679, 7.714){} node[anchor=north west, align=left, text width=0.22cm, inner sep=6pt] at (1.357, 8){V=0};
	\draw (1, 9) -- (1, 8);
\end{tikzpicture}
$$$
|||
If you try to build this, one of those assumptions will fail. What might that look like?

### Transistors
	
- Three connections: gate, source, drain
- If the gate is on, voltage can flow from source to drain
- If the gate is off, flow is blocked

### Back to the Water Slide Analogy
	
- Voltage source: top of the water slide
- Ground: pool at the bottom
- Wires: platform where you wait
- Resistors: the slide
- Transistor: lifeguard. Empty lifeguard station means the area is closed

### Transistor Behavior

% https://www.101computing.net/creating-logic-gates-using-transistors/
$$$
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
$$$

### Transistor Behavior
|||
$$$
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
$$$
|||
$$$
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
$$$
|||

### Transistor Behavior
|||
$$$
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
$$$
|||
$$$
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
$$$
|||

### Historical Transistors

Ok, but how do you build something with this behavior?

$$$
\includegraphics[width=0.5\columnwidth]{images/tube-transistor-wiki}
$$$

### Modern Transistors

This will **not** be on the test
$$$
\includegraphics[width=\columnwidth]{images/semiconductor-transistor-overkill}
$$$

### Why do we have resistors on the inputs?
	
- Sometimes you see these, sometimes you don't
- When in doubt, use an extra resistor
- Too many resistors can cause your circuit to do nothing
- Too few resistors can allow things to catch fire

### Back to the example from earlier
$$$
	\begin{tikzpicture}
		% Paths, nodes and wires:
		\node[ground] at (5, 1.143){};
		\node[npn] at (5, 5){};
		\draw (2.857, 5) to[american resistor] (4, 5);
		\node[sground, yscale=-1] at (5, 5.857){};
		\node[npn] at (5, 3.286){};
		\draw (2.857, 3.286) to[american resistor] (4, 3.286);
		\draw (5, 2.429) to[american resistor] (5, 1.286);
		\draw (5, 2.714) -- (6, 2.714);
		\draw (5, 2.516) -- (5, 2.429);
		\draw (5, 1.286) -- (5, 1.143);
		\draw (5, 4.23) -- (5, 4.056);
		\draw (5, 5.857) -- (5, 5.77);
		\draw (4, 5) -- (4.16, 5);
		\draw (4, 3.286) -- (4.16, 3.286);
		\draw (2.857, 3.286) -- (2.571, 3.286);
		\draw (2.857, 5) -- (2.571, 5);
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (2.143, 5){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (1.857, 5.286){A};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (2.143, 3.286){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (1.857, 3.571){B};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (6.429, 2.714){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (6.143, 3){??};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (5.571, 6.429){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (5.286, 6.714){V>0};
		\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (5.571, 0.857){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (5.286, 1.143){V=0};
	\end{tikzpicture}
$$$

### Group Exercises

For the circuit on the previous slide:
	
- Work in groups!
- Draw this circuit four times on the board
- Plug in the four combinations of A and B inputs
- Figure out the output for each case
- Write out the truth table
- What is this?
	
### Another Two-Transistor Circuit
$$$
\begin{tikzpicture}
	% Paths, nodes and wires:
	\node[ground] at (12.569, 0.711){};
	\node[npn] at (12.14, 5.283){};
	\draw (9.854, 5.283) to[american resistor] (10.997, 5.283);
	\node[sground, yscale=-1] at (12.997, 6.426){};
	\node[npn] at (13.283, 3.569){};
	\draw (9.854, 3.569) to[american resistor] (10.997, 3.569);
	\draw (12.569, 1.997) to[american resistor] (12.569, 0.854);
	\draw (12.569, 0.854) -- (12.569, 0.711);
	\draw (9.854, 3.569) -- (9.569, 3.569);
	\draw (9.854, 5.283) -- (9.569, 5.283);
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (9.14, 5.283){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (8.854, 5.569){A};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (9.14, 3.569){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (8.854, 3.854){B};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (14.714, 2.286){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (14.429, 2.571){??};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (13.569, 6.997){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (13.283, 7.283){V>0};
	\node[shape=rectangle, minimum width=0.536cm, minimum height=0.536cm] at (13.14, 0.426){} node[anchor=north west, align=left, text width=0.148cm, inner sep=6pt] at (12.854, 0.711){V=0};
	\node[jump crossing] at (12.143, 3.569){};
	\draw (12.14, 6.053) -- (12.14, 6.283) -- (13.283, 6.283) -- (13.283, 4.339);
	\draw (12.997, 6.426) -- (12.997, 6.283);
	\draw (12.143, 3.709) -- (12.14, 4.513);
	\draw (10.997, 5.283) -- (11.283, 5.283);
	\draw (13.283, 2.799) -- (13.283, 2.569) -- (12.14, 2.569) -- (12.14, 3.426);
	\draw (10.997, 3.569) -- (11.997, 3.569);
	\draw (12.283, 3.569) -- (12.426, 3.569);
	\draw (12.569, 1.997) -- (12.569, 2.569);
	\draw (12.569, 2.283) -- (14.283, 2.283);
\end{tikzpicture}
$$$






