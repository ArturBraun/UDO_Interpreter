"""@package UDO_Interpreter
Main module for this project. Contain main function.
 
This module include main function and functions describing parser grammar. 
"""

#____________________________________________
# TODO:
# -dodac funkcje zwiazane z meshem
# -istnieje problem z materialami, Editor ma jakies domyslne materialy jak np telfon i ich uzywa
#           a dla Modellera teflon jest nieznanym materialem np jest tak w przypadku "dielf1" !
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
import random
import sys

# Written:
from GlobalData import *
from Exceptions import *
from UdoCommands import *

#--------------------------------------------
# GRAMMAR FUNCTIONS
#--------------------------------------------

# GENERAL RULES

def header():
    """
    Grammar rule for header.
    """
    return OneOrMore([comment, parameterDeclaration, substitutionOperator]), "ENDHEADER;"

def parameterDeclaration():
    """
    Grammar rule for parameter declaration.
    """
    return ["PAR"], "(",  ZeroOrMore(expression,","), Optional(expression), ")", ";"

def comment():
    """
    Grammar rule for comment.
    """
    return apperggioRegEx(r'[#]{1}[ -~]*')

def program(): 
    """
    Grammar rule for whole UDO file.
    """
    return Optional(header), OneOrMore([comment, UDO_command, statement, expression]), EOF


# NORMAL GRAMMAR RULES

def UDO_command():
    """
    Grammar rule for UDO command.
    """
    return [ 
        "TEST",
        "ADDLINE",
        "ADDY",
        "ADDX",
        "NEWLINE",
        "CLOSELINE",
        "ELEMENT",
        "ENDELEM",
        "CALL",
        "OPENOBJECT",
        "CLOSEOBJ",
        "GETIOPAR",
        "INSERTMEDIUM",        
        "MEDIUMPAR",        
        "MEDIUMCOL",  
        "PORTEXC",
        "PORT",
        "ENDPORT",
        "MARKFJ",
        "MARK",
        "JOIN",
        "ROTATE",
        "RENAME",
        "DELETE",
        "FERRITEPAR",
        "THERMALPAR",
        "VISCOSITY",
        "SETSUSPFLAGS",
        "CIRTYPE",
        "LOSSES",
        "EXPOPT",
        "UNITS",
        "MESHPAR",
    ], Optional("("),  ZeroOrMore(expression,","), Optional(expression), Optional(")"), ";"

def variable():
    """
    Grammar rule for variable.
    """
    return apperggioRegEx(r'[a-zA-Z]{1}[a-zA-Z0-9_]*') 

def substitutionOperator():
    """
    Grammar rule for substitution operator.
    """
    return variable, OneOrMore(["="], expression), ";" 

def functions():
    """
    Grammar rule for functions.
    """
    return [mathFunctions, afterVariableOperator, beforeVariableOperator]

def afterVariableOperator():
    """
    Grammar rule for operator that appears on right hand side of variable in substitution operator.
    """
    return variable, ["++", "--"]

def beforeVariableOperator():
    """
    Grammar rule for operator that appears on left hand side of variable
    """
    return ["~"], variable

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
    return apperggioRegEx(r'\d*\.\d+|\d+') 

def string():
    """
    Grammar rule for string.
    """
    return '"', apperggioRegEx(r'[ !#-~]*'), '"'

def withSign():
    """
    Grammar rule to apply sign to expression.
    """
    return Optional(["+","-"]),[functions, variable, number, string, ("(", expression, ")")]

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

def simpleExpression():
    """
    Grammar rule for simple expression.
    """
    return multiplicationOrDivision, ZeroOrMore(["+","-", "@"], multiplicationOrDivision)

def expression():
    """
    Grammar rule for expression
    """
    return simpleExpression, ZeroOrMore(["<=", "=<", ">=", "=>", "&&", "||", "==", "!=", ">", "<"], simpleExpression)

def statement():
    """
    Grammar rule for UDO statements that should occur in body section.
    """
    return OneOrMore([compoundStatement, substitutionOperator, UDO_command, (afterVariableOperator, ";")])

def compoundStatement():
    """
    Grammar rule for compound statement.
    """
    return [whileLoop, ifStatement]


# SPECIAL STATEMENTS

def whileLoop():
    """
    Grammar rule for while loop.
    """
    return "while", specialExpression, "do", specialStatement, "endwhile;"

def ifStatement():
    """
    Grammar rule for if statement.
    """
    return "if", specialExpression, "do", specialStatement, "endif;"


# GRAMMAR RULES THAT OCCUR ONLY IN "if" OR "while" STATEMENTS

def specialUdoCommand():
    """
    Grammar rule for UDO command.
    """
    return [
        "TEST",
        "ADDLINE",
        "ADDY",
        "ADDX",
        "NEWLINE",
        "CLOSELINE",
        "ELEMENT",
        "ENDELEM",
        "CALL",
        "OPENOBJECT",
        "CLOSEOBJ",
        "GETIOPAR",
        "INSERTMEDIUM",        
        "MEDIUMPAR",        
        "MEDIUMCOL",    
        "PORTEXC",
        "PORT",
        "ENDPORT",
        "MARKFJ",
        "MARK",
        "JOIN",
        "ROTATE",
        "RENAME",
        "DELETE",
        "FERRITEPAR",
        "THERMALPAR",
        "VISCOSITY",
        "SETSUSPFLAGS",
        "CIRTYPE",
        "LOSSES",
        "EXPOPT",
        "UNITS",
        "MESHPAR",
        ], Optional("("),  ZeroOrMore(specialExpression,","), Optional(specialExpression), Optional(")"), ";"

def specialVariable():
    """
    Grammar rule for variable.
    """
    return apperggioRegEx(r'[a-zA-Z]{1}[a-zA-Z0-9_]*') 

def specialSubstitutionOperator():
    """
    Grammar rule for substitution operator.
    """
    return specialVariable, OneOrMore(["="], specialExpression), ";" 

def specialFunctions():
    """
    Grammar rule for functions.
    """
    return [specialMathFunctions, specialAfterVariableOperator, specialBeforeVariableOperator]

def specialAfterVariableOperator():
    """
    Grammar rule for operator that appears on right hand side of variable in substitution operator.
    """
    return specialVariable, ["++", "--"]

def specialBeforeVariableOperator():
    """
    Grammar rule for operator that appears on left hand side of variable
    """
    return ["~"], specialVariable

def specialMathFunctions():
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
        "srand"], "(", [specialExpression], ")"

def specialNumber():
    """
    Grammar rule for number.
    """
    return apperggioRegEx(r'\d*\.\d+|\d+') 

def specialString():
    """
    Grammar rule for string.
    """
    return '"', apperggioRegEx(r'[ !#-~]*'), '"'

def specialWithSign():
    """
    Grammar rule to apply sign to expression.
    """
    return Optional(["+","-"]),[specialFunctions, specialVariable, specialNumber, specialString, ("(", specialExpression, ")")]

def specialPower():
    """
    Grammar rule for exponentiation.
    """
    return specialWithSign, ZeroOrMore(["^"], specialWithSign)

def specialMultiplicationOrDivision():
    """
    Grammar rule for multiplication or division.
    """
    return specialPower, ZeroOrMore(["*","/"], specialPower)

def specialSimpleExpression():
    """
    Grammar rule for simple expression.
    """
    return specialMultiplicationOrDivision, ZeroOrMore(["+","-", "@"], specialMultiplicationOrDivision)

def specialExpression():
    """
    Grammar rule for expression
    """
    return specialSimpleExpression, ZeroOrMore(["<=", "=<", ">=", "=>", "&&", "||", "==", "!=", ">", "<"], specialSimpleExpression)

def specialStatement():
    """
    Grammar rule for UDO statements that should occur in body section.
    """
    return OneOrMore([specialCompoundStatement, specialSubstitutionOperator, specialUdoCommand, (specialAfterVariableOperator, ";"), comment])

def specialCompoundStatement():
    """
    Grammar rule for compound statement.
    """
    return [specialWhileLoop, specialIfStatement]

def specialWhileLoop():
    """
    Grammar rule for while loop.
    """
    return "while", specialExpression, "do", specialStatement, "endwhile;"

def specialIfStatement():
    """
    Grammar rule for if statement.
    """
    return "if", specialExpression, "do", specialStatement, "endif;"


#--------------------------------------------
# CLASSES AND MAIN FUNCTION:
#--------------------------------------------

class GrammarRulesVisitor(PTNodeVisitor):
    """
    Class that applies behaviour (concrete function) when the particular grammar rule is met.
    """
#    def __init__(self, interpreter_debug = False, isNestedParsing = False, **kwargs):

    def __init__(self, interpreter_debug = False, isNestedParsing = False, nestedParameters = False, isSpecialParsing = False, 
                 udoCommands = False, createPyFiles = True, **kwargs):
        super().__init__(**kwargs)
        self.interpreter_debug = interpreter_debug
        self.isNestedParsing = isNestedParsing
        if isNestedParsing:
            self.parameterNumber = 0
        if nestedParameters:
            self.nestedParameters = nestedParameters
        self.createPyFiles = createPyFiles
        self.globalData = GlobalData()
        self.mathFunctions = MathematicalFunctions()
        self.logicalOperators = LogicalOperators()
        if udoCommands:
            self.udoCommands = udoCommands
        else:
            self.udoCommands = UDO_commands(isForNestedParsing = isNestedParsing, isSpecialParsing = isSpecialParsing, createPyFiles = createPyFiles)
        
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

    def visit_simpleExpression(self, node, children):
        """
        Adds or substracts numbers or concatenates strings.
        """
        expression = children[0]
        for i in range(2, len(children), 2):
            if children[i-1] == "-":
                expression -= children[i]
            elif children[i-1] == "+" or children[i-1] == "@":
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
        result = self.mathFunctions.callFunction(stringWith_UDO_FunctionName = children[0], arguments=children[1:])
        if self.interpreter_debug:
            print("MathFunctions = {}.\nMathFunctions = {}.".format(node.value.replace("|",""),result))
        return result

    def visit_variable(self, node, children):
        """
        Returns value of variable.
        """      
        if node.value not in self.globalData.variables:
            return node.value
        if self.interpreter_debug:
            print("Variable {} = {}".format(node.value.replace("|",""), self.globalData.variables[node.value]))
        return self.globalData.variables[node.value][1]

    def visit_substitutionOperator(self, node, children):
        """
        Applies value to variable.
        """
        if (type(children[-1]) is float) or (type(children[-1]) is str):
            value = children[-1]
        else:
            value = self.globalData.variables[children[-1]]

        for i in range(len(children)-3,-1,-2):
            self.globalData.variables[node[0].value] = ["", value]

        if self.interpreter_debug:
            print("SubstitutionOperator {}.\nSubstitutionOperator {} = {}.".format(node.value.replace("|",""), node[0].value, value))

    def visit_afterVariableOperator(self, node, children):
        """
        Aplies r-operator to variable.
        """
        if children[1] == "++":
            self.globalData.variables[node[0].value][1] += 1
        elif children[1] == "--":
            self.globalData.variables[node[0].value][1] -= 1
        if self.interpreter_debug:
            print("AfterVariableOperator {} = {}.".format(node.value.replace("|",""),self.globalData.variables[node[0].value]))
        return self.globalData.variables[node[0].value][1]

    def visit_beforeVariableOperator(self, node, children):
        """
        Apllies l-operator to variable.
        """
        if children[0] == "~":
            self.globalData.variables[node[1].value][1] *= (-1)
        if self.interpreter_debug:
            print("BeforeVariableOperator {} = {}.".format(node.value.replace("|",""),self.globalData.variables[node[1].value]))
        return self.globalData.variables[node[1].value][1]

    def visit_expression(self, node, children):
        """
        Does expression operation.
        """
        if len(children) == 1:
            return children[0]
        else:
            result = float(self.logicalOperators.callFunction(stringWithLogicalOperator = children[1], variable1 = children[0], variable2 = children[2]))
            if result:
                for i in range(4,len(children),2):
                    result = float(self.logicalOperators.callFunction(stringWithLogicalOperator = children[i-1], variable1 = result, variable2 = children[i]))
            if self.interpreter_debug:
                print("LogicalOperator {} = {}.".format(node.value.replace("|",""),result))
            return result

    def visit_string(self, node, children):
        """
        Converts node value to string.
        """
        if self.interpreter_debug:
            print("String {} = {}.".format(children, node.value))
        if children:
            return str(children[0])
        else:
            return ""

    def visit_parameterDeclaration(self, node, children):
        """
        Adds new parameter.
        """
        if self.interpreter_debug:
            print("ParameterDeclaration {}.".format(children))
        if self.isNestedParsing:
            self.globalData.variables[node[4].value] = [children[1], self.nestedParameters[self.parameterNumber]]
            self.parameterNumber += 1
        else:
            self.globalData.variables[node[4].value] = [children[1], children[3]]

    def visit_UDO_command(self, node, children):
        """
        Does command from UDO language.
        """
        self.udoCommands.callFunction(stringWithUdoCommand = children[0], argumentsList = children[2:-1])

    def visit_whileLoop(self, node, children):
        """
        Does while loop operation.
        """
        logicalContent = self.globalData.udoFileContent[node[1].position : node[1].position_end]
        whileLoopContent = self.globalData.udoFileContent[node[3].position : node[3].position_end]
        
        grammarRulesVistor = GrammarRulesVisitor(isSpecialParsing = True, udoCommands = self.udoCommands)
        parser = ParserPython(program, debug=False, reduce_tree=True)

        currentUdoFileContent = self.globalData.udoFileContent

        while(True):
            self.globalData.udoFileContent = logicalContent
            parse_tree = parser.parse(logicalContent)
            logicalContentResult = visit_parse_tree(parse_tree, grammarRulesVistor)

            if not logicalContentResult: 
                break

            self.globalData.udoFileContent = whileLoopContent
            parse_tree = parser.parse(whileLoopContent)
            whileLoopContentResult = visit_parse_tree(parse_tree, grammarRulesVistor)

        self.globalData.udoFileContent = currentUdoFileContent

    def visit_ifStatement(self, node, children):
        """
        Does if statement operation.
        """
        logicalContent = self.globalData.udoFileContent[node[1].position : node[1].position_end]
        ifStatementContent = self.globalData.udoFileContent[node[3].position : node[3].position_end]
        
        grammarRulesVistor = GrammarRulesVisitor(isSpecialParsing = True, udoCommands = self.udoCommands)
        parser = ParserPython(program, debug=False, reduce_tree=True)

        currentUdoFileContent = self.globalData.udoFileContent
        self.globalData.udoFileContent = logicalContent

        # Get value from logical content
        parse_tree = parser.parse(logicalContent)
        logicalContentResult = visit_parse_tree(parse_tree, grammarRulesVistor)

        self.globalData.udoFileContent = ifStatementContent
        if logicalContentResult:            
            parse_tree = parser.parse(ifStatementContent)
            ifStatementContentResult = visit_parse_tree(parse_tree, grammarRulesVistor)

        self.globalData.udoFileContent = currentUdoFileContent

    def visit_statement(self, node, children):
        """
        Does nothing when visiting statement.
        """
        pass

    def visit_compoundStatement(self, node, children):
        """
        Does nothing when visiting compound statement.
        """
        pass

    def visit_header(self, node, children):
        """
        Does nothing when visiting header.
        """
        pass

    def addLastLineToFilesIfRequired(self):
        """
        Runs UDO_commands->addLastLineToFilesIfRequired()
        """
        self.udoCommands.addLastLineToFilesIfRequired()


    # GRAMMAR RULES THAT OCCUR ONLY IN "if" OR "while" STATEMENTS

    def visit_specialUdoCommand(self, node, children):
        """
        Suppress node with UDO command.
        """
        return None

    def visit_specialVariable(self, node, children):
        """
        Suppress node with variable.
        """
        return None

    def visit_specialSubstitutionOperator(self, node, children):
        """
        Suppress node with substitution operator.
        """
        return None

    def visit_specialFunctions(self, node, children):
        """
        Suppress node with functions.
        """
        return None

    def visit_specialAfterVariableOperator(self, node, children):
        """
        Suppress node with operator that appears on right hand side of variable in substitution operator.
        """
        return None

    def visit_specialBeforeVariableOperator(self, node, children):
        """
        Suppress node with for operator that appears on left hand side of variable
        """
        return None

    def visit_specialMathFunctions(self, node, children):
        """
        Suppress node with for mathematical functions.
        """
        return None

    def visit_specialNumber(self, node, children):
        """
        Suppress node with for number.
        """
        return None

    def visit_specialString(self, node, children):
        """
        Suppress node with for string.
        """
        return None

    def visit_specialWithSign(self, node, children):
        """
        Suppress node with sign to expression.
        """
        return None

    def visit_specialPower(self, node, children):
        """
        Suppress node with exponentiation.
        """
        return None

    def visit_specialMultiplicationOrDivision(self, node, children):
        """
        Suppress node with multiplication or division.
        """
        return None

    def visit_specialSimpleExpression(self, node, children):
        """
        Suppress node with simple expression.
        """
        return None

    def visit_specialExpression(self, node, children):
        """
        Suppress node with expression
        """
        return None

    def visit_specialStatement(self, node, children):
        """
        Suppress node with UDO statements that should occur in body section.
        """
        return None

    def visit_specialCompoundStatement(self, node, children):
        """
        Suppress node with compound statement.
        """
        return None

    def visit_specialWhileLoop(self, node, children):
        """
        Suppress node with while loop.
        """
        return None

    def visit_specialIfStatement(self, node, children):
        """
        Suppress node with if statement.
        """
        return None


def doTestParsing(UDO_FileContent, createPyFiles = False):
    """
    Function that does parse UDO from string as a test and returns result to check for corectness.
    """
    globalData = GlobalData(projectName = "testProject", 
                            filePath = "",
                            pathToGeneratePyFiles = "",
                            createPyFiles = createPyFiles,
                            printMessages = False,
                            udoFileContent = UDO_FileContent,
                            )
    grammarRulesVistor = GrammarRulesVisitor(interpreter_debug = False, isNestedParsing = False, createPyFiles = createPyFiles)

    parser = ParserPython(program, debug=False, reduce_tree=True)
    parse_tree = parser.parse(UDO_FileContent)
            
    result = None
    try:
        result = visit_parse_tree(parse_tree, grammarRulesVistor)

    except NestedParsingFileNotFoundError as e:
        print(str(e) + "\n" + ".py generated files contain errors!\n")

    # For unit test purpose:
    del GlobalData._singleton
    GlobalData._singleton = None

    return result


def doParsing(debug, interpreter_debug, showDotFile, UDO_FilePath, pathToGeneratePyFiles, customProjectName = "", printMessages = True):
    """
    Function which reads the UDO file, does parsing and visits parse tree to properly create QW Modeller python script. 
    """
    if printMessages:
        print("UDO Interpreter\n\n")
    
    if UDO_FilePath:
        try:
            UDO_File = open(UDO_FilePath)

        except FileNotFoundError:
            if printMessages:
                print("Error -> Cannot find the file in given directory!\n\n")

        else:
            UDO_FileContent = UDO_File.read()

            projectName = customProjectName
            if not customProjectName:
                projectName = UDO_FilePath[UDO_FilePath.rfind("\\")+1:].split(".")[0]

            globalData = GlobalData(projectName = projectName, 
                                    filePath = UDO_FilePath[:UDO_FilePath.rfind("\\")+1],
                                    pathToGeneratePyFiles = pathToGeneratePyFiles[:pathToGeneratePyFiles.rfind("\\")+1],
                                    printMessages = printMessages,
                                    udoFileContent = UDO_FileContent,
                                    )
            grammarRulesVistor = GrammarRulesVisitor(interpreter_debug = interpreter_debug, isNestedParsing = False)

            parser = ParserPython(program, debug=debug, reduce_tree=True)
            parse_tree = parser.parse(UDO_FileContent)

            if showDotFile:
                parseTreeVisualizationFileName = pathToGeneratePyFiles + globalData._singleton.projectName + "_ParseTreeVisualization.dot"
                PTDOTExporter().exportFile(parse_tree, parseTreeVisualizationFileName)    
                s = Source.from_file(parseTreeVisualizationFileName)
                s.view()
            
            try:
                result = visit_parse_tree(parse_tree, grammarRulesVistor)

                if printMessages:
                    print("result = {result}\n\n".format(result = result))

                grammarRulesVistor.addLastLineToFilesIfRequired()
                if printMessages:
                    print("Parsing UDO file is completed!\nCheck .py generated files.\n\n")

            except NestedParsingFileNotFoundError as e:
                if printMessages:
                    print(str(e) + "\n" + ".py generated files contain errors!\n")

            globalData.closeAllModellerScripts()
            UDO_File.close() 

            # For unit test purpose:
            del GlobalData._singleton
            GlobalData._singleton = None
            
    else:
        if printMessages:
            print("Error -> File Path is empty!\n\n")


def doNestedParsing(nestedParameters, UDO_FilePath, debug = False, interpreter_debug = False, showDotFile = False, printMessages = True):
    """
    Does nested parsing (when UDO command 'CALL' is executed). 
    """
    if printMessages:
        print("Nested UDO Interpreter -> {0}".format(UDO_FilePath))
    
    try:
        UDO_File = open(UDO_FilePath)

    except FileNotFoundError:
        raise NestedParsingFileNotFoundError("Cannot find file for nested parsing in directory: " + UDO_FilePath + "!")

    else:
        UDO_FileContent = UDO_File.read()
        globalData = GlobalData()

        previousFileContent = globalData.udoFileContent
        globalData.udoFileContent = UDO_FileContent

        currentElementsNamesDictStorage = globalData.currentElementsNamesDict
        globalData.currentElementsNamesDict = {}

        variableStorage = globalData.variables
        globalData.variables = createStandardVariables()
        globalData.variables["x"] = ["", nestedParameters[-3]]
        globalData.variables["y"] = ["", nestedParameters[-2]]
        globalData.variables["z"] = ["", nestedParameters[-1]]

        grammarRulesVistor = GrammarRulesVisitor(interpreter_debug = interpreter_debug, isNestedParsing = True, nestedParameters = nestedParameters)

        parser = ParserPython(program, debug=debug, reduce_tree=True)
        parse_tree = parser.parse(UDO_FileContent)
           
        try:
            result = visit_parse_tree(parse_tree, grammarRulesVistor)
            if showDotFile:
                PTDOTExporter().exportFile(parse_tree,"UDO_InterpreterParseTree.dot")   # Nadpisuje pliki.dot !!! 
                s = Source.from_file("UDO_InterpreterParseTree.dot")
                s.view()
            
            if printMessages:
                print("Nested parsing UDO file is completed!\n")

        except NestedParsingFileNotFoundError as e:
            raise NestedParsingFileNotFoundError(str(e))

        UDO_File.close()   

        currentElementsNamesDictStorage.update(globalData.currentElementsNamesDict)
        globalData.currentElementsNamesDict = currentElementsNamesDictStorage
        globalData.udoFileContent = previousFileContent
        globalData.variables = variableStorage

            
def main():
    """
    Main function of UDO_Interpreter project.
    """
    udoName = "rt2w"

    pathToFolder = "..\\tests\\" + udoName + "\\"
    fileToInterpret = udoName + ".udo"

    doParsing(debug = False, interpreter_debug = False, showDotFile = False, UDO_FilePath = pathToFolder + fileToInterpret,
        pathToGeneratePyFiles = pathToFolder)

if __name__ == "__main__":
    main()
