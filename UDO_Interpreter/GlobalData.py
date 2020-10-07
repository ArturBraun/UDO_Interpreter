"""@package GrammarRulesVisitor
This module include class used to store data that is required to be global.
 
This module include class (which uses singleton design pattern) to store data for example variables from UDO files
and the generated QW-Modeller python scripts.  
"""

#--------------------------------------------
""" INCLUDED MODULES: """
#--------------------------------------------
import re
import os

#--------------------------------------------
""" CLASSES: """
#--------------------------------------------
class GlobalData:
    """
    Class that uses Singleton design pattern. It stores all data that is required to be global, including for example variables from UDO files
    and the generated QW-Modeller python scripts.
    """
    _singleton = None

    def __new__(cls, *args, **kwargs):
        """
        Class to store data which is required to be global.
        If there wasn't an instance of this class before it creates the new one, otherwise it returns reference to the one created before.
        With this behaviour there is only one instance of this class in whole project.
        """
        if not cls._singleton:
            cls._singleton = super(GlobalData, cls).__new__(cls)
            # Content of class:
            cls._singleton.variables = {
                                "x":["", 0.0],
                                "y":["", 0.0],
                                "z":["", 0.0],
                                "air":["", "air"]
                                } 
            if re.fullmatch("[a-zA-Z]{1}[a-zA-Z0-9_]*", kwargs["projectName"]): cls._singleton.projectName = kwargs["projectName"]
            else: cls._singleton.projectName = "project"

            cls.objectsNames = []
            cls.UDO_filePath = kwargs["filePath"]
            cls.pathToGeneratePyFiles = kwargs["pathToGeneratePyFiles"]

            cls.printMessages = True
            if "printMessages" in kwargs:
                cls.printMessages = kwargs["printMessages"]

            createPyFiles = True
            if "createPyFiles" in kwargs:
                createPyFiles = kwargs["createPyFiles"]

            if createPyFiles:
                cls._singleton.mainFile = open(cls.pathToGeneratePyFiles + cls._singleton.projectName + ".py", "w")
                cls._singleton.circuitFile = open(cls.pathToGeneratePyFiles + cls._singleton.projectName + "_circuit.py", "w")
                cls._singleton.excitFile = open(cls.pathToGeneratePyFiles + cls._singleton.projectName + "_excit.py", "w")
                cls._singleton.geomMediaFile = open(cls.pathToGeneratePyFiles + cls._singleton.projectName + "_geom_media.py", "w")
                cls._singleton.meshFile = open(cls.pathToGeneratePyFiles + cls._singleton.projectName + "_mesh.py", "w")
                cls._singleton.ppostFile = open(cls.pathToGeneratePyFiles + cls._singleton.projectName + "_ppost.py", "w")
                cls._singleton.projFile = open(cls.pathToGeneratePyFiles + cls._singleton.projectName + "_proj.py", "w")
                cls._singleton.runsimulFile = open(cls.pathToGeneratePyFiles + cls._singleton.projectName + "_runsimul.py", "w")
                cls._singleton.setsimulFile = open(cls.pathToGeneratePyFiles + cls._singleton.projectName + "_setsimul.py", "w")

        return cls._singleton

    def closeAllModellerScripts(self):
        """
        Function that closes all Modeller python scripts files.
        """
        self._singleton.mainFile.close()
        self._singleton.circuitFile.close()
        self._singleton.excitFile.close()
        self._singleton.geomMediaFile.close()
        self._singleton.meshFile.close()
        self._singleton.ppostFile.close()
        self._singleton.projFile.close()
        self._singleton.runsimulFile.close()
        self._singleton.setsimulFile.close()

    def writeToMainFile(self,content):
        """
        Function that writes content to the main file.
        """
        self._singleton.mainFile.write(content)

    def writeToCircuitFile(self,content):
        """
        Function that writes content to the circuit file.
        """
        self._singleton.circuitFile.write(content)

    def writeToExcitFile(self,content):
        """
        Function that writes content to the excit file.
        """
        self._singleton.excitFile.write(content)

    def writeToGeomMediaFile(self,content):
        """
        Function that writes content to geom media file.
        """
        self._singleton.geomMediaFile.write(content)

    def writeToMeshFile(self,content):
        """
        Function that writes content to mesh file.
        """
        self._singleton.meshFile.write(content)

    def writeToPpostFile(self,content):
        """
        Function that writes content to ppost file.
        """
        self._singleton.ppostFile.write(content)

    def writeToProjFile(self,content):
        """
        Function that writes content to the proj file.
        """
        self._singleton.projFile.write(content)

    def writeToRunsimulFile(self,content):
        """
        Function that writes content to runsimul file.
        """
        self._singleton.runsimulFile.write(content)

    def writeToSetsimulFile(self,content):
        """
        Function that writes content to setsimul file.
        """
        self._singleton.setsimulFile.write(content)

