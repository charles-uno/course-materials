beamer: true
---

# Assembly Conditionals

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

