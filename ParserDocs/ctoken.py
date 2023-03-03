from grammarSymbol import GrammarSymbol
"""
Token Class
author: Victor Emmanuel Guerra Aguado

Description: 
    The Token Class provides a value object for the tokens created in the 
    Lexical Analysis phase of a compiler.

Attributes:
    + name: str;
      The name of the token.
    + line: int;
      The line in which this token was detected during the lexical analysis
      phase.
    + keyword_id: int; 
      The number that tells what type of valid word for the language the token 
      represents.
    + symboltable_ref: int; 
      The ID number that indicates an entry to a Symbol Table, if not an 
      IDENTIFIER or NUMERICAL_CONST, it defaults to -1.
    
"""
class Token(GrammarSymbol):
    """
    Token Class Constructor
    
    __init__(self, kwid: int, st_ref: int) -> Token
    """
    def __init__(self, name: str= "", line: int = None, kwid: int = 0, st_ref: int = None):
        self.name = name
        self.line = line
        self.keyword_id = kwid
        self.symboltable_ref = st_ref

    def __eq__(self, o: object):
        if isinstance(o, Token):
            return self.kwid == o.kwid and self.symboltable_ref == o.symboltable_ref
        return False

    """
    Token toStr method

    Description:
        Provides a way to transform the Token Object into a string of characters 
        that can be printed onto the screen for visualization or written into a 
        file for storage.

    toStr(self) -> str
    """
    def toStr(self) -> str:
        if self.symboltable_ref is None:
           return f"({self.keyword_id})"
        return f"({self.keyword_id}, {self.symboltable_ref})"
        
    """
    Token fromStr method

    Description:
        Provides a way to transform Strings of characters created by the 
        Token.print method into an actual Token Object in order to work with 
        previously printed Token Objects.

    fromStr(str: str) -> Token
    """
    def fromStr(tokenstr: str):
        temp = tokenstr[1: -1:].split(",")
        return Token(int(temp[0]), int(temp[0]))
