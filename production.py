from grammarSymbol import GrammarSymbol

"""
Production Class
author: Victor Emmanuel Guerra Aguado

Description: 
    The Production Class provides a structure for the entries made into the list
    of Productions of the language grammar.

Attributes:
    + lhs: GrammarSymbol; 
      The symbol at the left-hand-side of the production.
    + rhs: [GrammarSymbol]; 
      The list of symbols that appear at the right-hand-side of the production.
"""
class Production: 
    def __init__(self, lhs: GrammarSymbol, rhs: [GrammarSymbol]):
        self.lhs = lhs
        self.rhs = rhs

