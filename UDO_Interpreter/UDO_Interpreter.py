"""@package UDO_Interpreter
Main module for this project. Contain main function.
 
This module include main function and functions describing parser grammar. 
"""

#____________________________________________
# TODO:
# -dokonczyc pisac funkcje matematyczne w klasie MathematicalFunctions
# -stworzyc dokumentacje w pliku UDO_functions
# -dodac pisanie tresci podstawowych w skryptach Modeller w pliku UDO_functions w funkcji writeBasicScriptsToFiles()
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

#--------------------------------------------
# GRAMMAR FUNCTIONS
#--------------------------------------------
def UDO_command():
    return [
        "TEST",
        "ADDY",
        "ADDX",
        "NEWLINE",
        "CLOSELINE",
        "ELEMENT",
        "ENDELEM"
        ], "(",  ZeroOrMore([logicalOperator, string, expression, variable],","), Optional([logicalOperator, string, expression, variable]), ")", ";"

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


def doParsing(debug = False, interpreter_debug = False, showDotFile = False, UDO_FilePath = ""):
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
            globalData = GlobalData(projectName = UDO_FilePath.split(".")[0])

            parser = ParserPython(program, debug=debug)
            parse_tree = parser.parse(UDO_FileContent)
            result = visit_parse_tree(parse_tree,GrammarRulesVisitor(debug=debug, interpreter_debug = interpreter_debug))

            inputExprValue = -3

            print("\n\n{} = {}".format("Python value","programulated result from parser"))
            print("{} = {}\n".format(inputExprValue,result))

            if showDotFile:
                PTDOTExporter().exportFile(parse_tree,"UDO_InterpreterParseTree.dot")    
                s = Source.from_file("UDO_InterpreterParseTree.dot")
                s.view()

            globalData.closeAllModellerScripts()
            UDO_File.close()            

    else:
        print("Error -> File Path is empty!\n\n")


def main():
    """
    Main function of UDO_Interpreter project.
    """
    doParsing(debug = False, interpreter_debug = True, showDotFile = True, UDO_FilePath = "udo_file_1.txt")

if __name__ == "__main__":
    main()
