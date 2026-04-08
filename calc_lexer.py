import ply.lex as lex

tokens: tuple[str, ...] = (
    'NUMBER',
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

reserved: dict[str, str] = {}

t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'

def t_NUMBER(t):
    r'(-?)(\d+\.\d+|\d+)([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"[Lexer] Illegal character '{t.value[0]}' at line {t.lexer.lineno} — skipping.")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == '__main__':
    test_expression = input("Enter a mathematical expression: ")

    print(f"Input  : {test_expression!r}")
    print("-" * 50)
    print(f"{'Token Type':<12} {'Value'}")
    print("-" * 50)

    lexer.input(test_expression)

    for tok in lexer:
        print(f"{tok.type:<12} {tok.value}")

    print("-" * 50)
    print("Lexical analysis complete.")