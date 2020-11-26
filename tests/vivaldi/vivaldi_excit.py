
from FreeCAD import Base
import QW_Modeller
from qw_project import *
from qw_units import *


def set_Excitation(qwm_doc):
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","pml_bot")
    qwm_doc.pml_bot.Orientation = "Z"
    qwm_doc.pml_bot.Length = 80.0
    qwm_doc.pml_bot.Width = 120.0
    qwm_doc.pml_bot.Placement = FreeCAD.Placement(FreeCAD.Vector(20.0, 45.0, -20.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.pml_bot.Position = -20.0
    qwm_doc.pml_bot.Activity = "PLUS"
    FreeCAD.Gui.ActiveDocument.pml_bot.AbsorberDepth = 2.00000
    FreeCAD.Gui.ActiveDocument.pml_bot.ShowText = True
    FreeCAD.Gui.ActiveDocument.pml_bot.TextSize = 14
    FreeCAD.Gui.ActiveDocument.pml_bot.TextPlace = 3
    qwm_doc.pml_bot.Type = "PML"
    qwm_doc.pml_bot.PMLProfile = "Parabolic"
    qwm_doc.pml_bot.Thickness = 8
    qwm_doc.pml_bot.ParabolicA = 1.00000
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","pml_top")
    qwm_doc.pml_top.Orientation = "Z"
    qwm_doc.pml_top.Length = 80.0
    qwm_doc.pml_top.Width = 120.0
    qwm_doc.pml_top.Placement = FreeCAD.Placement(FreeCAD.Vector(20.0, 45.0, 20.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.pml_top.Position = 20.0
    qwm_doc.pml_top.Activity = "MINUS"
    FreeCAD.Gui.ActiveDocument.pml_top.AbsorberDepth = 2.00000
    FreeCAD.Gui.ActiveDocument.pml_top.ShowText = True
    FreeCAD.Gui.ActiveDocument.pml_top.TextSize = 14
    FreeCAD.Gui.ActiveDocument.pml_top.TextPlace = 3
    qwm_doc.pml_top.Type = "PML"
    qwm_doc.pml_top.PMLProfile = "Parabolic"
    qwm_doc.pml_top.Thickness = 8
    qwm_doc.pml_top.ParabolicA = 1.00000
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","pml_left")
    qwm_doc.pml_left.Orientation = "X"
    qwm_doc.pml_left.Length = 120.0
    qwm_doc.pml_left.Width = 40.0
    qwm_doc.pml_left.Placement = FreeCAD.Placement(FreeCAD.Vector(-20.0, 45.0, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.pml_left.Position = -20.0
    qwm_doc.pml_left.Activity = "PLUS"
    FreeCAD.Gui.ActiveDocument.pml_left.AbsorberDepth = 2.00000
    FreeCAD.Gui.ActiveDocument.pml_left.ShowText = True
    FreeCAD.Gui.ActiveDocument.pml_left.TextSize = 14
    FreeCAD.Gui.ActiveDocument.pml_left.TextPlace = 3
    qwm_doc.pml_left.Type = "PML"
    qwm_doc.pml_left.PMLProfile = "Parabolic"
    qwm_doc.pml_left.Thickness = 8
    qwm_doc.pml_left.ParabolicA = 1.00000
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","pml_right")
    qwm_doc.pml_right.Orientation = "X"
    qwm_doc.pml_right.Length = 120.0
    qwm_doc.pml_right.Width = 40.0
    qwm_doc.pml_right.Placement = FreeCAD.Placement(FreeCAD.Vector(60.0, 45.0, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.pml_right.Position = 60.0
    qwm_doc.pml_right.Activity = "MINUS"
    FreeCAD.Gui.ActiveDocument.pml_right.AbsorberDepth = 2.00000
    FreeCAD.Gui.ActiveDocument.pml_right.ShowText = True
    FreeCAD.Gui.ActiveDocument.pml_right.TextSize = 14
    FreeCAD.Gui.ActiveDocument.pml_right.TextPlace = 3
    qwm_doc.pml_right.Type = "PML"
    qwm_doc.pml_right.PMLProfile = "Parabolic"
    qwm_doc.pml_right.Thickness = 8
    qwm_doc.pml_right.ParabolicA = 1.00000
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","pml_down")
    qwm_doc.pml_down.Orientation = "Y"
    qwm_doc.pml_down.Length = 40.0
    qwm_doc.pml_down.Width = 80.0
    qwm_doc.pml_down.Placement = FreeCAD.Placement(FreeCAD.Vector(20.0, -15.0, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.pml_down.Position = -15.0
    qwm_doc.pml_down.Activity = "PLUS"
    FreeCAD.Gui.ActiveDocument.pml_down.AbsorberDepth = 2.00000
    FreeCAD.Gui.ActiveDocument.pml_down.ShowText = True
    FreeCAD.Gui.ActiveDocument.pml_down.TextSize = 14
    FreeCAD.Gui.ActiveDocument.pml_down.TextPlace = 3
    qwm_doc.pml_down.Type = "PML"
    qwm_doc.pml_down.PMLProfile = "Parabolic"
    qwm_doc.pml_down.Thickness = 8
    qwm_doc.pml_down.ParabolicA = 1.00000
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","pml_up")
    qwm_doc.pml_up.Orientation = "Y"
    qwm_doc.pml_up.Length = 40.0
    qwm_doc.pml_up.Width = 80.0
    qwm_doc.pml_up.Placement = FreeCAD.Placement(FreeCAD.Vector(20.0, 105.0, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.pml_up.Position = 105.0
    qwm_doc.pml_up.Activity = "MINUS"
    FreeCAD.Gui.ActiveDocument.pml_up.AbsorberDepth = 2.00000
    FreeCAD.Gui.ActiveDocument.pml_up.ShowText = True
    FreeCAD.Gui.ActiveDocument.pml_up.TextSize = 14
    FreeCAD.Gui.ActiveDocument.pml_up.TextPlace = 3
    qwm_doc.pml_up.Type = "PML"
    qwm_doc.pml_up.PMLProfile = "Parabolic"
    qwm_doc.pml_up.Thickness = 8
    qwm_doc.pml_up.ParabolicA = 1.00000
    QW_Modeller.addQWObject("QW_Modeller::NTFBox","ntfbox")
    qwm_doc.ntfbox.Length = 50.0
    qwm_doc.ntfbox.Width = 100.0
    qwm_doc.ntfbox.Height = 13.1496
    qwm_doc.ntfbox.Placement = FreeCAD.Placement(FreeCAD.Vector(20.0, 45.0, 0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    FreeCAD.Gui.ActiveDocument.ntfbox.ShowText = True
    FreeCAD.Gui.ActiveDocument.ntfbox.TextSize = 14
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","spxl1")
    qwm_doc.spxl1.Placement = FreeCAD.Placement(FreeCAD.Vector(14.0, 0.5, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.spxl1.Orientation = "X"
    qwm_doc.spxl1.Position = 14.0
    qwm_doc.spxl1.Length = 1.0
    qwm_doc.spxl1.Width = 0.0
    FreeCAD.Gui.ActiveDocument.spxl1.ShowText = False
    FreeCAD.Gui.ActiveDocument.spxl1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.spxl1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","spxp1")
    qwm_doc.spxp1.Placement = FreeCAD.Placement(FreeCAD.Vector(26.0, 0.5, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.spxp1.Orientation = "X"
    qwm_doc.spxp1.Position = 26.0
    qwm_doc.spxp1.Length = 1.0
    qwm_doc.spxp1.Width = 0.0
    FreeCAD.Gui.ActiveDocument.spxp1.ShowText = False
    FreeCAD.Gui.ActiveDocument.spxp1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.spxp1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","spzl1")
    qwm_doc.spzl1.Placement = FreeCAD.Placement(FreeCAD.Vector(0.5, 0.5, -2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.spzl1.Orientation = "Z"
    qwm_doc.spzl1.Position = -2.0
    qwm_doc.spzl1.Length = 1.0
    qwm_doc.spzl1.Width = 1.0
    FreeCAD.Gui.ActiveDocument.spzl1.ShowText = False
    FreeCAD.Gui.ActiveDocument.spzl1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.spzl1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","spzp1")
    qwm_doc.spzp1.Placement = FreeCAD.Placement(FreeCAD.Vector(0.5, 0.5, 5.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.spzp1.Orientation = "Z"
    qwm_doc.spzp1.Position = 5.0
    qwm_doc.spzp1.Length = 1.0
    qwm_doc.spzp1.Width = 1.0
    FreeCAD.Gui.ActiveDocument.spzp1.ShowText = False
    FreeCAD.Gui.ActiveDocument.spzp1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.spzp1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","ip")
    qwm_doc.ip.Length = 3.1496
    qwm_doc.ip.Width = 12.0
    qwm_doc.ip.Placement = FreeCAD.Placement(FreeCAD.Vector(20.0, 0.0, 1.5748), FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.ip.Orientation = "Y"
    qwm_doc.ip.Position = 0.0
    qwm_doc.ip.Activity = "PLUS"
    qwm_doc.ip.Type = "Source"
    qwm_doc.ip.SymmetryH = False
    qwm_doc.ip.SymmetryV = False
    qwm_doc.ip.PointCoordX = 20.0
    qwm_doc.ip.PointCoordY = 0.0
    qwm_doc.ip.PointCoordZ = 1.5748
    qwm_doc.ip.effectivePermitivityMode = "AUTO"
    qwm_doc.ip.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('delta'),1,0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),1,50,1,0))
    qwm_doc.ip.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.ip.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.ip.ReferenceOffset = abs(qwm_doc.ip.PointCoordY - 0.0)
