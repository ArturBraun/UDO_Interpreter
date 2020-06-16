# (C) QWED Sp. z o.o. 2015.11.10
# QW-Modeller python qw_project file
# This file is not intended to be change

# QuickWave QW-Modeller Python Project Base Class
# Concrete QuickWave Project will inherit from this class
# Default parameters values for QuickWave project items are exposed
# Actual values for some of these parameters should be set in derived class function calls

import os
import FreeCAD, QW_Modeller

def setProjectDefaultFolder(qwm_doc,publicdir):
    publicexamplesUserdir = publicdir+"examples/QW-User/"
    thisExampleSubdir = publicexamplesUserdir+qwm_doc.Name+"/"
    if not os.path.isdir(thisExampleSubdir):
        os.makedirs(thisExampleSubdir)
    return thisExampleSubdir

class QW_Project(object):
    def __init__(self, qwm_doc, param):
        self.qwm_doc = qwm_doc
        self.param = param

    def set_Circuit_Parameters(self):
        # defaults set by Circuit settings QW-Modeller dialog
        # User should adjust required values in the project_name_circuit.py set_Circuit_Parameters(qwm_doc) function
        self.qwm_doc.QW_MediaLibrary.BackgroundMedium = "air"
        self.qwm_doc.QW_MediaLibrary.ActiveMedium = "air"
        self.qwm_doc.QW_Circuit.FreqencyFrom = 5.00000
        self.qwm_doc.QW_Circuit.FreqencyTo = 15.00000
        self.qwm_doc.QW_Circuit.FreqencyStep = 0.1000
        self.qwm_doc.QW_Circuit.Units = "mm"
        self.qwm_doc.QW_Circuit.Description = "No description"
        self.qwm_doc.QW_Circuit.CircuitType = "3D"
        self.qwm_doc.QW_Circuit.PeriodicityX = False
        self.qwm_doc.QW_Circuit.PeriodicityY = False
        self.qwm_doc.QW_Circuit.PeriodicityZ = True
        self.qwm_doc.QW_Circuit.PhaseShiftType = "Phase shift/period"
        self.qwm_doc.QW_Circuit.PhaseShiftX = 0.00000
        self.qwm_doc.QW_Circuit.PhaseShiftY = 0.00000
        self.qwm_doc.QW_Circuit.PhaseShiftZ = 0.00000
        self.qwm_doc.QW_Circuit.Phi = 0.00000
        self.qwm_doc.QW_Circuit.Theta = 0.00000
        self.qwm_doc.QW_Circuit.PhaseConstant = 0.00000
        self.qwm_doc.QW_Circuit.AngularVariation = 1
        self.qwm_doc.QW_Circuit.MetalLossesBandwidth = "Decade"
        self.qwm_doc.QW_Circuit.SuppressLossesDielectric = False
        self.qwm_doc.QW_Circuit.SuppressLossesMetal = False
        self.qwm_doc.QW_Circuit.SuppressLossesMagnetic = False
        self.qwm_doc.QW_Circuit.SuppressSingularityCorrections = False
        self.qwm_doc.QW_Circuit.SuppressDensity_SAR = False

    def set_GeometryAndMedia(self):
        # User should define project geometry in project_name_geom_media.py
        # set_GeometryAndMedia(qwm_doc, project_name_par) function
        pass

    def set_Mesh(self):
        # defaults set by Mesh settings QW-Modeller dialog
        # User should adjust required values in the project_name_mesh.py set_Mesh(qwm_doc) function
        self.qwm_doc.QW_Mesh.CellX = 10.00000
        self.qwm_doc.QW_Mesh.CellY = 10.00000
        self.qwm_doc.QW_Mesh.CellZ = 10.00000
        self.qwm_doc.QW_Mesh.AutoSnapToGeometryX = True
        self.qwm_doc.QW_Mesh.AutoSnapToGeometryY = True
        self.qwm_doc.QW_Mesh.AutoSnapToGeometryZ = True
        self.qwm_doc.QW_Mesh.AutoSnapToMetalX = True
        self.qwm_doc.QW_Mesh.AutoSnapToMetalY = True
        self.qwm_doc.QW_Mesh.AutoSnapToMetalZ = True
        self.qwm_doc.QW_Mesh.MinCellX = 0.10000
        self.qwm_doc.QW_Mesh.MinCellY = 0.10000
        self.qwm_doc.QW_Mesh.MinCellZ = 0.10000
        self.qwm_doc.QW_Mesh.AmigoCellsPerWavelength = 15.00000
        self.qwm_doc.QW_Mesh.AmigoX = False
        self.qwm_doc.QW_Mesh.AmigoY = False
        self.qwm_doc.QW_Mesh.AmigoZ = False

    def set_Excitation(self):
        # User should define project excitation parameters in project_name_excit.py
        # set_Excitation(qwm_doc, param) function
        pass

    def set_Postprocessing(self):
        # User should define project postprocessing in project_name_ppost.py
        # set_Postprocessing(qwm_doc) function
        pass

    def set_Simulation(self):
        # User should define project simulation settings in project_name_setsimul.py
        # set_Simulation(qwm_doc) function
        publicdir = FreeCAD.ConfigGet("QWPUBLICDIR")
        thisExampleSubdir = setProjectDefaultFolder(self.qwm_doc, publicdir)
        self.qwm_doc.saveAs(thisExampleSubdir+self.qwm_doc.Name+".QWpro")
        QW_Modeller.generateMesh(self.qwm_doc.Name)

    def run_Simulation(self):
        # User should define project run simulation settings in project_name_runsimul.py
        # run_Simulation(qwm_doc) function
        pass

class QW_model_Geometry_Parameters(object):
    def __init__(self, oname):
        self.oname = oname


