
import ply.yacc as yacc
import ply.lex as lex

from main_lexar import *

lexar = lex.lex()


# Get the token map from the lexer.  This is required.
# Gammer for All statements.
def p_statement(p):
    """
    statement ::= assign
    statement ::= if
    statement ::= while
    statement ::= print
    statement ::= for
    statement ::= unset
    statement ::= until
    statement ::= function
    statement ::= statement statement
    """

# Grammer for while loop.


def p_while(p):
    """while : WHILE boolean DO statement DONE """

# Grammer for `for` loop.


def p_for(p):
    """ for : FOR ID IN rangefor DO statement DONE
        rangefor : factor
        rangefor : factor rangefor
        rangefor : ps
        rangefor : range
        """

# Grammer for funciton Defination.


def p_fucntion(p):
    """ function : FUNCTION ID LPAREN RPAREN LFLOWERPAREN statement RFLOWERPAREN
        function : ID LPAREN RPAREN LFLOWERPAREN statement RFLOWERPAREN"""

# Grammer for range of an array.


def p_range(p):
    """ range : LFLOWERPAREN NUMBER rangevalue NUMBER rangevalue NUMBER RFLOWERPAREN
              | LFLOWERPAREN NUMBER rangevalue NUMBER RFLOWERPAREN """

# Grammer for until loop.


def p_until(p):
    """until : UNTIL boolean DO statement DONE """

# Grammer for unset.


def p_unset(p):
    """ unset : UNSET ID """

# Grammer for echo.


def p_print(p):
    """
    print ::= ECHO S
        S ::= S S
        S ::= S comma S
        S ::= expression
         S ::= ps
        S ::= boolean
        S ::= dollar ID
    """

# Grammer for if condition stms.


def p_if(p):
    """
    if ::= IF bif THEN statement ELSEIF
    ELSEIF ::= ELIF bif  THEN statement ELSEIF
    ELSEIF ::= ELSE statement endif
            | endif
    bif ::= boolean
    bif ::= expression
    """

# Grammer for assignment.


def p_assign(p):
    """assign ::= ID assignment expression
    assign ::= ID assignment string"""

# Grammer for evaluation id/bools.


def p_boolean(p):
    """
    boolean ::= BOXLPAREN Con
    Con ::= c1 conditionalint c1 morecon
    c1  ::= expression
    c1 ::= string
    morecon ::= BOXRPAREN
            |  or Con
            |  and Con
    """

# Grammer for arithment +.


def p_expression_plus(p):
    """
    expression : expression PLUS term"""

# Grammer for arithment -.


def p_expression_minus(p):
    """
    expression : expression MINUS term"""

# Grammer for ID .


def p_factor_id(p):
    """factor : ID"""
    # if p[1] in a:
    #     p[0] = a[p[1]]
    # else:
    #     print(f'"{p[1]}" variable not defined in line',p.lineno(1))
    #     p_error(p)


def p_expression_term(p):
    """expression : term
                    """

# Grammer for arithment *.


def p_term_times(p):
    """term : term TIMES factor"""

# Grammer for arithment /.


def p_term_div(p):
    """term : term DIVIDE factor"""


def p_term_factor(p):
    """term : factor"""


def p_factor_num(p):
    """factor : NUMBER"""


def p_factor_expr(p):
    """factor : LPAREN expression RPAREN"""


# Error rule for syntax errors
def p_error(p):
    global error
    error = 1
    print("Syntax error in input")
    # if p:
    #     print(p.lineno)
    #     print(p.lexpos)


# Build the parser
parser = yacc.yacc()


if __name__ == "__main__":
    while True:
        code = ''
        error = 0
        try:
            print("---------------------------------------------------------------------")
            print(
                "Enter code  - (type the word 'end' in new line to stop taking input) \n")
            i = 1
            while True:
                s = input(f'{i}) $ ')
                if s == "end":
                    break
                i += 1
                if code == '':
                    code = s
                else:
                    code = code + '\n' + s
            s1 = code
            # print(code)
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(code, tracking=True)
        # print(f"Output :\n{result}")
        print("---------------------------------------------------------------------")
