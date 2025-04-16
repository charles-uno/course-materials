#!/usr/bin/bash

# Case 0: compile the code

TEST_CASE_NAME="compile"

rm a.out 
gcc add_two.s 
if [[ "$?" != "0" || -f a.out ]]; then 
    echo "$TEST_CASE_NAME - ok"
else
    echo "$TEST_CASE_NAME - build failed"
fi

# Case 1: small positive ints

TEST_CASE_NAME="positive"

INPUT="3
4"
EXPECTED_OUTPUT="Enter a number: Enter a number: Sum: 7"
ACTUAL_OUTPUT=$(echo "$INPUT" | ./a.out)

if [[ "$EXPECTED_OUTPUT" != "$ACTUAL_OUTPUT" ]]; then
    echo "$TEST_CASE_NAME - expected \"$EXPECTED_OUTPUT\" but got \"$ACTUAL_OUTPUT\""
else
    echo "$TEST_CASE_NAME - ok"
fi

# Case 2: sum to zero

TEST_CASE_NAME="opposite"

INPUT="-3
3"
EXPECTED_OUTPUT="Enter a number: Enter a number: Sum: 0"
ACTUAL_OUTPUT=$(echo "$INPUT" | ./a.out)

if [[ "$EXPECTED_OUTPUT" != "$ACTUAL_OUTPUT" ]]; then
    echo "$TEST_CASE_NAME - expected \"$EXPECTED_OUTPUT\" but got \"$ACTUAL_OUTPUT\""
else
    echo "$TEST_CASE_NAME - ok"
fi

# Case 3: negatives

TEST_CASE_NAME="negative"

INPUT="-3
-106"
EXPECTED_OUTPUT="Enter a number: Enter a number: Sum: -109"
ACTUAL_OUTPUT=$(echo "$INPUT" | ./a.out)

if [[ "$EXPECTED_OUTPUT" != "$ACTUAL_OUTPUT" ]]; then
    echo "$TEST_CASE_NAME - expected \"$EXPECTED_OUTPUT\" but got \"$ACTUAL_OUTPUT\""
else
    echo "$TEST_CASE_NAME - ok"
fi
