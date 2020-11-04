"""@package UDO_Interpreter
Main module for this project. Contain main function.
 
This module include main function and functions describing parser grammar. 
"""

#____________________________________________
# TODO:
# -dodac funkcje zwiazane z meshem
# -poprawic content zapisywany do pliku w funkcji do_endport() !!! - poprawic orientacje i pobudzenie
# -przetestowac interpretacje wgtocx1
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
        "PORT",
        "ENDPORT",
        "GETIOPAR",
        "INSERTMEDIUM",        
        "MEDIUMPAR",        
        "MEDIUMCOL",        
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
        "PORT",
        "ENDPORT",
        "GETIOPAR",
        "INSERTMEDIUM",        
        "MEDIUMPAR",        
        "MEDIUMCOL",    
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
#CLASSES AND MAIN FUNCTION
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
        return math.sin(math.radians(kwargs["arguments"][0]))

    def do_cos(self, **kwargs):
        """
        Does cosine operation.
        """
        return math.cos(math.radians(kwargs["arguments"][0]))

    def do_tan(self, **kwargs):
        """
        Does tangent operation.
        """
        return math.tan(math.radians(kwargs["arguments"][0]))

    def do_asin(self, **kwargs):
        """
        Does arcsine operation.
        """
        return math.asin(math.radians(kwargs["arguments"][0]))

    def do_acos(self, **kwargs):
        """
        Does arccosine operation.
        """
        return math.acos(math.radians(kwargs["arguments"][0]))

    def do_atan(self, **kwargs):
        """
        Does arctangent operation.
        """
        return math.atan(math.radians(kwargs["arguments"][0]))

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
        """
        Does sgn (signum function) operation.
        """
        if kwargs["arguments"][0] < 0:
            return -1
        elif kwargs["arguments"][0] == 0:
            return 0
        elif kwargs["arguments"][0] > 0:
            return 1

    def do_int(self, **kwargs):
        """
        Converts argument to integer number, truncates the fractional part.
        """
        return int(kwargs["arguments"][0])

    def do_frac(self, **kwargs):
        """
        Get fractional part of number.
        """
        numStr = str(float(kwargs["arguments"][0]))
        pos = numStr.rfind(".")
        fractionalPart = float(numStr[pos:])
        
        return fractionalPart

    def do_rand(self, **kwargs):
        """
        Generates random number in range <0; max number size allowed in user system>.
        """
        return random.randint(0, sys.maxsize)

    def do_srand(self, **kwargs):
        """
        Initializes pseudo rand number generator. It is not needed in python so the function does nothing.
        """
        pass

class LogicalOperators:
    """
    Class used for logical operations.
    """
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
        """
        Calls particular logical functions to get results.
        """
        return getattr(self, self.functionsNames[stringWithLogicalOperator])(**kwargs)

    def do_nothing(self, **kwargs):
        """
        Function that does nothing. Used when the stringWithLogicalOperator doesn't match any particular function. 
        """
        pass

    def do_logicalAnd(self, **kwargs):
        """
        Does logical AND operation.
        """
        return bool(kwargs["variable1"]) and bool(kwargs["variable2"])

    def do_logicalOr(self, **kwargs):
        """
        Does logical OR operation.
        """
        return bool(kwargs["variable1"]) or bool(kwargs["variable2"])

    def do_equalTo(self, **kwargs):
        """
        Does logical EQUAL TO operation.
        """
        return kwargs["variable1"] == kwargs["variable2"]

    def do_differentThan(self, **kwargs):
        """
        Does logical DIFFERENT THAN operation.
        """
        return kwargs["variable1"] != kwargs["variable2"]

    def do_lessThan(self, **kwargs):
        """
        Does logical LESS THAN operation.
        """
        return kwargs["variable1"] < kwargs["variable2"]

    def do_greaterThan(self, **kwargs):
        """
        Does logical GREATER THAN operation.
        """
        return kwargs["variable1"] > kwargs["variable2"]

    def do_lessOrEqualTo(self, **kwargs):
        """
        Does logical LESS OR EQUAL TO operation.
        """
        return kwargs["variable1"] <= kwargs["variable2"]

    def do_greaterOrEqualTo(self, **kwargs):
        """
        Does logical GREATER OR EQUAL TO operation.
        """
        return kwargs["variable1"] >= kwargs["variable2"]


class UDO_commands:
    """
    Class used when visiting UDO_command grammar rule. This class creates behaviour for all UDO commands.
    """
    def __init__(self, isForNestedParsing = False, isSpecialParsing = False, createPyFiles = True):
        self.globalData = GlobalData()
        self.createPyFiles = createPyFiles

        if (not isForNestedParsing) and (not isSpecialParsing) and self.createPyFiles:
            self.writeBasicScriptsToFiles()

        self.functionsNames = {
            "TEST":"do_test",
            "ADDLINE":"do_addline",
            "ELEMENT":"do_element",
            "ENDELEM":"do_endelem",
            "NEWLINE":"do_newline",
            "CLOSELINE":"do_closeline",
            "ADDY":"do_addy",
            "ADDX":"do_addx",
            "CALL":"do_call",
            "OPENOBJECT":"do_openobject",
            "CLOSEOBJ":"do_closeobj",
            "PORT":"do_port",
            "ENDPORT":"do_endport",
            "GETIOPAR":"do_getiopar",
            "INSERTMEDIUM":"do_insertmedium",
            "MEDIUMPAR":"do_mediumpar",
            "MEDIUMCOL":"do_mediumcol",    
            }

        # Says which command is analised at the moment
        self.currentCommand = {
            "element":False,
            "port":False,
            }

        # ELEMENT command variables
        self.elementCommandLevel = 0.0
        self.elementCommandHeight = 0.0
        self.elementCommandType = 0
        self.elementCommandTypeCombinedDict = {}
        self.elementCommandMediumName = ""
        self.elementCommandName = ""
        self.elementCommandSpinWire = ""

        # PORT command dict
        self.portCommandDict = {
            "level":None,
            "height":None,
            "type":None,
            "activity":None,
            "name":None,
            "reference":None,
            "x1":None,
            "y1":None,
            "x2":None,
            "y2":None,
            "x3":None,
            "y3":None,
            "x4":None,
            "y4":None,
            "currentPoint":1,
            "excitationPointX":None,
            "excitationPointY":None,
            "excitationPointZ":None,
            }

        # ***Line command variables
        self.newlineCommandFirstPoint = [0.0, 0.0]
        self.lineCommandLastPoint = [0.0, 0.0]

    def writeBasicScriptsToFiles(self):
        """
        Writes content to python scripts that is constant for all UDO projects.
        """

        # main file
        content = """
import sys, os
import inspect

if '__file__' not in locals():
    __file__ = inspect.getframeinfo(inspect.currentframe())[0]

cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)  # for multifile QW-Modeller macro processing
qwutilspath=cwd+"/../qw-utils"
sys.path.append(qwutilspath)

from qw_paths import *
setqwutilspath(qwutilspath)
qw_modeller_path = get_qw_modeller_path(qwutilspath)+"/bin"
sys.path.insert(0, qw_modeller_path)
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = qw_modeller_path+"\platforms" #wersja  freecad 018 qt5 python 3.6

import FreeCADGui
import QW_Modeller
import FreeCAD

from {projectName}_proj import *

GUIMode = FreeCAD.ConfigGet("RunMode")

if not GUIMode:
    FreeCADGui.showMainWindow()

FreeCADGui.activateWorkbench("QW_ModellerWorkbench")

qwm_doc = QW_Modeller.newQWDocument("{projectName}")

FreeCADGui.activeDocument().activeView().viewAxometric()

proj = {projectName}_Project(qwm_doc)
proj.set_Circuit_Parameters()
proj.set_GeometryAndMedia()
proj.set_Mesh()
proj.set_Excitation()
proj.set_Postprocessing()
proj.set_Simulation()
proj.run_Simulation()

FreeCADGui.SendMsgToActiveView("ViewFit")
qwm_doc.recompute()

if not GUIMode:
    FreeCADGui.exec_loop() #for quick tests

        """.format(projectName = self.globalData.projectName)
        self.globalData.writeToMainFile(content)


        # circuit file
        content = """
from qw_units import *
# Circuit settings
def set_Circuit_Parameters(qwm_doc):
"""
        self.globalData.writeToCircuitFile(content)


        # excit file
        content = """
from FreeCAD import Base
import QW_Modeller
from qw_project import *
from qw_units import *


def set_Excitation(qwm_doc):
"""
        self.globalData.writeToExcitFile(content)


        # geom media file
        content = """
import FreeCAD
import FreeCADGui
from FreeCAD import Base
import QW_Modeller
from qw_project import *
import Part
import Sketcher
from qw_units import *
from qw_paths import *

setGHzBaseFreqUnit()
setmmBaseGeomUnit()

def set_GeometryAndMedia(qwm_doc):
""".format(projectName = self.globalData.projectName)
        self.globalData.writeToGeomMediaFile(content)


        # mesh file
        content = """
import FreeCADGui,QW_Modeller
#from qw_project import *
from qw_units import *

def set_Mesh(qwm_doc):
"""
        self.globalData.writeToMeshFile(content)


        # ppost file
        content = """
from qw_units import *
from qw_project import *

# S postprocessing set
def set_Postprocessing(qwm_doc):
"""
        self.globalData.writeToPpostFile(content)


        # proj file
        content = """
import QW_Modeller, FreeCADGui
from {projectName}_circuit import *
from {projectName}_geom_media import *
from {projectName}_mesh import *
from {projectName}_excit import *
from {projectName}_ppost import *
from {projectName}_setsimul import *
from {projectName}_runsimul import *

class {projectName}_Project(QW_Project): # test
    def __init__(self, qwm_doc):
        self.qwm_doc = qwm_doc
        qwm_doc.Company = 'QWED SP. z o.o.'
        qwm_doc.CreatedBy = 'Automatically generated'
        qwm_doc.Comment = '{projectName}'

    def set_Circuit_Parameters(self):
        #most parameters are defaults taken from qw_project
        super({projectName}_Project, self).set_Circuit_Parameters()
        set_Circuit_Parameters(self.qwm_doc)

    def set_GeometryAndMedia(self):
        super({projectName}_Project, self).set_GeometryAndMedia()
        set_GeometryAndMedia(self.qwm_doc)

    def set_Mesh(self):
        #most parameters are defaults taken from qw_project
        super({projectName}_Project, self).set_Mesh()
        set_Mesh(self.qwm_doc)

    def set_Excitation(self):
        super({projectName}_Project, self).set_Excitation()
        set_Excitation(self.qwm_doc)

    def set_Postprocessing(self):
        super({projectName}_Project, self).set_Postprocessing()
        set_Postprocessing(self.qwm_doc)

    def set_Simulation(self):
        super({projectName}_Project, self).set_Simulation()
        set_Simulation(self.qwm_doc)

    def run_Simulation(self):
        super({projectName}_Project, self).run_Simulation()
        run_Simulation(self.qwm_doc)

        """.format(projectName=self.globalData.projectName)
        self.globalData.writeToProjFile(content)


        # runsimul file
        content = """
import os, QW_Modeller, FreeCAD
import subprocess
from qw_paths import *
from qw_project import *


def run_Simulation(qwm_doc):
"""
        self.globalData.writeToRunsimulFile(content)


        # setsimul file
        content = """
import QW_Modeller, FreeCAD, FreeCADGui
import subprocess
from qw_paths import *
from qw_project import *

def set_Simulation(qwm_doc):
"""
        self.globalData.writeToSetsimulFile(content)

    def addLastLineToFilesIfRequired(self):
        """
        Adds 'pass' keyword to files if it is required -> if no content has been added to those files.
        """
        if (not self.globalData.hasSomethingBeenAddedToFiles["circuitFile"]):
            self.globalData.writeToCircuitFile("    pass\n")

        if (not self.globalData.hasSomethingBeenAddedToFiles["excitFile"]):
            self.globalData.writeToExcitFile("    pass\n")

        if (not self.globalData.hasSomethingBeenAddedToFiles["geomMediaFile"]):
            self.globalData.writeToGeomMediaFile("    pass\n")

        if (not self.globalData.hasSomethingBeenAddedToFiles["meshFile"]):
            self.globalData.writeToMeshFile("    pass\n")

        if (not self.globalData.hasSomethingBeenAddedToFiles["ppostFile"]):
            self.globalData.writeToPpostFile("    pass\n")

        if (not self.globalData.hasSomethingBeenAddedToFiles["runsimulFile"]):
            self.globalData.writeToRunsimulFile("    pass\n")

        if (not self.globalData.hasSomethingBeenAddedToFiles["setsimulFile"]):
            self.globalData.writeToSetsimulFile("    pass\n")

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
            raise Exception(argumentsList[1])
            #print(argumentsList[1])

    def do_element(self,argumentsList):
        """
        Does ELEMENT command from UDO language.
        """
        self.globalData.hasSomethingBeenAddedToFiles["geomMediaFile"] = True
        self.currentCommand["element"] = True

        self.elementCommandLevel = argumentsList[0]
        self.elementCommandHeight = argumentsList[1]
        self.elementCommandType = argumentsList[2]
        self.elementCommandMediumName = argumentsList[3]
        self.elementCommandName = argumentsList[4]
        self.elementCommandSpinWire = argumentsList[5]

        while True:
            if self.elementCommandName in self.globalData._singleton.objectsNames:
                self.globalData.numberForEqualElementsNames += 1
                self.elementCommandName += str(self.globalData.numberForEqualElementsNames)
            else: 
                break
        self.globalData._singleton.objectsNames.append(self.elementCommandName)

        if self.elementCommandType in [5,6,15,16]:
            self.elementCommandTypeCombinedDict[self.elementCommandType] = "sketch_" + self.elementCommandName
        
        if self.createPyFiles:
            content = """    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_{name}')
    qwm_doc.sketch_{name}.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,{level}),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
""".format(name = self.elementCommandName, level = self.elementCommandLevel)
        
            self.globalData.writeToGeomMediaFile(content)

    def do_endelem(self,argumentsList):
        """
        Does ENDELEM command from UDO language.
        """
        content = ""

        if self.elementCommandType == 0 or self.elementCommandType == 10:
            content = """    qwm_doc.addObject("Part::Extrusion", "{name}")
    qwm_doc.{name}.Base = qwm_doc.sketch_{name}
    qwm_doc.{name}.Dir = (0, 0, {height})
    qwm_doc.{name}.Solid = True
    {name}_viewObject = qwm_doc.{name}.ViewObject
    {name}_viewObject.Transparency = 60
    qwm_doc.{name}.Medium = QW_Modeller.getQWMedium("{mediumName}")\n""".format(
        name = self.elementCommandName, 
        height = self.elementCommandHeight, 
        mediumName = self.elementCommandMediumName)

        else:
            isCombinedElement = 5 in self.elementCommandTypeCombinedDict and 6 in self.elementCommandTypeCombinedDict
            isBiphasedElement = 15 in self.elementCommandTypeCombinedDict and 16 in self.elementCommandTypeCombinedDict

            if isCombinedElement or isBiphasedElement:
                bottomNumber = 5
                coverNumber = 6

                if isBiphasedElement:
                    bottomNumber += 10
                    coverNumber += 10

                content = """    qwm_doc.addObject("Part::Loft", "{name}")
    qwm_doc.{name}.Sections=[qwm_doc.{sketch1}, qwm_doc.{sketch2}]
    qwm_doc.{name}.Solid=True
    qwm_doc.{name}.Ruled=False
    qwm_doc.{name}.Closed=False
    {name}_viewObject = qwm_doc.{name}.ViewObject
    {name}_viewObject.Transparency = 60
    qwm_doc.{name}.Medium = QW_Modeller.getQWMedium("{mediumName}")\n""".format(
                    name = self.elementCommandName, 
                    mediumName = self.elementCommandMediumName,
                    sketch1 = self.elementCommandTypeCombinedDict[bottomNumber], 
                    sketch2 = self.elementCommandTypeCombinedDict[coverNumber])

                self.elementCommandTypeCombinedDict = {}

        if self.createPyFiles:
            self.globalData.writeToGeomMediaFile(content)

        self.currentCommand["element"] = False

    def do_newline(self,argumentsList):
        """
        Does NEWLINE command from UDO language.
        """

        _x1 = argumentsList[0]
        _y1 = argumentsList[1]
        _x2 = argumentsList[2]
        _y2 = argumentsList[3]

        if self.createPyFiles and self.currentCommand["element"]:
            content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
""".format(name = self.elementCommandName, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)
               
            self.globalData.writeToGeomMediaFile(content)

        self.newlineCommandFirstPoint = [_x1, _y1]
        self.lineCommandLastPoint = [_x2, _y2]

        if self.currentCommand["port"]:       
            self.addPortPoints(_x1, _y1, _x2, _y2, isNewLine = True)

    def do_closeline(self,argumentsList):
        """
        Does CLOSELINE command from UDO language.
        """

        _x1 = self.lineCommandLastPoint[0]
        _y1 = self.lineCommandLastPoint[1]
        _x2 = self.newlineCommandFirstPoint[0]
        _y2 = self.newlineCommandFirstPoint[1]

        if self.createPyFiles and self.currentCommand["element"]:
            content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
""".format(name = self.elementCommandName, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

            self.globalData.writeToGeomMediaFile(content)

        self.lineCommandLastPoint = [_x2, _y2]

    def do_addy(self,argumentsList):
        """
        Does ADDY command from UDO language.
        """

        _x1 = self.lineCommandLastPoint[0]
        _y1 = self.lineCommandLastPoint[1]
        _x2 = self.lineCommandLastPoint[0]
        _y2 = self.lineCommandLastPoint[1] + argumentsList[0]

        if self.createPyFiles and self.currentCommand["element"]:
            content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
""".format(name = self.elementCommandName, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)
        
            self.globalData.writeToGeomMediaFile(content)

        self.lineCommandLastPoint = [_x2, _y2]

        if self.currentCommand["port"]:       
            self.addPortPoints(_x1, _y1, _x2, _y2)

    def do_addx(self,argumentsList):
        """
        Does ADDX command from UDO language.
        """

        _x1 = self.lineCommandLastPoint[0]
        _y1 = self.lineCommandLastPoint[1]
        _x2 = self.lineCommandLastPoint[0] + argumentsList[0]
        _y2 = self.lineCommandLastPoint[1]

        if self.createPyFiles and self.currentCommand["element"]:
            content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
""".format(name = self.elementCommandName, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

            self.globalData.writeToGeomMediaFile(content)

        self.lineCommandLastPoint = [_x2, _y2]

        if self.currentCommand["port"]:       
            self.addPortPoints(_x1, _y1, _x2, _y2)

    def do_addline(self,argumentsList):
        """
        Does ADDLINE command from UDO language.
        """

        _x1 = self.lineCommandLastPoint[0]
        _y1 = self.lineCommandLastPoint[1] 
        _x2 = argumentsList[0]
        _y2 = argumentsList[1]

        if self.createPyFiles and self.currentCommand["element"]:
            content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
""".format(name = self.elementCommandName, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

            self.globalData.writeToGeomMediaFile(content)

        self.lineCommandLastPoint = [_x2, _y2]

        if self.currentCommand["port"]:       
            self.addPortPoints(_x1, _y1, _x2, _y2)

    def addPortPoints(self, _x1, _y1, _x2, _y2, isNewLine = False):
        """
        Remembers port's points coordinates.
        """       
        if self.portCommandDict["currentPoint"] > 4 or (self.portCommandDict["currentPoint"] >= 3 and self.portCommandDict["height"] != 0):
            self.portCommandDict["excitationPointX"] = _x1
            self.portCommandDict["excitationPointY"] = _y1
        else:
            if isNewLine:
                p1 = self.portCommandDict["currentPoint"]
                p2 = self.portCommandDict["currentPoint"] + 1

                self.portCommandDict["x" + str(p1)] = _x1
                self.portCommandDict["y" + str(p1)] = _y1

                self.portCommandDict["x" + str(p2)] = _x2
                self.portCommandDict["y" + str(p2)] = _y2

                self.portCommandDict["currentPoint"] += 2
            else:
                p2 = self.portCommandDict["currentPoint"]

                self.portCommandDict["x" + str(p2)] = _x2
                self.portCommandDict["y" + str(p2)] = _y2

                self.portCommandDict["currentPoint"] += 1

    def do_call(self,argumentsList):
        """
        Does CALL command from UDO language.
        """
        UDO_FilePath = self.globalData.UDO_filePath + argumentsList[0]
        doNestedParsing(argumentsList[1:-1], UDO_FilePath, debug = False, interpreter_debug = False, 
                        showDotFile = False, printMessages = self.globalData.printMessages)

    def do_openobject(self,argumentsList):
        """
        Does OPENOBJECT command from UDO language.
        """
        pass

    def do_closeobj(self,argumentsList):
        """
        Does CLOSEOBJ command from UDO language.
        """
        pass

    def do_port(self, argumentsList):
        """
        Does PORT command from UDO language.
        """
        self.globalData.hasSomethingBeenAddedToFiles["excitFile"] = True
        self.currentCommand["port"] = True

        self.portCommandDict["level"] = argumentsList[0]
        self.portCommandDict["height"] = argumentsList[1]
        self.portCommandDict["type"] = argumentsList[2]
        self.portCommandDict["activity"] = argumentsList[3]
        self.portCommandDict["name"] = argumentsList[4]
        self.portCommandDict["reference"] = argumentsList[5]

        if self.portCommandDict["type"] != "REFERENCE":
            content = """    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","{portName}")\n""".format(portName = self.portCommandDict["name"])
            
            if self.createPyFiles:
                self.globalData.writeToExcitFile(content)

    def do_endport(self, argumentsList):
        """
        Does ENDPORT command from UDO language.
        """
        length = None
        width = None
        excitationPointZ = None
        portType = None
        activity = None
        orientation = None
        position = None
        rotation = None

        if self.portCommandDict["height"] == 0:
            length = abs(self.portCommandDict["y1"] - self.portCommandDict["y3"])
            width = abs(self.portCommandDict["x1"] - self.portCommandDict["x2"])
            excitationPointZ = self.portCommandDict["level"]
            orientation = "Z"
            position = excitationPointZ
            rotation = "0.0, 0.0, 0.0, 1.0"
        else: 
            length = abs(self.portCommandDict["y1"] - self.portCommandDict["y2"])  
            width = self.portCommandDict["height"]          
            excitationPointZ = self.portCommandDict["level"] + self.portCommandDict["height"]/2
            orientation = "X"
            position = self.portCommandDict["excitationPointX"]
            rotation = "0.5, 0.5, 0.5, 0.5"

        self.portCommandDict["excitationPointZ"] = excitationPointZ

        if self.portCommandDict["type"] == "OUTTEMPLATE":
            portType = "Load"
        else:
            portType = "Source"
        #if self.portCommandDict["type"] == "INPTEMPLATE":
        #    portType = "Source"

        if self.portCommandDict["activity"] == "UP":
            activity = "PLUS"
        else:
            activity = "MINUS"
        #elif self.portCommandDict["activity"] == "DOWN":
        #    activitydirection = "MINUS"
        #elif self.portCommandDict["activity"] == "NONE":
        #    pass

        isSpecialWithZeroHeight = not (self.portCommandDict["type"] == "SPECIAL" and self.portCommandDict["height"] == 0)

        if self.createPyFiles and isSpecialWithZeroHeight:
            content = ""

            if self.portCommandDict["type"] == "REFERENCE":
                referenceValue = 0.0
                if orientation == "X":
                    referenceValue = self.portCommandDict["excitationPointX"]
                elif orientation == "Z":
                    referenceValue = self.portCommandDict["excitationPointZ"]

                content = """    qwm_doc.{portName}.ReferenceOffset = abs(qwm_doc.{portName}.PointCoord{orientation} - {referenceValue})\n""".format(
                    portName = self.portCommandDict["reference"],
                    orientation = orientation,
                    referenceValue = referenceValue)

            else:
                content = """    qwm_doc.{portName}.Length = {length}
    qwm_doc.{portName}.Width = {width}
    qwm_doc.{portName}.Placement = Base.Placement(Base.Vector({excitationPointX}, {excitationPointY}, {excitationPointZ}), Base.Rotation({rotation}))
    qwm_doc.{portName}.Orientation = "{orientation}"
    qwm_doc.{portName}.Position = {position}
    qwm_doc.{portName}.Activity = "{activity}"
    qwm_doc.{portName}.Type = "{portType}"
    qwm_doc.{portName}.SymmetryH = False
    qwm_doc.{portName}.SymmetryV = False
    qwm_doc.{portName}.PointCoordX = {excitationPointX}
    qwm_doc.{portName}.PointCoordY = {excitationPointY}
    qwm_doc.{portName}.PointCoordZ = {excitationPointZ}
    qwm_doc.{portName}.effectivePermitivityMode = "AUTO"
    qwm_doc.{portName}.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('delta'),1,0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),1,50,1,0))
    qwm_doc.{portName}.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.{portName}.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)\n""".format(
                portName = self.portCommandDict["name"],
                length = length,
                width = width,
                excitationPointX = self.portCommandDict["excitationPointX"],
                excitationPointY = self.portCommandDict["excitationPointY"],
                excitationPointZ = self.portCommandDict["excitationPointZ"],
                portType = portType,
                activity = activity,
                orientation = orientation,
                position = position,
                rotation = rotation,
                )

            self.globalData.writeToExcitFile(content)


        self.currentCommand["port"] = False
        self.portCommandDict["currentPoint"] = 1

    def do_getiopar(self, argumentsList):
        """
        Does GETIOPAR command from UDO language.
        """
        pass  

    def do_insertmedium(self, argumentsList):
        """
        Does INSERTMEDIUM command from UDO language.
        """
        self.globalData.hasSomethingBeenAddedToFiles["geomMediaFile"] = True

        if self.createPyFiles:
            mediumName = argumentsList[0]
            mediumType = argumentsList[1]

            mediumType = mediumType[0].upper() + mediumType[1:].lower() #first letter should stay uppercase, rest lowercase
 
            content = """    {mediumName} = QW_Modeller.addQWMedium("{mediumName}")
    {mediumName}.materialtype = "{mediumType}"\n""".format(
                mediumName = mediumName,
                mediumType = mediumType)

            self.globalData.writeToGeomMediaFile(content)

    def do_mediumpar(self, argumentsList):
        """
        Does MEDIUMPAR command from UDO language.
        """
        # MEDIUMPAR (<mediumname>, <epsx>, <mux>, <sigx>, <msigx>, <epsy>, <muy>, <sigy>, <msigy>, 
        #           <epsz>, <muz>, <sigz>, <msigz>, <density>) 

        if self.createPyFiles:

            mediumName = argumentsList[0]
            epsx    = argumentsList[1]
            mux     = argumentsList[2]
            sigx    = argumentsList[3]
            msigx   = argumentsList[4]
            epsy    = argumentsList[5]
            muy     = argumentsList[6]
            sigy    = argumentsList[7]
            msigy   = argumentsList[8]
            epsz    = argumentsList[9]
            muz     = argumentsList[10]
            sigz    = argumentsList[11]
            msigz   = argumentsList[12]
            density = argumentsList[13]

            content = """    {mediumName}.Eps = [{epsx}, {epsy}, {epsz}]
    {mediumName}.Mu = [{mux}, {muy}, {muz}]
    {mediumName}.Sigma = [{sigx}, {sigy}, {sigz}]
    {mediumName}.SigmaM = [{msigx}, {msigy}, {msigz}]
    {mediumName}.density = {density}\n""".format(
                mediumName = mediumName,
                epsx    = epsx,
                mux     = mux,
                sigx    = sigx,
                msigx   = msigx,
                epsy    = epsy,
                muy     = muy,
                sigy    = sigy,
                msigy   = msigy,
                epsz    = epsz,
                muz     = muz,
                sigz    = sigz,
                msigz   = msigz,
                density = density)
            
            self.globalData.writeToGeomMediaFile(content)

    def do_mediumcol(self, argumentsList):
        """
        Does MEDIUMCOL command from UDO language.
        """
        # MEDIUMCOL (<mediumname>, <pen_R>, <pen_G>, <pen_B>, <pen_style>, <pen_width>, <brush_pen_R>, 
        #       <brush_pen_G>, <brush_pen_B>, <brush_bkg_R>, <brush_bkg_G>, <brush_bkg_B>, <brush_style>) 

        if self.createPyFiles:
            mediumName      = argumentsList[0]
            pen_R           = argumentsList[1] / 255
            pen_G           = argumentsList[2] / 255
            pen_B           = argumentsList[3] / 255
            pen_style       = int(argumentsList[4])
            pen_width       = int(argumentsList[5])
            brush_pen_R     = argumentsList[6] / 255
            brush_pen_G     = argumentsList[7] / 255
            brush_pen_B     = argumentsList[8] / 255
            brush_bkg_R     = argumentsList[9] / 255
            brush_bkg_G     = argumentsList[10] / 255
            brush_bkg_B     = argumentsList[11] / 255
            brush_style     = int(argumentsList[12])

            content = """    {mediumName}.mcolor_PENPARAMS = ({pen_R},{pen_G},{pen_B},0.0)
    {mediumName}.mstyle_PENPARAMS = {pen_style}
    {mediumName}.mwidth_PENPARAMS = {pen_width}
    {mediumName}.mpencolor_BRUSHPARAMS = ({brush_pen_R},{brush_pen_G},{brush_pen_B},0.0)
    {mediumName}.mbkcolor_BRUSHPARAMS = ({brush_bkg_R},{brush_bkg_G},{brush_bkg_B},0.0)
    {mediumName}.mstyle_BRUSHPARAMS = {brush_style}\n""".format(
                mediumName      = mediumName,
                pen_R           = pen_R,
                pen_G           = pen_G,
                pen_B           = pen_B,
                pen_style       = pen_style,
                pen_width       = pen_width,
                brush_pen_R     = brush_pen_R,
                brush_pen_G     = brush_pen_G,
                brush_pen_B     = brush_pen_B,
                brush_bkg_R     = brush_bkg_R,
                brush_bkg_G     = brush_bkg_G,
                brush_bkg_B     = brush_bkg_B,
                brush_style     = brush_style)
        
            self.globalData.writeToGeomMediaFile(content)


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

        variableStorage = globalData._singleton.variables
        globalData._singleton.variables = {
                                "x":["", nestedParameters[-3]],
                                "y":["", nestedParameters[-2]],
                                "z":["", nestedParameters[-1]],
                                "air":["", "air"]
                                } 
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

    globalData.udoFileContent = previousFileContent
    globalData._singleton.variables = variableStorage

            
def main():
    """
    Main function of UDO_Interpreter project.
    """
    udoName = "wgtocx1"

    pathToFolder = "..\\tests\\" + udoName + "\\"
    fileToInterpret = udoName + ".udo"

    doParsing(debug = False, interpreter_debug = False, showDotFile = False, UDO_FilePath = pathToFolder + fileToInterpret,
        pathToGeneratePyFiles = pathToFolder)

if __name__ == "__main__":
    main()
