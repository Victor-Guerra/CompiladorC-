import sys
from ctoken import Token
from production import Production
from symboltable import SymbolTable
from grammarSymbol import GrammarSymbol as gs
from grammarSymbol import NonTerminalSymbol as nt

""" 
Parser Class
author: Victor Emmanuel Guerra Aguado

Description: 
    The Parser Class provides the methods and logic for the Parsing phase of
    the compiler.

Attributes:
    + parsing_table: { Token, { NonTerminal, int } }; The parsing table 
      that allows the predictive parser to decide how to proceed given a 
      NonTerminal on the stack and a Terminal/Token in the scanner output.
    + stack: [GrammarSymbol]; The stack needed for the LL(1) predictive parser
      algorithm.
    + symbol_tables: { str, SymbolTable }; The symbol tables that hold the 
      information about the identifiers and numerical constants.
    + productions: [Production]; The list of productions of the C minus grammar.
"""
class Parser:
    def __init__(self, symbol_tables: {str, SymbolTable}):
        self.parsing_table: { nt, [int] } = {
            #                      else   if  input int   output return  void while    +     -     *     /     >    >=     <    <=    ==    !=     =     ;     ,     (     )     {     }     [     ]    ID    NUM    $
            "program":            [None, None, None,    1, None,   None,    1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            "declaration_list":   [None, None, None,    2, None,   None,    2, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            "declaration_listP":  [None, None, None,    3, None,   None,    3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,    4],
            "declaration":        [None, None, None,    5, None,   None,    6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            "declarationP":       [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None,    7, None,    8, None, None, None,    7, None, None, None, None],
            "var_declarationP":   [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None,    9, None, None, None, None, None,   10, None, None, None, None],
            "params":             [None, None, None,   11, None,   None,   12, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            "param_list":         [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   13, None,   14, None, None, None, None, None, None, None],
            "paramP":             [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   16, None,   16, None, None,   15, None, None, None, None],
            "compound_stmt":      [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   17, None, None, None, None, None, None],
            "local_declarations": [None,   19,   19,   18,   19,     19, None,   19, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   19,   19, None, None,   19, None, None],
            "statement_list":     [None,   20,   20, None,   20,     20, None,   20, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   20,   21, None, None,   20, None, None],
            "statement":          [None,   24,   27, None,   28,     26, None,   25, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   23, None, None, None,   22, None, None],
            "var_or_call_stmt":   [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None,   29, None, None,   30, None, None, None,   29, None, None, None, None],
            "var_or_call":        [None, None, None, None, None,   None, None, None,   31,   31,   31,   31,   31,   31,   31,   31,   31,   31, None,   31,   31,   32,   31, None, None,   31,   31, None, None, None],
            "selection_stmt":     [None,   33, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            "selection_stmtP":    [  34,   35,   35, None,   35,     35, None,   35, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   35,   35, None, None,   35, None, None],
            "return_stmtP":       [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None,   36, None,   37, None, None, None, None, None,   37,   37, None],
            "varP":               [None, None, None, None, None,   None, None, None,   39,   39,   39,   39,   39,   39,   39,   39,   39,   39,   39,   39,   39, None,   39, None, None,   38,   39, None, None, None],
            "expression":         [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   40, None, None, None, None, None,   40,   40, None],
            "expressionP":        [None, None, None, None, None,   None, None, None, None, None, None, None,   41,   41,   41,   41,   41,   41, None,   42, None, None,   42, None, None, None, None, None, None, None],
            "relop":              [None, None, None, None, None,   None, None, None, None, None, None, None,   45,   46,   44,   43,   47,   48, None, None, None, None, None, None, None, None, None, None, None, None],
            "arithmetic_exp":     [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   49, None, None, None, None, None,   49,   49, None],
            "arithmetic_exprime": [None, None, None, None, None,   None, None, None,   50,   50, None, None,   51,   51,   51,   51,   51,   51, None,   51,   51, None,   51, None, None, None,   51, None, None, None],
            "addop":              [None, None, None, None, None,   None, None, None,   52,   53, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            "term":               [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   54, None, None, None, None, None,   54,   54, None],
            "termP":              [None, None, None, None, None,   None, None, None,   56,   56,   55,   55,   56,   56,   56,   56,   56,   56, None,   56,   56, None,   56, None, None, None,   56, None, None, None],
            "mulop":              [None, None, None, None, None,   None, None, None, None, None,   57,   58, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            "factor":             [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   59, None, None, None, None, None,   60,   61, None],
            "callP":              [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   62,   63, None, None, None, None,   62,   62, None],
            "args":               [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   64, None, None, None, None, None,   64,   64, None],
            "args_list":          [None, None, None, None, None,   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   65, None,   66, None, None, None, None, None, None, None],
        }
        self.stack = [gs("$")]
        self.symbol_tables = symbol_tables
        self.productions = [
            #1
            Production(nt("program"), [nt("declaration_list")]),
            #2
            Production(nt("declaration_list"), [nt("declaration"), nt("declaration_listP")]),
            #3
            Production(nt("declaration_listP"), [nt("declaration"), nt("declaration_listP")]),
            #4
            Production(nt("declaration_listP"), [gs("epsilon")]),
            #5
            Production(nt("declaration"), [Token("int", None, 4), Token("IDENTIFIER", None, 28), nt("declarationP")]),
            Production(nt("declaration"), [Token("void", None, 7), Token("IDENTIFIER", None, 28), Token("(", None, 22), nt("params"), Token(")", None, 23), nt("compound_stmt")]),
            Production(nt("declarationP"), [nt("var_declarationP")]),
            Production(nt("declarationP"), [Token("(", None, 22), nt("params"), Token(")", None, 23), nt("compound_stmt")]),
            Production(nt("var_declarationP"), [Token(";", None, 20)]),
            Production(nt("var_declarationP"), [Token("[", None, 26), Token("NUM_CONSTANT", None, 29), Token("]", None, 27), Token(";", None, 20)]),
            Production(nt("params"), [Token("int", None, 4), Token("IDENTIFIER", None, 28), nt("paramP"), nt("param_list")]),
            Production(nt("params"), [Token("void", None, 7)]),
            Production(nt("param_list"), [Token(",", None, 21), Token("int", None, 4), Token("IDENTIFIER", None, 28), nt("paramP"), nt("param_list")]),
            Production(nt("param_list"), [gs("epsilon")]),
            Production(nt("paramP"), [Token("[", None, 26), Token("]", None, 27)]),
            Production(nt("paramP"), [gs("epsilon")]),
            Production(nt("compound_stmt"), [Token("{", None, 24), nt("local_declarations"), nt("statement_list"), Token("}", None, 25)]),
            Production(nt("local_declarations"), [Token("int", None, 4), Token("IDENTIFIER", None, 28), nt("var_declarationP"), nt("local_declarations")]),
            Production(nt("local_declarations"), [gs("epsilon")]),
            Production(nt("statement_list"), [nt("statement"), nt("statement_list")]),
            Production(nt("statement_list"), [gs("epsilon")]),
            Production(nt("statement"), [Token("IDENTIFIER", None, 28), nt("var_or_call_stmt")]),
            Production(nt("statement"), [nt("compound_stmt")]),
            Production(nt("statement"), [nt("selection_stmt")]),
            Production(nt("statement"), [Token("while", None, 8), Token("(", None, 22), nt("expression"), Token(")", None, 23), nt("statement")]),
            Production(nt("statement"), [Token("return", None, 6), nt("return_stmtP")]),
            Production(nt("statement"), [Token("input", None, 3), Token("IDENTIFIER", None, 28), nt("varP"), Token(";", None, 20)]),
            Production(nt("statement"), [Token("output", None, 5), nt("expression"), Token(";", None, 20)]),
            Production(nt("var_or_call_stmt"), [nt("varP"), Token("=", None, 19), nt("expression"), Token(";", None, 20)]),
            Production(nt("var_or_call_stmt"), [Token("(", None, 22), nt("callP"), Token(";", None, 20)]),
            Production(nt("var_or_call"), [nt("varP")]),
            Production(nt("var_or_call"), [Token("(", None, 22), nt("callP")]),
            Production(nt("selection_stmt"), [Token("if", None, 2), Token("(", None, 22), nt("expression"), Token(")", None, 23), nt("statement"), nt("selection_stmtP")]),
            Production(nt("selection_stmtP"), [Token("else", None, 1), nt("statement")]),
            Production(nt("selection_stmtP"), [gs("epsilon")]),
            Production(nt("return_stmtP"), [Token(";", None, 20)]),
            Production(nt("return_stmtP"), [nt("expression"), Token(";", None, 20)]),
            Production(nt("varP"), [Token("[", None, 26), nt("arithmetic_exp"), Token("]", None, 27)]),
            Production(nt("varP"), [gs("epsilon")]),
            Production(nt("expression"), [nt("arithmetic_exp"), nt("expressionP")]),
            Production(nt("expressionP"), [nt("relop"), nt("arithmetic_exp")]),
            Production(nt("expressionP"), [gs("epsilon")]),
            Production(nt("relop"), [Token("<=", None, 16)]),
            Production(nt("relop"), [Token("<", None, 15)]),
            Production(nt("relop"), [Token(">", None, 13)]),
            Production(nt("relop"), [Token(">=", None, 14)]),
            Production(nt("relop"), [Token("==", None, 17)]),
            Production(nt("relop"), [Token("!=", None, 18)]),
            Production(nt("arithmetic_exp"), [nt("term"), nt("arithmetic_exprime")]),
            Production(nt("arithmetic_exprime"), [nt("addop"), nt("term"), nt("arithmetic_exprime")]),
            Production(nt("arithmetic_exprime"), [gs("epsilon")]),
            Production(nt("addop"), [Token("+", None, 9)]),
            Production(nt("addop"), [Token("-", None, 10)]),
            Production(nt("term"), [nt("factor"), nt("termP")]),
            Production(nt("termP"), [nt("mulop"), nt("factor"), nt("termP")]),
            Production(nt("termP"), [gs("epsilon")]),
            Production(nt("mulop"), [Token("*", None, 11)]),
            Production(nt("mulop"), [Token("/", None, 12)]),
            Production(nt("factor"), [Token("(", None, 22), nt("arithmetic_exp"), Token(")", None, 23)]),
            Production(nt("factor"), [Token("IDENTIFIER", None, 28), nt("var_or_call")]),
            Production(nt("factor"), [Token("NUM_CONSTANT", None, 29)]),
            Production(nt("callP"), [nt("args"), Token(")", None, 23)]),
            Production(nt("callP"), [Token(")", None, 23)]),
            Production(nt("args"), [nt("arithmetic_exp"), nt("args_list")]),
            Production(nt("args_list"), [Token(",", None, 21), nt("arithmetic_exp"), nt("args_list")]),
            Production(nt("args_list"), [gs("epsilon")]),
        ]
            
    def parse(self, scanner_output: [Token], valid_tokens: {str, int}):
        scanner_output = scanner_output[::-1]
        
        token = scanner_output.pop()
        prev_token = None
        next_token = scanner_output[len(scanner_output) - 1]
        self.stack.append(nt("program"))
        topStack = self.stack[len(self.stack) - 1]

        noArgs = 0
        countParams = False
        shouldReturn = False
        currentFun = ""
        isGlobal = True
        
        while( topStack.name != "$" ):
            print( f"{topStack.name} : {token.name}")
            if topStack.name in ["declaration_list", "declaration"]:
                isGlobal = True
            elif topStack.name in ["local_declarations", "params"]:
                isGlobal = False
            
            if topStack.name == "params":
                countParams = True

            #x = input(">>>")
            # Is the Symbol atop the stack the same Terminal/Token as the next
            # Token in the Scanner Output ? 
            if topStack.name == token.name:
                if topStack.name == ")" and countParams:
                    countParams = False
                    self.symbol_tables["IDENTIFIER"].lookupEntryId(self.symbol_tables["IDENTIFIER"].lookupEntryValue(currentFun)).fields[3] = f"{noArgs}"
                    noArgs = 0
                        
                # If the Token has an entry in a symbol table ( is ID or NUM )
                if token.symboltable_ref != None:
                    # If the token is an ID
                    if token.keyword_id == 28:
                        entry = self.symbol_tables["IDENTIFIER"].lookupEntryId(token.symboltable_ref)
                        if countParams:
                            noArgs = noArgs + 1
                        
                        # Add the dataType info to the symbol tables
                        if entry.fields[2] == "":
                            if prev_token.name not in ["int", "void"]:
                                # error exit
                                sys.exit(f"Use of Identifier: {self.symbol_tables[token.name].lookupEntryId(token.symboltable_ref).value} before declaration. In line: {token.line}")
                            else:
                                entry.fields[2] = prev_token.name
                        # Add the isGlobal / isLocal fields to the entries
                        if entry.fields[4] == "" and entry.fields[5] == "":
                            if isGlobal:
                                entry.fields[4] = "True"
                                entry.fields[5] = "False"
                            else:
                                entry.fields[4] = "False"
                                entry.fields[5] = "True"
                        #print("next token:", next_token.name)
                        # Add The information of isVar and isFunc to the symbol tables
                        if entry.fields[0] == "" and entry.fields[1] == "":
                            if prev_token.name not in ["int", "void"]:
                                # error exit
                                sys.exit(f"Variable or Function is used before declaration at line: {token.line}")
                            if next_token.name == "(": 
                                if prev_token.name == "int":
                                    shouldReturn = True
                                else:
                                    shouldReturn = False

                                entry.fields[0] = "False"
                                entry.fields[1] = "True"
                                currentFun = self.symbol_tables["IDENTIFIER"].lookupEntryId(token.symboltable_ref).value
                                count_params = True
                            elif next_token.name == ";" or next_token.name == "," or next_token.name == "[" or next_token.name == ")":
                                entry.fields[0] = "True"
                                entry.fields[1] = "False"
                                entry.fields[3] = "0"
                        #print(str(self.symbol_tables["IDENTIFIER"].lookupEntryValue(entry.value)) + " | " + entry.value + " | " + " | ".join(entry.fields))
                    # If the token is a NUM
                    elif token.keyword_id == 29:
                        entry = self.symbol_tables["NUM_CONSTANT"].lookupEntryId(token.symboltable_ref)
                        if entry.fields[2] == "":
                            entry.fields[2] = "int"
                        #print(str(self.symbol_tables["NUM_CONSTANT"].lookupEntryValue(entry.value)) + " | " + entry.value + " | " + " | ".join(entry.fields))
                    #print(entry)
                
                print("match")
                self.stack.pop()
                prev_token = token
                token = scanner_output.pop()
                if len(scanner_output) > 1:
                    next_token = scanner_output[len(scanner_output) - 1]
            # Is the Symbol atop the stack a Terminal/Token ?
            elif topStack.name in valid_tokens.keys():
                # Identificar el error
                sys.exit(f"Expected a: {topStack.name}, received: {token.name} on line {token.line}.")
            # Is receiving this Terminal/Token during the current NonTerminal
            # an error ?
            elif self.parsing_table[topStack.name][valid_tokens[token.name] - 1] == None:
                if topStack.name == "expression":
                    # exit error
                    sys.exit(f"Expected an expression, received: {token.name} at line: {token.line}")
                elif topStack.name == "local_declarations":
                    # exit error
                    if token.name == "void":
                        sys.exit(f"A variable cannot have type: void, at line: {token.line}.")
                elif topStack.name in ["declaration_listP", "declaration_list", "declaration", "program", "local_declarations"] and token.name == "IDENTIFIER":
                    if prev_token.name not in ["int", "void"]:
                        # exit error
                        sys.exit(f"Variable or Function is used before declaration at line: {token.line}")

                # Llamar al error correspondiente
                if token.name != "$":
                    sys.exit(f"Error with: {topStack.name}, received: {token.name}, in line: {token.line}")
                else:
                    sys.exit(f"Error with: {topStack.name}, received: {token.name} (EOF), in line: {prev_token.line}")
                    
            # What production do I insert with the given NonTerminal and Terminal
            elif prod_no := self.parsing_table[topStack.name][valid_tokens[token.name] - 1]:
                print(f"Given: {topStack.name}, and: {token.name}, go to: {prod_no}")
                # Take out the NonTerminal from the top of the stack
                self.stack.pop()
                prod = self.productions[prod_no - 1]
                
                # If the Production is X -> epsilon, don't push
                if gs("epsilon") not in prod.rhs:
                # Push the RHS of the Production in inverse order, so the first
                # Symbol is on top of the Stack
                    for symbol in prod.rhs[::-1]:
                        self.stack.append(symbol)
            topStack = self.stack[len(self.stack) - 1]

        if topStack.name == "$" and token.name == "$":
            main_func = self.symbol_tables["IDENTIFIER"].lookupEntryValue("main")
            if main_func == None:
                sys.exit("No main function was declared.")
                #exit()
            elif self.symbol_tables["IDENTIFIER"].lookupEntryId(main_func).fields[3] != "0":
                sys.exit("main function receives more than: 0 arguments.")
                #exit()
            else:
                count = main_func + 1
                while count < len(self.symbol_tables["IDENTIFIER"].entries):
                    if self.symbol_tables["IDENTIFIER"].lookupEntryId(count).fields[1] == "True":
                        sys.exit("main function is not last declaration.")
                        #exit()
                    count = count + 1

            print(f"PARSING OK")
            return self.symbol_tables
        else:
            sys.exit(f"PARSING NOT OK")
            #exit()