import symboltableentry as ste
""" 
SymbolTable Class
author: Victor Emmanuel Guerra Aguado

Description: 
    The SymbolTable Class represents one of the Symbol Tables created during the 
    Lexical Analysis phase of a compiler.

Attributes:
    + fields: [str]; 
      Names or descriptions of the fields contained within an entry to the 
      SymbolTable.
    + entries: [SymbolTableEntry]; 
      The entries of the Symbol Table.
"""
class SymbolTable:
    """
    SymbolTable Class Constructor

    __init__(self, fields: [str]) -> SymbolTable
    """
    def __init__(self, fields: [str] = []):
        self.fields = fields
        self.entries = []

    """
    SymbolTable addEntry method

    Description:
        Method for adding an entry to the Symbol Table, given its value and fields.

    addEntry(self, value: str, fields: [str]) -> None
    """
    def addEntry(self, value: str, fields: [str] = []):
        if len(fields) != len(self.fields):
            print("Entries' fields do not match the Tables' fields.")
            exit()
        else:
            temp = ste.SymbolTableEntry(value, fields)
            self.entries.append(temp)
            
    """
    SymbolTable lookupEntryId method

    Description:
        Method for looking up an entry in the SymbolTable given an index or 
        entry ID.

    lookupEntryId(self, index: int) -> SymbolTableEntry
    """
    def lookupEntryId(self, index: int) -> ste.SymbolTableEntry:
        return self.entries[index]

    """
    SymbolTable lookupEntryValue method

    Description:
        Method for looking up an entry in the SymbolTable given a String value. 
        Returns the entry index.

    lookupEntryValue(self, value: str) -> int
    """
    def lookupEntryValue(self, value: str) -> int:
        for entry in self.entries:
            if entry.value == value:
                return self.entries.index(entry)
        
        return None
    
    """ 
    SymbolTable printTable method

    Description:
        Method for printing the contents of the SymbolTable, in case visualization 
        of the table is needed.

    printTable(self) -> None
    """
    def printTable(self):
        print("| ID | VALUE | " + "|".join(self.fields))
        for entry in self.entries:
            print(str(self.lookupEntryValue(entry.value)) + " | " + entry.value 
            + " | " + " | ".join(entry.fields))