



TEST_CASES := $(wildcard tests/*.incl.md)

test: clean
	@for TC in $(TEST_CASES); do ./test-md2tex.py $$TC; done

clean:
	@ rm tests/*.gen.tex