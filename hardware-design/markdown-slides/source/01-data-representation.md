
# Data Representation}

### How do computers store information?

Computers work using electrical signals which can be on or off. If we let:

- On means 1
- Off means 0

We can use sequences of 0s and 1s to represent information

## Positive Integers in Binary

### Numbers in Base Ten (aka Decimal)

Let's start by talking about how we write numbers normally.

For example, let's look at the number 109:

\begin{align*}
    109 & = 100 \;+\; 0 \;+\; 9                                   \\
        & = 1 \Times 10^2 \;+\; 0 \Times 10^1 \;+\; 9 \Times 10^0
\end{align*}

This way of writing numbers is called base ten. We use ten digits (0 to 9 inclusive) and each position in the number is scaled by a power of ten.

In terms of math, there is nothing special about base ten. We probably use it because we have ten fingers. Some ancient civilizations used sompletely different systems for counting!

### Numbers in Base Two (aka Binary)

Computers don't have fingers. They express everything as sequences of 1s and 0s. This format is called binary:

\begin{align*}
    0b1101101 & =
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

Importantly: we always use the prefix ``0b'' to avoid confusion when writing numbers in binary.

1101 is one thousand one hundred and one

0b1101 is thirteen

### Converting from Decimal to Binary

If the number is odd, append a 1 on the left. Otherwise, append a 0. Then
divide your decimal number by two and ignore any remainder. Repeat until your
decimal number is zero. \\

For example, starting with 58:

- 58 is even, so append *0*. Divide by two, leaving 29.
- 29 is odd, so append *1*0. Divide by two, leaving 14.
- 14 is even, so append *0*10. Divide by two, leaving 7.
- 7 is odd, so append *1*010. Divide by two, leaving 3.
- 3 is odd, so append *1*1010. Divide by two, leaving 1.
- 1 is odd, so append *1*11010. Divide by two, leaving 0.

So 58 in binary is 0b111010.

### Converting from Binary to Decimal

We can confirm by converting back. The rightmost bit is worth 1, then 2, then 4, and so on:

\begin{align*}
    0b111010 & =
    1 \Times 2^5 +
    1 \Times 2^4 +
    1 \Times 2^3 +
    0 \Times 2^2 +
    1 \Times 2^1 +
    0 \Times 2^0                          \\
                & = 32 + 16  + 8 + 0 + 2 + 0 \\
                & = 58
\end{align*}

### Addition in Binary

Binary addition works just like decimal addition. Start from the right, add straight down, and carry when you run out of digits.

For example:

\begin{equation*}
    \begin{array}{ccccccccc}
        1 & 1 & 1 & 1 & 1 &   &   &   &   \\
            & 0 & 0 & 1 & 1 & 1 & 0 & 0 & 0 \\
        + & 1 & 1 & 1 & 0 & 1 & 0 & 0 & 1 \\
        \hline
        1 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 \\
    \end{array}
\end{equation*}

What happens if we try to perform this operation but we only have 8 bits to store the answer?


### Multiplication in Binary

Binary multiplication works just like decimal multiplication.
Multiply the top number by the rightmost digit of the bottom number.
Then move to the next line, add a zero, and repeat for the next digit.
Finally, add up the lines. For example:

\begin{equation*}
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
\end{equation*}

### Division in Binary

To divide by 2, shift the bits one place to the right.

To divide by 4, shift the bits two places to the right.

That's about as deep as we go in this class. If you're curious to learn more,
see the textbook.

## Hexadecimal

### What? Why?

Binary is how machines store data. But writing out binary by hand is a chore.
In practice, it's often convenient to use hexadecimal (base 16) instead.

    - Decimal uses ten digits, 0-9
    - Binary uses two digits, 0 and 1
    - Hexadecimal uses sixteen digits: 0-9 along with A-F

Hexadecimal values are always prefixed with ``0x'' to avoid ambiguity.

### Converting Between Binary and Hexadecimal

Converting back and forth between binary and hexadecimal does not require any
math! Every four bits become one hex digit.

\begin{align*}
    0b0000 & = 0x0 = 0 & 0b1000 & = 0x8 = 8  \\
    0b0001 & = 0x1 = 1 & 0b1001 & = 0x9 = 9  \\
    0b0010 & = 0x2 = 2 & 0b1010 & = 0xA = 10 \\
    0b0011 & = 0x3 = 3 & 0b1011 & = 0xB = 11 \\
    0b0100 & = 0x4 = 4 & 0b1100 & = 0xC = 12 \\
    0b0101 & = 0x5 = 5 & 0b1101 & = 0xD = 13 \\
    0b0110 & = 0x6 = 6 & 0b1110 & = 0xE = 14 \\
    0b0111 & = 0x7 = 7 & 0b1111 & = 0xF = 15 \\
\end{align*}

### Converting Hexadecimal to Decimal

Hexadecimal is base 16. So each place corresponds to a power of 16.

\begin{align*}
    0x3AB & = 3 \times 16^2 + 10 \times 16^1 + 11 \times 16^0 \\
            & = 3 \times 256 + 10 \times 16 + 11 \times 1       \\
            & = 768 + 160 + 11                                  \\
            & = 954                                             \\
\end{align*}

Hexadecimal is very compact! These numbers get big fast

### Arithmetic in Hexadecimal

Addition and multiplication work in hexadecimal just like they do in binary and
decimal. Just be careful about carrying.

\begin{equation*}
    \begin{array}{ccccc}
        1 &   &   & 1 &   \\
            & 4 & 1 & 7 & B \\
        + & C & 2 & 0 & F \\
        \hline
        1 & 0 & 3 & 8 & A \\
    \end{array}
\end{equation*}

## Negatives in Binary

### First Attempt: Signed Magnitude

We can use the first digit to hold the sign, then the rest of the digits to
hold magnitue:

- 0b*0*1011001 is positive 0b10110001, so 89
- 0b*1*1011001 is negative 0b1011001, so -89

This is nice and straightforward!

### Addition and Subtraction with Signed Magnitude

Adding positive numbers works just the same. But what happens if we throw a minus sign in there?

For example, let's look at 12 - 5. First, rewrite it as 12 + (-5). Then:

\begin{equation*}
    \begin{array}{ccccccccc}
            & 0 & 0 & 0 & 0 & 1 & 1 & 0 & 0 \\
        + & 1 & 0 & 0 & 0 & 0 & 1 & 0 & 1 \\
        \hline
            & ? & ? & ? & ? & ? & ? & ? & ? \\
    \end{array}
\end{equation*}

We know the result should be 7 (0b00000111). But our regular rules for addition do not get us there.

### Zero with Signed Magnitude

Using signed magnitude, 0b00000000 is zero.

And 0b10000000 is negative zero (which is also zero).

Using this convention, we have to worry about the difference between numerical
equality and bitwise equality. That seems pretty messy.

### Can We Do Better?

Signed magnitude was a swing and a miss. What do we want when we talk about negative numbers?

- We want positive numbers to work like we expect
- We want 0b00000000 to be zero, with no ambiguity
- We want addition and subtraction to work the same for positive and negative

### Another Idea: Two's Complement

We know 1 - 1 = 0. Put another way, 1 + (-1) = 0. Can we work backwards from there to figure out how to write -1?

\begin{equation*}
    \begin{array}{ccccccccc}
            & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
        + & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
        \hline
            & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    \end{array}
\end{equation*}

Remember: on a computer, our numbers have to fit in a set number of bits.
Anything past that gets thrown away. This is called overflow. In this case,
overflow works in our favor!

### Working Backwards from Zero

We can use the same trick to identify the rest of the negative numbers:

- 0b00000000 is 0
- 0b11111111 is -1
- 0b11111110 is -2
- 0b11111101 is -3
- 0b11111100 is -4
- etc

### The Sign Bit (Again)

We only have 256 possible integers. How do we decide where the positives end and the negatives begin?

Unsigned int: bits are worth 1, 2, 4, 8, 16, 32, 64, 128

Signed magnitude: bits are worth $\pm1, \pm2, \pm4, \pm8, \pm16, \pm32, \pm64$,
and the last bit tells us whether to use positive or negative (yikes)

Two's complement: bits are worth 1, 2, 4, 8, 16, 32, 64, \Highlight{-128}

Range of possible values is -128 to 127.

### Flipping Signs in Two's Complement

To flip the sign of a two's complement integer, flip all the bits then add 1. Ignore the overflow (if any). This works for both positive and negative numbers.

For example:

- 55 is 0b01010111
- Flip the bits: 0b10101000, then add 1: 0b10101001
- So -55 is 0b10101001
- Flip the bits again: 0b01010110, add 1: 0b01010111
- So -(-55) = 55 = 0b01010111

What happens if we negate zero?

### Overflow

Overflow is important for two's complement. It ensures that positive zero and negative zero are the same. But it is also a constraint!

Try adding 0b01101001 + 0b01011010:

\begin{equation*}
    \begin{array}{ccccccccc}
            &   & 1 & 1 & 1 &   &   &   &   \\
            & 0 & 1 & 1 & 0 & 1 & 0 & 0 & 1 \\
        + & 0 & 1 & 0 & 1 & 1 & 0 & 1 & 0 \\
        \hline
            & 1 & 1 & 0 & 0 & 0 & 0 & 1 & 1 \\
    \end{array}
\end{equation*}

These are two's complement numbers. Convert them to decimal. What just happened?

## Fractions and Decimals

### The Decimal Point

Sometimes we need to store numbers that aren't integers.

Before we worry about binary, what does 21.867 mean?

\begin{align*}
    21.867 & = 2 \Times 10^1 + 1 \Times 10^0 + 8 \Times ?? + 6 \Times ?? + 7 \Times ??
\end{align*}

### The Decimal Point

In decimal:

\begin{align*}
    21.867 & = 2 \Times 10^1 + 1 \Times 10^0 + 8 \Times 10^{-1} + 6 \Times 10^{-2} + 7 \Times 10^{-3}             \\
            & =2 \Times 10 + 1 \Times 1 + 8 \Times \frac{1}{10} + 6 \Times \frac{1}{100} + 7 \Times \frac{1}{1000} \\
\end{align*}

In binary, we can use the same idea:

\begin{align*}
    0b101.010 & = 1 \Times 2^2 + 0 \Times 2^1 + 1 \Times 2^0 + 0 \Times 2^{-1} + 1 \Times 2^{-2} + 0 \Times 2^{-3} \\
                & = 1 \Times 4 + 0 + 1 \Times 1 + 0 + 1 \Times \frac{1}{4} + 0                                       \\
                & = 5.25                                                                                             \\
\end{align*}

### Fixed Point Representation

The computer just stores 1s and 0s, not decimal points. How do we distinguish
these values?

- 0b0101110.1 = 46.5
- 0b010111.01 = 23.25
- 0b01011.101 = 11.625

One option is to specify the location of the decimal point ahead of time. For
example, we could say that our eight-bit binary decimal always has two decimal
bits.

What is an upside of this approach? What is a downside?

### Floating Point Representation

Floating point numbers are a bit more complicated, but much more flexible. For
a 16-bit floating point number we get:

- 1 bit for the sign
- 5 bits for the exponent (value -14 to 15)
- 10 bits for the significand (value 0 to 1023)

To turn those components into a value we use:

\begin{align*}
    \text{value} & = (-1)^{\text{sign}} \times 2^{\text{exponent} - 15} \times \left(1 + \frac{\text{significand}}{1024} \right)
\end{align*}

Why offset the exponent?

Why add 1 to the significand fraction?

### Floating Point Examples

\begin{align*}
    \underbrace{0}_\text{sign} \; \underbrace{01111}_\text{exponent} \; \underbrace{0000000000}_\text{significand} & = (-1)^0 \times 2^{15 - 15} \times \left( 1 + \frac{0}{1024} \right) \\
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


### Floating Point Special Cases

\begin{equation*}
    \begin{array}{ccccr}
        0 & 00000 & 0000000000     & = 0          \\
        1 & 00000 & 0000000000     & = -0         \\
        0 & 11111 & 0000000000     & = \infty     \\
        1 & 11111 & 0000000000     & = -\infty    \\
        0 & 11111 & \text{nonzero} & = \text{NaN} \\
    \end{array}
\end{equation*}

There's more to it than this. If you're curious, read up on subnormal numbers
[here](https://en.wikipedia.org/wiki/Half-precision_floating-point_format)

### Floating Point for Big Integers

If we're dealing with big numbers, floating point often works better than fixed
point. This is true even if both formats use the same number of bits.

- 8-bit unsigned integer: max value 255
- 16-bit unsigned integer: max value 65,535
- 32-bit unsigned integer: max value 4.2 billion 
- 16-bit floating point: max value 65,504 (also handles negatives, fractions)
- 32-bit floating point: max value 340 billion billion billion billion (also handles negatives, fractions)

### Floating Point Limitations

So what's the catch?

## Beyond Numbers

### What else do computers store?

There are many cases where we want a computer to store non-numerical data:

- Text
- Colors
- Sounds
- Images
- Videos
- Websites

### Characters and Strings
	
- Each character is represented by a number
- The most straightforward encoding is ASCII
- Modern use cases typically use Unicode (much bigger)
- To make a string, put a bunch of characters in a row
- Question: how do we identify the end of a string?

### ASCII Table

\includegraphics[width=\columnwidth]{images/ascii-table}

### Colors and Images
	
- A color can be described by three numbers (R, G, B)
- We can represent an image as a grid of colored pixels
- Question: do we need a null byte at the end of a pixel/row/image? Why or why not?

\includegraphics[width=\columnwidth]{images/mario-pixels}

### Sound

- Sound is pressure vibrations in the air
- We can create sound by moving a speaker cone rapidly
- To store sound, store the movement of the speaker cone

\includegraphics[width=0.5\columnwidth]{images/speakers}

### Structured Data

- When you go to a website, how does your browser know what to display?
- When you add an item to your online cart, what data is sent?

\begin{columns}
    \begin{column}{0.5\textwidth}
        \includegraphics[width=\columnwidth]{images/html-example}
    \end{column}
    \begin{column}{0.5\textwidth}
        \includegraphics[width=\columnwidth]{images/json-example}
    \end{column}
\end{columns}









