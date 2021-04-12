# pylama_mnd

Linter for magic number with PyLama

## What is a magic number

This linter considers a magic number to be:

- a digit or number greater than 1
- used in a function or as named arguments
- in a function: not assigned to a variable

/!\ HTTP status code will be considered as magic numbers. I will try to add a settings to avoid it but for now, you can
ever use HTTPStatus libs or ignore errors locally.

## Grammar

```Ocaml
MND:
    FILE: PASS START_FUNCTION FUN FILE
    FUN: START_COMMENT PASS \n | START_STR PASS START_STR | ASSIGN | NUMBER => MND Error | PASS
    
    START_FUNCTION -> def
    START_LAMBDA -> lambda
    START_COMMENT -> #
    START_STR -> ' | " | """ | '''
    NUMBER -> 0|1|...|9
    PASS -> anything not interesting here.
```
