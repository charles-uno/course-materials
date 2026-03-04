

// Using two accumulators (res1, res2) breaks the dependency.
// A superscalar CPU can perform BOTH additions in the same cycle.
for (int i = 0; i < 100000000; i += 2) {
    res1 += data[i];
    res2 += data[i+1];
}
res = res1 + res2;