import sys
from symboltable import SymbolTable
from transitiontable import TransitionTable
from ctoken import Token
"""
Scanner Class
author: Victor Emmanuel Guerra Aguado

Description: 
    The Scanner class provides management and operation of the Scanner phase of a
    Compiler.

Attributes:
    + input_text: str; 
      The text to scan and tokenize; It is consumed along with the scanning and 
      recognition.
    + dfa: TransitionTable; 
      The DFA, or rather its Transition Table implemented as a TransitionTable 
      Object.
    + symbol_tables: {str, SymbolTable}; 
      The symbol tables created during the lexical analysis.
    + token_stream: [Token]; 
      The list of tokens that have been recognized by the scanner.
    + line: int; 
      The counter for the lines read during scanning.
    + comment_displacement: int; 
      The counter for the lines that occurred inside of a comment, in case said 
      comment is not closed.
"""
class Scanner:
    """ 
    Scanner Class Constructor
    
    __init__(self, input_txt: str, dfa: TransitionTable ) -> Scanner
    """
    def __init__(self, input_txt: str, dfa: TransitionTable, field_names: [str]):
        self.input_text: str = input_txt
        self.dfa: TransitionTable = dfa
        self.field_names: [str] = field_names
        self.symbol_tables: {str, SymbolTable} = {}
        self.token_stream: [Token] = []
        self.line: int = 1
        self.comment_displacement = 0
    """
    Scanner addSymbolTable method

    Description:
        Allows for the addition of a new distinct Symbol Table for the tokens 
        produced by the Scanner.

    addSymbolTable(self, name: str, symboltable: SymbolTable) -> None
    """
    def addSymbolTable(self, name: str, symboltable: SymbolTable):
        self.symbol_tables.setdefault(name, symboltable)
        
    """
    Scanner addToken method

    Description:
        Allows for the addition of a new token to the token stream of the scanner.

    addToken(self, token: Token) -> None
    """
    def addToken(self, token: Token):
        self.token_stream.append(token)
        
    """
    Scanner runDfa method

    Description:
        Runs the TransitionTable equivalent of the DFA provided exactly once,
        and returns the resulting word and end state.

    runDfa(self) -> (state: int, word: str)
    """
    def runDfa(self) -> (int, str):
        self.input_text = self.input_text[::-1]
        state = 0
        word = ""
        current_ch = ""
        while not self.dfa.accepts(state) and not self.dfa.errors(state):
            if not self.input_text:
                return (state, word)
            current_ch = self.input_text[-1]
            #print("current_ch: " + current_ch)
            trans = self.dfa.nextTransition(state, current_ch)

            if trans.isConsuming:
                self.input_text = self.input_text[:-1]
                # if current_ch is not BLANK
                if current_ch not in ["\n", "\t", " ", "\r"]:
                    word = word + current_ch

            state = trans.target
            #print("state: " + str(state))

            if current_ch == '\n':
                self.line = self.line + 1
                if state == 8 or state == 9:
                    self.comment_displacement = self.comment_displacement + 1

        self.input_text = self.input_text[::-1]
        #print("word: " + word)
        return (state, word)
            
    """
    Scanner tokenizeInput method

    Description:
        Runs the runDfa Class function until the input_text provided is empty, 
        and adds a token to the token_stream for every valid word recognized.

    tokenizeInput(self) -> None
    """
    def tokenizeInput(self):
        while self.input_text != "":
            state, word = self.runDfa()
            
            # In state 10 the word is either a keyword or an identifier
            if state == 10:
                # If word is a keyword
                if word.lower() in self.dfa.valid_tokens.keys():
                    tok = Token(word.lower(), self.line, self.dfa.valid_tokens[word.lower()])
                    self.addToken(tok)

                # If word is an identifier
                else:
                ## Name of the SymbolTable should also be dynamic, not hardcoded

                    valid_token_id = self.dfa.valid_tokens["IDENTIFIER"]
                    stid = self.symbol_tables["IDENTIFIER"].lookupEntryValue(word)
                    # If there is already an entry in the ST with this value
                    if stid != None:
                        tok = Token("IDENTIFIER", self.line, valid_token_id, stid)
                        self.addToken(tok)
                    # If there is NO entry with this value
                    else:
                        self.symbol_tables["IDENTIFIER"].addEntry(word, ["","","","","",""])
                        st_ref = self.symbol_tables["IDENTIFIER"].lookupEntryValue(word)
                        tok = Token("IDENTIFIER", self.line, valid_token_id, st_ref)
                        self.addToken(tok)

            # In state 11 the word is a  numerical constant
            elif state == 11:
                valid_token_id = self.dfa.valid_tokens["NUM_CONSTANT"]
                stid = self.symbol_tables["NUM_CONSTANT"].lookupEntryValue(word)
                # If there is already an entry in the ST with this value
                if stid != None:
                    tok = Token("NUM_CONSTANT", self.line, valid_token_id, stid)
                    self.addToken(tok)
                # If there is NO entry with this value
                else:
                    self.symbol_tables["NUM_CONSTANT"].addEntry(word, ["","","","","",""])
                    st_ref = self.symbol_tables["NUM_CONSTANT"].lookupEntryValue(word)
                    tok = Token("NUM_CONSTANT", self.line, valid_token_id, st_ref)
                    self.addToken(tok)
            
            elif state == 32:
                sys.exit(f"Invalid Character Error in line: {self.line}")
            elif state == 33:
                sys.exit(f"Invalid Character '!' Error in line: {self.line}")
            elif state == 34:
                sys.exit(f"Invalid Identifier Error in line: {self.line}")
            elif state == 35:
                sys.exit(f"Invalid Number Constant Error in line: {self.line}")
            elif state == 8 or state == 9:
                sys.exit(f"Incomplete Comment Error in line: {self.line - self.comment_displacement}")
            elif state == 31:
                self.comment_displacement = 0
                pass
            elif state in range(12,31):
                tok = Token(word.lower(), self.line, self.dfa.valid_tokens[word.lower()])
                self.addToken(tok)
                