
from FreeCAD import Base
import QW_Modeller
from qw_project import *
from qw_units import *


def set_Excitation(qwm_doc):
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","guideinp")
    qwm_doc.guideinp.Length = 10.0
    qwm_doc.guideinp.Width = 5.0
    qwm_doc.guideinp.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 5.0, 2.5), FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.guideinp.Orientation = "X"
    qwm_doc.guideinp.Position = 0.0
    qwm_doc.guideinp.Activity = "PLUS"
    qwm_doc.guideinp.Type = "Source"
    qwm_doc.guideinp.SymmetryH = False
    qwm_doc.guideinp.SymmetryV = False
    qwm_doc.guideinp.PointCoordX = 0.0
    qwm_doc.guideinp.PointCoordY = 5.0
    qwm_doc.guideinp.PointCoordZ = 2.5
    qwm_doc.guideinp.effectivePermitivityMode = "AUTO"
    qwm_doc.guideinp.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('delta'),1,0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),1,50,1,0))
    qwm_doc.guideinp.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.guideinp.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.guideinp.ReferenceOffset = abs(qwm_doc.guideinp.PointCoordX - 5.2)
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","coaxout")
    qwm_doc.coaxout.Length = 5.0
    qwm_doc.coaxout.Width = 5.0
    qwm_doc.coaxout.Placement = FreeCAD.Placement(FreeCAD.Vector(19.6, 5.0, 14.0), FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.coaxout.Orientation = "Z"
    qwm_doc.coaxout.Position = 14.0
    qwm_doc.coaxout.Activity = "MINUS"
    qwm_doc.coaxout.Type = "Load"
    qwm_doc.coaxout.SymmetryH = False
    qwm_doc.coaxout.SymmetryV = False
    qwm_doc.coaxout.PointCoordX = 19.6
    qwm_doc.coaxout.PointCoordY = 5.0
    qwm_doc.coaxout.PointCoordZ = 14.0
    qwm_doc.coaxout.effectivePermitivityMode = "AUTO"
    qwm_doc.coaxout.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('delta'),1,0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),1,50,1,0))
    qwm_doc.coaxout.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.coaxout.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.coaxout.ReferenceOffset = abs(qwm_doc.coaxout.PointCoordZ - 9.0)
