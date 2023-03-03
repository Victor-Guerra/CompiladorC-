from parser import Parser
from scanner import Scanner
from symboltable import SymbolTable
from grammarSymbol import GrammarSymbol
from transitiontable import TransitionTable

""" 
Compiler Class
author: Victor Emmanuel Guerra Aguado

Description: 
    The Compiler Class serves as an interface to the multiple steps of compilation.

Attributes:
    + scanner: Scanner; The compilers Scanner, in charge of the lexical analysis.
    + symbol_tables: {str, SymbolTable}; The symbol tables created during the 
      lexical analysis.
"""
class Compiler:
    """ 
    Compiler Class Constructor

    __init__(self) -> Compiler
    """
    def __init__(self):
        self.scanner: Scanner = None
        self.symbol_tables: {str, SymbolTable} = {}

        # The Compiler Class expects further expansion, to account for the 
        # following phases of compilation
        self.parser = None
        self.syntax_tree = None

    """
    Compiler scannerPrep method

    Description:
        Executes the necessary preparations for the compilers' scanner given a 
        text to scan, and a dfa to set the languages' constraints.

    scannerPrep(self, text: str, dfa: TransitionTable, st_names: [str]) -> None
    """
    def scannerPrep(self, text: str, dfa: TransitionTable, st_names: [str], field_names: [str]):
        self.scanner = Scanner(text, dfa, field_names)
        for name in st_names:
            # Add the names of the fields added in the parsing stage
            self.scanner.addSymbolTable(name, SymbolTable(field_names))
        
    """
    Compiler compile method

    Description:
        Executes all of the main components' methods to produce an output as 
        indicated by the architecture diagram. Said output is usually passed
        as an argument as input to the next method.

    compile(self) -> None
    """
    def compile(self):
        
        # Lexical Analysis Phase
        self.scanner.tokenizeInput()
        token_stream = self.scanner.token_stream
        self.symbol_tables = self.scanner.symbol_tables
        
        token_stream.append(GrammarSymbol("$"))
        self.parser = Parser(self.symbol_tables)
        self.parser.parse(token_stream, self.scanner.dfa.valid_tokens)

        # Visualization of both outputs of the Lexical Analysis
        """
        for token in token_stream:
            print(token.toStr())
        """
            
        for table in self.symbol_tables:
            print(table)
            self.symbol_tables[table].printTable()