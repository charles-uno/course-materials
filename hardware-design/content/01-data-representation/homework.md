title: Data Representation
date: 18 Feb, 2027
---

Please work through each exercise individually. Compare your answers with two peers. If there is any disagreement, talk it out until everyone is on the same page.

Please do the math by hand. Do not use a calculator or computer. This is important practice for the test. Show your work!

Make sure to include the appropriate prefixes on binary and hex values. The numbers 1011, 0b1011, and 0x1011 are very different! 

# Positive Integers

Recommended reading: sections 4.1, 4.2, and 4.4 from [Dive Into Systems](https://diveintosystems.org/book/index.html)

## Binary to Decimal

Convert each number from 8-bit binary to decimal. Show your work. 

1. Convert $0b10010001$ to decimal
1. Convert $0b01111001$ to decimal
1. Convert $0b00000000$ to decimal
1. Convert $0b11111111$ to decimal 
1. Convert $0b00110011$ to decimal 

## Decimal to Binary

Convert from decimal to 8-bit binary. Show your work. 

1. Convert $79$ to binary
1. Convert $36$ to binary
1. Convert $127$ to binary
1. Convert $7$ to binary
1. Convert $55$ to binary

## Binary Arithmetic

Perform each operation in binary. Convert to decimal to check your result. 

1. Compute $0b01110011 + 0b00001001$
1. Compute $0b00110011 + 0b10011001$
1. Compute $0b00011101 \times 0b00000011$
1. Compute $0b00000111 \times 0b00001001$

## Overflow

Which of the following operations will result in an overflow error using 8-bit binary?

1. Does $0b01101110 + 0b01000100$ overflow?
1. Does $0b01101110 + 0b11111111$ overflow?
1. Does $0b10001110 + 0b10000001$ overflow?
1. Does $0b00001100 \times 0b00001010$ overflow?

## Hexadecimal to/from Decimal

Convert values between decimal and hexadecimal. Show your work. 

1. Convert 250 to hex
1. Convert 172 to hex
1. Convert 0x9B to decimal 
1. Convert 0x75 to decimal 

## Hexadecimal to/from Binary

Convert values between binary and hexadecimal. Do not convert to decimal in between. Show your work.

1. Convert 0xE7 to binary
1. Convert 0x9B to binary
1. Convert 0b00011100 to hex
1. Convert 0b01011001 to hex

# Negative Integers

Recommended reading: section 4.3 and 4.5 from [Dive Into Systems](https://diveintosystems.org/book/index.html)

## Signed Magnitude

Convert decimal values to 8-bit signed magnitude binary. Show your work.

1. Convert $-123$ to signed magnitude binary
1. Convert $-98$ to signed magnitude binary
1. Convert $-56$ to signed magnitude binary

## Two's Complement

Convert decimal values to 8-bit two's complement binary. Show your work.

1. Convert $-123$ to two's complement binary. 
1. Convert $-98$ to two's complement binary. 
1. Convert $-56$ to two's complement binary.

## Binary Subtraction

Treat binary values below as 8-bit two's complement. Perform the subtractions in binary. Show your work. Convert to decimal to check your result.

1. Compute $0b00001001 - 0b01110011$
1. Compute $0b00000011 - 0b10011001$
1. Compute $0b00100011 - 0b00001001$

## Domain Comparison

1. What are the minimum and maximum values that can be represented as an 8-bit unsigned binary integer?
1. What are the minimum and maximum values that can be represented as an 8-bit signed binary integer?
1. What are the minimum and maximum values that can be represented as an 8-bit two's complement binary integer?

# Non-Integer Data

Recommended reading: section 4.8 from [Dive Into Systems](https://diveintosystems.org/book/index.html)

## Fixed Point

1. Convert $0b0101.1010$ to decimal.
1. Convert $0b110010.11$ to decimal. 

## Floating Point

In this exercise we'll walk through converting a 16-bit floating point value (also called IEEE half-precision) to decimal. You are *not* expected to memorize this process.

Start with the binary value: 0b1100100101100000

1. The first bit is the sign bit. What is it?
1. The next five bits are the exponent. What are they?
1. Convert the exponent bits to decimal. Treat them like an *unsigned* 5-bit binary integer
1. The remaining bits are called the mantissa. What are they?
1. Convert the mantissa bits to decimal. Treat them like an unsigned 10-bit binary integer
1. Now plug those values into the following formula (S=sign, E=exponent, M=mantissa). What's the result?
   $$$
   $(-1)^{S} \; \times \; 2^{E - 15} \; \times \; \left(1 + \frac{M}{1024}\right)$
   $$$
1. Why do we subtract 15 from the exponent? How does this affect the range of possible values?
1. Why do we divide the mantissa by 1024? How does this affect the range of possible values?
1. There is another half-precision floating point format (called `bfloat16`) which uses an 8-bit exponent and a 7-bit mantissa. How would this affect the range and precision?

# Data Transformation



## ASCII

Look up an ASCII table. and use it to fill out the corresponding values for each character below. Enter values in decimal. An ASCII table will be provided if you need one on the test.
            
1. Write the string `"CSCI241"` as a sequence of ASCII values. Don't forget the null byte at the end of the string.
1. Write the string `"h3ll0 :)"` as a sequence of ASCII values.





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

In this exercise you and a peer will perform RSA encryption by hand. You may use a calculator for the math.

Person A: create your public and private keys

1. Choose two prime numbers $p$ and $q$ between 50 and 100. Keep $p$ and $q$ secret
2. Compute $n = pq$
3. Compute the lowest common multiple of $p-1$ and $q-1$. This value is called $\lambda$. Keep $\lambda$ secret
4. Choose a prime number $e < \lambda$
5. Find a value $d$ such that $e \cdot d \equiv 1 \pmod{\lambda}$. Keep $d$ secret
6. Share $n$ and $e$ with person B. These two values make up your public key

Person B: encrypt a message for person A using their public key

1. Choose a number $m < n$. Keep $m$ secret
2. Compute $c = m^e \pmod{n}$
3. Share $c$ (your encrypted number) with person A

Person A: decrypt the message using your private key

1. Compute $m = c^d \pmod{n}$
1. Confirm with your partner that you have correctly decrypted their value






