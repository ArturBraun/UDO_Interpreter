"""@package UDO_functions
This module include classes, which functions are used during visiting parse tree.  

Contain mathematical functions and logical operators.
"""

#--------------------------------------------
""" INCLUDED MODULES: """
#--------------------------------------------
import math
from GlobalData import *

#--------------------------------------------
""" CLASSES: """
#--------------------------------------------

class MathematicalFunctions:
    """
    Class used when visiting mathFunctions grammar rule.
    """
    def __init__(self):
        self.functionsNames = {
            "nothing" : "do_nothing",
            "sin" : "do_sin",
            "cos" : "do_cos",
            "tan" : "do_tan",
            "asin" : "do_sin",
            "acos" : "do_acos",
            "atan" : "do_atan",
            "atan2" : "do_atan2",
            "log" : "do_log",
            "logd" : "do_logd",
            "exp" : "do_exp",
            "sqrt" : "do_sqrt",
            "abs" : "do_abs",
            "sgn" : "do_sgn",
            "int" : "do_int",
            "frac" : "do_frac",
            "rand" : "do_rand",
            "srand" : "do_srand"
            }

    def callFunction(self, stringWith_UDO_FunctionName = "nothing", **kwargs):
        """
        Function that uses dictionary to math and call appropriate function from given string with math function name. 
        """
        return getattr(self, self.functionsNames[stringWith_UDO_FunctionName])(**kwargs)

    def do_nothing(self, **kwargs):
        """
        Function that does nothing.
        """
        pass

    def do_sin(self, **kwargs):
        """
        Does sine operation.
        """
        return math.sin(kwargs["arguments"][0])

    def do_cos(self, **kwargs):
        """
        Does cosine operation.
        """
        return math.cos(kwargs["arguments"][0])

    def do_tan(self, **kwargs):
        """
        Does tangent operation.
        """
        return math.tan(kwargs["arguments"][0])

    def do_asin(self, **kwargs):
        """
        Does arcsine operation.
        """
        return math.asin(kwargs["arguments"][0])

    def do_acos(self, **kwargs):
        """
        Does arccosine operation.
        """
        return math.acos(kwargs["arguments"][0])

    def do_atan(self, **kwargs):
        """
        Does arctangent operation.
        """
        return math.atan(kwargs["arguments"][0])

    def do_atan2(self, **kwargs): #POPRAWIC powinna przyjmowac dwa argumenty x i y!!!
        """
        Does atan(y / x) in radians.
        """
        return math.atan2(kwargs["arguments"][0])

    def do_log(self, **kwargs): #SPRAWDZIC jak ta funkcja dziala w UDO !!!
        """
        Does logarithm operation to base e.
        """
        return math.log(kwargs["arguments"][0])

    def do_logd(self, **kwargs):
        """
        Does logarithm operation to base 10.
        """
        return math.log10(kwargs["arguments"][0]) #Co robi funkcja logd() w UDO ????

    def do_exp(self, **kwargs):
        """
        Does e to power of x.
        """
        return math.exp(kwargs["arguments"][0])

    def do_sqrt(self, **kwargs):
        """
        Does square root.
        """
        return math.sqrt(kwargs["arguments"][0])

    def do_abs(self, **kwargs):
        """
        Does modulus operation.
        """
        return math.fabs(kwargs["arguments"][0])

    def do_sgn(self, **kwargs):
        pass

    def do_int(self, **kwargs):
        pass

    def do_frac(self, **kwargs):
        pass

    def do_rand(self, **kwargs):
        pass

    def do_srand(self, **kwargs):
        pass

class LogicalOperators:
    def __init__(self):
        self.functionsNames = {
            "nothing" : "do_nothing",
            "&&" : "do_logicalAnd",
            "||" : "do_logicalOr",
            "==" : "do_equalTo",
            "!=" : "do_differentThan",
            "<" : "do_lessThan",
            ">" : "do_greaterThan",
            "<=" : "do_lessOrEqualTo",
            "=<" : "do_lessOrEqualTo",
            ">=" : "do_greaterOrEqualTo",
            "=>" : "do_greaterOrEqualTo"
            }

    def callFunction(self, stringWithLogicalOperator = "nothing", **kwargs):
        return getattr(self, self.functionsNames[stringWithLogicalOperator])(**kwargs)

    def do_nothing(self, **kwargs):
        pass

    def do_logicalAnd(self, **kwargs):
        return kwargs["variable1"] and kwargs["variable2"]

    def do_logicalOr(self, **kwargs):
        return kwargs["variable1"] or kwargs["variable2"]

    def do_equalTo(self, **kwargs):
        return kwargs["variable1"] == kwargs["variable2"]

    def do_differentThan(self, **kwargs):
        return kwargs["variable1"] != kwargs["variable2"]

    def do_lessThan(self, **kwargs):
        return kwargs["variable1"] < kwargs["variable2"]

    def do_greaterThan(self, **kwargs):
        return kwargs["variable1"] > kwargs["variable2"]

    def do_lessOrEqualTo(self, **kwargs):
        return kwargs["variable1"] <= kwargs["variable2"]

    def do_greaterOrEqualTo(self, **kwargs):
        return kwargs["variable1"] >= kwargs["variable2"]


class UDO_commands:
    """
    Class used when visiting UDO_command grammar rule. This class creates behaviour for all UDO commands.
    """
    def __init__(self):
        self.functionsNames = {
            "TEST":"do_test",
            "ELEMENT":"do_element",
            "ENDELEM":"do_endelem",
            "NEWLINE":"do_newline",
            "CLOSELINE":"do_closeline",
            "ADDY":"do_addy",
            "ADDX":"do_addx"
            }

    def callFunction(self,stringWithUdoCommand,argumentsList):
        """
        Function that uses dictionary to math and call appropriate function from given string with math function name. 
        """
        return getattr(self, self.functionsNames[stringWithUdoCommand])(argumentsList)

    def do_test(self, argumentsList):
        """
        Does TEST command from UDO language.
        """
        if not argumentsList[0]:
            #zla wartosc zmiennej -> nalezy dac stosowny komunikat
            print(argumentsList[1])

    def do_element(self,argumentsList):
        """
        Does ELEMENT command from UDO language.
        """
        pass

    def do_endelem(self,argumentList):
        """
        Does ENDELEM command from UDO language.
        """
        pass

    def do_newline(self,argumentList):
        """
        Does NEWLINE command from UDO language.
        """
        pass

    def do_closeline(self,argumentList):
        """
        Does CLOSELINE command from UDO language.
        """
        pass

    def do_addy(self,argumentList):
        """
        Does ADDY command from UDO language.
        """
        pass

    def do_addx(self,argumentList):
        """
        Does ADDX command from UDO language.
        """
        pass




