
from FreeCAD import Base
import QW_Modeller
from qw_project import *
from qw_units import *


def set_Excitation(qwm_doc):
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","SourcePort")
    qwm_doc.SourcePort.Length = 10.0
    qwm_doc.SourcePort.Width = 5.0
    qwm_doc.SourcePort.Placement = FreeCAD.Placement(FreeCAD.Vector(-15.0, 0.0, 2.5), FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.SourcePort.Orientation = "X"
    qwm_doc.SourcePort.Position = -15.0
    qwm_doc.SourcePort.Activity = "PLUS"
    qwm_doc.SourcePort.Type = "Source"
    qwm_doc.SourcePort.SymmetryH = False
    qwm_doc.SourcePort.SymmetryV = False
    qwm_doc.SourcePort.PointCoordX = -15.0
    qwm_doc.SourcePort.PointCoordY = 0.0
    qwm_doc.SourcePort.PointCoordZ = 2.5
    qwm_doc.SourcePort.effectivePermitivityMode = "AUTO"
    qwm_doc.SourcePort.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('pulse of spectrum f1<f<f2',15.0,25.0,3.0),1.0,0.0,1,0),'R_TE10','Ez',1,QW_Modeller.TemplateGenerationConf('Automatic',(22.5,10.0),(20.0,25.0,0.02),0.556170282105275,76,1,0))
    qwm_doc.SourcePort.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.SourcePort.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.SourcePort.ReferenceOffset = abs(qwm_doc.SourcePort.PointCoordX - -9.8)
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","LoadPort")
    qwm_doc.LoadPort.Length = 5.0
    qwm_doc.LoadPort.Width = 5.0
    qwm_doc.LoadPort.Placement = FreeCAD.Placement(FreeCAD.Vector(4.6, 0.0, 14.0), FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.LoadPort.Orientation = "Z"
    qwm_doc.LoadPort.Position = 14.0
    qwm_doc.LoadPort.Activity = "MINUS"
    qwm_doc.LoadPort.Type = "Load"
    qwm_doc.LoadPort.SymmetryH = False
    qwm_doc.LoadPort.SymmetryV = False
    qwm_doc.LoadPort.PointCoordX = 4.6
    qwm_doc.LoadPort.PointCoordY = 0.0
    qwm_doc.LoadPort.PointCoordZ = 14.0
    qwm_doc.LoadPort.effectivePermitivityMode = "AUTO"
    qwm_doc.LoadPort.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('pulse of spectrum f1<f<f2',15.0,25.0,3.0),1.0,0.0,1,0),'TEM','Ez',1,QW_Modeller.TemplateGenerationConf('Automatic',(22.5,10.0),(20.0,25.0,0.02),1.0,76,1,0))
    qwm_doc.LoadPort.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.LoadPort.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.LoadPort.ReferenceOffset = abs(qwm_doc.LoadPort.PointCoordZ - 10.5)
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_2")
    qwm_doc.specX_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.60233, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_2.Orientation = "X"
    qwm_doc.specX_E_2.Position = -14.60233
    qwm_doc.specX_E_2.Length = 0.5
    qwm_doc.specX_E_2.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_3")
    qwm_doc.specX_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.20465, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_3.Orientation = "X"
    qwm_doc.specX_E_3.Position = -14.20465
    qwm_doc.specX_E_3.Length = 0.5
    qwm_doc.specX_E_3.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_4")
    qwm_doc.specX_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(-13.80698, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_4.Orientation = "X"
    qwm_doc.specX_E_4.Position = -13.80698
    qwm_doc.specX_E_4.Length = 0.5
    qwm_doc.specX_E_4.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_5")
    qwm_doc.specX_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(-13.4093, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_5.Orientation = "X"
    qwm_doc.specX_E_5.Position = -13.4093
    qwm_doc.specX_E_5.Length = 0.5
    qwm_doc.specX_E_5.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_6")
    qwm_doc.specX_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(-13.01163, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_6.Orientation = "X"
    qwm_doc.specX_E_6.Position = -13.01163
    qwm_doc.specX_E_6.Length = 0.5
    qwm_doc.specX_E_6.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_7")
    qwm_doc.specX_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(-12.61395, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_7.Orientation = "X"
    qwm_doc.specX_E_7.Position = -12.61395
    qwm_doc.specX_E_7.Length = 0.5
    qwm_doc.specX_E_7.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_8")
    qwm_doc.specX_E_8.Placement = FreeCAD.Placement(FreeCAD.Vector(-12.21628, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_8.Orientation = "X"
    qwm_doc.specX_E_8.Position = -12.21628
    qwm_doc.specX_E_8.Length = 0.5
    qwm_doc.specX_E_8.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_8.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_8.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_8.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_9")
    qwm_doc.specX_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(-11.8186, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_9.Orientation = "X"
    qwm_doc.specX_E_9.Position = -11.8186
    qwm_doc.specX_E_9.Length = 0.5
    qwm_doc.specX_E_9.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_10")
    qwm_doc.specX_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(-11.42093, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_10.Orientation = "X"
    qwm_doc.specX_E_10.Position = -11.42093
    qwm_doc.specX_E_10.Length = 0.5
    qwm_doc.specX_E_10.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_11")
    qwm_doc.specX_E_11.Placement = FreeCAD.Placement(FreeCAD.Vector(-11.02326, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_11.Orientation = "X"
    qwm_doc.specX_E_11.Position = -11.02326
    qwm_doc.specX_E_11.Length = 0.5
    qwm_doc.specX_E_11.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_11.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_11.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_11.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_12")
    qwm_doc.specX_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(-10.62558, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_12.Orientation = "X"
    qwm_doc.specX_E_12.Position = -10.62558
    qwm_doc.specX_E_12.Length = 0.5
    qwm_doc.specX_E_12.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_13")
    qwm_doc.specX_E_13.Placement = FreeCAD.Placement(FreeCAD.Vector(-10.22791, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_13.Orientation = "X"
    qwm_doc.specX_E_13.Position = -10.22791
    qwm_doc.specX_E_13.Length = 0.5
    qwm_doc.specX_E_13.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_13.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_13.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_13.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_14")
    qwm_doc.specX_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.83023, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_14.Orientation = "X"
    qwm_doc.specX_E_14.Position = -9.83023
    qwm_doc.specX_E_14.Length = 0.5
    qwm_doc.specX_E_14.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_15")
    qwm_doc.specX_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.43256, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_15.Orientation = "X"
    qwm_doc.specX_E_15.Position = -9.43256
    qwm_doc.specX_E_15.Length = 0.5
    qwm_doc.specX_E_15.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_16")
    qwm_doc.specX_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.03488, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_16.Orientation = "X"
    qwm_doc.specX_E_16.Position = -9.03488
    qwm_doc.specX_E_16.Length = 0.5
    qwm_doc.specX_E_16.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_17")
    qwm_doc.specX_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(-8.63721, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_17.Orientation = "X"
    qwm_doc.specX_E_17.Position = -8.63721
    qwm_doc.specX_E_17.Length = 0.5
    qwm_doc.specX_E_17.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_18")
    qwm_doc.specX_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(-8.23953, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_18.Orientation = "X"
    qwm_doc.specX_E_18.Position = -8.23953
    qwm_doc.specX_E_18.Length = 0.5
    qwm_doc.specX_E_18.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_19")
    qwm_doc.specX_E_19.Placement = FreeCAD.Placement(FreeCAD.Vector(-7.84186, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_19.Orientation = "X"
    qwm_doc.specX_E_19.Position = -7.84186
    qwm_doc.specX_E_19.Length = 0.5
    qwm_doc.specX_E_19.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_19.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_19.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_19.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_20")
    qwm_doc.specX_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(-7.44419, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_20.Orientation = "X"
    qwm_doc.specX_E_20.Position = -7.44419
    qwm_doc.specX_E_20.Length = 0.5
    qwm_doc.specX_E_20.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_21")
    qwm_doc.specX_E_21.Placement = FreeCAD.Placement(FreeCAD.Vector(-7.04651, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_21.Orientation = "X"
    qwm_doc.specX_E_21.Position = -7.04651
    qwm_doc.specX_E_21.Length = 0.5
    qwm_doc.specX_E_21.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_21.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_21.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_21.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_22")
    qwm_doc.specX_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(-6.64884, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_22.Orientation = "X"
    qwm_doc.specX_E_22.Position = -6.64884
    qwm_doc.specX_E_22.Length = 0.5
    qwm_doc.specX_E_22.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_23")
    qwm_doc.specX_E_23.Placement = FreeCAD.Placement(FreeCAD.Vector(-6.25116, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_23.Orientation = "X"
    qwm_doc.specX_E_23.Position = -6.25116
    qwm_doc.specX_E_23.Length = 0.5
    qwm_doc.specX_E_23.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_23.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_23.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_23.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_24")
    qwm_doc.specX_E_24.Placement = FreeCAD.Placement(FreeCAD.Vector(-5.85349, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_24.Orientation = "X"
    qwm_doc.specX_E_24.Position = -5.85349
    qwm_doc.specX_E_24.Length = 0.5
    qwm_doc.specX_E_24.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_24.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_24.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_24.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_25")
    qwm_doc.specX_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(-5.45581, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_25.Orientation = "X"
    qwm_doc.specX_E_25.Position = -5.45581
    qwm_doc.specX_E_25.Length = 0.5
    qwm_doc.specX_E_25.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_26")
    qwm_doc.specX_E_26.Placement = FreeCAD.Placement(FreeCAD.Vector(-5.05814, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_26.Orientation = "X"
    qwm_doc.specX_E_26.Position = -5.05814
    qwm_doc.specX_E_26.Length = 0.5
    qwm_doc.specX_E_26.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_26.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_26.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_26.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_27")
    qwm_doc.specX_E_27.Placement = FreeCAD.Placement(FreeCAD.Vector(-4.66047, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_27.Orientation = "X"
    qwm_doc.specX_E_27.Position = -4.66047
    qwm_doc.specX_E_27.Length = 0.5
    qwm_doc.specX_E_27.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_27.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_27.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_27.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_28")
    qwm_doc.specX_E_28.Placement = FreeCAD.Placement(FreeCAD.Vector(-4.26279, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_28.Orientation = "X"
    qwm_doc.specX_E_28.Position = -4.26279
    qwm_doc.specX_E_28.Length = 0.5
    qwm_doc.specX_E_28.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_28.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_28.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_28.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_29")
    qwm_doc.specX_E_29.Placement = FreeCAD.Placement(FreeCAD.Vector(-3.86512, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_29.Orientation = "X"
    qwm_doc.specX_E_29.Position = -3.86512
    qwm_doc.specX_E_29.Length = 0.5
    qwm_doc.specX_E_29.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_29.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_29.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_29.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_30")
    qwm_doc.specX_E_30.Placement = FreeCAD.Placement(FreeCAD.Vector(-3.46744, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_30.Orientation = "X"
    qwm_doc.specX_E_30.Position = -3.46744
    qwm_doc.specX_E_30.Length = 0.5
    qwm_doc.specX_E_30.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_30.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_30.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_30.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_31")
    qwm_doc.specX_E_31.Placement = FreeCAD.Placement(FreeCAD.Vector(-3.06977, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_31.Orientation = "X"
    qwm_doc.specX_E_31.Position = -3.06977
    qwm_doc.specX_E_31.Length = 0.5
    qwm_doc.specX_E_31.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_31.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_31.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_31.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_32")
    qwm_doc.specX_E_32.Placement = FreeCAD.Placement(FreeCAD.Vector(-2.67209, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_32.Orientation = "X"
    qwm_doc.specX_E_32.Position = -2.67209
    qwm_doc.specX_E_32.Length = 0.5
    qwm_doc.specX_E_32.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_32.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_32.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_32.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_33")
    qwm_doc.specX_E_33.Placement = FreeCAD.Placement(FreeCAD.Vector(-2.27442, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_33.Orientation = "X"
    qwm_doc.specX_E_33.Position = -2.27442
    qwm_doc.specX_E_33.Length = 0.5
    qwm_doc.specX_E_33.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_33.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_33.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_33.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_34")
    qwm_doc.specX_E_34.Placement = FreeCAD.Placement(FreeCAD.Vector(-1.87674, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_34.Orientation = "X"
    qwm_doc.specX_E_34.Position = -1.87674
    qwm_doc.specX_E_34.Length = 0.5
    qwm_doc.specX_E_34.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_34.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_34.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_34.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_35")
    qwm_doc.specX_E_35.Placement = FreeCAD.Placement(FreeCAD.Vector(-1.47907, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_35.Orientation = "X"
    qwm_doc.specX_E_35.Position = -1.47907
    qwm_doc.specX_E_35.Length = 0.5
    qwm_doc.specX_E_35.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_35.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_35.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_35.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_36")
    qwm_doc.specX_E_36.Placement = FreeCAD.Placement(FreeCAD.Vector(-1.0814, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_36.Orientation = "X"
    qwm_doc.specX_E_36.Position = -1.0814
    qwm_doc.specX_E_36.Length = 0.5
    qwm_doc.specX_E_36.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_36.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_36.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_36.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_37")
    qwm_doc.specX_E_37.Placement = FreeCAD.Placement(FreeCAD.Vector(-0.68372, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_37.Orientation = "X"
    qwm_doc.specX_E_37.Position = -0.68372
    qwm_doc.specX_E_37.Length = 0.5
    qwm_doc.specX_E_37.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_37.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_37.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_37.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_38")
    qwm_doc.specX_E_38.Placement = FreeCAD.Placement(FreeCAD.Vector(-0.28605, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_38.Orientation = "X"
    qwm_doc.specX_E_38.Position = -0.28605
    qwm_doc.specX_E_38.Length = 0.5
    qwm_doc.specX_E_38.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_38.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_38.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_38.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_39")
    qwm_doc.specX_E_39.Placement = FreeCAD.Placement(FreeCAD.Vector(0.11163, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_39.Orientation = "X"
    qwm_doc.specX_E_39.Position = 0.11163
    qwm_doc.specX_E_39.Length = 0.5
    qwm_doc.specX_E_39.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_39.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_39.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_39.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_40")
    qwm_doc.specX_E_40.Placement = FreeCAD.Placement(FreeCAD.Vector(0.5093, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_40.Orientation = "X"
    qwm_doc.specX_E_40.Position = 0.5093
    qwm_doc.specX_E_40.Length = 0.5
    qwm_doc.specX_E_40.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_40.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_40.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_40.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_41")
    qwm_doc.specX_E_41.Placement = FreeCAD.Placement(FreeCAD.Vector(0.90698, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_41.Orientation = "X"
    qwm_doc.specX_E_41.Position = 0.90698
    qwm_doc.specX_E_41.Length = 0.5
    qwm_doc.specX_E_41.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_41.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_41.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_41.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_42")
    qwm_doc.specX_E_42.Placement = FreeCAD.Placement(FreeCAD.Vector(1.30465, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_42.Orientation = "X"
    qwm_doc.specX_E_42.Position = 1.30465
    qwm_doc.specX_E_42.Length = 0.5
    qwm_doc.specX_E_42.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_42.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_42.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_42.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_43")
    qwm_doc.specX_E_43.Placement = FreeCAD.Placement(FreeCAD.Vector(1.70233, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_43.Orientation = "X"
    qwm_doc.specX_E_43.Position = 1.70233
    qwm_doc.specX_E_43.Length = 0.5
    qwm_doc.specX_E_43.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_43.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_43.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_43.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_45")
    qwm_doc.specX_E_45.Placement = FreeCAD.Placement(FreeCAD.Vector(2.48462, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_45.Orientation = "X"
    qwm_doc.specX_E_45.Position = 2.48462
    qwm_doc.specX_E_45.Length = 0.5
    qwm_doc.specX_E_45.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_45.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_45.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_45.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_46")
    qwm_doc.specX_E_46.Placement = FreeCAD.Placement(FreeCAD.Vector(2.86923, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_46.Orientation = "X"
    qwm_doc.specX_E_46.Position = 2.86923
    qwm_doc.specX_E_46.Length = 0.5
    qwm_doc.specX_E_46.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_46.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_46.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_46.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_47")
    qwm_doc.specX_E_47.Placement = FreeCAD.Placement(FreeCAD.Vector(3.25385, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_47.Orientation = "X"
    qwm_doc.specX_E_47.Position = 3.25385
    qwm_doc.specX_E_47.Length = 0.5
    qwm_doc.specX_E_47.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_47.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_47.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_47.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_48")
    qwm_doc.specX_E_48.Placement = FreeCAD.Placement(FreeCAD.Vector(3.63846, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_48.Orientation = "X"
    qwm_doc.specX_E_48.Position = 3.63846
    qwm_doc.specX_E_48.Length = 0.5
    qwm_doc.specX_E_48.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_48.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_48.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_48.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_49")
    qwm_doc.specX_E_49.Placement = FreeCAD.Placement(FreeCAD.Vector(4.02308, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_49.Orientation = "X"
    qwm_doc.specX_E_49.Position = 4.02308
    qwm_doc.specX_E_49.Length = 0.5
    qwm_doc.specX_E_49.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_49.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_49.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_49.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_50")
    qwm_doc.specX_E_50.Placement = FreeCAD.Placement(FreeCAD.Vector(4.40769, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_50.Orientation = "X"
    qwm_doc.specX_E_50.Position = 4.40769
    qwm_doc.specX_E_50.Length = 0.5
    qwm_doc.specX_E_50.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_50.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_50.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_50.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_51")
    qwm_doc.specX_E_51.Placement = FreeCAD.Placement(FreeCAD.Vector(4.79231, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_51.Orientation = "X"
    qwm_doc.specX_E_51.Position = 4.79231
    qwm_doc.specX_E_51.Length = 0.5
    qwm_doc.specX_E_51.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_51.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_51.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_51.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_52")
    qwm_doc.specX_E_52.Placement = FreeCAD.Placement(FreeCAD.Vector(5.17692, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_52.Orientation = "X"
    qwm_doc.specX_E_52.Position = 5.17692
    qwm_doc.specX_E_52.Length = 0.5
    qwm_doc.specX_E_52.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_52.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_52.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_52.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_53")
    qwm_doc.specX_E_53.Placement = FreeCAD.Placement(FreeCAD.Vector(5.56154, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_53.Orientation = "X"
    qwm_doc.specX_E_53.Position = 5.56154
    qwm_doc.specX_E_53.Length = 0.5
    qwm_doc.specX_E_53.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_53.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_53.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_53.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_54")
    qwm_doc.specX_E_54.Placement = FreeCAD.Placement(FreeCAD.Vector(5.94615, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_54.Orientation = "X"
    qwm_doc.specX_E_54.Position = 5.94615
    qwm_doc.specX_E_54.Length = 0.5
    qwm_doc.specX_E_54.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_54.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_54.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_54.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_55")
    qwm_doc.specX_E_55.Placement = FreeCAD.Placement(FreeCAD.Vector(6.33077, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_55.Orientation = "X"
    qwm_doc.specX_E_55.Position = 6.33077
    qwm_doc.specX_E_55.Length = 0.5
    qwm_doc.specX_E_55.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_55.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_55.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_55.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_56")
    qwm_doc.specX_E_56.Placement = FreeCAD.Placement(FreeCAD.Vector(6.71538, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_56.Orientation = "X"
    qwm_doc.specX_E_56.Position = 6.71538
    qwm_doc.specX_E_56.Length = 0.5
    qwm_doc.specX_E_56.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_56.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_56.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_56.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_58")
    qwm_doc.specX_E_58.Placement = FreeCAD.Placement(FreeCAD.Vector(7.495, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_58.Orientation = "X"
    qwm_doc.specX_E_58.Position = 7.495
    qwm_doc.specX_E_58.Length = 0.5
    qwm_doc.specX_E_58.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_58.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_58.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_58.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_59")
    qwm_doc.specX_E_59.Placement = FreeCAD.Placement(FreeCAD.Vector(7.89, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_59.Orientation = "X"
    qwm_doc.specX_E_59.Position = 7.89
    qwm_doc.specX_E_59.Length = 0.5
    qwm_doc.specX_E_59.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_59.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_59.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_59.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_60")
    qwm_doc.specX_E_60.Placement = FreeCAD.Placement(FreeCAD.Vector(8.285, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_60.Orientation = "X"
    qwm_doc.specX_E_60.Position = 8.285
    qwm_doc.specX_E_60.Length = 0.5
    qwm_doc.specX_E_60.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_60.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_60.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_60.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_61")
    qwm_doc.specX_E_61.Placement = FreeCAD.Placement(FreeCAD.Vector(8.68, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_61.Orientation = "X"
    qwm_doc.specX_E_61.Position = 8.68
    qwm_doc.specX_E_61.Length = 0.5
    qwm_doc.specX_E_61.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_61.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_61.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_61.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_62")
    qwm_doc.specX_E_62.Placement = FreeCAD.Placement(FreeCAD.Vector(9.075, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_62.Orientation = "X"
    qwm_doc.specX_E_62.Position = 9.075
    qwm_doc.specX_E_62.Length = 0.5
    qwm_doc.specX_E_62.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_62.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_62.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_62.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_63")
    qwm_doc.specX_E_63.Placement = FreeCAD.Placement(FreeCAD.Vector(9.47, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_63.Orientation = "X"
    qwm_doc.specX_E_63.Position = 9.47
    qwm_doc.specX_E_63.Length = 0.5
    qwm_doc.specX_E_63.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_63.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_63.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_63.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_64")
    qwm_doc.specX_E_64.Placement = FreeCAD.Placement(FreeCAD.Vector(9.865, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_64.Orientation = "X"
    qwm_doc.specX_E_64.Position = 9.865
    qwm_doc.specX_E_64.Length = 0.5
    qwm_doc.specX_E_64.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_64.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_64.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_64.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_65")
    qwm_doc.specX_E_65.Placement = FreeCAD.Placement(FreeCAD.Vector(10.26, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_65.Orientation = "X"
    qwm_doc.specX_E_65.Position = 10.26
    qwm_doc.specX_E_65.Length = 0.5
    qwm_doc.specX_E_65.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_65.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_65.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_65.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_66")
    qwm_doc.specX_E_66.Placement = FreeCAD.Placement(FreeCAD.Vector(10.655, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_66.Orientation = "X"
    qwm_doc.specX_E_66.Position = 10.655
    qwm_doc.specX_E_66.Length = 0.5
    qwm_doc.specX_E_66.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_66.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_66.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_66.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_67")
    qwm_doc.specX_E_67.Placement = FreeCAD.Placement(FreeCAD.Vector(11.05, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_67.Orientation = "X"
    qwm_doc.specX_E_67.Position = 11.05
    qwm_doc.specX_E_67.Length = 0.5
    qwm_doc.specX_E_67.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_67.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_67.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_67.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_68")
    qwm_doc.specX_E_68.Placement = FreeCAD.Placement(FreeCAD.Vector(11.445, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_68.Orientation = "X"
    qwm_doc.specX_E_68.Position = 11.445
    qwm_doc.specX_E_68.Length = 0.5
    qwm_doc.specX_E_68.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_68.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_68.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_68.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_69")
    qwm_doc.specX_E_69.Placement = FreeCAD.Placement(FreeCAD.Vector(11.84, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_69.Orientation = "X"
    qwm_doc.specX_E_69.Position = 11.84
    qwm_doc.specX_E_69.Length = 0.5
    qwm_doc.specX_E_69.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_69.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_69.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_69.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_70")
    qwm_doc.specX_E_70.Placement = FreeCAD.Placement(FreeCAD.Vector(12.235, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_70.Orientation = "X"
    qwm_doc.specX_E_70.Position = 12.235
    qwm_doc.specX_E_70.Length = 0.5
    qwm_doc.specX_E_70.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_70.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_70.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_70.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_71")
    qwm_doc.specX_E_71.Placement = FreeCAD.Placement(FreeCAD.Vector(12.63, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_71.Orientation = "X"
    qwm_doc.specX_E_71.Position = 12.63
    qwm_doc.specX_E_71.Length = 0.5
    qwm_doc.specX_E_71.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_71.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_71.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_71.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_72")
    qwm_doc.specX_E_72.Placement = FreeCAD.Placement(FreeCAD.Vector(13.025, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_72.Orientation = "X"
    qwm_doc.specX_E_72.Position = 13.025
    qwm_doc.specX_E_72.Length = 0.5
    qwm_doc.specX_E_72.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_72.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_72.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_72.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_73")
    qwm_doc.specX_E_73.Placement = FreeCAD.Placement(FreeCAD.Vector(13.42, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_73.Orientation = "X"
    qwm_doc.specX_E_73.Position = 13.42
    qwm_doc.specX_E_73.Length = 0.5
    qwm_doc.specX_E_73.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_73.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_73.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_73.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_74")
    qwm_doc.specX_E_74.Placement = FreeCAD.Placement(FreeCAD.Vector(13.815, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_74.Orientation = "X"
    qwm_doc.specX_E_74.Position = 13.815
    qwm_doc.specX_E_74.Length = 0.5
    qwm_doc.specX_E_74.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_74.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_74.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_74.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_75")
    qwm_doc.specX_E_75.Placement = FreeCAD.Placement(FreeCAD.Vector(14.21, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_75.Orientation = "X"
    qwm_doc.specX_E_75.Position = 14.21
    qwm_doc.specX_E_75.Length = 0.5
    qwm_doc.specX_E_75.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_75.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_75.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_75.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_76")
    qwm_doc.specX_E_76.Placement = FreeCAD.Placement(FreeCAD.Vector(14.605, -4.75, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_76.Orientation = "X"
    qwm_doc.specX_E_76.Position = 14.605
    qwm_doc.specX_E_76.Length = 0.5
    qwm_doc.specX_E_76.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specX_E_76.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_76.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_76.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_X_Bottom")
    qwm_doc.Border_X_Bottom.Placement = FreeCAD.Placement(FreeCAD.Vector(-15.0, -4.75, 7.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.Border_X_Bottom.Orientation = "X"
    qwm_doc.Border_X_Bottom.Position = -15.0
    qwm_doc.Border_X_Bottom.Length = 0.5
    qwm_doc.Border_X_Bottom.Width = 14.0
    FreeCAD.Gui.ActiveDocument.Border_X_Bottom.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_X_Bottom.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_X_Bottom.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_X_Top")
    qwm_doc.Border_X_Top.Placement = FreeCAD.Placement(FreeCAD.Vector(15.0, -4.75, 7.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.Border_X_Top.Orientation = "X"
    qwm_doc.Border_X_Top.Position = 15.0
    qwm_doc.Border_X_Top.Length = 0.5
    qwm_doc.Border_X_Top.Width = 14.0
    FreeCAD.Gui.ActiveDocument.Border_X_Top.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_X_Top.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_X_Top.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_2")
    qwm_doc.specY_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -4.64286, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_2.Orientation = "Y"
    qwm_doc.specY_E_2.Position = -4.64286
    qwm_doc.specY_E_2.Length = 0.5
    qwm_doc.specY_E_2.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_3")
    qwm_doc.specY_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -4.28571, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_3.Orientation = "Y"
    qwm_doc.specY_E_3.Position = -4.28571
    qwm_doc.specY_E_3.Length = 0.5
    qwm_doc.specY_E_3.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_4")
    qwm_doc.specY_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -3.92857, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_4.Orientation = "Y"
    qwm_doc.specY_E_4.Position = -3.92857
    qwm_doc.specY_E_4.Length = 0.5
    qwm_doc.specY_E_4.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_5")
    qwm_doc.specY_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -3.57143, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_5.Orientation = "Y"
    qwm_doc.specY_E_5.Position = -3.57143
    qwm_doc.specY_E_5.Length = 0.5
    qwm_doc.specY_E_5.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_6")
    qwm_doc.specY_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -3.21429, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_6.Orientation = "Y"
    qwm_doc.specY_E_6.Position = -3.21429
    qwm_doc.specY_E_6.Length = 0.5
    qwm_doc.specY_E_6.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_7")
    qwm_doc.specY_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -2.85714, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_7.Orientation = "Y"
    qwm_doc.specY_E_7.Position = -2.85714
    qwm_doc.specY_E_7.Length = 0.5
    qwm_doc.specY_E_7.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_9")
    qwm_doc.specY_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -2.11538, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_9.Orientation = "Y"
    qwm_doc.specY_E_9.Position = -2.11538
    qwm_doc.specY_E_9.Length = 0.5
    qwm_doc.specY_E_9.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_10")
    qwm_doc.specY_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -1.73077, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_10.Orientation = "Y"
    qwm_doc.specY_E_10.Position = -1.73077
    qwm_doc.specY_E_10.Length = 0.5
    qwm_doc.specY_E_10.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_11")
    qwm_doc.specY_E_11.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -1.34615, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_11.Orientation = "Y"
    qwm_doc.specY_E_11.Position = -1.34615
    qwm_doc.specY_E_11.Length = 0.5
    qwm_doc.specY_E_11.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_11.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_11.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_11.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_12")
    qwm_doc.specY_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -0.96154, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_12.Orientation = "Y"
    qwm_doc.specY_E_12.Position = -0.96154
    qwm_doc.specY_E_12.Length = 0.5
    qwm_doc.specY_E_12.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_13")
    qwm_doc.specY_E_13.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -0.57692, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_13.Orientation = "Y"
    qwm_doc.specY_E_13.Position = -0.57692
    qwm_doc.specY_E_13.Length = 0.5
    qwm_doc.specY_E_13.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_13.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_13.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_13.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_14")
    qwm_doc.specY_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -0.19231, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_14.Orientation = "Y"
    qwm_doc.specY_E_14.Position = -0.19231
    qwm_doc.specY_E_14.Length = 0.5
    qwm_doc.specY_E_14.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_15")
    qwm_doc.specY_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 0.19231, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_15.Orientation = "Y"
    qwm_doc.specY_E_15.Position = 0.19231
    qwm_doc.specY_E_15.Length = 0.5
    qwm_doc.specY_E_15.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_16")
    qwm_doc.specY_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 0.57692, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_16.Orientation = "Y"
    qwm_doc.specY_E_16.Position = 0.57692
    qwm_doc.specY_E_16.Length = 0.5
    qwm_doc.specY_E_16.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_17")
    qwm_doc.specY_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 0.96154, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_17.Orientation = "Y"
    qwm_doc.specY_E_17.Position = 0.96154
    qwm_doc.specY_E_17.Length = 0.5
    qwm_doc.specY_E_17.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_18")
    qwm_doc.specY_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 1.34615, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_18.Orientation = "Y"
    qwm_doc.specY_E_18.Position = 1.34615
    qwm_doc.specY_E_18.Length = 0.5
    qwm_doc.specY_E_18.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_19")
    qwm_doc.specY_E_19.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 1.73077, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_19.Orientation = "Y"
    qwm_doc.specY_E_19.Position = 1.73077
    qwm_doc.specY_E_19.Length = 0.5
    qwm_doc.specY_E_19.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_19.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_19.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_19.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_20")
    qwm_doc.specY_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 2.11538, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_20.Orientation = "Y"
    qwm_doc.specY_E_20.Position = 2.11538
    qwm_doc.specY_E_20.Length = 0.5
    qwm_doc.specY_E_20.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_22")
    qwm_doc.specY_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 2.85714, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_22.Orientation = "Y"
    qwm_doc.specY_E_22.Position = 2.85714
    qwm_doc.specY_E_22.Length = 0.5
    qwm_doc.specY_E_22.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_23")
    qwm_doc.specY_E_23.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 3.21429, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_23.Orientation = "Y"
    qwm_doc.specY_E_23.Position = 3.21429
    qwm_doc.specY_E_23.Length = 0.5
    qwm_doc.specY_E_23.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_23.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_23.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_23.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_24")
    qwm_doc.specY_E_24.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 3.57143, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_24.Orientation = "Y"
    qwm_doc.specY_E_24.Position = 3.57143
    qwm_doc.specY_E_24.Length = 0.5
    qwm_doc.specY_E_24.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_24.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_24.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_24.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_25")
    qwm_doc.specY_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 3.92857, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_25.Orientation = "Y"
    qwm_doc.specY_E_25.Position = 3.92857
    qwm_doc.specY_E_25.Length = 0.5
    qwm_doc.specY_E_25.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_26")
    qwm_doc.specY_E_26.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 4.28571, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_26.Orientation = "Y"
    qwm_doc.specY_E_26.Position = 4.28571
    qwm_doc.specY_E_26.Length = 0.5
    qwm_doc.specY_E_26.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_26.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_26.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_26.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_27")
    qwm_doc.specY_E_27.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 4.64286, 0.25),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_27.Orientation = "Y"
    qwm_doc.specY_E_27.Position = 4.64286
    qwm_doc.specY_E_27.Length = 0.5
    qwm_doc.specY_E_27.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specY_E_27.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_27.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_27.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_Y_Bottom")
    qwm_doc.Border_Y_Bottom.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -5.0, 7.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.Border_Y_Bottom.Orientation = "Y"
    qwm_doc.Border_Y_Bottom.Position = -5.0
    qwm_doc.Border_Y_Bottom.Length = 14.0
    qwm_doc.Border_Y_Bottom.Width = 0.5
    FreeCAD.Gui.ActiveDocument.Border_Y_Bottom.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_Y_Bottom.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_Y_Bottom.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_Y_Top")
    qwm_doc.Border_Y_Top.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, 5.0, 7.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.Border_Y_Top.Orientation = "Y"
    qwm_doc.Border_Y_Top.Position = 5.0
    qwm_doc.Border_Y_Top.Length = 14.0
    qwm_doc.Border_Y_Top.Width = 0.5
    FreeCAD.Gui.ActiveDocument.Border_Y_Top.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_Y_Top.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_Y_Top.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_2")
    qwm_doc.specZ_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 0.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_2.Orientation = "Z"
    qwm_doc.specZ_E_2.Position = 0.5
    qwm_doc.specZ_E_2.Length = 0.5
    qwm_doc.specZ_E_2.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_3")
    qwm_doc.specZ_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 1.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_3.Orientation = "Z"
    qwm_doc.specZ_E_3.Position = 1.0
    qwm_doc.specZ_E_3.Length = 0.5
    qwm_doc.specZ_E_3.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_4")
    qwm_doc.specZ_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 1.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_4.Orientation = "Z"
    qwm_doc.specZ_E_4.Position = 1.5
    qwm_doc.specZ_E_4.Length = 0.5
    qwm_doc.specZ_E_4.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_5")
    qwm_doc.specZ_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_5.Orientation = "Z"
    qwm_doc.specZ_E_5.Position = 2.0
    qwm_doc.specZ_E_5.Length = 0.5
    qwm_doc.specZ_E_5.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_6")
    qwm_doc.specZ_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 2.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_6.Orientation = "Z"
    qwm_doc.specZ_E_6.Position = 2.5
    qwm_doc.specZ_E_6.Length = 0.5
    qwm_doc.specZ_E_6.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_7")
    qwm_doc.specZ_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 3.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_7.Orientation = "Z"
    qwm_doc.specZ_E_7.Position = 3.0
    qwm_doc.specZ_E_7.Length = 0.5
    qwm_doc.specZ_E_7.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_8")
    qwm_doc.specZ_E_8.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 3.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_8.Orientation = "Z"
    qwm_doc.specZ_E_8.Position = 3.5
    qwm_doc.specZ_E_8.Length = 0.5
    qwm_doc.specZ_E_8.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_8.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_8.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_8.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_9")
    qwm_doc.specZ_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_9.Orientation = "Z"
    qwm_doc.specZ_E_9.Position = 4.0
    qwm_doc.specZ_E_9.Length = 0.5
    qwm_doc.specZ_E_9.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_10")
    qwm_doc.specZ_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 4.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_10.Orientation = "Z"
    qwm_doc.specZ_E_10.Position = 4.5
    qwm_doc.specZ_E_10.Length = 0.5
    qwm_doc.specZ_E_10.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_12")
    qwm_doc.specZ_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 5.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_12.Orientation = "Z"
    qwm_doc.specZ_E_12.Position = 5.5
    qwm_doc.specZ_E_12.Length = 0.5
    qwm_doc.specZ_E_12.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_13")
    qwm_doc.specZ_E_13.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_13.Orientation = "Z"
    qwm_doc.specZ_E_13.Position = 6.0
    qwm_doc.specZ_E_13.Length = 0.5
    qwm_doc.specZ_E_13.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_13.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_13.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_13.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_14")
    qwm_doc.specZ_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 6.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_14.Orientation = "Z"
    qwm_doc.specZ_E_14.Position = 6.5
    qwm_doc.specZ_E_14.Length = 0.5
    qwm_doc.specZ_E_14.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_15")
    qwm_doc.specZ_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 7.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_15.Orientation = "Z"
    qwm_doc.specZ_E_15.Position = 7.0
    qwm_doc.specZ_E_15.Length = 0.5
    qwm_doc.specZ_E_15.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_16")
    qwm_doc.specZ_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 7.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_16.Orientation = "Z"
    qwm_doc.specZ_E_16.Position = 7.5
    qwm_doc.specZ_E_16.Length = 0.5
    qwm_doc.specZ_E_16.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_17")
    qwm_doc.specZ_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 8.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_17.Orientation = "Z"
    qwm_doc.specZ_E_17.Position = 8.0
    qwm_doc.specZ_E_17.Length = 0.5
    qwm_doc.specZ_E_17.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_18")
    qwm_doc.specZ_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 8.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_18.Orientation = "Z"
    qwm_doc.specZ_E_18.Position = 8.5
    qwm_doc.specZ_E_18.Length = 0.5
    qwm_doc.specZ_E_18.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_19")
    qwm_doc.specZ_E_19.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 9.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_19.Orientation = "Z"
    qwm_doc.specZ_E_19.Position = 9.0
    qwm_doc.specZ_E_19.Length = 0.5
    qwm_doc.specZ_E_19.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_19.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_19.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_19.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_20")
    qwm_doc.specZ_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 9.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_20.Orientation = "Z"
    qwm_doc.specZ_E_20.Position = 9.5
    qwm_doc.specZ_E_20.Length = 0.5
    qwm_doc.specZ_E_20.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_21")
    qwm_doc.specZ_E_21.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 10.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_21.Orientation = "Z"
    qwm_doc.specZ_E_21.Position = 10.0
    qwm_doc.specZ_E_21.Length = 0.5
    qwm_doc.specZ_E_21.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_21.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_21.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_21.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_22")
    qwm_doc.specZ_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 10.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_22.Orientation = "Z"
    qwm_doc.specZ_E_22.Position = 10.5
    qwm_doc.specZ_E_22.Length = 0.5
    qwm_doc.specZ_E_22.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_23")
    qwm_doc.specZ_E_23.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 11.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_23.Orientation = "Z"
    qwm_doc.specZ_E_23.Position = 11.0
    qwm_doc.specZ_E_23.Length = 0.5
    qwm_doc.specZ_E_23.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_23.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_23.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_23.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_24")
    qwm_doc.specZ_E_24.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 11.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_24.Orientation = "Z"
    qwm_doc.specZ_E_24.Position = 11.5
    qwm_doc.specZ_E_24.Length = 0.5
    qwm_doc.specZ_E_24.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_24.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_24.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_24.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_25")
    qwm_doc.specZ_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 12.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_25.Orientation = "Z"
    qwm_doc.specZ_E_25.Position = 12.0
    qwm_doc.specZ_E_25.Length = 0.5
    qwm_doc.specZ_E_25.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_26")
    qwm_doc.specZ_E_26.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 12.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_26.Orientation = "Z"
    qwm_doc.specZ_E_26.Position = 12.5
    qwm_doc.specZ_E_26.Length = 0.5
    qwm_doc.specZ_E_26.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_26.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_26.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_26.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_27")
    qwm_doc.specZ_E_27.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 13.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_27.Orientation = "Z"
    qwm_doc.specZ_E_27.Position = 13.0
    qwm_doc.specZ_E_27.Length = 0.5
    qwm_doc.specZ_E_27.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_27.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_27.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_27.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_28")
    qwm_doc.specZ_E_28.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 13.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_28.Orientation = "Z"
    qwm_doc.specZ_E_28.Position = 13.5
    qwm_doc.specZ_E_28.Length = 0.5
    qwm_doc.specZ_E_28.Width = 0.5
    FreeCAD.Gui.ActiveDocument.specZ_E_28.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_28.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_28.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_Z_Bottom")
    qwm_doc.Border_Z_Bottom.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -4.75, 0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.Border_Z_Bottom.Orientation = "Z"
    qwm_doc.Border_Z_Bottom.Position = 0.0
    qwm_doc.Border_Z_Bottom.Length = 0.5
    qwm_doc.Border_Z_Bottom.Width = 0.5
    FreeCAD.Gui.ActiveDocument.Border_Z_Bottom.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_Z_Bottom.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_Z_Bottom.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_Z_Top")
    qwm_doc.Border_Z_Top.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.75, -4.75, 14.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.Border_Z_Top.Orientation = "Z"
    qwm_doc.Border_Z_Top.Position = 14.0
    qwm_doc.Border_Z_Top.Length = 0.5
    qwm_doc.Border_Z_Top.Width = 0.5
    FreeCAD.Gui.ActiveDocument.Border_Z_Top.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_Z_Top.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_Z_Top.TextPlace = 3
