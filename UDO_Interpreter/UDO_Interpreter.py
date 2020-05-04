"""@package UDO_Interpreter
Main module for this project. Contain main function.
 
This module include main function and functions describing parser grammar. 
"""

#____________________________________________
# TODO:
# -dokonczyc pisac funkcje matematyczne w klasie MathematicalFunctions
# -stworzyc dokumentacje w pliku UDO_functions
#____________________________________________

#--------------------------------------------
# INCLUDED MODULES:
#--------------------------------------------
# Built-in:
from arpeggio import *
from arpeggio import RegExMatch as apperggioRegEx
from arpeggio.export import PTDOTExporter
from graphviz import Source
import math

# Written:
from GrammarRulesVisitor import *
from GlobalData import *
from Exceptions import *

#--------------------------------------------
# GRAMMAR FUNCTIONS
#--------------------------------------------
def UDO_command():
    return [
        "TEST",
        "ADDLINE",
        "ADDY",
        "ADDX",
        "NEWLINE",
        "CLOSELINE",
        "ELEMENT",
        "ENDELEM",
        "CALL"
        ], Optional("("),  ZeroOrMore([logicalOperator, string, expression, variable],","), Optional([logicalOperator, string, expression, variable]), Optional(")"), ";"

def parameterDeclaration():
    return [
        "PAR"], "(",  ZeroOrMore([string, logicalOperator, expression, variable],","), Optional([string, logicalOperator, expression, variable]), ")", ";"

def comment():
    """
    Grammar rule for comment.
    """
    return apperggioRegEx(r'[#]{1}[ -~]*')

def variable():
    """
    Grammar rule for variable.
    """
    return apperggioRegEx(r'[a-zA-Z]{1}[a-zA-Z0-9_]*') 

def substitutionOperator():
    """
    Grammar rule for substitution operator.
    """
    return variable, OneOrMore(["="],[logicalOperator, string, expression, variable]), ";" 

def functions():
    """
    Grammar rule for functions.
    """
    return ([mathFunctions, afterVariableOperator, beforeVariableOperator])

def afterVariableOperator():
    """
    Grammar rule for operator that appears on right hand side of variable.
    """
    return variable, ["++", "--"]

def beforeVariableOperator():
    """
    Grammar rule for operator that appears on left hand side of variable
    """
    return ["~"], variable

def logicalOperator():
    """
    Grammar rule for logical operator.
    """
    return [variable, expression], OneOrMore(
        ["<=", "=<", ">=", "=>", "&&", "||", "==", "!=", ">", "<"],[variable, expression])

def mathFunctions():
    """
    Grammar rule for mathematical functions.
    """
    return [
        "sin",
        "cos",
        "tan",
        "asin",
        "acos",
        "atan",
        "atan2",
        "log",
        "logd",
        "exp",
        "sqrt",
        "abs",
        "sgn",
        "int",
        "frac",
        "rand",
        "srand"], "(", [expression], ")"

def number():
    """
    Grammar rule for number.
    """
    return apperggioRegEx(r'\d+\.\d+|\d+') 
# Sprawdzic czy wedlug UDO .2 to tez liczba
# Aktualnie dziala tylko dla liczb normalnych typu 0.2 itd.

def string():
    """
    Grammar rule for string.
    """
    return '"', apperggioRegEx(r'[ !#-~]*'), '"'

def withSign():
    """
    Grammar rule to apply sign to expression.
    """
    return Optional(["+","-"]),[functions, variable, number, ("(", expression, ")")]

def power():
    """
    Grammar rule for exponentiation.
    """
    return withSign, ZeroOrMore(["^"], withSign)

def multiplicationOrDivision():
    """
    Grammar rule for multiplication or division.
    """
    return power, ZeroOrMore(["*","/"], power)

def expression():
    """
    Grammar rule for expression.
    """
    return multiplicationOrDivision, ZeroOrMore(["+","-"], multiplicationOrDivision)

def program(): 
    """
    Grammar rule for whole UDO file.
    """
    return OneOrMore([comment, parameterDeclaration, UDO_command ,substitutionOperator, "ENDHEADER;", expression]), EOF


#--------------------------------------------
#CLASSES AND MAIN FUNCTION
#--------------------------------------------

def doParsing(debug, interpreter_debug, showDotFile, UDO_FilePath, pathToGeneratePyFiles):
    """
    Function which reads the UDO file, does parsing and visits parse tree to properly create QW Modeller python script. 
    """
    print("UDO Interpreter\n\n")
    
    if UDO_FilePath:
        try:
            UDO_File = open(UDO_FilePath)

        except FileNotFoundError:
            print("Error -> Cannot find the file in given directory!\n\n")

        else:
            UDO_FileContent = UDO_File.read()
            globalData = GlobalData(projectName = UDO_FilePath[UDO_FilePath.rfind("\\")+1:].split(".")[0], 
                                    filePath = UDO_FilePath[:UDO_FilePath.rfind("\\")+1],
                                    pathToGeneratePyFiles = pathToGeneratePyFiles[:pathToGeneratePyFiles.rfind("\\")+1]
                                    )
            grammarRulesVistor = GrammarRulesVisitor(debug=debug, interpreter_debug = interpreter_debug, isNestedParsing = False)

            parser = ParserPython(program, debug=debug)
            parse_tree = parser.parse(UDO_FileContent)
            
            try:
                result = visit_parse_tree(parse_tree, grammarRulesVistor)
                if showDotFile:
                    PTDOTExporter().exportFile(parse_tree,"UDO_InterpreterParseTree.dot")    
                    s = Source.from_file("UDO_InterpreterParseTree.dot")
                    s.view()

                grammarRulesVistor.addLastLineToFilesIfRequired()
                print("Parsing UDO file is completed!\nCheck .py generated files.\n\n")

            except NestedParsingFileNotFoundError as e:
                print(str(e) + "\n" + ".py generated files contain errors!\n")

            globalData.closeAllModellerScripts()
            UDO_File.close()              
    else:
        print("Error -> File Path is empty!\n\n")


def doNestedParsing(nestedParameters, UDO_FilePath, debug = False, interpreter_debug = False, showDotFile = False):
    """
    Does nested parsing (when UDO command 'CALL' is executed). 
    """
    print("Nested UDO Interpreter\n")
    
    try:
        UDO_File = open(UDO_FilePath)

    except FileNotFoundError:
        raise NestedParsingFileNotFoundError("Cannot find file for nested parsing in directory: " + UDO_FilePath + "!")

    else:
        UDO_FileContent = UDO_File.read()
        globalData = GlobalData()
        variableStorage = globalData._singleton.variables
        globalData._singleton.variables = {
                                "x":["", nestedParameters[-3]],
                                "y":["", nestedParameters[-2]],
                                "z":["", nestedParameters[-1]],
                                "air":["", "air"]
                                } 
        grammarRulesVistor = GrammarRulesVisitor(debug=debug, interpreter_debug = interpreter_debug, isNestedParsing = True,
                                                nestedParameters = nestedParameters )

        parser = ParserPython(program, debug=debug)
        parse_tree = parser.parse(UDO_FileContent)
            
        try:
            result = visit_parse_tree(parse_tree, grammarRulesVistor)
            if showDotFile:
                PTDOTExporter().exportFile(parse_tree,"UDO_InterpreterParseTree.dot")   # Nadpisuje pliki.dot !!! 
                s = Source.from_file("UDO_InterpreterParseTree.dot")
                s.view()

            print("Nested parsing UDO file is completed!\n")

        except NestedParsingFileNotFoundError as e:
            raise NestedParsingFileNotFoundError(str(e))

        UDO_File.close()   

    globalData._singleton.variables = variableStorage
            
def main():
    """
    Main function of UDO_Interpreter project.
    """

    # It is always required to provide full path !!!
    #doParsing(debug = False, interpreter_debug = True, showDotFile = True, UDO_FilePath = "C:\\Users\\artur\\Desktop\\UDO_Interpreter\\UDO_Interpreter\\udo_file_1.txt",
    #            pathToGeneratePyFiles = "C:\\Users\\artur\\Desktop\\praca_inz\\generowanePlikiPy\\")
    # "C:\\Users\\Public\\QWED\\QW-Modeller\\v2017x64\\macros\\bb_antenna\\"

    doParsing(debug = False, interpreter_debug = False, showDotFile = False, UDO_FilePath = "C:\\Users\\artur\\Desktop\\UDO_Interpreter\\UDO_Interpreter\\udo_file_3.txt",
            pathToGeneratePyFiles = "C:\\Users\\artur\\Desktop\\praca_inz\\generowanePlikiPy\\")

if __name__ == "__main__":
    main()
