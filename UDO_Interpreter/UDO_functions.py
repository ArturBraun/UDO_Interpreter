"""@package UDO_functions
This module include classes, which functions are used during visiting parse tree.  

Contain mathematical functions and logical operators.
"""

#--------------------------------------------
""" INCLUDED MODULES: """
#--------------------------------------------
import math
from GlobalData import *
from UDO_Interpreter import doNestedParsing
from GrammarRulesVisitor import *
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
        self.globalData = GlobalData()
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

        sketchName = "sketch_{name}".format(name = self.elementCommandName)
        while True:
            if sketchName in self.globalData._singleton.objectsNames:
                sketchName += "1"
            else: 
                break
        self.elementCommandName = sketchName[7:]
        
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

        content = """    qwm_doc.sketch_{name}.addGeometry(Part.Line(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
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

        content = """    qwm_doc.sketch_{name}.addGeometry(Part.Line(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
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

        content = """    qwm_doc.sketch_{name}.addGeometry(Part.Line(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
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

        content = """    qwm_doc.sketch_{name}.addGeometry(Part.Line(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
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

        content = """    qwm_doc.sketch_{name}.addGeometry(Part.Line(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))
""".format(name = self.elementCommandName, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

        self.globalData.writeToGeomMediaFile(content)

        self.lineCommandLastPoint = [_x2, _y2]

    def do_call(self,argumentsList):
        """
        Does CALL command from UDO language.
        """
        UDO_FilePath = argumentsList[0]
        doNestedParsing(argumentsList[1:-1], UDO_FilePath, debug = False, interpreter_debug = False, showDotFile = False)


