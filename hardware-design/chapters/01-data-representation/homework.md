template: assignment.tex
date: February 22, 2027
---

# Data Representation

Please work through each exercise individually. Check your answer against two peers. If there is any disagreement, talk it out until everyone is on the same page.

## Integers

Do these exercises by hand. Do not use any calculator. This is important practice for the test. Show your work!

Make sure to include the appropriate prefixes on binary and hex values. The numbers $1011$, $0b1011$, and $0x1011$ are very different!

1. Read Sections 4.1, 4.2, and 4.3 from [Dive Into Systems](https://diveintosystems.org/book/index.html). Write down something you learned.
1. Convert $0b10010001$ from 8-bit binary to decimal. 
1. Convert $0b01111001$ to decimal.
1. Convert $0b00000000$ to decimal.
1. Convert $0b11111111$ to decimal. 
1. Convert $0b00110011$ to decimal. 
1. Convert $79$ from decimal to 8-bit binary.
1. Convert $36$ to binary.
1. Convert $64$ to binary.
1. Convert $7$ to binary. 
1. Convert $55$ to binary.
1. Compute binary addition $0b01110011 + 0b00001001$. Convert to decimal to check your result.
1. Compute binary addition $0b00110011 + 0b10011001$. 
1. Compute binary multiplication $0b00011101 \times 0b00000011$. 
1. Compute binary multiplication $0b00000111 \times 0b00001001$. 
1. Convert $0xE7$ to binary. 
1. Convert $0x9B$ to binary. 
1. Convert $0b00011100$ to hexadecimal. 
1. Convert $0b01011001$ to hexadecimal. 
1. Convert $0xE7$ to decimal.
1. Convert $0x9B$ to decimal. 
1. Convert $0x75$ to decimal. 
1. Convert $1677$ to hexadecimal.
1. Convert $250$ to hexadecimal. 
1. Convert $172$ to hexadecimal. 
1. Read Sections 4.4, 4.5, and 4.8 from [Dive into Systems](https://diveintosystems.org/book/index.html). Write down something you learned
1. Convert $-123$ to signed magnitude binary.
1. Convert $-98$ to signed magnitude binary.
1. Convert $-56$ to signed magnitude binary. 
1. Convert $-123$ to two's complement binary. 
1. Convert $-98$ to two's complement binary. 
1. Convert $-56$ to two's complement binary.
1. Compute binary subtraction $0b00001001 - 0b01110011$. Convert to decimal to check your result.
1. Compute binary subtraction $0b00000011 - 0b10011001$.
1. When adding the two's complement binary numbers $0b01101110$ and $0b01000100$, does an overflow error occur?
1. When adding the two's complement binary numbers $0b01101110$ and $0b11111111$, does an overflow error occur?
1. When adding the two's complement binary numbers $0b10001110$ and $0b11111111$, does an overflow error occur?
1. When adding the two's complement binary numbers $0b10001110$ and $0b10000001$, does an overflow error occur?
1. What are the minimum and maximum values that can be represented as an 8-bit unsigned binary integer?
1. What are the minimum and maximum values that can be represented as an 8-bit signed binary integer?
1. What are the minimum and maximum values that can be represented as an 8-bit two's complement binary integer?

## Fractions \& Decimals

1. Convert $0b0101.1010$ to decimal.
1. Convert $0b110010.11$ to decimal. 
1. This exercise walks you through converting the following IEEE 754 standard floating point binary number to decimal. You are *not* expected to memorize this process.
    $10111010100110000010000000000000$
    The first (left-most) bit is the sign bit. What is the sign bit?
    
    Is the number above positive or negative?
    
    After the sign bit, then next eight bits are the exponent bits, representing an unsigned binary integer. What are these eight bits? 
    
    The remaining bits are the significand bits. What are these bits? 
    
    Imagine there is a binary point before the start of these bits, and convert the resulting binary fixed point number into decimal. Your answer should be between 0 and 1. 
            
    To put these pieces together, we use: $(-1)^{\textrm{[sign bit]}}\times 2^{\textrm{[converted exponent bits]}} \times 1.\textrm{[converted significand bits]}$

## Serialization


Look up an ASCII table. and use it to fill out the corresponding values for each character below. Enter values in decimal. An ASCII table will be provided if you need one on the test.
            
1. Write the string $"CSCI241"$ as a sequence of ASCII values. Don't forget the null byte at the end of the string.
1. Write the string $"h3ll0 :)"$ as a sequence of ASCII values.





1. Convert 0b01011001 from binary to decimal.
1. Convert 243 from decimal to binary.
1. Convert 0x13 from hexadecimal to binary (do not convert to decimal in between).
1. Convert 0b11110110 from binary to hexadecimal (do not convert to decimal in between).
1. Convert 0x13 from hex to decimal.
1. Convert 10957 from decimal to hex.
1. Convert -17 to 8-bit signed magnitude binary.
1. Convert -17 to 8-bit two's complement binary.
1. Compute the sum 0b11010111 + 0b01001001 of two's complement binary integers. Verify your computation by converting the summands and result to decimal.
1. Compute the difference 0b10000111 - 0b01001001 of two's complement binary integers. Convert all three integers to decimal to verify your answer.
1. Compute the product 0b00000110 * 0b00001111 of two's complement binary integers. Convert all three integers to decimal to verify your answer.
1. Convert the unsigned fixed point binary number 0b01.100010 into decimal.
1. Find each character in the table below, and fill in its ASCII value (in decimal).
    TODO
1. Write the string "Hardware Design" as a sequence of ASCII values, by matching up each character with its ASCII value. Don't forget the null character!

## Encryption

Person A: create your public and private keys

1. Choose two prime numbers $p$ and $q$ between 50 and 100. Keep $p$ and $q$ secret
2. Compute $n = pq$
3. Compute the lowest common multiple of $p-1$ and $q-1$. This value is called $\lambda$. You may use any tool you like. Keep $\lambda$ secret
4. Choose a prime number $e < \lambda$
5. Find a value $d$ such that $e \cdot d \equiv 1 \pmod{\lambda}$. You may use any tool you like. Keep $d$ secret
6. Share $n$ and $e$ with person B. These two values make up your public key

Person B: encrypt a message for person A using their public key

1. Choose a number $m < n$. Keep $m$ secret
2. Compute $c = m^e \pmod{n}$. You may use any tool you like
3. Share $c$ (your encrypted number) with person A

Person A: decrypt the message using your private key

1. Compute $m = c^d \pmod{n}$. You may use any tool you like






