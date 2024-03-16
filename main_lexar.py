import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LFLOWERPAREN',
    'RFLOWERPAREN',
    'BOXLPAREN',
    'BOXRPAREN',
    'ID',
    'comma',
    'conditionalint',
    'string',
    'assignment',
    'newline',
    'and',
    'or',
    'quote',
    'ps',
    'dollar',
    'rangevalue'
]

# Regular expression rules for simple tokens
t_rangevalue = r'\.\.'
t_dollar = r'\$'
t_LFLOWERPAREN = r'\{'
t_RFLOWERPAREN = r'\}'
t_BOXLPAREN = r'\['
t_BOXRPAREN = r'\]'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_comma = r'\,'
t_and = r'\&&'
t_or = r'\|\|'
t_conditionalint = r'\-gt|-lt|-eq|-ne|-le|-ge'
reserved = {'echo': 'ECHO',
            r'if': 'IF',
            'then': 'THEN',
            'else': 'ELSE',
            'while': 'WHILE',
            'until': 'UNTIL',
            'fi': 'endif',
            'elif': 'ELIF',
            'do': 'DO',
            'done': 'DONE',
            'unset': 'UNSET',
            'for': 'FOR',
            'in': 'IN',
            'function': 'FUNCTION',
            }
t_string = r'\[a-zA-Z_0-9!@\#%^&\*()-\+]*'

t_assignment = r'\='
tokens = tokens + list(reserved.values())
# print(tokens)


# A regular expression rule with some action code
def t_NUMBER(t):
    r"""\d+"""
    t.value = int(t.value)
    return t


def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_ps(t):
    r"""\"?[a-zA-Z0-9]+\"?"""
    t.type = reserved.get(t.value, 'ps')
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    print("Line Number :", t.lineno)
    t.lexer.skip(1)
