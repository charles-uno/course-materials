beamer: true
---

# Assembly Conditionals

## Branching

### Branch (and Sometimes Link)

Recall from our hello world program:

- We print with `bl printf`
- We exit the program with `b exit`

And recall from the instruction cycle:

- Special register PC is the program counter
- PC holds the address of the next instruction

### Manipulating the Program Counter

`b` is **branch**. It updates PC. This causes us to "jump" to a different part of the code.

`bl` is **branch and link**. It also updates PC. But first it stores the *current* PC in the link register. This makes it possible for us to return from the 




it also sets the link register (LR) so we know how to get back.





### Branching

- `b`
- `bl`


### Conditional Branching

- cmp
- beq
- bne
- blt
- ble
- bgt
- bge

### If

```python
if x > 0:
    print("positive")
```

### If/Else

```python
if x > 0:
    print("positive")
else:
    print("negative or zero")
```

### For Loop

```python
for x in range(5):
    print(x)
```

What does this actually do?

```
x = 0
loop:
print(x)
x += 1
if x < 5:
    goto loop
```

### While Loop

