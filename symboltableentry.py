"""
SymbolTableEntry Class
author: Victor Emmanuel Guerra Aguado

Description: 
    The SymbolTableEntry Class provides a structure for the entries made into a 
    Symbol Table during the Lexical Analysis phase of a Compiler.

Attributes:
    + value: str; 
      The value to be stored as an entry of the symbol table, represents a lexeme 
      recognized by the scanner.
    + fields: [str]; 
      Fields where any necessary extra information about the lexeme will be stored.
"""
class SymbolTableEntry:
    """
    SymbolTableEntry Class Constructor

    __init__(self, value: str, fields: [str]) -> SymbolTableEntry
    """
    def __init__(self, value: str, fields: [str] = []):
        self.value = value
        self.fields = fields
        

