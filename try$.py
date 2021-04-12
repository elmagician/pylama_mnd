from src.linter.parse import lexer


## TEst:
# Test it out
data = """
    major=18
    def test():
        if age > 18:
            print("Il peut boire au volant")
"""

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
