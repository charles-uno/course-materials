
// fewer jumps

for (int i = 0; i < 100000000/4; i+=4) {
    res1 += data[i];
    res2 += data[i+1];
    res3 += data[i+2];
    res4 += data[i+3];
}


// maybe also compile with -fno-tree-vectorize to see the difference from SIMD