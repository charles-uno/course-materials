
# None of the built-in lexers work well for ARM v7 assembly
# trying to create a custom lexer
# Working from https://tex.stackexchange.com/questions/699890/custom-language-lexer-alias-not-found-by-pygments-for-minted
# Also looking at the existing ones, eg /opt/homebrew/lib/python3.14/site-packages/pygments/lexers/ada.py

# usage should look about like:
"""
	\begin{minted}{'armlexer.py:MyCustomLexer -x'}
		.section .rodata
		greeting: .ascii "Hello world!\n\0"

		.section .text
		.global _start
		@ execution starts here
		_start:
		ldr r0, =greeting
		bl printf
		mov r0, #0
		bl exit
	\end{minted}
"""

from pygments.lexer import RegexLexer, words
from pygments.lexer import DelegatingLexer, RegexLexer, include, \
    bygroups, using, default, words, combined, this
from pygments.util import get_bool_opt, shebang_matches
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Generic, Other, Error, Whitespace
from pygments import unistring as uni

class ArmLexer(RegexLexer):
    name = 'arm'
    aliases = ['armv7', 'assembly', 'assembler']
    filenames = ['*.s']

    tokens = {
        'root': [
            (r'@.*$', Comment.Single),
            (r'\\\n', Text),
            (r'\\', Text),
            include('numbers'),
            include('builtins'),
        ],
        'numbers': [
            (r'#[0-9]+', Number.Integer),
        ],
        'builtins': [
            (words((
                '.section', '.global', '.text', '.global', '.data', '.rodata'), prefix=r'(?<!\.)', suffix=r'\b'),
             Name.Builtin),],
    }


MyLexer = ArmLexer