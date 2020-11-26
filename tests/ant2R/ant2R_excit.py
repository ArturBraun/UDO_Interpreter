
from FreeCAD import Base
import QW_Modeller
from qw_project import *
from qw_units import *


def set_Excitation(qwm_doc):
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","port")
    qwm_doc.port.Length = 20.0
    qwm_doc.port.Width = 1.0
    qwm_doc.port.Placement = FreeCAD.Placement(FreeCAD.Vector(-20.0, 18.0, 0.5), FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.port.Orientation = "X"
    qwm_doc.port.Position = -20.0
    qwm_doc.port.Activity = "PLUS"
    qwm_doc.port.Type = "Source"
    qwm_doc.port.SymmetryH = False
    qwm_doc.port.SymmetryV = False
    qwm_doc.port.PointCoordX = -20.0
    qwm_doc.port.PointCoordY = 18.0
    qwm_doc.port.PointCoordZ = 0.5
    qwm_doc.port.effectivePermitivityMode = "AUTO"
    qwm_doc.port.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('delta'),1,0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),1,50,1,0))
    qwm_doc.port.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.port.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.port.ReferenceOffset = abs(qwm_doc.port.PointCoordX - -2.0)
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","abs_left")
    qwm_doc.abs_left.Orientation = "X"
    qwm_doc.abs_left.Length = 697.8187226079011
    qwm_doc.abs_left.Width = 1.0
    qwm_doc.abs_left.Placement = FreeCAD.Placement(FreeCAD.Vector(-80.0, 348.90936130395056, 0.5),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.abs_left.Position = -80.0
    qwm_doc.abs_left.Activity = "PLUS"
    FreeCAD.Gui.ActiveDocument.abs_left.AbsorberDepth = 1.00000
    FreeCAD.Gui.ActiveDocument.abs_left.ShowText = True
    FreeCAD.Gui.ActiveDocument.abs_left.TextSize = 14
    FreeCAD.Gui.ActiveDocument.abs_left.TextPlace = 3
    qwm_doc.abs_left.Type = "MUR"
    qwm_doc.abs_left.EffectivePermittivity = 1
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","abs_right")
    qwm_doc.abs_right.Orientation = "X"
    qwm_doc.abs_right.Length = 697.8187226079011
    qwm_doc.abs_right.Width = 1.0
    qwm_doc.abs_right.Placement = FreeCAD.Placement(FreeCAD.Vector(552.0, 348.90936130395056, 0.5),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.abs_right.Position = 552.0
    qwm_doc.abs_right.Activity = "MINUS"
    FreeCAD.Gui.ActiveDocument.abs_right.AbsorberDepth = 1.00000
    FreeCAD.Gui.ActiveDocument.abs_right.ShowText = True
    FreeCAD.Gui.ActiveDocument.abs_right.TextSize = 14
    FreeCAD.Gui.ActiveDocument.abs_right.TextPlace = 3
    qwm_doc.abs_right.Type = "MUR"
    qwm_doc.abs_right.EffectivePermittivity = 1
    qwm_doc.QW_Mesh_Borders.BorderXMin = "PMC"
    qwm_doc.QW_Mesh_Borders.BorderXMax = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderYMin = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderYMax = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderZMin = "PEC"
    qwm_doc.QW_Mesh_Borders.BorderZMax = "PEC"
    qwm_doc.QW_Mesh.AutoAdjustMeshBoundaryCheck = False
    qwm_doc.QW_Mesh.bboxminX = -80.0
    qwm_doc.QW_Mesh.bboxmaxX = 552.0
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","abs_up")
    qwm_doc.abs_up.Orientation = "Y"
    qwm_doc.abs_up.Length = 1.0
    qwm_doc.abs_up.Width = 632.0
    qwm_doc.abs_up.Placement = FreeCAD.Placement(FreeCAD.Vector(236.0, 697.8187226079011, 0.5),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.abs_up.Position = 697.8187226079011
    qwm_doc.abs_up.Activity = "MINUS"
    FreeCAD.Gui.ActiveDocument.abs_up.AbsorberDepth = 1.00000
    FreeCAD.Gui.ActiveDocument.abs_up.ShowText = True
    FreeCAD.Gui.ActiveDocument.abs_up.TextSize = 14
    FreeCAD.Gui.ActiveDocument.abs_up.TextPlace = 3
    qwm_doc.abs_up.Type = "MUR"
    qwm_doc.abs_up.EffectivePermittivity = 1
    QW_Modeller.addQWObject("QW_Modeller::NTFBox","ntfbox")
    qwm_doc.ntfbox.Length = 512.0
    qwm_doc.ntfbox.Width = 617.8187226079011
    qwm_doc.ntfbox.Height = 0.5
    qwm_doc.ntfbox.Placement = FreeCAD.Placement(FreeCAD.Vector(236.0, 308.90936130395056, 0.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    FreeCAD.Gui.ActiveDocument.ntfbox.ShowText = True
    FreeCAD.Gui.ActiveDocument.ntfbox.TextSize = 14
