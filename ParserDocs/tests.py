import unittest
from transitiontable import TransitionTable
from compiler import Compiler
from ctoken import Token
from transition import Transition
from symboltable import SymbolTable

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


""" 
TestScanner Class
author: Victor Emmanuel Guerra Aguado

Description:
    The TestScanner Class contains unit tests for the Scanner Class, or more
    specifically, unit tests for the lexical analysis phase of a compiler.
"""
class TestScanner(unittest.TestCase):
    """ 
    setUpClass method

    Description:
        For the set up needed before running the tests. Creates the TransitionTable
        object needed for compilation, provides the names of the symbol tables, and 
        initializes the Compiler object.
    """
    @classmethod
    def setUpClass(self):
        self.dfa = TransitionTable(acceptingstates, errorstates, transitions, keywords, valid_tokens)
        self.compiler = Compiler()
        self.symbol_table_names = ["IDENTIFIER", "NUM_CONSTANT"]
        self.st_fields = ["isVar","isFunc","dataType", "noArgs", "isGlobal", "isLocal"]

    """ 
    Test Case CMCTC-01

    Description/Purpose:
        To verify that the scanner object creates tokens completely and correctly
        from the given input text and according to the C Minus language definition.
    """
    def test_token_creation(self):
        input_txt = """void main(){
    else if input int output return void while;
    i = 0;
    i + 1
    i - 1
    i * 1
    i / 1
    i > 1 >= 0
    i < 1 <= 0
    i == 1
    i != 1
    [, ]
    /**/
}"""

        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)
        
        expected_token_stream = [Token(kwid = 7),Token(kwid = 28,st_ref = 0),Token(kwid=22),Token(kwid=23), Token(kwid=24),
        Token(kwid=1), Token(kwid=2), Token(kwid=3), Token(kwid=4), Token(kwid=5), Token(kwid=6), Token(kwid=7), Token(kwid=8), 
        Token(kwid=20), Token(kwid=28,st_ref=1), Token(kwid=19), Token(kwid=29,st_ref=0), Token(kwid=20), Token(kwid=28,st_ref=1), Token(kwid=9), 
        Token(kwid=29,st_ref=1), Token(kwid=28,st_ref=1), Token(kwid=10), Token(kwid=29,st_ref=1), Token(kwid=28,st_ref=1), Token(kwid=11), 
        Token(kwid=29,st_ref=1), Token(kwid=28,st_ref=1), Token(kwid=12), Token(kwid=29,st_ref=1), Token(kwid=28,st_ref=1), Token(kwid=13), 
        Token(kwid=29,st_ref=1), Token(kwid=14), Token(kwid=29,st_ref=0), Token(kwid=28,st_ref=1), Token(kwid=15), Token(kwid=29,st_ref=1), 
        Token(kwid=16), Token(kwid=29,st_ref=0), Token(kwid=28,st_ref=1), Token(kwid=17), Token(kwid=29,st_ref=1), Token(kwid=28,st_ref=1), 
        Token(kwid=18), Token(kwid=29,st_ref=1), Token(kwid=26), Token(kwid=21), Token(kwid=27), Token(kwid=25)]
        
        self.compiler.scanner.tokenizeInput()
        actual_tokens_stream = self.compiler.scanner.token_stream
        
        expected_tokens = []
        for tok in expected_token_stream:
            expected_tokens.append(tok.toStr())
            
        actual_tokens = []
        for tok in actual_tokens_stream:
            actual_tokens.append(tok.toStr())

        self.assertListEqual(expected_tokens, actual_tokens)


    """ 
    Test Case CMCTC-02

    Description/Purpose:
        To verify that the scanner completely and correctly creates SymbolTable
        entries of any valid given type.
    """
    def test_symbol_table_entries(self):
        input_txt = """void main() {
    one = 0;
    two = 1;
    three = 2;
}
"""
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)
        
        expected_token_stream = [Token(kwid = 7), Token(kwid=28,st_ref=0), Token(kwid=22), Token(kwid=23), Token(kwid=24), 
        Token(kwid=28,st_ref=1), Token(kwid=19), Token(kwid=29,st_ref=0), Token(kwid=20), Token(kwid=28,st_ref=2), Token(kwid=19), 
        Token(kwid=29,st_ref=1), Token(kwid=20), Token(kwid=28,st_ref=3), Token(kwid=19), Token(kwid=29,st_ref=2), Token(kwid=20), Token(kwid=25)]

        self.compiler.scanner.tokenizeInput()
        actual_tokens_stream = self.compiler.scanner.token_stream

        expected_tokens = []
        for tok in expected_token_stream:
            expected_tokens.append(tok.toStr())
            
        actual_tokens = []
        for tok in self.compiler.scanner.token_stream:
            actual_tokens.append(tok.toStr())

        self.assertListEqual(expected_tokens, actual_tokens)


    """ 
    Test Case CMCTC-03

    Description/Purpose:
        To verify that the scanner raises an error when encountering an unclosed 
        comment.
    """
    def test_unclosed_comment(self):
        input_txt = """void main() {
            /* Main Function */
            if(true){
                /* Comment
            }
        }
"""
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)
        
        with self.assertRaises(SystemExit) as res:
            self.compiler.compile()
        print(res.exception)
        self.assertEqual(res.exception.__str__(), "Incomplete Comment Error in line: 4")
    
    """ 
    Test Case CMCTC-04

    Description/Purpose:
        To verify that the scanner raises an error when encountering an invalid 
        character for the language.
    """
    def test_invalid_character(self):
        input_txt = """void main() {
                int 編譯器;
                編譯器 = 10; 
        }
"""
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)
        
        with self.assertRaises(SystemExit) as res:
            self.compiler.compile()
        print(res.exception)
        self.assertEqual(res.exception.__str__(), "Invalid Character Error in line: 2")

    """ 
    Test Case CMCTC-05

    Description/Purpose:
        To verify that the scanner accepts any character, even invalid characters
        for the language, if it is placed inside a comment.
    """
    def test_characters_in_comment(self):
        input_txt = """void main() {
                /* 冰淇凌 */
}
"""
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)
        
        expected_token_stream = [Token(kwid=7), Token(kwid=28,st_ref=0), Token(kwid=22), Token(kwid=23), Token(kwid=24), 
        Token(kwid=25)]

        self.compiler.scanner.tokenizeInput()
        actual_tokens_stream = self.compiler.scanner.token_stream

        expected_tokens = []
        for tok in expected_token_stream:
            expected_tokens.append(tok.toStr())
            
        actual_tokens = []
        for tok in self.compiler.scanner.token_stream:
            actual_tokens.append(tok.toStr())

        self.assertListEqual(expected_tokens, actual_tokens)

    """ 
    Test Case CMCTC-06

    Description/Purpose:
        To verify that the scanner can raise an error when recognizing an invalid
        identifier.
    """
    def test_invalid_identifier(self):
        input_txt = """void main() {
                int i2;
                i2 = 0;
}
"""
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)
        
        with self.assertRaises(SystemExit) as res:
            self.compiler.compile()
        print(res.exception)
        self.assertEqual(res.exception.__str__(), "Invalid Identifier Error in line: 2")

    """ 
    Test Case CMCTC-07

    Description/Purpose:
        To verify that the scanner can raise an error when recognizing an invalid
        numerical constant.
    """
    def test_invalid_num_constant(self):
        input_txt = """void main() {
        int i;
        i = 2b;
}
"""
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)
        
        with self.assertRaises(SystemExit) as res:
            self.compiler.compile()
        print(res.exception)
        self.assertEqual(res.exception.__str__(), "Invalid Number Constant Error in line: 3")

""" 
TestParser Class
author: Victor Emmanuel Guerra Aguado

Description:
    The TestParser Class contains unit tests for the Parser Class, or more
    specifically, unit tests for the syntax analysis phase of a compiler.
"""
class TestParser(unittest.TestCase):
    """ 
    setUpClass method

    Description:
        For the set up needed before running the tests. Creates the TransitionTable
        object needed for compilation, provides the names of the symbol tables, and 
        initializes the Compiler object.
    """
    @classmethod
    def setUpClass(self):
        self.dfa = TransitionTable(acceptingstates, errorstates, transitions, keywords, valid_tokens)
        self.compiler = Compiler()
        self.symbol_table_names = ["IDENTIFIER", "NUM_CONSTANT"]
        self.st_fields = ["isVar","isFunc","dataType", "noArgs", "isGlobal", "isLocal"]
    
    """ 
    Test Case CMCTC-08

    Description/Purpose:
        To verify that the Parser adequately parses a correct structure.
    """
    def test_correct_parsing(self):
        input_txt = """int x[10];

int miniloc(int a[], int low, int high){
    int i; int x; int k;

    k = low;
    x = a[low];
    i = low + 1;
    while(i < high){
        if(a[i] < x){
            x = a[i];
            k = i;
        }
        i = i + 1;
    }
    return k;
} /* END of miniloc() */

void sort(int a[], int low, int high){
    int i; int k;

    i = low;
    while(i < high - 1){
        int t;
        /* minloc / I */
        k = miniloc(a,i,high);
        t = a[k];
        a[k] = a[i];
        a[i] = t;
        i = i +1;
    }
} /* END of sort() */ 

void main(void){
    int i;
    i = 0;

    while(i<10){
        input x[i];
        i = i + 1;
    }
    
    sort(x,0,10);
    i = 0;
    while (i<10){
        output x[i];
        i = i + 1;
    }
} /* END of main() 戰勝利 */
"""
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)
        
        expected_sts = SymbolTable(["isVar", "isFunc", "dataType", "noArgs", "isGlobal", "isLocal"])
        expected_sts.addEntry("x", ["True", "False", "int", "0", "True", "False"])
        expected_sts.addEntry("miniloc", ["False", "True", "int", "3", "True", "False"])
        expected_sts.addEntry("a", ["True", "False", "int", "0", "False", "True"])
        expected_sts.addEntry("low", ["True", "False", "int", "0", "False", "True"])
        expected_sts.addEntry("high", ["True", "False", "int", "0", "False", "False"])
        expected_sts.addEntry("i", ["True", "False", "int", "0", "False", "True"])
        expected_sts.addEntry("k", ["True", "False", "int", "0", "False", "True"])
        expected_sts.addEntry("sort", ["False", "True", "void", "3", "True", "False"])
        expected_sts.addEntry("t", ["True", "False", "int", "0", "False", "True"])
        expected_sts.addEntry("main", ["False", "True", "void", "0", "True", "False"])

        self.compiler.compile()
        self.assertEqual(self.compiler.symbol_tables["IDENTIFIER"].entries[0].value, expected_sts.entries[0].value)
        self.assertEqual(self.compiler.symbol_tables["IDENTIFIER"].entries[1].value, expected_sts.entries[1].value)
        self.assertEqual(self.compiler.symbol_tables["IDENTIFIER"].entries[2].value, expected_sts.entries[2].value)
        self.assertEqual(self.compiler.symbol_tables["IDENTIFIER"].entries[3].value, expected_sts.entries[3].value)
        self.assertEqual(self.compiler.symbol_tables["IDENTIFIER"].entries[4].value, expected_sts.entries[4].value)
        self.assertEqual(self.compiler.symbol_tables["IDENTIFIER"].entries[5].value, expected_sts.entries[5].value)
        self.assertEqual(self.compiler.symbol_tables["IDENTIFIER"].entries[6].value, expected_sts.entries[6].value)
        self.assertEqual(self.compiler.symbol_tables["IDENTIFIER"].entries[7].value, expected_sts.entries[7].value)
        self.assertEqual(self.compiler.symbol_tables["IDENTIFIER"].entries[8].value, expected_sts.entries[8].value)
        self.assertEqual(self.compiler.symbol_tables["IDENTIFIER"].entries[9].value, expected_sts.entries[9].value)

    """ 
    Test Case CMCTC-09

    Description/Purpose:
        To verify that the Parser adequately recognizes and raises an error for: 
        missing main declaration.
    """
    def test_missing_main_declaration(self):
        input_txt = """void sort(void){
            int i;
        }
        """
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)

        with self.assertRaises(SystemExit) as res:
            self.compiler.compile()
        print(res.exception)
        self.assertEqual(res.exception.__str__(), "No main function was declared.")

    """ 
    Test Case CMCTC-10

    Description/Purpose:
        To verify that the Parser adequately recognizes and raises an error for: 
        main function is not last declaration.
    """
    def test_main_is_not_last(self):
        input_txt = """void main(void){
            int i;
        }
        
        void sort(void){
            int i;
        }
        """
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)

        with self.assertRaises(SystemExit) as res:
            self.compiler.compile()
        print(res.exception)
        self.assertEqual(res.exception.__str__(), "main function is not last declaration.")

    """ 
    Test Case CMCTC-11

    Description/Purpose:
        To verify that the Parser adequately recognizes and raises an error for: 
        main function receives more than: 0 arguments.
    """
    def test_main_has_no_arguments(self):
        input_txt = """void main(int i, int a[]){
            int j;
        }
        """
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)

        with self.assertRaises(SystemExit) as res:
            self.compiler.compile()
        print(res.exception)
        self.assertEqual(res.exception.__str__(), "main function receives more than: 0 arguments.")

    """ 
    Test Case CMCTC-12

    Description/Purpose:
        To verify that the Parser adequately recognizes and raises an error for: 
        a variable has been assigned a void type.
    """
    def test_variable_is_not_void(self):
        input_txt = """void main(void){
            void i;
        }
        """
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)

        with self.assertRaises(SystemExit) as res:
            self.compiler.compile()
        print(res.exception)
        self.assertEqual(res.exception.__str__(), "A variable cannot have type: void, at line: 2.")
    
    """ 
    Test Case CMCTC-13

    Description/Purpose:
        To verify that the Parser adequately recognizes and raises an error for: 
        a variable or function has been used before declaration.
    """
    def test_use_var_or_fun_before_declaration(self):
        input_txt = """void main(void){
            sort();
        }
        """
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)

        with self.assertRaises(SystemExit) as res:
            self.compiler.compile()
        print(res.exception)
        self.assertEqual(res.exception.__str__(), "Use of Identifier: sort before declaration. In line: 2")

    """ 
    Test Case CMCTC-14

    Description/Purpose:
        To verify that the Parser adequately recognizes and raises an error for: 
        unexpected characters and tokens.
    """
    def test_expected_token(self):
        input_txt = """void main void){
        int i;
        i = 0;

    }
        """
        self.compiler.scannerPrep(input_txt, self.dfa, self.symbol_table_names, self.st_fields)

        with self.assertRaises(SystemExit) as res:
            self.compiler.compile()
        print(res.exception)
        self.assertEqual(res.exception.__str__(), "Expected a: (, received: void on line 1.")

if __name__ == "__main__":
    unittest.main()