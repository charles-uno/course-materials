#!/usr/bin/bash

# exit as soon as we hit an error
# set -e

function run_and_check {
    local TEST_CASE_NAME="$1"
    local INPUT="$2"
    local EXPECTED_OUTPUT="$3"
    ACTUAL_OUTPUT=$(echo "$INPUT" | ./a.out) ||:
    if [[ "$EXPECTED_OUTPUT" != "$ACTUAL_OUTPUT" ]]; then
        echo "$TEST_CASE_NAME - expected \"$EXPECTED_OUTPUT\" but got \"$ACTUAL_OUTPUT\""
    else
        echo "$TEST_CASE_NAME - ok"
    fi
}


# Case 0: compile the code
CASE_NAME="compile"
rm a.out ||:
gcc add_two.s 
if [[ "$?" != "0" || -f a.out ]]; then 
    echo "$CASE_NAME - ok"
else
    echo "$CASE_NAME - build failed"
fi

# Case 1: small positive ints
CASE_NAME="positive"
INPUT="3
4"
EXPECTED_OUTPUT="Enter a number: Enter a number: Sum: 7"
run_and_check "$CASE_NAME" "$INPUT" "$EXPECTED_OUTPUT"

# Case 2: sum to zero
CASE_NAME="opposite"
INPUT="-3
3"
EXPECTED_OUTPUT="Enter a number: Enter a number: Sum: 0"
run_and_check "$CASE_NAME" "$INPUT" "$EXPECTED_OUTPUT"

# Case 3: negatives
CASE_NAME="negative"
INPUT="-3
-106"
EXPECTED_OUTPUT="Enter a number: Enter a number: Sum: -109"
run_and_check "$CASE_NAME" "$INPUT" "$EXPECTED_OUTPUT"


