
from FreeCAD import Base
import QW_Modeller
from qw_project import *
from qw_units import *


def set_Excitation(qwm_doc):
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","spx1")
    qwm_doc.spx1.Placement = FreeCAD.Placement(FreeCAD.Vector(-10.0, 0.05, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.spx1.Orientation = "X"
    qwm_doc.spx1.Position = -10.0
    qwm_doc.spx1.Length = 0.1
    qwm_doc.spx1.Width = 0.0
    FreeCAD.Gui.ActiveDocument.spx1.ShowText = False
    FreeCAD.Gui.ActiveDocument.spx1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.spx1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","spx2")
    qwm_doc.spx2.Placement = FreeCAD.Placement(FreeCAD.Vector(10.0, 0.05, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.spx2.Orientation = "X"
    qwm_doc.spx2.Position = 10.0
    qwm_doc.spx2.Length = 0.1
    qwm_doc.spx2.Width = 0.0
    FreeCAD.Gui.ActiveDocument.spx2.ShowText = False
    FreeCAD.Gui.ActiveDocument.spx2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.spx2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","spy1")
    qwm_doc.spy1.Placement = FreeCAD.Placement(FreeCAD.Vector(0.05, -7.5, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.spy1.Orientation = "Y"
    qwm_doc.spy1.Position = -7.5
    qwm_doc.spy1.Length = 0.0
    qwm_doc.spy1.Width = 0.1
    FreeCAD.Gui.ActiveDocument.spy1.ShowText = False
    FreeCAD.Gui.ActiveDocument.spy1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.spy1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","spy2")
    qwm_doc.spy2.Placement = FreeCAD.Placement(FreeCAD.Vector(0.05, 7.5, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.spy2.Orientation = "Y"
    qwm_doc.spy2.Position = 7.5
    qwm_doc.spy2.Length = 0.0
    qwm_doc.spy2.Width = 0.1
    FreeCAD.Gui.ActiveDocument.spy2.ShowText = False
    FreeCAD.Gui.ActiveDocument.spy2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.spy2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","inp")
    qwm_doc.inp.Length = 10.0
    qwm_doc.inp.Width = 5.0
    qwm_doc.inp.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -20.0), FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.inp.Orientation = "Z"
    qwm_doc.inp.Position = -20.0
    qwm_doc.inp.Activity = "PLUS"
    qwm_doc.inp.Type = "Source"
    qwm_doc.inp.SymmetryH = False
    qwm_doc.inp.SymmetryV = False
    qwm_doc.inp.PointCoordX = 0.0
    qwm_doc.inp.PointCoordY = 0.0
    qwm_doc.inp.PointCoordZ = -20.0
    qwm_doc.inp.effectivePermitivityMode = "AUTO"
    qwm_doc.inp.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('delta'),1,0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),1,50,1,0))
    qwm_doc.inp.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.inp.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.inp.ReferenceOffset = abs(qwm_doc.inp.PointCoordZ - -15.0)
