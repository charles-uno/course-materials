template: assignment.tex
date: February 22, 2027
---

# Data Representation

Please work through each exercise individually. Check your answer against two peers. If there is any disagreement, talk it out until everyone is on the same page.

## Positive Integers in Binary

fizz

buzz



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






