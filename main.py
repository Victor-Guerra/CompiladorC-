import sys
from compiler import Compiler
from transitiontable import TransitionTable
from transition import Transition

"""
    Main Program File for the C Minus Compiler
    author: Victor Emmanuel Guerra Aguado

Description:
    The main file of the entire compiler program, where the language definition is 
    provided, and the source code text is obtained. So far, the hardcoded language
    definition is compliant to both that of the C Minus language, and that of the
    class diagrams designed during the design phase.

Attributes:
    None
"""
if __name__ == "__main__":
    # Obtain a Compiler Object
    comp = Compiler()
    
    # Get the file to parse
    if len(sys.argv) < 2:
        sys.exit("Input file not provided.")
    
    filename = sys.argv[1]
    input_file = open(filename, 'r')
    
    input_txt = input_file.read()

    input_file.close()
    
    
    # To prepare the Scanner, define a transition table of a DFA
    acceptingstates = [
        0,0,0,0,0,
        0,0,0,0,0,
        1,1,1,1,1,
        1,1,1,1,1,
        1,1,1,1,1,
        1,1,1,1,1,
        1,1,1,1,1,
        1
    ]
    
    errorstates = [
        0,0,0,0,0,
        0,0,0,0,0,
        0,0,0,0,0,
        0,0,0,0,0,
        0,0,0,0,0,
        0,0,0,0,0,
        0,0,1,1,1,
        1
    ]

    transitions = {
        ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'): [
            Transition(1,True),Transition(1,True),Transition(35,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ], 
        ('0','1','2','3','4','5','6','7','8','9'):  [
            Transition(2,True),Transition(34,False),Transition(2,True),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('\n', ' ', '\r', '\t'): [
            Transition(0,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('<'): [
            Transition(3,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('>'): [
            Transition(4,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('='): [
            Transition(5,True),Transition(10,False),Transition(11,False),Transition(12,True),Transition(14,True),
            Transition(16,True),Transition(29,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('!'): [
            Transition(6,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('/'): [
            Transition(7,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(31,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('+'): [
            Transition(18,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('-'): [
            Transition(19,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('*'): [
            Transition(20,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(8,True),Transition(9,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        (';'): [
            Transition(21,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        (','): [
            Transition(22,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('('): [
            Transition(23,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        (')'): [
            Transition(24,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('['): [
            Transition(25,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        (']'): [
            Transition(26,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('{'): [
            Transition(27,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('}'): [
            Transition(28,True),Transition(10,False),Transition(11,False),Transition(13,False),Transition(15,False),
            Transition(17,False),Transition(33,True),Transition(30,False),Transition(8,True),Transition(8,True), 
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
        ('INVALIDCH'): [
            Transition(32,True),Transition(32,True),Transition(32,True),Transition(32,True),Transition(32,True),
            Transition(32,True),Transition(32,True),Transition(32,True),Transition(8,True),Transition(8,True),
            Transition(10,False),Transition(11,False),Transition(12,False),Transition(13,False),Transition(14,False),
            Transition(15,False),Transition(16,False),Transition(17,False),Transition(18,False),Transition(19,False),
            Transition(20,False),Transition(21,False),Transition(22,False),Transition(23,False),Transition(24,False),
            Transition(25,False),Transition(26,False),Transition(27,False),Transition(28,False),Transition(29,False),
            Transition(30,False),Transition(31,False),Transition(32,False),Transition(33,False),Transition(34,False),Transition(35,False)
        ],
    }
    
    keywords = ["else", "if", "input", "int", "output", "return", "void", "while"]
    
    valid_tokens = {
        "else": 1,
        "if": 2,
        "input": 3,
        "int": 4, 
        "output": 5, 
        "return": 6, 
        "void": 7, 
        "while": 8, 
        "+": 9, 
        "-": 10, 
        "*": 11, 
        "/": 12, 
        ">": 13, 
        ">=": 14, 
        "<": 15, 
        "<=": 16, 
        "==": 17, 
        "!=": 18, 
        "=": 19, 
        ";": 20, 
        ",": 21, 
        "(": 22, 
        ")": 23, 
        "{": 24, 
        "}": 25, 
        "[": 26, 
        "]": 27, 
        "IDENTIFIER": 28, 
        "NUM_CONSTANT": 29, 
        "COMMENT": 30, 
        "$": 30
    }

    cminusdfa = TransitionTable(acceptingstates, errorstates, transitions, keywords, valid_tokens)
    
    # We add the DFA and the Input text to the scanner
    comp.scannerPrep(input_txt, cminusdfa, ["IDENTIFIER", "NUM_CONSTANT"], ["isVar","isFunc","dataType", "noArgs", "isGlobal", "isLocal"])
    
    # Start the compilation process
    comp.compile()