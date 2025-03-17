#!/usr/bin/bash

# exit on error
set -e


# Lowercase to uppercase
./armtest char_flipper.s -i 'g' -o 'Enter a letter: Flipped case: G'

# Uppercase to lowercase
./armtest char_flipper.s -i 'B' -o 'Enter a letter: Flipped case: b'

# Bad input (non letter)
./armtest char_flipper.s -i '?' -o 'Enter a letter: Invalid letter: ?' -r 1


