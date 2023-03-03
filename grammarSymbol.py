"""
GrammarSymbol Class
author: Victor Emmanuel Guerra Aguado

Description: 
    The GrammarSymbol class provides an abstraction of the grammar symbols present in 
    a Context Free Grammar.
Attributes:
    + name: str; 
        The name of the GrammarSymbol object
"""
class GrammarSymbol:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, o: object):
        if isinstance(o, GrammarSymbol):
            return self.name == o.name
        return False
    
    """
    GrammarSymbol toStr method

    Description:
        Provides a way to transform the GrammarSymbol Object into a string of characters 
        that can be printed onto the screen for visualization or written into a 
        file for storage.

    toStr(self) -> str
    """
    def toStr(self) -> str:
        return f"({self.name})"
        
class NonTerminalSymbol(GrammarSymbol):
    def __init__(self, name: str):
        self.name = name
        
