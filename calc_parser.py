#Grammar rules and parser for the calculator
#expression : expression PLUS term
#           | expression MINUS term
#           | term
#term       : term TIMES factor
#           | term DIVIDE factor
#           | factor
#factor     : NUMBER
#           | ID
#           | LPAREN expression RPAREN  

import ply.yacc as yacc
from calc_lexer import tokens

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    pass

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    pass

def p_factor(p):
    '''factor : NUMBER
              | ID
              | LPAREN expression RPAREN'''
    pass

def p_error(p):
    if p:
        print(f"[Parser] Syntax error at token '{p.value}' (type: {p.type}) on line {p.lineno}.")
    else:
        print("[Parser] Syntax error at EOF.")

parser = yacc.yacc()

if __name__ == '__main__':
    test_expression = input("Enter a mathematical expression: ")
    parser.parse(test_expression)
    print("[Parser] Parsing completed.")