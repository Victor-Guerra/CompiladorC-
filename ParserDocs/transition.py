"""
Transition Class
author: Victor Emmanuel Guerra Aguado

Description: 
    The Transition Class provides a structure for the entries made into the 
    Transition Table made as an implementation of the DFA of a language.

Attributes:
    + target: int; 
      The state to which this transition points.
    + isConsuming: bool; 
      Whether this specific transition causes the DFA to advance to the next 
      character.
"""
class Transition:
    """ 
    Transition Class Constructor

    __init__(self, target: int, consumes: bool) -> Transition
    """
    def __init__(self, target: int, consumes: bool):
        self.target = target
        self.isConsuming = consumes