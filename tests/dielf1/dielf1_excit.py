
from FreeCAD import Base
import QW_Modeller
from qw_project import *
from qw_units import *


def set_Excitation(qwm_doc):
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","inp")
    qwm_doc.inp.Length = 20.0
    qwm_doc.inp.Width = 10.0
    qwm_doc.inp.Placement = Base.Placement(Base.Vector(0.0, 0.0, 5.0), Base.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.inp.Orientation = "X"
    qwm_doc.inp.Position = 0.0
    qwm_doc.inp.Activity = "PLUS"
    qwm_doc.inp.Type = "Source"
    qwm_doc.inp.SymmetryH = False
    qwm_doc.inp.SymmetryV = False
    qwm_doc.inp.PointCoordX = 0.0
    qwm_doc.inp.PointCoordY = 0.0
    qwm_doc.inp.PointCoordZ = 5.0
    qwm_doc.inp.effectivePermitivityMode = "AUTO"
    qwm_doc.inp.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('delta'),1,0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),1,50,1,0))
    qwm_doc.inp.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.inp.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.inp.ReferenceOffset = abs(qwm_doc.inp.PointCoordX - 10.0)
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","out")
    qwm_doc.out.Length = 20.0
    qwm_doc.out.Width = 10.0
    qwm_doc.out.Placement = Base.Placement(Base.Vector(60.0, 0.0, 5.0), Base.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.out.Orientation = "X"
    qwm_doc.out.Position = 60.0
    qwm_doc.out.Activity = "MINUS"
    qwm_doc.out.Type = "Load"
    qwm_doc.out.SymmetryH = False
    qwm_doc.out.SymmetryV = False
    qwm_doc.out.PointCoordX = 60.0
    qwm_doc.out.PointCoordY = 0.0
    qwm_doc.out.PointCoordZ = 5.0
    qwm_doc.out.effectivePermitivityMode = "AUTO"
    qwm_doc.out.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('delta'),1,0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),1,50,1,0))
    qwm_doc.out.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.out.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.out.ReferenceOffset = abs(qwm_doc.out.PointCoordX - 50.0)
