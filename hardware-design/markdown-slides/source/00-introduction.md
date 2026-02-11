# Introduction

### Course Overview 

![dune robot hbo](images/dune-robot-hbo)

Thou shalt not make a machine in the likeness of a human mind

- Dune, Frank Herbert

## Grading

### Peer Reviews

- Participation score (10\% of your total grade) is mostly based on peer reviews
- Reviews will be short. Less than one page. They should include *specific examples* of ways your peers helped you succeed
- You can get full credit here without too much trouble. Show up. Work together. Make it easy for your peers to write nice things about you
- I recommend keeping notes over the course of the semester when someone is particularly helpful, insightful, etc

### Important Links

- Dive Into Systems: https://diveintosystems.org/book/index.html
- Doenet: https://www.doenet.org/course?tool=dashboard&courseId=_GnqAk2zB64CHKPeZY9Ren
- ARM Tutorial: https://diveintosystems.org/book/C9-ARM64/index.html
- ARM Simulator: http://163.238.35.161/~zhangs/arm64simulator/
- Circuitverse: https://circuitverse.org/simulator


### Hello World

```C
#include <stdio.h>

int main() {
    printf("Hello world!\n");
    return 0;
}
```


### Align Example

\begin{align*}
    f(A, B) & = \text{(A or B) and not (A and B)}               \\
            & = \LogicAnd{(\LogicOr{A}{B})}{(\LogicNand{A}{B})} \\
\end{align*}


