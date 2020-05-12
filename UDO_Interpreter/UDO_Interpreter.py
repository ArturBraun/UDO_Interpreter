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

def whileLoop():
    """
    Grammar rule for while loop.
    """
    return ["while"], content, ["do"], content, ["endwhile"];

def ifStatement():
    """
    Grammar rule for if statement.
    """
    return ["if"], content, ["do"], content, ["endif"];

def content():
    """
    Grammar rule for content inside if statements and while loops.
    """
    return apperggioRegEx(r'[ -~]*')

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
    def __init__(self, isForNestedParsing = False):
        self.globalData = GlobalData()
        if not isForNestedParsing:
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
            "CALL":"do_call"
            }
        self.hasSomethingBeenAddedToFiles = {
            "circuitFile" : False,
            "excitFile" : False,
            "geomMediaFile" : False,
            "meshFile" : False,
            "ppostFile" : False,
            "runsimulFile" : False,
            "setsimulFile" : False
            }

        # ELEMENT command variables
        self.elementCommandLevel = 0.0
        self.elementCommandHeight = 0.0
        self.elementCommandType = 0
        self.elementCommandMediumName = ""
        self.elementCommandName = ""
        self.elementCommandSpinWire = ""

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

#sys.path.insert(0, os.path.dirname(__file__))
#sys.path.append(os.path.dirname(__file__))
#sys.path.append("{filesPath}")
#sys.path.insert(0, '{filesPath}')

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

        """.format(projectName = self.globalData.projectName, filesPath = self.globalData.pathToGeneratePyFiles)
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
        if (not self.hasSomethingBeenAddedToFiles["circuitFile"]):
            self.globalData.writeToCircuitFile("    pass\n")

        if (not self.hasSomethingBeenAddedToFiles["excitFile"]):
            self.globalData.writeToExcitFile("    pass\n")

        if (not self.hasSomethingBeenAddedToFiles["geomMediaFile"]):
            self.globalData.writeToGeomMediaFile("    pass\n")

        if (not self.hasSomethingBeenAddedToFiles["meshFile"]):
            self.globalData.writeToMeshFile("    pass\n")

        if (not self.hasSomethingBeenAddedToFiles["ppostFile"]):
            self.globalData.writeToPpostFile("    pass\n")

        if (not self.hasSomethingBeenAddedToFiles["runsimulFile"]):
            self.globalData.writeToRunsimulFile("    pass\n")

        if (not self.hasSomethingBeenAddedToFiles["setsimulFile"]):
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
        self.hasSomethingBeenAddedToFiles["geomMediaFile"] = True

        self.elementCommandLevel = argumentsList[0]
        self.elementCommandHeight = argumentsList[1]
        self.elementCommandType = argumentsList[2]
        self.elementCommandMediumName = argumentsList[3]
        self.elementCommandName = argumentsList[4]
        self.elementCommandSpinWire = argumentsList[5]

        #sketchName = "sketch_{name}".format(name = self.elementCommandName)
        while True:
            if self.elementCommandName in self.globalData._singleton.objectsNames:
                #sketchName += "1"
                self.elementCommandName += "1"
            else: 
                break
        self.globalData._singleton.objectsNames.append(self.elementCommandName)
        #self.elementCommandName = sketchName[7:]
        
        content = """    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_{name}')
    qwm_doc.sketch_{name}.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,{level}),FreeCAD.Rotation(0.5,0.0,0.0,0.0))
""".format(name = self.elementCommandName, level = self.elementCommandLevel)

        self.globalData.writeToGeomMediaFile(content)

    def do_endelem(self,argumentsList):
        """
        Does ENDELEM command from UDO language.
        """
        self.hasSomethingBeenAddedToFiles["geomMediaFile"] = True

        content = """    qwm_doc.addObject("Part::Extrusion", "{name}")
    qwm_doc.{name}.Base = qwm_doc.sketch_{name}
    qwm_doc.{name}.Dir = (0, 0, {height})
    qwm_doc.{name}.Solid = True
    {name}_viewObject = qwm_doc.{name}.ViewObject
    {name}_viewObject.Transparency = 60
    qwm_doc.{name}.Medium = QW_Modeller.getQWMedium("{mediumName}")
    qwm_doc.recompute()
""".format(name = self.elementCommandName, height = self.elementCommandHeight, mediumName = self.elementCommandMediumName)

        self.globalData.writeToGeomMediaFile(content)

    def do_newline(self,argumentsList):
        """
        Does NEWLINE command from UDO language.
        """
        self.hasSomethingBeenAddedToFiles["geomMediaFile"] = True

        _x1 = argumentsList[0]
        _y1 = argumentsList[1]
        _x2 = argumentsList[2]
        _y2 = argumentsList[3]

        content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
""".format(name = self.elementCommandName, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

        self.globalData.writeToGeomMediaFile(content)

        self.newlineCommandFirstPoint = [_x1, _y1]
        self.lineCommandLastPoint = [_x2, _y2]

    def do_closeline(self,argumentsList):
        """
        Does CLOSELINE command from UDO language.
        """
        self.hasSomethingBeenAddedToFiles["geomMediaFile"] = True

        _x1 = self.lineCommandLastPoint[0]
        _y1 = self.lineCommandLastPoint[1]
        _x2 = self.newlineCommandFirstPoint[0]
        _y2 = self.newlineCommandFirstPoint[1]

        content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
""".format(name = self.elementCommandName, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

        self.globalData.writeToGeomMediaFile(content)

        self.lineCommandLastPoint = [_x2, _y2]

    def do_addy(self,argumentsList):
        """
        Does ADDY command from UDO language.
        """
        self.hasSomethingBeenAddedToFiles["geomMediaFile"] = True

        _x1 = self.lineCommandLastPoint[0]
        _y1 = self.lineCommandLastPoint[1]
        _x2 = self.lineCommandLastPoint[0]
        _y2 = self.lineCommandLastPoint[1] + argumentsList[0]

        content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
""".format(name = self.elementCommandName, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

        self.globalData.writeToGeomMediaFile(content)

        self.lineCommandLastPoint = [_x2, _y2]

    def do_addx(self,argumentsList):
        """
        Does ADDX command from UDO language.
        """
        self.hasSomethingBeenAddedToFiles["geomMediaFile"] = True

        _x1 = self.lineCommandLastPoint[0]
        _y1 = self.lineCommandLastPoint[1]
        _x2 = self.lineCommandLastPoint[0] + argumentsList[0]
        _y2 = self.lineCommandLastPoint[1]

        content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
""".format(name = self.elementCommandName, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

        self.globalData.writeToGeomMediaFile(content)

        self.lineCommandLastPoint = [_x2, _y2]

    def do_addline(self,argumentsList):
        """
        Does ADDLINE command from UDO language.
        """
        self.hasSomethingBeenAddedToFiles["geomMediaFile"] = True

        _x1 = self.lineCommandLastPoint[0]
        _y1 = self.lineCommandLastPoint[1] 
        _x2 = argumentsList[0]
        _y2 = argumentsList[1]

        content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
""".format(name = self.elementCommandName, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

        self.globalData.writeToGeomMediaFile(content)

        self.lineCommandLastPoint = [_x2, _y2]

    def do_call(self,argumentsList):
        """
        Does CALL command from UDO language.
        """
        UDO_FilePath = argumentsList[0]
        doNestedParsing(argumentsList[1:-1], UDO_FilePath, debug = False, interpreter_debug = False, showDotFile = False)


class GrammarRulesVisitor(PTNodeVisitor):
    """
    Class that applies behaviour (concrete function) when the particular grammar rule is met.
    """
#    def __init__(self, interpreter_debug = False, isNestedParsing = False, **kwargs):

    def __init__(self, interpreter_debug = False, isNestedParsing = False, nestedParameters = False,**kwargs):
        super().__init__(**kwargs)
        self.interpreter_debug = interpreter_debug
        self.isNestedParsing = isNestedParsing
        if isNestedParsing:
            self.parameterNumber = 0
        if nestedParameters:
            self.nestedParameters = nestedParameters
        self.globalData = GlobalData()
        self.mathFunctions = MathematicalFunctions()
        self.logicalOperators = LogicalOperators()
        self.udoCommands = UDO_commands(isForNestedParsing = isNestedParsing)
        
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
        pass

    def visit_ifStatement(self, node, children):
        """
        Does if statement operation.
        """
        pass

    def visit_content():
        """
        Does nothing when visits content of while loops and if statements.
        """
        pass

    def addLastLineToFilesIfRequired(self):
        """
        Runs UDO_commands->addLastLineToFilesIfRequired()
        """
        self.udoCommands.addLastLineToFilesIfRequired()


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
            grammarRulesVistor = GrammarRulesVisitor(interpreter_debug = interpreter_debug, isNestedParsing = False)

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
        grammarRulesVistor = GrammarRulesVisitor(interpreter_debug = interpreter_debug, isNestedParsing = True, nestedParameters = nestedParameters)

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
