"""@package GrammarRulesVisitor
This module include class used to store data that is required to be global.
 
This module include class (which uses singleton design pattern) to store data for example variables from UDO files
and the generated QW-Modeller python scripts.  
"""

#--------------------------------------------
""" INCLUDED MODULES: """
#--------------------------------------------


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
                                "x":["", 0],
                                "y":["", 0],
                                "z":["", 0],
                                "air":["", "air"]
                                } 
            cls._singleton.projectName = kwargs["projectName"]
            cls._singleton.projectFile = open(cls._singleton.projectName + ".py", "w")

        return cls._singleton

    def writeToProjectFile(self,content):
        """
        Function that writes content to the project file.
        """
        self._singleton.projectFile.write(content)

    def closeAllModellerScripts(self):
        """
        Function that closes all Modeller python scripts files.
        """
        self._singleton.projectFile.close()