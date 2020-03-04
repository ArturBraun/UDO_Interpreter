"""@package UDO_Interpreter
Main module for this project. Contain main function.
 
This module include main function, functions describing parser grammar and a grammar class (which uses visitor
design pattern to appropriately behave when the specific grammar rule is met). 
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
from UDO_functions import MathematicalFunctions, LogicalOperators

#--------------------------------------------
# GRAMMAR FUNCTIONS
#--------------------------------------------
def comment():
    """
    Grammar rule for comment.
    """
    return apperggioRegEx(r'[#]{1}[ -~]*[\n]{1}')

def variable():
    """
    Grammar rule for variable.
    """
    return apperggioRegEx(r'[a-zA-Z]{1}[a-zA-Z0-9]*') 

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
        "srand"], ["("], [expression], [")"]

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

def calc(): 
    """
    Grammar rule for whole UDO file.
    """
    return OneOrMore([substitutionOperator, expression]), EOF


#--------------------------------------------
#CLASSES AND MAIN FUNCTION
#--------------------------------------------

class GrammarRulesVisitor(PTNodeVisitor):
    """
    Class that applies behaviour (concrete function) when the particular grammar rule is met.
    """
    def __init__(self, interpreter_debug = False, **kwargs):
        super().__init__(**kwargs)
        self.interpreter_debug = interpreter_debug
        self.mathFunctions = MathematicalFunctions()
        self.logicalOperators = LogicalOperators()
        self.variables = {
            "x":0,
            "y":0,
            "z":0
            }

    def visit_number(self, node, children):
        """
        Converts Node value to float.
        """
        if self.interpreter_debug:
            print("Converting {}.".format(node.value))
        return float(node.value)
    
    def visit_withSign(self, node, children):
        """
        Applies a sign to expression or number.
        """
        if len(children) == 1:
            return children[0]
        sign = -1 if children[0] == "-" else 1
        result = sign * children[-1]
        if self.interpreter_debug:
            print("NumberWithSign {}.\nNumberWithSign {}.".format(node.value.replace("|",""),result))
        return result

    def visit_power(self, node, children):
        """
        Raises number to Power.
        """
        power = children[0]
        for i in range(2, len(children), 2):
            if children[i-1] == "^":
                power **= children[i]
        if self.interpreter_debug:
            print("Power {}.\nPower = {}.".format(node.value.replace("|",""), power))
        return power
    
    def visit_multiplicationOrDivision(self, node, children):
        """
        Divides or Multiplies number.
        """
        multiplicationOrDivision = children[0]
        for i in range(2, len(children), 2):
            if children[i-1] == "*":
                multiplicationOrDivision *= children[i]
            elif children[i-1] == "/":
                multiplicationOrDivision /= children[i]
        if self.interpreter_debug:
            print("MultiplicationOrDivision {}.\nMultiplicationOrDivision = {}.".format(node.value.replace("|",""), multiplicationOrDivision))
        return multiplicationOrDivision

    def visit_expression(self, node, children):
        """
        Adds or substracts numbers.
        """
        expression = children[0]
        for i in range(2, len(children), 2):
            if children[i-1] == "-":
                expression -= children[i]
            elif children[i-1] == "+":
                expression += children[i]
        if self.interpreter_debug:
            print("Expression {}.\nExpression = {}.".format(node.value.replace("|",""), expression))
        return expression

    def visit_functions(self, node, children):
        """
        Runs proper type of function e.g. mathFunctions.
        """
        if self.interpreter_debug:
            print("Functions {}.".format(children))
        return children[0]

    def visit_mathFunctions(self, node, children):
        """
        Does mathematical functions e.g. sin, cos, tan ...
        """
        result = self.mathFunctions.callFunction(stringWith_UDO_FunctionName = children[0], child=children[2])
        if self.interpreter_debug:
            print("MathFunctions = {}.\nMathFunctions = {}.".format(node.value.replace("|",""),result))
        return result

    def visit_variable(self, node, children):
        """
        Returns value of variable.
        """        
        if node.value not in self.variables:
            return node.value
        if self.interpreter_debug:
            print("Variable {} = {}".format(node.value.replace("|",""), self.variables[node.value]))
        return self.variables[node.value]

    def visit_substitutionOperator(self, node, children):
        """
        Applies value to variable.
        """
        if (type(children[-1]) is float) or (type(children[-1]) is str):
            value = children[-1]
        else:
            value = self.variables[children[-1]]

        for i in range(len(children)-3,-1,-2):
            self.variables[node[0].value] = value

        if self.interpreter_debug:
            print("SubstitutionOperator {}.\nSubstitutionOperator {} = {}.".format(node.value.replace("|",""), node[0].value, value))

    def visit_afterVariableOperator(self, node, children):
        """
        Aplies r-operator to variable.
        """
        if children[1] == "++":
            self.variables[node[0].value] += 1
        elif children[1] == "--":
            self.variables[node[0].value] -= 1
        if self.interpreter_debug:
            print("AfterVariableOperator {} = {}.".format(node.value.replace("|",""),self.variables[node[0].value]))
        return self.variables[node[0].value]

    def visit_beforeVariableOperator(self, node, children):
        """
        Apllies l-operator to variable.
        """
        if children[0] == "~":
            self.variables[node[1].value] *= (-1)
        if self.interpreter_debug:
            print("BeforeVariableOperator {} = {}.".format(node.value.replace("|",""),self.variables[node[1].value]))
        return self.variables[node[1].value]

    def visit_logicalOperator(self, node, children):
        """
        Does logical operation.
        """
        result = float(self.logicalOperators.callFunction(stringWithLogicalOperator = children[1], value1 = children[0], value2 = children[2]))
        if result:
            for i in range(4,len(children),2):
                result = float(self.logicalOperators.callFunction(stringWithLogicalOperator = children[i-1], value1 = result, value2 = children[i]))
        if self.interpreter_debug:
            print("LogicalOperator {} = {}.".format(node.value.replace("|",""),result))
        return result

    def visit_string(self, node, children):
        """
        Converts node value to string.
        """
        if self.interpreter_debug:
            print("String {} = {}.".format(children, node.value))
        return str(children[0])



def doParsing(debug = False, interpreter_debug = False, showDotFile = False, UDO_FilePath = ""):
    """
    Function which reads the UDO file, does parsing and visits parse tree to properly create QW Modeller python script. 
    """
    print("UDO Interpreter\n\n")
    
    if UDO_FilePath:
        try:
            UDO_File = open(UDO_FilePath)

        except FileNotFoundError:
            print("Error -> Cannot find the file in given directory!")

        else:
            UDO_FileContent = UDO_File.read()

            parser = ParserPython(calc, debug=debug)
            parse_tree = parser.parse(UDO_FileContent)
            result = visit_parse_tree(parse_tree,GrammarRulesVisitor(debug=debug, interpreter_debug = interpreter_debug))

            inputExprValue = -3

            print("\n\n{} = {}".format("Python value","Calculated result from parser"))
            print("{} = {}\n".format(inputExprValue,result))

            if showDotFile:
                PTDOTExporter().exportFile(parse_tree,"UDO_InterpreterParseTree.dot")    
                s = Source.from_file("UDO_InterpreterParseTree.dot")
                s.view()

        finally:
            UDO_File.close()

    else:
        print("Error -> File Path is empty!")


def main():
    """
    Main function of UDO_Interpreter project.
    """
    doParsing(debug = False, interpreter_debug = True, showDotFile = True, UDO_FilePath = "udo_file_1.txt")

if __name__ == "__main__":
    main()
