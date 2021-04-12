from ply import lex


tokens = (
    "START_FUNCTION",
    "START_LAMBDA",
    "START_COMMENT",
    "START_STR",
    "NUMBER",
    "EQUALS",
    "LPAREN",
    "RPAREN",
)

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_EQUALS = r"="


def t_START_STR(t):
    r'\'|"|"{3}|\'{3}'
    t.value = '"'
    return t


# A regular expression rule with some action code
def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# Unmatched caracter are ignore here cause irelevant for the linter
def t_error(t):
    t.lexer.skip(1)


lexer = lex.lex()
