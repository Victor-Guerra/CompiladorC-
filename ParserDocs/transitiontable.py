from transition import Transition
""" 
TransitionTable Class
author: Victor Emmanuel Guerra Aguado

Description: 
    The TransitionTable Class represents the implementation of a Deterministic 
    Finite Automaton for a given language into code. It performs everything the 
    DFA would.

Attributes:
    + isAcceptingState: [bool]; 
      The list that represents the Accepting States of the Automaton.
    + isErrorState: [bool]; 
      The list thar represents the Error States of the Automaton.
    + transitions: {str, [Transition]}; 
      The list of transitions of the DFA, the lists in the dictionary act as the 
      columns of a transition table, The specific transition is then obtained by 
      using the index as the row of the table.
    + keywords: [str]; 
      The Keywords of the language, exclusively keywords, no symbols.
    + valid_tokens: {str, int}; 
      The enumeration of the valid tokens of the language
"""
class TransitionTable:
    """ 
    TransitionTable Class Constructor

    __init__(self, 
             acceptingstates: [bool], 
             errorstates: [bool], 
             transitions: {str, [Transition]}, 
             keywords: [String], 
             valid_tokens: {String: Number}) -> TransitionTable
    """
    def __init__(self, acceptingstates: [bool], errorstates: [bool], 
        transitions: dict, keywords: [str], valid_tokens: {str, int}):
        self.isAcceptingState = acceptingstates
        self.isErrorState = errorstates
        self.transitions = transitions
        self.keywords = keywords
        self.valid_tokens = valid_tokens
        
    """
    TransitionTable accepts method

    Description:
        Method for finding out if the state provided is an Accepting State

    accepts(self, state: int) -> bool
    """
    def accepts(self, state: int) -> bool:
        return self.isAcceptingState[state]
     
    
    """
    TransitionTable errors method

    Description:
        Method for finding out if the state provided is an Error State

    errors(self, state: int) -> bool
    """
    def errors(self, state: int) -> bool:
        return self.isErrorState[state]

    """
    TransitionTable nextTransition method

    Description:
        Method for finding the transition that results by the given state and 
        condition.

    nextTransition(self, state: int, condition: str) -> Transition
    """
    def nextTransition(self, state: int, condition: str) -> Transition:
        transition = self.transitions["INVALIDCH"][state]
        for col in self.transitions:
            if condition in col:
                transition = self.transitions[col][state]
                break
         
        return transition