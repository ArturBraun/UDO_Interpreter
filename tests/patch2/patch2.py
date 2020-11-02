
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

from patch2_proj import *

GUIMode = FreeCAD.ConfigGet("RunMode")

if not GUIMode:
    FreeCADGui.showMainWindow()

FreeCADGui.activateWorkbench("QW_ModellerWorkbench")

qwm_doc = QW_Modeller.newQWDocument("patch2")

FreeCADGui.activeDocument().activeView().viewAxometric()

proj = patch2_Project(qwm_doc)
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

        