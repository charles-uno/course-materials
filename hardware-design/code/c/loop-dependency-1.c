

// Each addition depends on the previous one.
// The CPU must wait for result 'a' to calculate 'b'.
for (int i = 0; i < 100000000; i++) {
    res = (res + data[i]); 
}

