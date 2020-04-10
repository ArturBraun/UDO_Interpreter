"""@package GrammarRulesVisitor
This module include class used when the appropriate grammar rule is met. Function visit_* is called.
 
This module include grammar class (which uses visitor design pattern to appropriately behave when the specific grammar rule is met).  
"""

#--------------------------------------------
""" INCLUDED MODULES: """
#--------------------------------------------
import math
from arpeggio import *
from UDO_functions import *
from GlobalData import *


#--------------------------------------------
""" CLASSES: """
#--------------------------------------------

class GrammarRulesVisitor(PTNodeVisitor):
    """
    Class that applies behaviour (concrete function) when the particular grammar rule is met.
    """
    def __init__(self, interpreter_debug = False, **kwargs):
        super().__init__(**kwargs)
        self.interpreter_debug = interpreter_debug
        self.globalData = GlobalData()
        self.mathFunctions = MathematicalFunctions()
        self.logicalOperators = LogicalOperators()
        self.udoCommands = UDO_commands()
        
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
            self.globalData.variables[node[0].value] += 1
        elif children[1] == "--":
            self.globalData.variables[node[0].value] -= 1
        if self.interpreter_debug:
            print("AfterVariableOperator {} = {}.".format(node.value.replace("|",""),self.globalData.variables[node[0].value]))
        return self.globalData.variables[node[0].value]

    def visit_beforeVariableOperator(self, node, children):
        """
        Apllies l-operator to variable.
        """
        if children[0] == "~":
            self.globalData.variables[node[1].value] *= (-1)
        if self.interpreter_debug:
            print("BeforeVariableOperator {} = {}.".format(node.value.replace("|",""),self.globalData.variables[node[1].value]))
        return self.globalData.variables[node[1].value]

    def visit_logicalOperator(self, node, children):
        """
        Does logical operation.
        """
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
        return str(children[0])

    def visit_parameterDeclaration(self, node, children):
        """
        Adds new parameter.
        """
        if self.interpreter_debug:
            print("ParameterDeclaration {}.".format(children))
        self.globalData.variables[node[4].value] = [children[1], children[3]]

    def visit_UDO_command(self, node, children):
        """
        Does command from UDO language.
        """
        self.udoCommands.callFunction(stringWithUdoCommand = children[0], argumentsList = children[2:-1])

    def addLastLineToFilesIfRequired(self):
        """
        Runs UDO_commands->addLastLineToFilesIfRequired()
        """
        self.udoCommands.addLastLineToFilesIfRequired()

