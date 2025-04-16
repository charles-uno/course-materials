#!/usr/bin/bash

# Case 0: compile the code

TEST_CASE_NAME="compile"

rm a.out 
gcc char_flipper.s 
if [[ "$?" != "0" || -f a.out ]]; then 
    echo "$TEST_CASE_NAME - ok"
else
    echo "$TEST_CASE_NAME - build failed"
fi

# Case 1: lowercase to uppercase

TEST_CASE_NAME="upper_to_lower"

INPUT="g"
EXPECTED_OUTPUT="Enter a letter: Flipped case: G"
ACTUAL_OUTPUT=$(echo "$INPUT" | ./a.out)

if [[ "$EXPECTED_OUTPUT" != "$ACTUAL_OUTPUT" ]]; then
    echo "$TEST_CASE_NAME - expected \"$EXPECTED_OUTPUT\" but got \"$ACTUAL_OUTPUT\""
else
    echo "$TEST_CASE_NAME - ok"
fi

# Case 2: uppercase to lowercase

TEST_CASE_NAME="lower_to_upper"

INPUT="Q"
EXPECTED_OUTPUT="Enter a letter: Flipped case: q"
ACTUAL_OUTPUT=$(echo "$INPUT" | ./a.out)

if [[ "$EXPECTED_OUTPUT" != "$ACTUAL_OUTPUT" ]]; then
    echo "$TEST_CASE_NAME - expected \"$EXPECTED_OUTPUT\" but got \"$ACTUAL_OUTPUT\""
else
    echo "$TEST_CASE_NAME - ok"
fi

# Test case 3: not a letter

TEST_CASE_NAME="bad_input"

INPUT="&"
EXPECTED_OUTPUT="Enter a letter: Invalid letter: &"
ACTUAL_OUTPUT=$(echo "$INPUT" | ./a.out)

if [[ "$EXPECTED_OUTPUT" != "$ACTUAL_OUTPUT" ]]; then
    echo "$TEST_CASE_NAME - expected \"$EXPECTED_OUTPUT\" but got \"$ACTUAL_OUTPUT\""
else
    echo "$TEST_CASE_NAME - ok"
fi