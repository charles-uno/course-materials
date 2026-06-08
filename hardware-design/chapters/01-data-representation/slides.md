beamer: true
template: slides.tex
---

### Goals

Goals for this chapter:

@@goals@@

### How do computers store information?

Computers work using electrical signals which can be on or off. If we let:

- On means 1
- Off means 0

We can use sequences of 0s and 1s to represent information

# Positive Integers

### Numbers in Base Ten (aka Decimal)

Let's start by talking about how we write numbers normally:

$$$
\begin{center}$\begin{array}{ccccccc}
	109 & = & 100 & + & 0 & + & 9                                   \\
		& = & 1 \Times 10^2 & + & 0 \Times 10^1 & + & 9 \Times 10^0
\end{array}$\end{center}
$$$

This way of writing numbers is called decimal, or base ten. We use ten digits (0 to 9 inclusive) and each position in the number is scaled by a power of ten.

In terms of math, there is nothing special about base ten. We probably use it
because we have ten fingers. Some ancient civilizations used sompletely
different systems for counting!

### Numbers in Base Two (aka Binary)

Computers don't have fingers. They express everything as sequences of 1s and 0s. This format is called binary:
$$$
\begin{align*}
    0\text{b}1101101 & =
    1 \Times 2^6 +
    1 \Times 2^5 +
    0 \Times 2^4 +
    1 \Times 2^3 +
    1 \Times 2^2 +
    0 \Times 2^1 +
    1 \Times 2^0                              \\
                & = 64 + 32 + 0 + 8 + 4 + 0 + 1 \\
                & = 109                         \\
\end{align*}
$$$

Importantly: we always use the prefix "0b" to avoid confusion when writing numbers in binary.

- 1101 is one thousand one hundred and one
- 0b1101 is thirteen

### Converting from Decimal to Binary

Divide your decimal number by two and keep track of the remainder. Repeat until your
decimal number is zero.

For example, starting with 58:

- 58/2 = 29, remainder 0
- 29/2 = 14, remainder 1
- 14/2 = 7, remainder 0
- 7/2 = 3, remainder 1
- 3/2 = 1, remainder 1
- 1/2 = 0, remainder 1

So, reading from the bottom, 58 in binary is 0b111010.

### Converting from Binary to Decimal

We can confirm by converting back. The rightmost bit is worth 1, then 2, then
4, and so on:
$$$
\begin{align*}
    0\text{b}111010 & =
    1 \Times 2^5 +
    1 \Times 2^4 +
    1 \Times 2^3 +
    0 \Times 2^2 +
    1 \Times 2^1 +
    0 \Times 2^0                          \\
                & = 32 + 16  + 8 + 0 + 2 + 0 \\
                & = 58
\end{align*}
$$$

### Addition in Binary

Binary addition works just like decimal addition.
Start from the right, add straight down, and carry when you run out of digits.

For example:
$$$
\[
    \begin{array}{ccccccccc}
         & 1 & 1 & 1 & 1 &   &   &   &   \\
            & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 \\
        + & 0 & 1 & 1 & 0 & 1 & 0 & 0 & 1 \\
        \hline
         & 1 & 0 & 1 & 0 & 0 & 0 & 0 & 1 \\
    \end{array}
\]
$$$

### Multiplication in Binary

Binary multiplication works just like decimal multiplication.
Multiply the top number by the rightmost digit of the bottom number.
Then move to the next line, add a zero, and repeat for the next digit.
Finally, add up the lines. For example:
$$$
\[
\begin{array}{cccccc}
        &   &        & 1 & 1 & 0 \\
        &   & \times & 1 & 0 & 1 \\
    \hline
        &   &        & 1 & 1 & 0 \\
        &   & 0      & 0 & 0 & 0 \\
    + & 1 & 1      & 0 & 0 & 0 \\
    \hline
        & 1 & 1      & 1 & 1 & 0 \\
\end{array}
\]
$$$

### Division in Binary

To divide by 2, shift the bits one place to the right.

To divide by 4, shift the bits two places to the right.

That's about as deep as we go in this class. If you're curious to learn more,
see the textbook.

### Overflow

- Let's say we are using 8-bit binary numbers. 
- What happens when we add $0b11111111 + 0b00000001$?

### Overflow

- Let's say we are using 8-bit binary numbers
- What happens when we add $0b11111111 + 0b00000001$?
- The sum is 0b100000000 (9 bits long), but we only have 8 bits to store it
- In some situations, an overflow error may crash your program
- Most of the time, the computer silently throws away the extra bit
- This is called **overflow**

### Hexadecimal

Binary is how machines store data. But writing out binary by hand is a chore.
In practice, it's often convenient to use hexadecimal (base 16) instead.

- Decimal uses ten digits, 0-9
- Binary uses two digits, 0 and 1
- Hexadecimal uses sixteen digits: 0-9 along with A-F

Hexadecimal values are always prefixed with "0x" to avoid ambiguity.

### Converting Between Binary and Hexadecimal

Converting back and forth between binary and hexadecimal does not require any
math! Every four bits become one hex digit.

|||

| Binary | Hex | Decimal |
|--------|-----|---------|
| 0b0000   | 0x0   | 0 |
| 0b0001   | 0x1   | 1 |
| 0b0010   | 0x2   | 2 |
| 0b0011   | 0x3   | 3 |
| 0b0100   | 0x4   | 4 |
| 0b0101   | 0x5   | 5 |
| 0b0110   | 0x6   | 6 |
| 0b0111   | 0x7   | 7 |

| Binary | Hex | Decimal |
|--------|-----|---------|
| 0b1000   | 0x8   | 8 |
| 0b1001   | 0x9   | 9 |
| 0b1010   | 0xA   | 10 |
| 0b1011   | 0xB   | 11 |
| 0b1100   | 0xC   | 12 |
| 0b1101   | 0xD   | 13 |
| 0b1110   | 0xE   | 14 |
| 0b1111   | 0xF   | 15 |

|||

### Converting from Decimal to Hexadecimal

Hexadecimal is base 16. So each place corresponds to a power of 16.
$$$
\begin{align*}
    0x3AB & = 3 \times 16^2 + 10 \times 16^1 + 11 \times 16^0 \\
            & = 3 \times 256 + 10 \times 16 + 11 \times 1       \\
            & = 768 + 160 + 11                                  \\
            & = 954                                             \\
\end{align*}
$$$

Hexadecimal is very compact! These numbers get big fast

### Arithmetic in Hexadecimal

Addition and multiplication work in hexadecimal just like they do in binary and
decimal. Just be careful about carrying.
$$$
\[
    \begin{array}{ccccc}
        1 &   &   & 1 &   \\
            & 4 & 1 & 7 & B \\
        + & C & 2 & 0 & F \\
        \hline
        1 & 0 & 3 & 8 & A \\
    \end{array}
\]
$$$

Note: it's very easy to make mistakes by hand. I will **not** ask you to do this on the quiz.

### Summary

- We normally write numbers in decimal. Ten digits, each place scaled by a power of ten
- Computers use binary. Two digits, each place scaled by a power of two
- Rules for addition and multiplication are the same
- Hexadecimal (base 16) is like binary but more compact

### Group Work

TODO: this

# Negative Integers

### Recall: Overflow

For 8-bit addition, $0b11111111 + 0b00000001 = 0b00000000$

255 + 1 = 0

### Counting Backwards from Zero

- The computer says $0b11111111 + 0b00000001 = 0b00000000$
- In other words: $0b11111111 + 1 = 0$
- Can we say $0b11111111 = -1$?
- Likewise 0b11111110 is -2
- 0b11111101 is -3
- 0b11111100 is -4
- etc

### Negative Integers in Binary

8-bit unsigned integer:
- Bits are worth 1, 2, 4, 8, 16, 32, 64, 128
- Range of possible values: 0 to 255

8-bit signed integer:
- Bits are worth 1, 2, 4, 8, 16, 32, 64, **-128**
- Range of possible values is -128 to 127.

This way of writing signed integers is called **two's complement**.

Important: the computer just stores ones and zeroes! It does not know if 0b11111111 is -1 or 255. That must be tracked within your program

### Flipping Signs

To flip the sign of a two's complement binary integer, flip all the bits then add 1. Ignore the overflow (if any). This works for both positive and negative numbers.

For example:

- 55 is 0b01010111
- Flip the bits: 0b10101000, then add 1: 0b10101001
- So -55 is 0b10101001
- Flip the bits again: 0b01010110, add 1: 0b01010111
- So -(-55) = 55 = 0b01010111

What happens if we negate zero?

### Binary Subtraction

TODO: this slide

### Overflow

Overflow is important for two's complement. It ensures that positive zero and negative zero are the same. But it is also a constraint!

Try adding 0b01101001 + 0b01011010:

$$$
\[
    \begin{array}{ccccccccc}
            &   & 1 & 1 & 1 &   &   &   &   \\
            & 0 & 1 & 1 & 0 & 1 & 0 & 0 & 1 \\
        + & 0 & 1 & 0 & 1 & 1 & 0 & 1 & 0 \\
        \hline
            & 1 & 1 & 0 & 0 & 0 & 0 & 1 & 1 \\
    \end{array}
\]
$$$
These are two's complement numbers. Convert them to decimal. What just happened?

### Group Work

Let's perform 58 - 87 in binary:

- Convert 58 to binary
- Convert 87 to binary
- Compute -87 in binary
- Add 58 + (-87) in binary
- Convert the result back to decimal

# Non-Integer Data

### What else do computers store?

There are many cases where we want a computer to store non-numerical data:

- Fractions/decimals
- Text
- Colors
- Sounds
- Images
- Videos
- Websites
- Multiple things at once

### The Decimal Point

Sometimes we need to store numbers that aren't integers.

Before we worry about binary, what does 21.867 mean?
$$$
\begin{align*}
    21.867 & = 2 \Times 10^1 + 1 \Times 10^0 + 8 \Times ?? + 6 \Times ?? + 7 \Times ??
\end{align*}
$$$

### Fixed Point Decimals

In decimal:
$$$
\begin{align*}
    21.867 & = 2 \Times 10^1 + 1 \Times 10^0 + 8 \Times 10^{-1} + 6 \Times 10^{-2} + 7 \Times 10^{-3}             \\
            & =2 \Times 10 + 1 \Times 1 + 8 \Times \frac{1}{10} + 6 \Times \frac{1}{100} + 7 \Times \frac{1}{1000}
\end{align*}
$$$
In binary, we can use the same idea:
$$$
\begin{align*}
    0b101.010 & = 1 \Times 2^2 + 0 \Times 2^1 + 1 \Times 2^0 + 0 \Times 2^{-1} + 1 \Times 2^{-2} + 0 \Times 2^{-3} \\
                & = 1 \Times 4 + 0 + 1 \Times 1 + 0 + 1 \Times \frac{1}{4} + 0                                       \\
                & = 5.25                                                                                            
\end{align*}
$$$

### Fixed Point Decimals

The computer just stores 1s and 0s, not decimal points. How do we distinguish these values?
- 0b0101110.1 = 46.5
- 0b010111.01 = 23.25
- 0b01011.101 = 11.625

### Floating Point Representation

Floating point numbers are a bit more complicated, but much more flexible. For
a 16-bit floating point number we get:

- 1 bit for the sign
- 5 bits for the exponent (value -14 to 15)
- 10 bits for the mantissa (value 0 to 1023)

To turn those components into a value we use:
$$$
\begin{align*}
    \text{value} & = (-1)^{\text{sign}} \times 2^{\text{exponent} - 15} \times \left(1 + \frac{\text{mantissa}}{1024} \right)
\end{align*}
$$$

Why offset the exponent?

Why add 1 to the mantissa fraction?

% normalizing to 1.xxx gives us a free bit of precision

% Explanation here for the 127 offset: https://www.quora.com/Why-do-we-add-127-to-the-exponent-in-IEEE-754-floating-number-format-to-get-the-actual-exponent-value

### Floating Point Examples

$$$
	\begin{align*}
		\underbrace{0}_\text{sign} \; \underbrace{01111}_\text{exponent} \; \underbrace{0000000000}_\text{mantissa} & = (-1)^0 \times 2^{15 - 15} \times \left( 1 + \frac{0}{1024} \right) \\
		                                                                                                               & = 1 \times 2^0   \times \left( 1 + 0 \right)                         \\
		                                                                                                               & = 1                                                                  \\
	\end{align*}
	\begin{align*}
		0 \; 01101 \; 0101010101 & = (-1)^0 \times 2^{13 - 15} \times \left( 1 + \frac{341}{1024} \right) \\
		                         & \approx 0.33325195                                                     \\
	\end{align*}
	\begin{align*}
		1 \; 11110 \; 1111111111 & = (-1)^1 \times 2^{30 - 15} \times \left( 1 + \frac{1023}{1024} \right) \\
		                         & = -65504                                                                \\
	\end{align*}
$$$

### Floating Point Special Cases

| Sign | Exp   | Mantissa   | $\rightarrow$ | Meaning   |
|------|-------|------------|---------------|-----------|
| 0    | 00000 | 0000000000 | $\rightarrow$ |  0        |
| 1    | 00000 | 0000000000 | $\rightarrow$ | -0        |
| 0    | 11111 | 0000000000 | $\rightarrow$ | $\infty$  |
| 1    | 11111 | 0000000000 | $\rightarrow$ | $-\infty$ |
| 0    | 11111 | nonzero    | $\rightarrow$ | NaN       |

There's more to it than this. If you're curious, read up on subnormal numbers [here](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)

### Floating Point for Big Integers

If we're dealing with big numbers, floating point often works better than fixed
point. This is true even if both formats use the same number of bits.

- 8-bit unsigned integer: max value 255
- 16-bit unsigned integer: max value 65,535
- 32-bit unsigned integer: max value 4.2 billion 
- 16-bit floating point: max value 65,504 (also handles negatives, fractions)
- 32-bit floating point: max value 340 billion billion billion billion (also handles negatives, fractions)

% 4,294,967,295
% 340,282,346,638,528,859,811,704,183,484,516,925,440 

### Floating Point Limitations

So what's the catch?

% can't express some numbers exactly. 0.1 + 0.2 = 0.30000000000000004
% loss of precision when subtracting similar numbers
% large gap between representable large numbers

% ### Group Exercises
% TODO: this

%        \item Convert 0b100110.10 from fixed-point binary to decimal.
%        \item Convert 23.75 from decimal to fixed-point binary.
%        \item Add fixed-point binary numbers 0b101101.01 + 0b010011.11. Convert to decimal to confirm your result.
%        \item Show that the 16-bit floating point expression ${1 \; 01000 \; 1100000000}$ is equal to -3.5 in decimal.


### Characters and Strings

- Each character is represented by a number
- The most straightforward encoding is ASCII
- Modern use cases typically use Unicode (accents, emoji, etc)
- To make a string, put a bunch of characters in a row
- Question: how do we identify the end of a string?

### ASCII Table
$$$
\includegraphics[width=\columnwidth]{images/ascii-table}
$$$

### Character Encodings

- ASCII strictly uses one byte per character
- Unicode uses 1-4 characters per bit
- How 

% ASCII is 128 characters. first bit of the byte is always zero. go from there
% first 128 characters of unicode are backwards compatible

### Color and Images

- A color can be described by three numbers (R, G, B)
- We can represent an image as a grid of colored pixels
- Question: do we need a null byte at the end of a pixel/row/image? Why or why not?
![video game sprite by pixel](images/mario-pixels)

### Sound

- Sound is pressure vibrations in the air
- We can create sound by moving a speaker cone rapidly
- To store sound, store the movement of the speaker cone
![speakers](images/speakers)

### Video

### Serializing Structured Data

- When you go to a website, how does your browser know what to display?
- When you add an item to your online cart, what data is sent?

|||
![example html](images/html-example)

![example json](images/json-example)
|||

% ### Group Exercises
% TODO: this

### Summary

- We can approximate decimals as fractions
- We can express fractions using integers
- We can express sound and color using integers
- Strings are sequences of characters
- We can express characters using integers
- Integers can be converted to binary

# Transforming Binary Data

### Hashing

### Checksums

### Compression

### Space/Time Tradeoff

### Lossy vs Lossless

### Encryption
