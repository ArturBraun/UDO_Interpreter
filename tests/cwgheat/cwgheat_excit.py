
from FreeCAD import Base
import QW_Modeller
from qw_project import *
from qw_units import *


def set_Excitation(qwm_doc):
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","cwghinp1")
    qwm_doc.cwghinp1.Length = 100.0
    qwm_doc.cwghinp1.Width = 100.0
    qwm_doc.cwghinp1.Placement = Base.Placement(Base.Vector(0.0, 0.0, 0.0), Base.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.cwghinp1.Orientation = "Z"
    qwm_doc.cwghinp1.Position = 0.0
    qwm_doc.cwghinp1.Activity = "PLUS"
    qwm_doc.cwghinp1.Type = "Source"
    qwm_doc.cwghinp1.SymmetryH = False
    qwm_doc.cwghinp1.SymmetryV = False
    qwm_doc.cwghinp1.PointCoordX = 0.0
    qwm_doc.cwghinp1.PointCoordY = 0.0
    qwm_doc.cwghinp1.PointCoordZ = 0.0
    qwm_doc.cwghinp1.effectivePermitivityMode = "AUTO"
    qwm_doc.cwghinp1.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('delta'),1,0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),1,50,1,0))
    qwm_doc.cwghinp1.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.cwghinp1.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.cwghinp1.ReferenceOffset = abs(qwm_doc.cwghinp1.PointCoordZ - 30.0)
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","cwghout1")
    qwm_doc.cwghout1.Length = 100.0
    qwm_doc.cwghout1.Width = 100.0
    qwm_doc.cwghout1.Placement = Base.Placement(Base.Vector(0.0, 0.0, 300.0), Base.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.cwghout1.Orientation = "Z"
    qwm_doc.cwghout1.Position = 300.0
    qwm_doc.cwghout1.Activity = "MINUS"
    qwm_doc.cwghout1.Type = "Load"
    qwm_doc.cwghout1.SymmetryH = False
    qwm_doc.cwghout1.SymmetryV = False
    qwm_doc.cwghout1.PointCoordX = 0.0
    qwm_doc.cwghout1.PointCoordY = 0.0
    qwm_doc.cwghout1.PointCoordZ = 300.0
    qwm_doc.cwghout1.effectivePermitivityMode = "AUTO"
    qwm_doc.cwghout1.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('delta'),1,0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),1,50,1,0))
    qwm_doc.cwghout1.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.cwghout1.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.cwghout1.ReferenceOffset = abs(qwm_doc.cwghout1.PointCoordZ - 270.0)
