"""@package UdoCommands
Module containing actions for UDO commands.
 
This module conducts UDO commands operations, when the specific action is needed. 
"""

#--------------------------------------------
# INCLUDED MODULES:
#--------------------------------------------
# Built-in:
import math
import random
import sys
import re

# Written:
from GlobalData import *
import UDO_Interpreter as udoInterpreter


#--------------------------------------------
# CLASSES:
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
            "PORTEXC":"do_portexc",
            "MARKFJ":"do_markfj",
            "MARK":"do_mark",
            "JOIN":"do_join",
            "ROTATE":"do_rotate",
            "RENAME":"do_rename",
            "DELETE":"do_delete",
            "FERRITEPAR":"do_ferritepar",
            "THERMALPAR":"do_thermalpar",
            "VISCOSITY":"do_viscosity",
            "SETSUSPFLAGS":"do_setsuspflags",
            "CIRTYPE":"do_cirtype",
            "LOSSES":"do_losses",
            "EXPOPT2":"do_expopt2",
            "EXPOPT":"do_expopt",
            "UNITS":"do_units",
            "MESHPAR":"do_meshpar",
            "SECTION":"do_section",
            "ENDSECTION":"do_endsection",
            "EPSEFF":"do_epseff",
            "MODE":"do_mode",
            "WAVEFORM":"do_waveform",
            "TEMPDP":"do_tempdp",
            "MULTIPOINT":"do_multipoint",
            "PORTPAR":"do_portpar",
            "SK1DIFF":"do_sk1diff",
            "NTF":"do_ntf",
            "NTFBKG":"do_ntfbkg",
            "UNITSGEOMETRY":"do_unitsgeometry",
            "UNITSFREQUENCY":"do_unitsfrequency",
            "ENERGYALLOW":"do_energyallow",
            "ENERGYPAR":"do_energypar",
            "ENERGYOPT":"do_energyopt",
            "BHMOPT":"do_bhmopt",
            "HTIMES":"do_htimes",
            "BHMHTIMES":"do_htimes", # Equivalent to HTIMES
            "BHMAFTER":"do_bhmafter", 
            "BHMCOMPFORMAT":"do_bhmcompformat", 
            "TEMPA":"do_tempa", 
            "SYMMETRY":"do_symmetry", 
            "SMNDIFF":"do_smndiff", 
            }

        # Says which command is analysed at the moment
        self.currentCommand = {
            "element":False,
            "port":False,
            "selection":False,
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
        self.portCommandDict = self.initPortCommandDict()

        # ***Line command variables
        self.newlineCommandFirstPoint = [0.0, 0.0]
        self.lineCommandLastPoint = [0.0, 0.0]

        # Boolean 3D operations variables
        self.markedElements = set()
        self.activeElements = set()
        self.passiveElements = set()

        # Selection command dict 
        self.selectionCommandDict = {
            "level":None,
            "height":None,
            "height2":None,
            "mediumName":None,
            "name":None,
            "upperName":None,
            "lowerName":None,
            }

    def initPortCommandDict(self):
        """
        Returns port command dictionary default content.
        """
        return {
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
            "portexcPointZ":None,
            "effectivePermittivity":1,
            "mode":"TEM",
            "waveform":"'delta'",
            "amplitude":1,
            "delay":0,
            "tempMethod":"Automatic",
            "tempMatchFreq":10,
            "tempWithin":0.2,
            "tempFrom":9,
            "tempTo":11,
            "tempStep":0.01,
            "tempComponent":"Ex",
            "tempPeriods":50,
            "multipointEnable":0,
            "multipointSizeShape":"0.1",
            "symmetryH":False,
            "symmetryV":False,
            }

    def isValidVariableName(self, string):
        """
        Checks if string is valid variable name.
        """
        result = re.fullmatch('[a-zA-Z]{1}[a-zA-Z0-9_]*', string)
        return bool(result)

    def createVariableName(self):
        """
        Returns valid not used variable name.
        """
        self.globalData.numberForEqualElementsNames += 1
        variableName = "var_" + str(self.globalData.numberForEqualElementsNames)
        while True:
            if variableName in self.globalData.currentElementsNamesDict or variableName in self.globalData.variables:
                self.globalData.numberForEqualElementsNames += 1
                variableName = "var_" + str(self.globalData.numberForEqualElementsNames)
            else: 
                break
        return variableName

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
import FreeCADGui,QW_Modeller,FreeCAD
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
        Function that uses dictionary to match and call appropriate function from given string with math function name. 
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

        tmpName = self.elementCommandName
        while True:
            if self.elementCommandName in self.globalData.currentElementsNamesDict:
                self.globalData.numberForEqualElementsNames += 1
                self.elementCommandName = tmpName + str(self.globalData.numberForEqualElementsNames)
            else: 
                break
        self.globalData.currentElementsNamesDict[self.elementCommandName] = self.elementCommandName
        self.globalData.elementsInThisFile[self.elementCommandName] = self.elementCommandName

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
        self.globalData.currentElementsNamesDict[self.elementCommandName] = self.elementCommandName
        self.globalData.elementsInThisFile[self.elementCommandName] = self.elementCommandName
        self.globalData.lastCreatedElement = self.elementCommandName

    def do_newline(self,argumentsList):
        """
        Does NEWLINE command from UDO language.
        """

        _x1 = argumentsList[0]
        _y1 = argumentsList[1]
        _x2 = argumentsList[2]
        _y2 = argumentsList[3]

        if self.createPyFiles and (self.currentCommand["element"] or self.currentCommand["selection"]):
            name = ""
            if self.currentCommand["element"]:
                name = self.elementCommandName
            elif self.currentCommand["selection"]:
                name = self.selectionCommandDict["name"]

            if _x1 != _x2 or _y1 != _y2:
                content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))\n""".format(
                    name = name, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)
               
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

        if self.createPyFiles and (self.currentCommand["element"] or self.currentCommand["selection"]):
            name = ""
            if self.currentCommand["element"]:
                name = self.elementCommandName
            elif self.currentCommand["selection"]:
                name = self.selectionCommandDict["name"]

            if _x1 != _x2 or _y1 != _y2:
                content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))\n""".format(
                    name = name, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

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

        if self.createPyFiles and (self.currentCommand["element"] or self.currentCommand["selection"]):
            name = ""
            if self.currentCommand["element"]:
                name = self.elementCommandName
            elif self.currentCommand["selection"]:
                name = self.selectionCommandDict["name"]

            if _x1 != _x2 or _y1 != _y2:
                content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))\n""".format(
                    name = name, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)
        
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

        if self.createPyFiles and (self.currentCommand["element"] or self.currentCommand["selection"]):
            name = ""
            if self.currentCommand["element"]:
                name = self.elementCommandName
            elif self.currentCommand["selection"]:
                name = self.selectionCommandDict["name"]
    
            if _x1 != _x2 or _y1 != _y2:
                content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))\n""".format(
                    name = name, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

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

        if self.createPyFiles and (self.currentCommand["element"] or self.currentCommand["selection"]):
            name = ""
            if self.currentCommand["element"]:
                name = self.elementCommandName
            elif self.currentCommand["selection"]:
                name = self.selectionCommandDict["name"]
    
            if _x1 != _x2 or _y1 != _y2:
                content = """    qwm_doc.sketch_{name}.addGeometry(Part.LineSegment(FreeCAD.Vector({x1},{y1},0), FreeCAD.Vector({x2},{y2},0)))\n""".format(
                    name = name, x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2)

                self.globalData.writeToGeomMediaFile(content)

        self.lineCommandLastPoint = [_x2, _y2]

        if self.currentCommand["port"]:       
            self.addPortPoints(_x1, _y1, _x2, _y2)

    def addPortPoints(self, _x1, _y1, _x2, _y2, isNewLine = False):
        """
        Remembers port's points coordinates.
        """       
        isDirectionZ = self.portCommandDict["currentPoint"] > 4
        isDirectionXY = self.portCommandDict["currentPoint"] >= 3 and self.portCommandDict["height"] != 0
        isDirectionXYAndSpecialWithZeroHeight = self.portCommandDict["type"] == "SPECIAL" and self.portCommandDict["currentPoint"] >= 3 and self.portCommandDict["height"] == 0 and _x1 == _x2 and _y1 == _y2
        
        if isDirectionZ or isDirectionXY or isDirectionXYAndSpecialWithZeroHeight:
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
        udoInterpreter.doNestedParsing(argumentsList[1:-1], UDO_FilePath, debug = False, interpreter_debug = False, 
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

        if not self.isValidVariableName(self.portCommandDict["name"]):
            self.portCommandDict["name"] = self.createVariableName()

        content = ""

        if self.portCommandDict["type"] == "INPTEMPLATE" or self.portCommandDict["type"] == "OUTTEMPLATE":
            content = """    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","{portName}")\n""".format(portName = self.portCommandDict["name"])
        elif self.portCommandDict["type"] == "MUR":
            content = """    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","{portName}")\n""".format(portName = self.portCommandDict["name"])
        elif self.portCommandDict["type"] == "NEAR2FAR": 
            content = """    QW_Modeller.addQWObject("QW_Modeller::NTFBox","{portName}")\n""".format(portName = self.portCommandDict["name"])
        elif self.portCommandDict["type"] == "SPECIAL": 
            content = """    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","{portName}")\n""".format(portName = self.portCommandDict["name"])

        if self.createPyFiles and content:
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

        if self.portCommandDict["height"] == 0 and self.portCommandDict["currentPoint"] > 3:
            length = abs(self.portCommandDict["x1"] - self.portCommandDict["x3"])
            width = abs(self.portCommandDict["y1"] - self.portCommandDict["y3"])
            excitationPointZ = self.portCommandDict["level"]
            orientation = "Z"
            position = excitationPointZ
            rotation = "0.0, 0.0, 0.0, 1.0"

        elif self.portCommandDict["x1"] == self.portCommandDict["x2"]: 
            length = abs(self.portCommandDict["y1"] - self.portCommandDict["y2"])  
            width = self.portCommandDict["height"]          
            excitationPointZ = self.portCommandDict["level"] + self.portCommandDict["height"]/2
            orientation = "X"
            position = self.portCommandDict["excitationPointX"]
            rotation = "0.5, 0.5, 0.5, 0.5"

        elif self.portCommandDict["y1"] == self.portCommandDict["y2"]: 
            length = self.portCommandDict["height"]  
            width = abs(self.portCommandDict["x1"] - self.portCommandDict["x2"])          
            excitationPointZ = self.portCommandDict["level"] + self.portCommandDict["height"]/2
            orientation = "Y"
            position = self.portCommandDict["excitationPointY"]
            rotation = "0.5, 0.5, 0.5, -0.5"
            
        if self.portCommandDict["portexcPointZ"]:
            self.portCommandDict["excitationPointZ"] = self.portCommandDict["portexcPointZ"]
            self.portCommandDict["portexcPointZ"] = None
        else:
            self.portCommandDict["excitationPointZ"] = excitationPointZ

        if self.portCommandDict["type"] == "OUTTEMPLATE":
            portType = "Load"
        if self.portCommandDict["type"] == "INPTEMPLATE":
            portType = "Source"

        if self.portCommandDict["activity"] == "UP":
            activity = "PLUS"
        elif self.portCommandDict["activity"] == "DOWN":
            activity = "MINUS"
        elif self.portCommandDict["activity"] == "NONE":
            activity = "NONE"

        if self.createPyFiles:
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

            elif self.portCommandDict["type"] == "INPTEMPLATE" or self.portCommandDict["type"] == "OUTTEMPLATE":
                content = """    qwm_doc.{portName}.Length = {length}
    qwm_doc.{portName}.Width = {width}
    qwm_doc.{portName}.Placement = FreeCAD.Placement(FreeCAD.Vector({excitationPointX}, {excitationPointY}, {excitationPointZ}), FreeCAD.Rotation({rotation}))
    qwm_doc.{portName}.Orientation = "{orientation}"
    qwm_doc.{portName}.Position = {position}
    qwm_doc.{portName}.Activity = "{activity}"
    qwm_doc.{portName}.Type = "{portType}"
    qwm_doc.{portName}.SymmetryH = {symmetryH}
    qwm_doc.{portName}.SymmetryV = {symmetryV}
    qwm_doc.{portName}.PointCoordX = {excitationPointX}
    qwm_doc.{portName}.PointCoordY = {excitationPointY}
    qwm_doc.{portName}.PointCoordZ = {excitationPointZ}
    qwm_doc.{portName}.effectivePermitivityMode = "AUTO"
    qwm_doc.{portName}.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform({waveform}),{amplitude},{delay},1,0),'{mode}','{tempComponent}',1,QW_Modeller.TemplateGenerationConf('{tempMethod}',({tempMatchFreq},{tempWithin}),({tempFrom},{tempTo},{tempStep}),{effectivePermittivity},{tempPeriods},1,0))
    qwm_doc.{portName}.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation({multipointEnable},"{multipointSizeShape}")
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
                effectivePermittivity = self.portCommandDict["effectivePermittivity"],
                mode = self.portCommandDict["mode"],
                waveform = self.portCommandDict["waveform"],
                amplitude = self.portCommandDict["amplitude"],
                delay = self.portCommandDict["delay"],
                tempMethod = self.portCommandDict["tempMethod"],
                tempMatchFreq = self.portCommandDict["tempMatchFreq"],
                tempWithin = self.portCommandDict["tempWithin"],
                tempFrom = self.portCommandDict["tempFrom"],
                tempTo = self.portCommandDict["tempTo"],
                tempStep = self.portCommandDict["tempStep"],
                tempComponent = self.portCommandDict["tempComponent"],
                tempPeriods = int(self.portCommandDict["tempPeriods"]),
                multipointEnable = int(self.portCommandDict["multipointEnable"]),
                multipointSizeShape = self.portCommandDict["multipointSizeShape"],
                symmetryH = self.portCommandDict["symmetryH"],
                symmetryV = self.portCommandDict["symmetryV"],
                )
        
            elif self.portCommandDict["type"] == "MUR":
                content = """    qwm_doc.{portName}.Orientation = "{orientation}"
    qwm_doc.{portName}.Length = {length}
    qwm_doc.{portName}.Width = {width}
    qwm_doc.{portName}.Placement = FreeCAD.Placement(FreeCAD.Vector({excitationPointX}, {excitationPointY}, {excitationPointZ}),FreeCAD.Rotation({rotation}))
    qwm_doc.{portName}.Position = {position}
    qwm_doc.{portName}.Activity = "{activity}"
    FreeCAD.Gui.ActiveDocument.{portName}.AbsorberDepth = 1.00000
    FreeCAD.Gui.ActiveDocument.{portName}.ShowText = True
    FreeCAD.Gui.ActiveDocument.{portName}.TextSize = 14
    FreeCAD.Gui.ActiveDocument.{portName}.TextPlace = 3
    qwm_doc.{portName}.Type = "MUR"
    qwm_doc.{portName}.EffectivePermittivity = {effectivePermittivity}\n""".format(
                    portName                = self.portCommandDict["name"],
                    orientation             = orientation,
                    length                  = length,
                    width                   = width,
                    excitationPointX        = self.portCommandDict["excitationPointX"],
                    excitationPointY        = self.portCommandDict["excitationPointY"],
                    excitationPointZ        = self.portCommandDict["excitationPointZ"],
                    rotation                = rotation,
                    position                = position,
                    activity                = activity,
                    effectivePermittivity   = self.portCommandDict["effectivePermittivity"],
                    )
            elif self.portCommandDict["type"] == "NEAR2FAR":
                content = """    qwm_doc.{portName}.Length = {length}
    qwm_doc.{portName}.Width = {width}
    qwm_doc.{portName}.Height = {height}
    qwm_doc.{portName}.Placement = FreeCAD.Placement(FreeCAD.Vector({excitationPointX}, {excitationPointY}, {excitationPointZ}),FreeCAD.Rotation({rotation}))
    FreeCAD.Gui.ActiveDocument.{portName}.ShowText = True
    FreeCAD.Gui.ActiveDocument.{portName}.TextSize = 14\n""".format(
                    portName                = self.portCommandDict["name"],
                    length                  = length,
                    width                   = width,
                    height                  = self.portCommandDict["height"],
                    excitationPointX        = self.portCommandDict["excitationPointX"],
                    excitationPointY        = self.portCommandDict["excitationPointY"],
                    excitationPointZ        = self.portCommandDict["excitationPointZ"],
                    rotation                = rotation,
                    )
        
            elif self.portCommandDict["type"] == "SPECIAL" and self.portCommandDict["currentPoint"] > 4:
                content = """    qwm_doc.{portName}.Placement = FreeCAD.Placement(FreeCAD.Vector({excitationPointX}, {excitationPointY}, {excitationPointZ}),FreeCAD.Rotation({rotation}))
    qwm_doc.{portName}.Orientation = "{orientation}"
    qwm_doc.{portName}.Position = {position}
    qwm_doc.{portName}.Length = {length}
    qwm_doc.{portName}.Width = {width}
    FreeCAD.Gui.ActiveDocument.{portName}.ShowText = False
    FreeCAD.Gui.ActiveDocument.{portName}.TextSize = 14
    FreeCAD.Gui.ActiveDocument.{portName}.TextPlace = 3\n""".format(
                    portName                = self.portCommandDict["name"],
                    excitationPointX        = self.portCommandDict["excitationPointX"],
                    excitationPointY        = self.portCommandDict["excitationPointY"],
                    excitationPointZ        = excitationPointZ,
                    rotation                = rotation,
                    orientation             = orientation,
                    position                = excitationPointZ,
                    length                  = length,
                    width                   = width,
                    )

            elif self.portCommandDict["type"] == "SPECIAL" and self.portCommandDict["currentPoint"] <= 4:

                if orientation == "X":
                    content = """    qwm_doc.{portName}.Placement = FreeCAD.Placement(FreeCAD.Vector({excitationPointX}, {excitationPointY}, {excitationPointZ}),FreeCAD.Rotation({rotation}))
    qwm_doc.{portName}.Orientation = "{orientation}"
    qwm_doc.{portName}.Position = {position}
    qwm_doc.{portName}.Length = {length}
    qwm_doc.{portName}.Width = {width}
    FreeCAD.Gui.ActiveDocument.{portName}.ShowText = False
    FreeCAD.Gui.ActiveDocument.{portName}.TextSize = 14
    FreeCAD.Gui.ActiveDocument.{portName}.TextPlace = 3\n""".format(
                        portName                = self.portCommandDict["name"],
                        excitationPointX        = self.portCommandDict["excitationPointX"],
                        excitationPointY        = self.portCommandDict["excitationPointY"],
                        excitationPointZ        = self.portCommandDict["excitationPointZ"],
                        rotation                = rotation,
                        orientation             = orientation,
                        position                = self.portCommandDict["excitationPointX"],
                        length                  = length,
                        width                   = width,
                        )

                elif orientation == "Y":
                    content = """    qwm_doc.{portName}.Placement = FreeCAD.Placement(FreeCAD.Vector({excitationPointX}, {excitationPointY}, {excitationPointZ}),FreeCAD.Rotation({rotation}))
    qwm_doc.{portName}.Orientation = "{orientation}"
    qwm_doc.{portName}.Position = {position}
    qwm_doc.{portName}.Length = {length}
    qwm_doc.{portName}.Width = {width}
    FreeCAD.Gui.ActiveDocument.{portName}.ShowText = False
    FreeCAD.Gui.ActiveDocument.{portName}.TextSize = 14
    FreeCAD.Gui.ActiveDocument.{portName}.TextPlace = 3\n""".format(
                        portName                = self.portCommandDict["name"],
                        excitationPointX        = self.portCommandDict["excitationPointX"],
                        excitationPointY        = self.portCommandDict["excitationPointY"],
                        excitationPointZ        = self.portCommandDict["excitationPointZ"],
                        rotation                = rotation,
                        orientation             = orientation,
                        position                = self.portCommandDict["excitationPointY"],
                        length                  = length,
                        width                   = width,
                        )
            
            elif self.portCommandDict["type"] == "OPEN":

                if orientation == "X":
                    content = """    qwm_doc.QW_Mesh_Borders.BorderXMin = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderXMax = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderYMin = "PMC"
    qwm_doc.QW_Mesh_Borders.BorderYMax = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderZMin = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderZMax = "PEC"
    qwm_doc.QW_Mesh.AutoAdjustMeshBoundaryCheck = False
    qwm_doc.QW_Mesh.bboxminY = {bboxMin}
    qwm_doc.QW_Mesh.bboxmaxY = {bboxMax}\n""".format(
                    bboxMin = self.portCommandDict["y1"],
                    bboxMax = self.portCommandDict["y2"],
                    )

                elif orientation == "Y":
                    content = """    qwm_doc.QW_Mesh_Borders.BorderXMin = "PMC"
    qwm_doc.QW_Mesh_Borders.BorderXMax = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderYMin = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderYMax = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderZMin = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderZMax = "PEC"
    qwm_doc.QW_Mesh.AutoAdjustMeshBoundaryCheck = False
    qwm_doc.QW_Mesh.bboxminX = {bboxMin}
    qwm_doc.QW_Mesh.bboxmaxX = {bboxMax}\n""".format(
                    bboxMin = self.portCommandDict["x1"],
                    bboxMax = self.portCommandDict["x2"],
                    )

                elif orientation == "Z":
                    content = """    qwm_doc.QW_Mesh_Borders.BorderXMin = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderXMax = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderYMin = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderYMax = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderZMin = "PMC"
    qwm_doc.QW_Mesh_Borders.BorderZMax = "PEC"
    qwm_doc.QW_Mesh.AutoAdjustMeshBoundaryCheck = False
    qwm_doc.QW_Mesh.bboxminZ = {bboxMin}
    qwm_doc.QW_Mesh.bboxmaxZ = {bboxMax}\n""".format(
                    bboxMin = self.portCommandDict["level"],
                    bboxMax = self.portCommandDict["level"] + self.portCommandDict["height"],
                    )

            self.globalData.writeToExcitFile(content)


        self.currentCommand["port"] = False
        self.portCommandDict = self.initPortCommandDict()

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
            if mediumType == "Pec":
                mediumType = "PEC"
            elif mediumType == "Pmc":
                mediumType = "PMC"
 
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

    def do_portexc(self, argumentsList):
        """
        Does PORTEXC command from UDO language.
        """
        self.portCommandDict["portexcPointZ"] = argumentsList[1]

    def do_markfj(self, argumentsList):
        """
        Does MARKFJ command from UDO language.
        """
        # MARKFJ (<item_type>,<range>,<command>)

        itemType = argumentsList[0]
        rangeOfOperation = argumentsList[1]
        command = argumentsList[2]

        currentElementsSet = set(self.globalData.elementsInThisFile.values())

        if rangeOfOperation == "ALL":
            if command == "ACTIVE":
                self.activeElements = currentElementsSet
            elif command == "PASSIVE":
                self.passiveElements = currentElementsSet
            else: # command == "RESET":
                self.activeElements = set()
                self.passiveElements = set()

        elif rangeOfOperation == "ALLACTIVE":
            if command == "ACTIVE":
                self.activeElements = currentElementsSet
            else: # command == "RESET":
                self.activeElements = set()

        elif rangeOfOperation == "ALLPASSIVE":
            if command == "PASSIVE":
                self.passiveElements = currentElementsSet
            else: # command == "RESET":
                self.passiveElements = set()

        elif rangeOfOperation == "LAST":
            if command == "ACTIVE":
                self.activeElements.add(self.globalData.lastCreatedElement)
            elif command == "PASSIVE":
                self.passiveElements.add(self.globalData.lastCreatedElement)
            else: # command == "RESET":
                if self.globalData.lastCreatedElement in self.activeElements:
                    self.activeElements.remove(self.globalData.lastCreatedElement)
                else: # self.globalData.lastCreatedElement in self.passiveElements
                    self.passiveElements.remove(self.globalData.lastCreatedElement)

        else:
            if command == "ACTIVE":
                self.activeElements.add(rangeOfOperation)
            elif command == "PASSIVE":
                self.passiveElements.add(rangeOfOperation)
            else: # command == "RESET":
                if rangeOfOperation in self.activeElements:
                    self.activeElements.remove(rangeOfOperation)
                else: # rangeOfOperation in self.passiveElements
                    self.passiveElements.remove(rangeOfOperation)


    def do_mark(self, argumentsList):
        """
        Does MARK command from UDO language.
        """

        itemType = argumentsList[0]
        rangeOfOperation = argumentsList[1]
        command = argumentsList[2]

        currentElementsSet = set(self.globalData.elementsInThisFile.values())

        if rangeOfOperation == "ALL":
            if command == "SET":
                self.markedElements = currentElementsSet
            else: # command == "RESET":
                self.markedElements = set()

        elif rangeOfOperation == "ALLACTIVE":
            if command == "SET":
                for elem in self.activeElements:
                    self.markedElements.add(elem)
            else: # command == "RESET":
                for elem in self.activeElements:
                    self.markedElements.remove(elem)

        elif rangeOfOperation == "ALLPASSIVE":
            if command == "SET":
                for elem in self.passiveElements:
                    self.markedElements.add(elem)
            else: # command == "RESET":
                for elem in self.passiveElements:
                    self.markedElements.remove(elem)

        elif rangeOfOperation == "LAST":
            if command == "SET":
                self.markedElements.add(self.globalData.lastCreatedElement)
            else: # command == "RESET":
                self.markedElements.remove(self.globalData.lastCreatedElement)

        else:
            if command == "SET":
                self.markedElements.add(rangeOfOperation)
            else: # command == "RESET":
                self.markedElements.remove(rangeOfOperation)

    def do_join(self, argumentsList):
        """
        Does JOIN command from UDO language.
        """
        operationType = argumentsList[0]
        content = ""
        self.globalData.numberForEqualElementsNames += 1

        shapesList = list(self.activeElements) + list(self.passiveElements)
        shapesListStr = "["
        for i in range(len(shapesList)):
            shapesList[i] = self.globalData.elementsInThisFile[shapesList[i]]
            shapesListStr += "qwm_doc." + shapesList[i] + ","
        shapesListStr += "]"

        if operationType == "CUT":
            objectName = "Cut" + str(self.globalData.numberForEqualElementsNames)

            content = """    qwm_doc.addObject("Part::Cut","{objectName}")
    qwm_doc.{objectName}.Base = qwm_doc.{base}
    qwm_doc.{objectName}.Tool = qwm_doc.{tool}
    qwm_doc.{objectName}.Medium = qwm_doc.{firstElementName}.Medium\n""".format(
                        objectName = objectName,
                        firstElementName = shapesList[0],
                        base = shapesList[-1],
                        tool = shapesList[0],
                        )
        
            for elem in shapesList:
                content += "    FreeCAD.Gui.activeDocument().hide('" + elem + "')\n"
        

        elif operationType == "INTERSECT":
            objectName = "Common" + str(self.globalData.numberForEqualElementsNames)

            content = """    qwm_doc.addObject("Part::MultiCommon","{objectName}")
    qwm_doc.{objectName}.Shapes = {shapesList}
    qwm_doc.{objectName}.Medium = qwm_doc.{firstElementName}.Medium\n""".format(
                        shapesList = shapesListStr,
                        objectName = objectName,
                        firstElementName = shapesList[0],
                        )
        
            for elem in shapesList:
                content += "    FreeCAD.Gui.activeDocument()." + elem + ".Visibility = False\n"


        elif operationType == "GLUE":
            objectName = "Fusion" + str(self.globalData.numberForEqualElementsNames)

            content = """    qwm_doc.addObject("Part::MultiFuse","{objectName}")
    qwm_doc.{objectName}.Shapes = {shapesList}
    qwm_doc.{objectName}.Medium = qwm_doc.{firstElementName}.Medium\n""".format(
                        shapesList = shapesListStr,
                        objectName = objectName,
                        firstElementName = shapesList[0],
                        )
        
            for elem in shapesList:
                content += "    FreeCAD.Gui.activeDocument()." + elem + ".Visibility = False\n"


        self.globalData.writeToGeomMediaFile(content)
        self.globalData.currentElementsNamesDict[objectName] = objectName
        self.globalData.elementsInThisFile[objectName] = objectName
        self.globalData.lastCreatedElement = objectName

    def do_rotate(self, argumentsList):
        """
        Does ROTATE command from UDO language.
        """
        angle = argumentsList[0]
        x0 = argumentsList[1]
        y0 = argumentsList[2]

        content = ""

        for elem in self.markedElements:
            content += """    qwm_doc.{elemName}.Placement=FreeCAD.Placement(FreeCAD.Vector(0,0,0), FreeCAD.Rotation(FreeCAD.Vector(0,0,1),{angle}), FreeCAD.Vector({x0},{y0},0))\n""".format(
                elemName = self.globalData.currentElementsNamesDict[elem],
                angle = (-1) * angle,
                x0 = x0,
                y0 = y0,
                )

        self.globalData.writeToGeomMediaFile(content)

    def do_rename(self, argumentsList):
        """
        Does RENAME command from UDO language.
        """
        rangeOfOperation = argumentsList[1]
        newName = argumentsList[2]
        oldName = ""
        content = ""

        if rangeOfOperation == "LAST":
            oldName = self.globalData.lastCreatedElement

            self.globalData.currentElementsNamesDict[newName] = self.globalData.currentElementsNamesDict.pop(oldName)
            self.globalData.elementsInThisFile[newName] = self.globalData.elementsInThisFile.pop(oldName)
            self.globalData.lastCreatedElement = newName

            content = "    qwm_doc.{originalName}.Label = '{newName}'\n".format(
                originalName = self.globalData.currentElementsNamesDict[newName],
                newName = newName,
                )

        else:
            oldName = rangeOfOperation

            self.globalData.currentElementsNamesDict[newName] = self.globalData.currentElementsNamesDict.pop(oldName)
            self.globalData.elementsInThisFile[newName] = self.globalData.elementsInThisFile.pop(oldName)

            content = "    qwm_doc.{originalName}.Label = '{newName}'\n".format(
                originalName = self.globalData.currentElementsNamesDict[newName],
                newName = newName,
                )

        if oldName in self.markedElements:
            self.markedElements.remove(oldName)
            self.markedElements.add(newName)
        if oldName in self.activeElements:
            self.activeElements.remove(oldName)
            self.activeElements.add(newName)
        if oldName in self.passiveElements:
            self.passiveElements.remove(oldName)
            self.passiveElements.add(newName)

        self.globalData.writeToGeomMediaFile(content)

    def do_delete(self, argumentsList):
        """
        Does DELETE command from UDO language.
        """
        rangeOfOperation = argumentsList[1]

        if rangeOfOperation == "ALLACTIVE":
            for elem in self.activeElements:
                if elem in self.markedElements:
                    self.markedElements.remove(elem)
            self.activeElements = set()

        elif rangeOfOperation == "ALLPASSIVE":
            for elem in self.passiveElements:
                if elem in self.markedElements:
                    self.markedElements.remove(elem)
            self.passiveElements = set()

        elif rangeOfOperation == "LAST":
            if self.globalData.lastCreatedElement in self.activeElements:
                self.activeElements.remove(self.globalData.lastCreatedElement)
            elif self.globalData.lastCreatedElement in self.passiveElements:
                self.passiveElements.remove(self.globalData.lastCreatedElement)
            elif self.globalData.lastCreatedElement in self.markedElements:
                self.markedElements.remove(self.globalData.lastCreatedElement)

    def do_ferritepar(self, argumentsList):
        """
        Does FERRITEPAR command from UDO language.
        """
        # FERRITEPAR (<mediumname>, <eps>, <mu>, <sigma>, <sigmaM>, <alpha>, <Ms>, <Hi>, <dens>)
        
        if self.createPyFiles:
            mediumName  = argumentsList[0]
            eps         = argumentsList[1]
            mu          = argumentsList[2]
            sigma       = argumentsList[3]
            sigmaM      = argumentsList[4]
            alpha       = argumentsList[5]
            Ms          = argumentsList[6]
            Hi          = argumentsList[7]
            dens        = argumentsList[8]
            
            content = """    {mediumName}.materialtype = "Ferrite"
    {mediumName}.Eps = {eps}
    {mediumName}.Mu = {mu}
    {mediumName}.Sigma = {sigma}
    {mediumName}.SigmaM = {sigmaM}
    {mediumName}.Fer_alfa = {alpha}
    {mediumName}.Fer_Ms = {Ms}
    {mediumName}.Fer_Hi = {Hi}
    {mediumName}.density = {dens}\n""".format(
                mediumName  = mediumName,
                eps         = eps,
                mu          = mu,
                sigma       = sigma,
                sigmaM      = sigmaM,
                alpha       = alpha,
                Ms          = Ms,
                Hi          = Hi,
                dens        = dens,
                )
            
            self.globalData.writeToGeomMediaFile(content)

    def do_thermalpar(self, argumentsList):
        """
        Does THERMALPAR command from UDO language.
        """
        # THERMALPAR (<mediumname>, <ini_temp>, <spec_heat>, <therm_cond_X>, <therm_cond_Y>, <therm_cond_Z>)

        if self.createPyFiles:
            mediumName  = argumentsList[0]
            ini_temp    = argumentsList[1]
            spec_heat   = argumentsList[2]
            therm_cond_X= argumentsList[3]
            therm_cond_Y= argumentsList[4]
            therm_cond_Z= argumentsList[5]

            content = """    {mediumName}.initemp = {ini_temp}
    {mediumName}.specheat = {spec_heat}
    {mediumName}.thermcond = [{therm_cond_X},{therm_cond_Y},{therm_cond_Z}]\n""".format(
                mediumName  = mediumName,
                ini_temp    = ini_temp,
                spec_heat   = spec_heat,
                therm_cond_X= therm_cond_X,
                therm_cond_Y= therm_cond_Y,
                therm_cond_Z= therm_cond_Z,
                )
            
            self.globalData.writeToGeomMediaFile(content)

    def do_viscosity(self, argumentsList):
        """
        Does VISCOSITY command from UDO language.
        """
        # VISCOSITY (<mediumname>, <viscosity>) 

        if self.createPyFiles:
            mediumName  = argumentsList[0]
            viscosity   = argumentsList[1]

            content = """    {mediumName}.viscosity = {viscosity}\n""".format(
                mediumName  = mediumName,
                viscosity   = viscosity,
                )
            
            self.globalData.writeToGeomMediaFile(content)

    def do_setsuspflags(self, argumentsList):
        """
        Does SETSUSPFLAGS command from UDO language.
        """
        pass

    def do_cirtype(self, argumentsList):
        """
        Does CIRTYPE command from UDO language.
        """
        if self.createPyFiles:
            self.globalData.hasSomethingBeenAddedToFiles["circuitFile"] = True

            type = argumentsList[0]
            defaultMedium = argumentsList[1]

            typeStr = ""
            if type == 0:
                typeStr = "2DV"
            elif type == 2:
                typeStr = "3DP"
            elif type == 4:
                typeStr = "BOR"
            else:
                typeStr = "3D"

            content = """    qwm_doc.QW_Circuit.CircuitType = "{typeStr}"\n""".format(
                typeStr = typeStr,
                )
            
            self.globalData.writeToCircuitFile(content)


    def do_losses(self, argumentsList):
        """
        Does LOSSES command from UDO language.
        """
        if self.createPyFiles:
            controlStr = argumentsList[0]

            suppressMagneticLosses = "-M" in controlStr
            suppressElectricLosses = "-E" in controlStr
            suppressMetalLosses = "-P" in controlStr

            metalLossesBandWidth = ""
            if "BN" in controlStr:
                metalLossesBandWidth = "Narrow"
            elif "BD" in controlStr:
                metalLossesBandWidth = "Decade"
            elif "BT" in controlStr:
                metalLossesBandWidth = "Two-Decades"

            content = """    qwm_doc.QW_Circuit.MetalLossesBandwidth = "{metalLossesBandWidth}"
    qwm_doc.QW_Circuit.SuppressLossesDielectric = {suppressElectricLosses}
    qwm_doc.QW_Circuit.SuppressLossesMetal = {suppressMetalLosses}
    qwm_doc.QW_Circuit.SuppressLossesMagnetic = {suppressMagneticLosses}\n""".format(
                suppressMagneticLosses = suppressMagneticLosses,
                suppressElectricLosses = suppressElectricLosses,
                suppressMetalLosses = suppressMetalLosses,
                metalLossesBandWidth = metalLossesBandWidth,
                )
            
            self.globalData.writeToCircuitFile(content)


    def do_expopt(self, argumentsList):
        """
        Does EXPOPT command from UDO language.
        """
        # EXPOPT (<Suppress singularity corrections>, <Suppress density/SAR>, <Allow BHM>) - Sets export options. Parameters: 1 – check option (on), 0 – uncheck option (off), 
        if self.createPyFiles:
            suppressSingularityCorrections  = bool(argumentsList[0])
            suppressDensitySar              = bool(argumentsList[1])
            allowBhm                        = bool(argumentsList[2])

            content = """    qwm_doc.QW_Circuit.SuppressSingularityCorrections = {suppressSingularityCorrections}
    qwm_doc.QW_Circuit.SuppressDensity_SAR = {suppressDensitySar}
    qwm_doc.QW_BHM.AllowBHM = {allowBhm}\n""".format(
                suppressSingularityCorrections = suppressSingularityCorrections,
                suppressDensitySar = suppressDensitySar,
                allowBhm = allowBhm,
                )
            
            self.globalData.writeToCircuitFile(content)

    def do_expopt2(self, argumentsList):
        """
        Does EXPOPT2 command from UDO language.
        """
        # EXPOPT2 (<what>, <OnOff>)
        # 0 - <Suppress singularity corrections>
        # 1 - <Suppress density/SAR>
        # 2 - <Allow BHM>
        # 3 - <Suppress subregions export>
        # 4 - <Allow Template QS Test>

        #if self.createPyFiles:
        #    what = argumentsList[0]
        #    isOn = argumentsList[1]

        #    content = """ """
            
        #    self.globalData.writeToCircuitFile(content)
        pass


    def do_units(self, argumentsList):
        """
        Does UNITS command from UDO language.
        """
        # UNITS (<space>,<frequency>) – Sets project units (space options: 0 - milimeters, 1 – micrometers, 2 - inches, 3 – mils, 4 – meters, 5 - nanometers; frequency always GHz)        
        if self.createPyFiles:
            geometryUnits  = argumentsList[0]
            
            geometryUnitsStr = ""
            if geometryUnits == 0:
                geometryUnitsStr = "mm"
            elif geometryUnits == 1:
                geometryUnitsStr = "um"
            elif geometryUnits == 2:
                geometryUnitsStr = "inch"
            elif geometryUnits == 3:
                geometryUnitsStr = "mils"
            elif geometryUnits == 4:
                geometryUnitsStr = "m"
            elif geometryUnits == 5:
                geometryUnitsStr = "nm"

            content = """    qwm_doc.QW_Circuit.Units = "{geometryUnitsStr}"
    qwm_doc.QW_Circuit.FrequencyUnits = "GHz"\n""".format(
                geometryUnitsStr = geometryUnitsStr,
                )
            
            self.globalData.writeToCircuitFile(content)

    def do_unitsgeometry(self, argumentsList):
        """
        Does UNITSGEOMETRY command from UDO language.
        """
        # UNITSGEOMETRY (<space>) – Sets project’s geometry units (space values: 0 - milimeters, 1 – micrometers, 2 - inches, 3 – mils, 4 – meters, 5 – nanometers, other - milimeters)
       
        if self.createPyFiles:
            geometryUnits  = argumentsList[0]
            
            geometryUnitsStr = ""
            if geometryUnits == 0:
                geometryUnitsStr = "mm"
            elif geometryUnits == 1:
                geometryUnitsStr = "um"
            elif geometryUnits == 2:
                geometryUnitsStr = "inch"
            elif geometryUnits == 3:
                geometryUnitsStr = "mils"
            elif geometryUnits == 4:
                geometryUnitsStr = "m"
            elif geometryUnits == 5:
                geometryUnitsStr = "nm"
            else:
                geometryUnitsStr = "mm"

            content = """    qwm_doc.QW_Circuit.Units = "{geometryUnitsStr}"\n""".format(
                geometryUnitsStr = geometryUnitsStr,
                )
            
            self.globalData.writeToCircuitFile(content)

    def do_unitsfrequency(self, argumentsList):
        """
        Does UNITSFREQUENCY command from UDO language.
        """
        # UNITSFREQUENCY (<frequency>) – Sets project’s frequency units (frequency values: 0 - GHz, 1 – Hz, 2 - kHz, 3 – MHz, 4 – THz, 5 – PHz, other - GHz)
        if self.createPyFiles:
            frequencyUnits  = argumentsList[0]
            
            frequencyUnitsStr = ""
            if frequencyUnits == 0:
                frequencyUnitsStr = "GHz"
            elif frequencyUnits == 1:
                frequencyUnitsStr = "Hz"
            elif frequencyUnits == 2:
                frequencyUnitsStr = "kHz"
            elif frequencyUnits == 3:
                frequencyUnitsStr = "MHz"
            elif frequencyUnits == 4:
                frequencyUnitsStr = "THz"
            elif frequencyUnits == 5:
                frequencyUnitsStr = "PHz"
            else:
                frequencyUnitsStr = "GHz"

            content = """    qwm_doc.QW_Circuit.FrequencyUnits = "{frequencyUnits}"\n""".format(
                frequencyUnits = frequencyUnitsStr,
                )
            
            self.globalData.writeToCircuitFile(content)

    def do_meshpar(self, argumentsList):
        """
        Does MESHPAR command from UDO language.
        """
        # MESHPAR (<arg1>, ...,<arg10>)
        if self.createPyFiles:
            self.globalData.hasSomethingBeenAddedToFiles["meshFile"] = True

            cellX           = argumentsList[0]
            cellY           = argumentsList[1]
            cellZ           = argumentsList[2]
            lowerLimX       = argumentsList[3]
            upperLimX       = argumentsList[4]
            lowerLimY       = argumentsList[5]
            upperLimY       = argumentsList[6]
            lowerLimZ       = argumentsList[7]
            upperLimZ       = argumentsList[8]
            adjustToObjects = argumentsList[9]

            length = upperLimX - lowerLimX
            width = upperLimY - lowerLimY
            height = upperLimZ - lowerLimZ

            locationX = (upperLimX + lowerLimX) / 2
            locationY = (upperLimY + lowerLimY) / 2
            locationZ = (upperLimZ + lowerLimZ) / 2
            
            self.globalData.numberForEqualElementsNames += 1
            objectName = "MeshBox" + str(self.globalData.numberForEqualElementsNames)

            content = """    {objectName} = QW_Modeller.addQWObject("QW_Modeller::MeshBox","{objectName}")
    {objectName}.Length = {length}
    {objectName}.Width = {width}
    {objectName}.Height = {height}
    {objectName}.Placement = FreeCAD.Placement(FreeCAD.Vector({locationX},{locationY},{locationZ}),FreeCAD.Rotation(0.0000000,0.0000000,0.0000000,1.0000000))
    {objectName}.MeshX = True
    {objectName}.MeshY = True
    {objectName}.MeshZ = True
    {objectName}.MeshXCellSize = {cellX}
    {objectName}.MeshYCellSize = {cellY}
    {objectName}.MeshZCellSize = {cellZ}
    {objectName}.SnapToXMinus = False
    {objectName}.SnapToXPlus = False
    {objectName}.SnapToYMinus = False
    {objectName}.SnapToYPlus = False
    {objectName}.SnapToZMinus = False
    {objectName}.SnapToZPlus = False\n""".format(
                objectName      = objectName,
                cellX           = cellX,
                cellY           = cellY,
                cellZ           = cellZ,
                locationX       = locationX,
                locationY       = locationY,
                locationZ       = locationZ,
                length          = length,
                width           = width,
                height          = height,
                )
            
            self.globalData.writeToMeshFile(content)


    def do_section(self, argumentsList):
        """
        Does SECTION command from UDO language.
        """
        self.globalData.hasSomethingBeenAddedToFiles["geomMediaFile"] = True
        self.currentCommand["selection"] = True

        self.selectionCommandDict["level"]      = argumentsList[0]
        self.selectionCommandDict["height"]     = argumentsList[1]
        self.selectionCommandDict["height2"]    = argumentsList[2]
        self.selectionCommandDict["mediumName"] = argumentsList[3]
        self.selectionCommandDict["name"]       = argumentsList[4]

        tmpName = self.selectionCommandDict["name"]
        while True:
            if self.selectionCommandDict["name"] in self.globalData.currentElementsNamesDict:
                self.globalData.numberForEqualElementsNames += 1
                self.selectionCommandDict["name"] = tmpName + str(self.globalData.numberForEqualElementsNames)
            else: 
                break
        self.selectionCommandDict["upperName"] = self.selectionCommandDict["name"] + "U"
        self.selectionCommandDict["lowerName"] = self.selectionCommandDict["name"] + "D"
        self.globalData.currentElementsNamesDict[self.selectionCommandDict["upperName"]] = self.selectionCommandDict["upperName"]
        self.globalData.elementsInThisFile[self.selectionCommandDict["upperName"]] = self.selectionCommandDict["upperName"]
        self.globalData.currentElementsNamesDict[self.selectionCommandDict["lowerName"]] = self.selectionCommandDict["lowerName"]
        self.globalData.elementsInThisFile[self.selectionCommandDict["lowerName"]] = self.selectionCommandDict["lowerName"]
        
        if self.createPyFiles:
            content = """    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_{name}')
    qwm_doc.sketch_{name}.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,{level}),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))\n""".format(
                name = self.selectionCommandDict["name"], 
                level = self.selectionCommandDict["level"],
                )
        
            self.globalData.writeToGeomMediaFile(content)

    def do_endsection(self, argumentsList):
        """
        Does ENDSECTION command from UDO language.
        """

        if self.createPyFiles:
            content = ""

            if self.selectionCommandDict["height"] > 0:
                content += """    qwm_doc.addObject("Part::Extrusion", "{upperName}")
    qwm_doc.{upperName}.Base = qwm_doc.sketch_{name}
    qwm_doc.{upperName}.Dir = (0, 0, {height})
    qwm_doc.{upperName}.Solid = True
    qwm_doc.{upperName}.ViewObject.Transparency = 60
    qwm_doc.{upperName}.Medium = QW_Modeller.getQWMedium("{mediumName}")\n""".format(
                    upperName   = self.selectionCommandDict["upperName"],
                    name        = self.selectionCommandDict["name"],
                    height      = self.selectionCommandDict["height"],
                    mediumName  = self.selectionCommandDict["mediumName"],
                    )
            
            if self.selectionCommandDict["height2"] > 0:
                content += """    qwm_doc.addObject("Part::Extrusion", "{lowerName}")
    qwm_doc.{lowerName}.Base = qwm_doc.sketch_{name}
    qwm_doc.{lowerName}.Dir = (0, 0, -{height2})
    qwm_doc.{lowerName}.Solid = True
    qwm_doc.{lowerName}.ViewObject.Transparency = 60
    qwm_doc.{lowerName}.Medium = QW_Modeller.getQWMedium("{mediumName}")\n""".format(
                    lowerName   = self.selectionCommandDict["lowerName"],
                    name        = self.selectionCommandDict["name"],
                    height2     = self.selectionCommandDict["height2"],
                    mediumName  = self.selectionCommandDict["mediumName"],
                    )

            self.globalData.writeToGeomMediaFile(content)

        self.currentCommand["selection"] = False
        self.globalData.currentElementsNamesDict[self.selectionCommandDict["upperName"]] = self.selectionCommandDict["upperName"]
        self.globalData.elementsInThisFile[self.selectionCommandDict["upperName"]] = self.selectionCommandDict["upperName"]
        self.globalData.currentElementsNamesDict[self.selectionCommandDict["lowerName"]] = self.selectionCommandDict["lowerName"]
        self.globalData.elementsInThisFile[self.selectionCommandDict["lowerName"]] = self.selectionCommandDict["lowerName"]
        self.globalData.currentElementsNamesDict[self.selectionCommandDict["name"]] = self.selectionCommandDict["name"]
        self.globalData.elementsInThisFile[self.selectionCommandDict["name"]] = self.selectionCommandDict["name"]
        self.globalData.lastCreatedElement = self.selectionCommandDict["name"]

    def do_epseff(self, argumentsList):
        """
        Does EPSEFF command from UDO language.
        """
        self.portCommandDict["effectivePermittivity"] = argumentsList[0]

    def do_mode(self, argumentsList):
        """
        Does MODE command from UDO language.
        """
        modeIndex = argumentsList[0]
        
        # (0 – Dynamic, 1 – TEM (Quasistatic), 2 – R_TE10 (TE10 mode in rectangular waveguide), 3- R_TE01 (TE01 mode in rectangular waveguide), 4 - R_TE11 (TE11 mode in rectangular waveguide), 5 - R_TM11 (TM11 mode in rectangular waveguide), 6 - C_TE11 (TE11 mode in circular waveguide), 7 - C_TM01 (TM01 mode in circular waveguide), 8 – multiTEM, 9 – planeTEM) 

        self.portCommandDict["mode"] = {
            0:"Arbitrary",
            1:"TEM",
            2:"R_TE10",
            3:"R_TE01",
            4:"R_TE11",
            5:"R_TM11",
            6:"C_TE11",
            7:"C_TM01",
            8:"TEM",
            9:"planeTEM",
            }[modeIndex]

    def do_waveform(self, argumentsList):
        """
        Does WAVEFORM command from UDO language.
        """
        # (<shape>,<f1>,<f2>,<duration>,<amplitude>,<delay>,<file_name>)

        shape       = argumentsList[0]
        f1          = argumentsList[1]
        f2          = argumentsList[2]
        duration    = argumentsList[3]
        fileName    = argumentsList[6]

        self.portCommandDict["amplitude"] = argumentsList[4]
        self.portCommandDict["delay"] = argumentsList[5]

        if shape == -1:
            self.portCommandDict["waveform"] = "'no excitation'"
        elif shape == 0:
            self.portCommandDict["waveform"] = "'delta'"
        elif shape == 1:
            self.portCommandDict["waveform"] = "'sinusoidal'," + str(f1)
        elif shape == 2:
            self.portCommandDict["waveform"] = "'pulse of spectrum f<f2',{f2},{duration}".format(
                f2          = f2,
                duration    = duration,
                )
        elif shape == 3:
            self.portCommandDict["waveform"] = "'pulse of spectrum f1<f<f2',{f1},{f2},{duration}".format(
                f1          = f1,
                f2          = f2,
                duration    = duration,
                )
        elif shape == 4:
            self.portCommandDict["waveform"] = "'Gauss of spectrum f=f1(-/+f2)',{f1},{f2},{duration}".format(
                f1          = f1,
                f2          = f2,
                duration    = duration,
                )
        elif shape == 5:
            self.portCommandDict["waveform"] = "'step pulse'"
        elif shape == 6:
            self.portCommandDict["waveform"] = "'step with finite rise time tr=1/f2'," + str(f2)
        elif shape == 7:
            self.portCommandDict["waveform"] = "'defined by user text file','{file}'".format(file = fileName)


    def do_tempdp(self, argumentsList):
        """
        Does TEMPDP command from UDO language.
        """
        # (<method>,<match_freq>,<within>,<from>,<to>,<step>,<component>,<periods>)

        if argumentsList[0] == 0:
            self.portCommandDict["tempMethod"] = "Automatic"
        elif argumentsList[0] == 1:
            self.portCommandDict["tempMethod"] = "Manual"

        self.portCommandDict["tempMatchFreq"] = argumentsList[1]
        self.portCommandDict["tempWithin"] = argumentsList[2]
        self.portCommandDict["tempFrom"] = argumentsList[3]
        self.portCommandDict["tempTo"] = argumentsList[4]
        self.portCommandDict["tempStep"] = argumentsList[5]

        if argumentsList[6] == 0:
            self.portCommandDict["tempComponent"] = "Ex"
        elif argumentsList[6] == 1:
            self.portCommandDict["tempComponent"] = "Ey"
        elif argumentsList[6] == 2:
            self.portCommandDict["tempComponent"] = "Ez"
        elif argumentsList[6] == 3:
            self.portCommandDict["tempComponent"] = "Hx"
        elif argumentsList[6] == 4:
            self.portCommandDict["tempComponent"] = "Hy"
        elif argumentsList[6] == 5:
            self.portCommandDict["tempComponent"] = "Hz"

        self.portCommandDict["tempPeriods"] = argumentsList[7]


    def do_multipoint(self, argumentsList):
        """
        Does MULTIPOINT command from UDO language.
        """
        
        self.portCommandDict["multipointEnable"] = argumentsList[0]
        self.portCommandDict["multipointSizeShape"] = argumentsList[1]


    def do_portpar(self, argumentsList):
        """
        Does PORTPAR command from UDO language.
        """
        pass

    def do_sk1diff(self, argumentsList):
        """
        Does SK1DIFF command from UDO language.
        """
        if self.createPyFiles:
            # (<lower_freq>,<upper_freq>,<freq_step>,<assumptions>)
            lowerFreq           = argumentsList[0]
            upperFreq           = argumentsList[1]
            freqStep            = argumentsList[2]
            assumptionsIndex    = argumentsList[3]

            reciprocalNport = False
            reciprocalLossless2port = False

            if assumptionsIndex == 1:
                reciprocalNport = True
            elif assumptionsIndex == 2:
                reciprocalLossless2port = True

            content = """    qwm_doc.QW_PostprocessingS.From = {lowerFreq}
    qwm_doc.QW_PostprocessingS.To = {upperFreq}
    qwm_doc.QW_PostprocessingS.Step = {freqStep}
    qwm_doc.QW_PostprocessingS.ReciprocalNport = {reciprocalNport}
    qwm_doc.QW_PostprocessingS.ReciprocalLossless2port = {reciprocalLossless2port}\n""".format(
                lowerFreq               = lowerFreq,
                upperFreq               = upperFreq,
                freqStep                = freqStep,
                reciprocalNport         = reciprocalNport,
                reciprocalLossless2port = reciprocalLossless2port,
                )
        
            self.globalData.writeToPpostFile(content)

    def do_ntf(self, argumentsList):
        """
        Does NTF command from UDO language.
        """
        if self.createPyFiles:
            strWithFreq = argumentsList[0]
            freqList = [float(elem) for elem in strWithFreq.split()]

            content = """    qwm_doc.QW_PostprocessingNTF.Active = True
    qwm_doc.QW_PostprocessingNTF.Frequencies = {freqList}\n""".format(
                freqList = freqList,
                )

            self.globalData.writeToPpostFile(content)


    def do_ntfbkg(self, argumentsList):
        """
        Does NTFBKG command from UDO language.
        """
        if self.createPyFiles:
            # (<eps>,<mu>,<sig>,<msig>) 

            content = """    qwm_doc.QW_PostprocessingNTF.Eps = {eps}
    qwm_doc.QW_PostprocessingNTF.Mu = {mu}
    qwm_doc.QW_PostprocessingNTF.Sigma = {sigma}
    qwm_doc.QW_PostprocessingNTF.SigmaM = {sigmaM}\n""".format(
                eps     = argumentsList[0],
                mu      = argumentsList[1],
                sigma   = argumentsList[2],
                sigmaM  = argumentsList[3],
                )

            self.globalData.writeToPpostFile(content)


    def do_energyallow(self, argumentsList):
        """
        Does ENERGYALLOW command from UDO language.
        """
        #  (<Allow>) – Switches on or off energy stop criterion that will be used in simulation: <Allow>: 0 – off, 1 – on
        if self.createPyFiles:
            isAllowed = bool(argumentsList[0])

            content = "    qwm_doc.QW_Circuit.UseEnergyLevel = {isAllowed}\n".format(isAllowed = isAllowed)
            
            self.globalData.writeToCircuitFile(content)


    def do_energypar(self, argumentsList):
        """
        Does ENERGYPAR command from UDO language.
        """
        #  (<energyLevelDescentDB>, <energyLevelLogEveryDB>, <energyProbingEvery>, <sParametersAccuracy>, <pulsesNbLimit>) – Sets parameters for energy stop criterion
        if self.createPyFiles:
            energyLevelDescentDB    = argumentsList[0]
            energyLevelLogEveryDB   = argumentsList[1]
            energyProbingEvery      = argumentsList[2]
            sParametersAccuracy     = argumentsList[3]
            pulsesNbLimit           = int(argumentsList[4])

            content = """    qwm_doc.QW_Circuit.EnergyLevelDescentDB = {energyLevelDescentDB}
    qwm_doc.QW_Circuit.EnergyLevelLogEveryDB = {energyLevelLogEveryDB}
    qwm_doc.QW_Circuit.EnergyProbingEvery = {energyProbingEvery}
    qwm_doc.QW_Circuit.SParametrsAccuracy = {sParametersAccuracy}
    qwm_doc.QW_Circuit.PulsesNbLimit = {pulsesNbLimit}\n""".format(
                energyLevelDescentDB    = energyLevelDescentDB,
                energyLevelLogEveryDB   = energyLevelLogEveryDB,
                energyProbingEvery      = energyProbingEvery,
                sParametersAccuracy     = sParametersAccuracy,
                pulsesNbLimit           = pulsesNbLimit,
                )
            
            self.globalData.writeToCircuitFile(content)


    def do_energyopt(self, argumentsList):
        """
        Does ENERGYOPT command from UDO language.
        """
        #  ENERGYOPT (<saveSParametersWhenFinished> ,<freezeWhenFinished>, <suspendWhenFinished>, <continueAfterPulsesNbLimit>)
        if self.createPyFiles:
            saveSParametersWhenFinished     = bool(argumentsList[0])
            freezeWhenFinished              = bool(argumentsList[1])
            suspendWhenFinished             = bool(argumentsList[2])
            continueAfterPulsesNbLimit      = bool(argumentsList[3])

            content = """    qwm_doc.QW_Circuit.SaveSParametrsWhenFinished = {saveSParametersWhenFinished}
    qwm_doc.QW_Circuit.FreezeWhenFinished = {freezeWhenFinished}
    qwm_doc.QW_Circuit.SuspendWhenFinished = {suspendWhenFinished}
    qwm_doc.QW_Circuit.ContinueAfterPulsesNbLimit = {continueAfterPulsesNbLimit}\n""".format(
                saveSParametersWhenFinished     = saveSParametersWhenFinished,
                freezeWhenFinished              = freezeWhenFinished,
                suspendWhenFinished             = suspendWhenFinished,
                continueAfterPulsesNbLimit      = continueAfterPulsesNbLimit,
                )
            
            self.globalData.writeToCircuitFile(content)

    def do_bhmopt(self, argumentsList):
        """
        Does BHMOPT command from UDO language.
        """
        #  BHMOPT (<Allow heat flow>, <Allow rotation>, <Movement>)
        if self.createPyFiles:
            allowHeatFlow               = bool(argumentsList[0])
            allowMovementAndRotation    = bool(argumentsList[1] and argumentsList[2])

            content = """    qwm_doc.QW_BHM.AllowHFM = {allowHeatFlow}
    qwm_doc.QW_BHM.AllowMovementAndRotation = {allowMovementAndRotation}\n""".format(
                allowHeatFlow               = allowHeatFlow,
                allowMovementAndRotation    = allowMovementAndRotation,
                )
            
            self.globalData.writeToCircuitFile(content)


    def do_htimes(self, argumentsList):
        """
        Does HTIMES command from UDO language.
        """
        #  HTIMES (<First EM steady state>, <Consecutive EM steady states>, <Heating pattern construction>, <Total heating time>, <Heating time step>)
        if self.createPyFiles:
            firtsEmSteadyState          = int(argumentsList[0])
            consecutiveEmSteadyStates   = int(argumentsList[1])
            heatingPatternConstruction  = int(argumentsList[2])
            totalHeatingTime            = argumentsList[3]
            totalHeatingTimeStep        = argumentsList[4]

            content = """    qwm_doc.QW_BHM.FirstEmSteadyState = {firtsEmSteadyState}
    qwm_doc.QW_BHM.NextEmSteadyState = {consecutiveEmSteadyStates}
    qwm_doc.QW_BHM.HeatingPatternConstruction = {heatingPatternConstruction}
    qwm_doc.QW_BHM.TotalHeatingTime = {totalHeatingTime}
    qwm_doc.QW_BHM.HeatingTimeStep = {totalHeatingTimeStep}\n""".format(
                firtsEmSteadyState          = firtsEmSteadyState,
                consecutiveEmSteadyStates   = consecutiveEmSteadyStates,
                heatingPatternConstruction  = heatingPatternConstruction,
                totalHeatingTime            = totalHeatingTime,
                totalHeatingTimeStep        = totalHeatingTimeStep,
                )
            
            self.globalData.writeToCircuitFile(content)


    def do_bhmafter(self, argumentsList):
        """
        Does BHMAFTER command from UDO language.
        """
        #  BHMAFTER (<what>, <after each>, <after step>) – Sets Suspend or Freeze for BHM steps:
        if self.createPyFiles:
            if argumentsList[0] == 0: # Suspend
                suspendAfterEach = bool(argumentsList[1])
                afterStep = argumentsList[2]

                suspendAfterStep = False
                suspendStep = 1
                if afterStep > 0:
                    suspendAfterStep = True
                    suspendStep = afterStep

                content = """    qwm_doc.QW_BHM.SuspendAfterEach = {suspendAfterEach}
    qwm_doc.QW_BHM.SuspendAfterStep = {suspendAfterStep}
    qwm_doc.QW_BHM.SuspendStep = {suspendStep}
    qwm_doc.QW_BHM.FreezeAfterEach = False
    qwm_doc.QW_BHM.FreezeAfterStep = False
    qwm_doc.QW_BHM.FreezeStep = 1\n""".format(
                    suspendAfterEach    = suspendAfterEach,
                    suspendAfterStep    = suspendAfterStep,
                    suspendStep         = suspendStep,
                    )

            elif argumentsList[0] == 1: # Freeze
                freezeAfterEach = bool(argumentsList[1])
                afterStep = argumentsList[2]

                freezeAfterStep = False
                freezeStep = 1
                if afterStep > 0:
                    freezeAfterStep = True
                    freezeStep = afterStep

                content = """    qwm_doc.QW_BHM.SuspendAfterEach = False
    qwm_doc.QW_BHM.SuspendAfterStep = False
    qwm_doc.QW_BHM.SuspendStep = 1
    qwm_doc.QW_BHM.FreezeAfterEach = {freezeAfterEach}
    qwm_doc.QW_BHM.FreezeAfterStep = {freezeAfterStep}
    qwm_doc.QW_BHM.FreezeStep = {freezeStep}\n""".format(
                    freezeAfterEach    = freezeAfterEach,
                    freezeAfterStep    = freezeAfterStep,
                    freezeStep         = freezeStep,
                    )
            
            self.globalData.writeToCircuitFile(content)


    def do_bhmcompformat(self, argumentsList):
        """
        Does BHMCOMPFORMAT command from UDO language.
        """
        #  BHMCOMPFORMAT (<Data Format>, <Include Shape Data>, <Include FDTD Mesh>) 
        if self.createPyFiles:
            dataFormat          = int(argumentsList[0])
            includeShapeData    = bool(argumentsList[1])
            includeFdtdMesh     = bool(argumentsList[2])

            content = """    qwm_doc.QW_BHM.ComponentsListFormat = {dataFormat}
    qwm_doc.QW_BHM.IncludeShapeData = {includeShapeData}
    qwm_doc.QW_BHM.IncludeFDTDMesh = {includeFdtdMesh}\n""".format(
                dataFormat          = dataFormat,
                includeShapeData    = includeShapeData,
                includeFdtdMesh     = includeFdtdMesh,
                )
            
            self.globalData.writeToCircuitFile(content)


    def do_tempa(self, argumentsList):
        """
        Does TEMPA command from UDO language.
        """
        # TEMPA (<mode>,<m>,<n>,<match_freq>,<dummy>)
        # <mode> - template mode (0 - rectangular TE, 1 - rectangular TM, 2 - circular TE, 3 - circular TM)
        # <m>, <n> - indices of the mode
        # <match_freq> - matching frequency for template generation

        #if self.createPyFiles:

        #    content = """    """

        #    self.globalData.writeToExcitFile(content)
        pass


    def do_symmetry(self, argumentsList):
        """
        Does SYMMETRY command from UDO language.
        """
        self.portCommandDict["symmetryH"] = bool(argumentsList[0])
        self.portCommandDict["symmetryV"] = bool(argumentsList[1])


    def do_smndiff(self, argumentsList):
        """
        Does SMNDIFF command from UDO language.
        """
        # SMNDIFF (<lower_freq>,<upper_freq>,<freq_step>,<assumptions>,<mode>,<IterForS>)
        if self.createPyFiles:
            lowerFreq           = argumentsList[0]
            upperFreq           = argumentsList[1]
            freqStep            = argumentsList[2]
            assumptionsIndex    = argumentsList[3]
            mode                = argumentsList[4]
            iterForS            = int(argumentsList[5])

            reciprocalNport = False
            reciprocalLossless2port = False

            if assumptionsIndex == 1:
                reciprocalNport = True
            elif assumptionsIndex == 2:
                reciprocalLossless2port = True

            smnType = "Sequential"
            if mode == 1:
                smnType = "Multi simulator"

            content = """    qwm_doc.QW_PostprocessingS.From = {lowerFreq}
    qwm_doc.QW_PostprocessingS.To = {upperFreq}
    qwm_doc.QW_PostprocessingS.Step = {freqStep}
    qwm_doc.QW_PostprocessingS.ReciprocalNport = {reciprocalNport}
    qwm_doc.QW_PostprocessingS.ReciprocalLossless2port = {reciprocalLossless2port}
    qwm_doc.QW_PostprocessingS.SmnIterationsPerPort = {iterForS}
    qwm_doc.QW_PostprocessingS.SmnType = "{smnType}"\n""".format(
                lowerFreq               = lowerFreq,
                upperFreq               = upperFreq,
                freqStep                = freqStep,
                reciprocalNport         = reciprocalNport,
                reciprocalLossless2port = reciprocalLossless2port,
                iterForS                = iterForS,
                smnType                 = smnType,
                )
        
            self.globalData.writeToPpostFile(content)