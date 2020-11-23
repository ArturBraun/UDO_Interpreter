
from FreeCAD import Base
import QW_Modeller
from qw_project import *
from qw_units import *


def set_Excitation(qwm_doc):
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_1")
    qwm_doc.MeshX_E_1.Placement = FreeCAD.Placement(FreeCAD.Vector(5.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_1.Orientation = "X"
    qwm_doc.MeshX_E_1.Position = 5.0
    qwm_doc.MeshX_E_1.Length = 5.143000000000001
    qwm_doc.MeshX_E_1.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_1.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_2")
    qwm_doc.MeshX_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(6.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_2.Orientation = "X"
    qwm_doc.MeshX_E_2.Position = 6.0
    qwm_doc.MeshX_E_2.Length = 5.143000000000001
    qwm_doc.MeshX_E_2.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_3")
    qwm_doc.MeshX_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(7.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_3.Orientation = "X"
    qwm_doc.MeshX_E_3.Position = 7.0
    qwm_doc.MeshX_E_3.Length = 5.143000000000001
    qwm_doc.MeshX_E_3.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_4")
    qwm_doc.MeshX_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(8.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_4.Orientation = "X"
    qwm_doc.MeshX_E_4.Position = 8.0
    qwm_doc.MeshX_E_4.Length = 5.143000000000001
    qwm_doc.MeshX_E_4.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_5")
    qwm_doc.MeshX_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(9.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_5.Orientation = "X"
    qwm_doc.MeshX_E_5.Position = 9.0
    qwm_doc.MeshX_E_5.Length = 5.143000000000001
    qwm_doc.MeshX_E_5.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_6")
    qwm_doc.MeshX_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(10.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_6.Orientation = "X"
    qwm_doc.MeshX_E_6.Position = 10.0
    qwm_doc.MeshX_E_6.Length = 5.143000000000001
    qwm_doc.MeshX_E_6.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_7")
    qwm_doc.MeshX_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(11.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_7.Orientation = "X"
    qwm_doc.MeshX_E_7.Position = 11.0
    qwm_doc.MeshX_E_7.Length = 5.143000000000001
    qwm_doc.MeshX_E_7.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_8")
    qwm_doc.MeshX_E_8.Placement = FreeCAD.Placement(FreeCAD.Vector(12.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_8.Orientation = "X"
    qwm_doc.MeshX_E_8.Position = 12.0
    qwm_doc.MeshX_E_8.Length = 5.143000000000001
    qwm_doc.MeshX_E_8.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_8.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_8.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_8.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_9")
    qwm_doc.MeshX_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(13.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_9.Orientation = "X"
    qwm_doc.MeshX_E_9.Position = 13.0
    qwm_doc.MeshX_E_9.Length = 5.143000000000001
    qwm_doc.MeshX_E_9.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_10")
    qwm_doc.MeshX_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(14.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_10.Orientation = "X"
    qwm_doc.MeshX_E_10.Position = 14.0
    qwm_doc.MeshX_E_10.Length = 5.143000000000001
    qwm_doc.MeshX_E_10.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_11")
    qwm_doc.MeshX_E_11.Placement = FreeCAD.Placement(FreeCAD.Vector(15.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_11.Orientation = "X"
    qwm_doc.MeshX_E_11.Position = 15.0
    qwm_doc.MeshX_E_11.Length = 5.143000000000001
    qwm_doc.MeshX_E_11.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_11.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_11.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_11.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_12")
    qwm_doc.MeshX_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(15.98208, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_12.Orientation = "X"
    qwm_doc.MeshX_E_12.Position = 15.98208
    qwm_doc.MeshX_E_12.Length = 5.143000000000001
    qwm_doc.MeshX_E_12.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_13")
    qwm_doc.MeshX_E_13.Placement = FreeCAD.Placement(FreeCAD.Vector(16.96417, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_13.Orientation = "X"
    qwm_doc.MeshX_E_13.Position = 16.96417
    qwm_doc.MeshX_E_13.Length = 5.143000000000001
    qwm_doc.MeshX_E_13.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_13.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_13.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_13.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_14")
    qwm_doc.MeshX_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(17.94625, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_14.Orientation = "X"
    qwm_doc.MeshX_E_14.Position = 17.94625
    qwm_doc.MeshX_E_14.Length = 5.143000000000001
    qwm_doc.MeshX_E_14.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_15")
    qwm_doc.MeshX_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(18.92833, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_15.Orientation = "X"
    qwm_doc.MeshX_E_15.Position = 18.92833
    qwm_doc.MeshX_E_15.Length = 5.143000000000001
    qwm_doc.MeshX_E_15.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_16")
    qwm_doc.MeshX_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(19.91042, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_16.Orientation = "X"
    qwm_doc.MeshX_E_16.Position = 19.91042
    qwm_doc.MeshX_E_16.Length = 5.143000000000001
    qwm_doc.MeshX_E_16.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_17")
    qwm_doc.MeshX_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(20.8925, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_17.Orientation = "X"
    qwm_doc.MeshX_E_17.Position = 20.8925
    qwm_doc.MeshX_E_17.Length = 5.143000000000001
    qwm_doc.MeshX_E_17.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_18")
    qwm_doc.MeshX_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(21.87458, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_18.Orientation = "X"
    qwm_doc.MeshX_E_18.Position = 21.87458
    qwm_doc.MeshX_E_18.Length = 5.143000000000001
    qwm_doc.MeshX_E_18.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_19")
    qwm_doc.MeshX_E_19.Placement = FreeCAD.Placement(FreeCAD.Vector(22.85667, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_19.Orientation = "X"
    qwm_doc.MeshX_E_19.Position = 22.85667
    qwm_doc.MeshX_E_19.Length = 5.143000000000001
    qwm_doc.MeshX_E_19.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_19.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_19.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_19.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_20")
    qwm_doc.MeshX_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(23.83875, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_20.Orientation = "X"
    qwm_doc.MeshX_E_20.Position = 23.83875
    qwm_doc.MeshX_E_20.Length = 5.143000000000001
    qwm_doc.MeshX_E_20.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_21")
    qwm_doc.MeshX_E_21.Placement = FreeCAD.Placement(FreeCAD.Vector(24.82083, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_21.Orientation = "X"
    qwm_doc.MeshX_E_21.Position = 24.82083
    qwm_doc.MeshX_E_21.Length = 5.143000000000001
    qwm_doc.MeshX_E_21.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_21.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_21.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_21.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_22")
    qwm_doc.MeshX_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(25.80292, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_22.Orientation = "X"
    qwm_doc.MeshX_E_22.Position = 25.80292
    qwm_doc.MeshX_E_22.Length = 5.143000000000001
    qwm_doc.MeshX_E_22.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_23")
    qwm_doc.MeshX_E_23.Placement = FreeCAD.Placement(FreeCAD.Vector(26.785, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_23.Orientation = "X"
    qwm_doc.MeshX_E_23.Position = 26.785
    qwm_doc.MeshX_E_23.Length = 5.143000000000001
    qwm_doc.MeshX_E_23.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_23.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_23.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_23.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_24")
    qwm_doc.MeshX_E_24.Placement = FreeCAD.Placement(FreeCAD.Vector(27.76708, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_24.Orientation = "X"
    qwm_doc.MeshX_E_24.Position = 27.76708
    qwm_doc.MeshX_E_24.Length = 5.143000000000001
    qwm_doc.MeshX_E_24.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_24.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_24.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_24.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_25")
    qwm_doc.MeshX_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(28.74917, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_25.Orientation = "X"
    qwm_doc.MeshX_E_25.Position = 28.74917
    qwm_doc.MeshX_E_25.Length = 5.143000000000001
    qwm_doc.MeshX_E_25.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_26")
    qwm_doc.MeshX_E_26.Placement = FreeCAD.Placement(FreeCAD.Vector(29.73125, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_26.Orientation = "X"
    qwm_doc.MeshX_E_26.Position = 29.73125
    qwm_doc.MeshX_E_26.Length = 5.143000000000001
    qwm_doc.MeshX_E_26.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_26.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_26.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_26.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_27")
    qwm_doc.MeshX_E_27.Placement = FreeCAD.Placement(FreeCAD.Vector(30.71333, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_27.Orientation = "X"
    qwm_doc.MeshX_E_27.Position = 30.71333
    qwm_doc.MeshX_E_27.Length = 5.143000000000001
    qwm_doc.MeshX_E_27.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_27.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_27.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_27.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_28")
    qwm_doc.MeshX_E_28.Placement = FreeCAD.Placement(FreeCAD.Vector(31.69542, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_28.Orientation = "X"
    qwm_doc.MeshX_E_28.Position = 31.69542
    qwm_doc.MeshX_E_28.Length = 5.143000000000001
    qwm_doc.MeshX_E_28.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_28.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_28.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_28.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_29")
    qwm_doc.MeshX_E_29.Placement = FreeCAD.Placement(FreeCAD.Vector(32.6775, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_29.Orientation = "X"
    qwm_doc.MeshX_E_29.Position = 32.6775
    qwm_doc.MeshX_E_29.Length = 5.143000000000001
    qwm_doc.MeshX_E_29.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_29.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_29.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_29.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_30")
    qwm_doc.MeshX_E_30.Placement = FreeCAD.Placement(FreeCAD.Vector(33.65958, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_30.Orientation = "X"
    qwm_doc.MeshX_E_30.Position = 33.65958
    qwm_doc.MeshX_E_30.Length = 5.143000000000001
    qwm_doc.MeshX_E_30.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_30.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_30.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_30.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_31")
    qwm_doc.MeshX_E_31.Placement = FreeCAD.Placement(FreeCAD.Vector(34.64167, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_31.Orientation = "X"
    qwm_doc.MeshX_E_31.Position = 34.64167
    qwm_doc.MeshX_E_31.Length = 5.143000000000001
    qwm_doc.MeshX_E_31.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_31.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_31.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_31.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_32")
    qwm_doc.MeshX_E_32.Placement = FreeCAD.Placement(FreeCAD.Vector(35.62375, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_32.Orientation = "X"
    qwm_doc.MeshX_E_32.Position = 35.62375
    qwm_doc.MeshX_E_32.Length = 5.143000000000001
    qwm_doc.MeshX_E_32.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_32.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_32.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_32.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_33")
    qwm_doc.MeshX_E_33.Placement = FreeCAD.Placement(FreeCAD.Vector(36.60583, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_33.Orientation = "X"
    qwm_doc.MeshX_E_33.Position = 36.60583
    qwm_doc.MeshX_E_33.Length = 5.143000000000001
    qwm_doc.MeshX_E_33.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_33.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_33.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_33.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_34")
    qwm_doc.MeshX_E_34.Placement = FreeCAD.Placement(FreeCAD.Vector(37.58792, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_34.Orientation = "X"
    qwm_doc.MeshX_E_34.Position = 37.58792
    qwm_doc.MeshX_E_34.Length = 5.143000000000001
    qwm_doc.MeshX_E_34.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_34.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_34.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_34.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_35")
    qwm_doc.MeshX_E_35.Placement = FreeCAD.Placement(FreeCAD.Vector(38.57, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_35.Orientation = "X"
    qwm_doc.MeshX_E_35.Position = 38.57
    qwm_doc.MeshX_E_35.Length = 5.143000000000001
    qwm_doc.MeshX_E_35.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_35.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_35.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_35.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_36")
    qwm_doc.MeshX_E_36.Placement = FreeCAD.Placement(FreeCAD.Vector(39.47714, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_36.Orientation = "X"
    qwm_doc.MeshX_E_36.Position = 39.47714
    qwm_doc.MeshX_E_36.Length = 5.143000000000001
    qwm_doc.MeshX_E_36.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_36.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_36.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_36.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_37")
    qwm_doc.MeshX_E_37.Placement = FreeCAD.Placement(FreeCAD.Vector(40.38429, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_37.Orientation = "X"
    qwm_doc.MeshX_E_37.Position = 40.38429
    qwm_doc.MeshX_E_37.Length = 5.143000000000001
    qwm_doc.MeshX_E_37.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_37.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_37.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_37.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_38")
    qwm_doc.MeshX_E_38.Placement = FreeCAD.Placement(FreeCAD.Vector(41.29143, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_38.Orientation = "X"
    qwm_doc.MeshX_E_38.Position = 41.29143
    qwm_doc.MeshX_E_38.Length = 5.143000000000001
    qwm_doc.MeshX_E_38.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_38.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_38.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_38.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_39")
    qwm_doc.MeshX_E_39.Placement = FreeCAD.Placement(FreeCAD.Vector(42.19857, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_39.Orientation = "X"
    qwm_doc.MeshX_E_39.Position = 42.19857
    qwm_doc.MeshX_E_39.Length = 5.143000000000001
    qwm_doc.MeshX_E_39.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_39.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_39.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_39.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_40")
    qwm_doc.MeshX_E_40.Placement = FreeCAD.Placement(FreeCAD.Vector(43.10571, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_40.Orientation = "X"
    qwm_doc.MeshX_E_40.Position = 43.10571
    qwm_doc.MeshX_E_40.Length = 5.143000000000001
    qwm_doc.MeshX_E_40.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_40.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_40.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_40.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_41")
    qwm_doc.MeshX_E_41.Placement = FreeCAD.Placement(FreeCAD.Vector(44.01286, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_41.Orientation = "X"
    qwm_doc.MeshX_E_41.Position = 44.01286
    qwm_doc.MeshX_E_41.Length = 5.143000000000001
    qwm_doc.MeshX_E_41.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_41.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_41.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_41.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_42")
    qwm_doc.MeshX_E_42.Placement = FreeCAD.Placement(FreeCAD.Vector(44.92, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_42.Orientation = "X"
    qwm_doc.MeshX_E_42.Position = 44.92
    qwm_doc.MeshX_E_42.Length = 5.143000000000001
    qwm_doc.MeshX_E_42.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_42.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_42.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_42.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_43")
    qwm_doc.MeshX_E_43.Placement = FreeCAD.Placement(FreeCAD.Vector(45.84364, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_43.Orientation = "X"
    qwm_doc.MeshX_E_43.Position = 45.84364
    qwm_doc.MeshX_E_43.Length = 5.143000000000001
    qwm_doc.MeshX_E_43.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_43.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_43.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_43.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_44")
    qwm_doc.MeshX_E_44.Placement = FreeCAD.Placement(FreeCAD.Vector(46.76727, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_44.Orientation = "X"
    qwm_doc.MeshX_E_44.Position = 46.76727
    qwm_doc.MeshX_E_44.Length = 5.143000000000001
    qwm_doc.MeshX_E_44.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_44.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_44.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_44.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_45")
    qwm_doc.MeshX_E_45.Placement = FreeCAD.Placement(FreeCAD.Vector(47.69091, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_45.Orientation = "X"
    qwm_doc.MeshX_E_45.Position = 47.69091
    qwm_doc.MeshX_E_45.Length = 5.143000000000001
    qwm_doc.MeshX_E_45.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_45.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_45.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_45.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_46")
    qwm_doc.MeshX_E_46.Placement = FreeCAD.Placement(FreeCAD.Vector(48.61455, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_46.Orientation = "X"
    qwm_doc.MeshX_E_46.Position = 48.61455
    qwm_doc.MeshX_E_46.Length = 5.143000000000001
    qwm_doc.MeshX_E_46.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_46.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_46.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_46.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_47")
    qwm_doc.MeshX_E_47.Placement = FreeCAD.Placement(FreeCAD.Vector(49.53818, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_47.Orientation = "X"
    qwm_doc.MeshX_E_47.Position = 49.53818
    qwm_doc.MeshX_E_47.Length = 5.143000000000001
    qwm_doc.MeshX_E_47.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_47.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_47.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_47.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_48")
    qwm_doc.MeshX_E_48.Placement = FreeCAD.Placement(FreeCAD.Vector(50.46182, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_48.Orientation = "X"
    qwm_doc.MeshX_E_48.Position = 50.46182
    qwm_doc.MeshX_E_48.Length = 5.143000000000001
    qwm_doc.MeshX_E_48.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_48.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_48.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_48.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_49")
    qwm_doc.MeshX_E_49.Placement = FreeCAD.Placement(FreeCAD.Vector(51.38545, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_49.Orientation = "X"
    qwm_doc.MeshX_E_49.Position = 51.38545
    qwm_doc.MeshX_E_49.Length = 5.143000000000001
    qwm_doc.MeshX_E_49.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_49.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_49.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_49.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_50")
    qwm_doc.MeshX_E_50.Placement = FreeCAD.Placement(FreeCAD.Vector(52.30909, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_50.Orientation = "X"
    qwm_doc.MeshX_E_50.Position = 52.30909
    qwm_doc.MeshX_E_50.Length = 5.143000000000001
    qwm_doc.MeshX_E_50.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_50.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_50.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_50.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_51")
    qwm_doc.MeshX_E_51.Placement = FreeCAD.Placement(FreeCAD.Vector(53.23273, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_51.Orientation = "X"
    qwm_doc.MeshX_E_51.Position = 53.23273
    qwm_doc.MeshX_E_51.Length = 5.143000000000001
    qwm_doc.MeshX_E_51.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_51.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_51.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_51.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_52")
    qwm_doc.MeshX_E_52.Placement = FreeCAD.Placement(FreeCAD.Vector(54.15636, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_52.Orientation = "X"
    qwm_doc.MeshX_E_52.Position = 54.15636
    qwm_doc.MeshX_E_52.Length = 5.143000000000001
    qwm_doc.MeshX_E_52.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_52.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_52.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_52.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_53")
    qwm_doc.MeshX_E_53.Placement = FreeCAD.Placement(FreeCAD.Vector(55.08, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_53.Orientation = "X"
    qwm_doc.MeshX_E_53.Position = 55.08
    qwm_doc.MeshX_E_53.Length = 5.143000000000001
    qwm_doc.MeshX_E_53.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_53.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_53.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_53.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_54")
    qwm_doc.MeshX_E_54.Placement = FreeCAD.Placement(FreeCAD.Vector(55.98714, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_54.Orientation = "X"
    qwm_doc.MeshX_E_54.Position = 55.98714
    qwm_doc.MeshX_E_54.Length = 5.143000000000001
    qwm_doc.MeshX_E_54.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_54.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_54.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_54.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_55")
    qwm_doc.MeshX_E_55.Placement = FreeCAD.Placement(FreeCAD.Vector(56.89429, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_55.Orientation = "X"
    qwm_doc.MeshX_E_55.Position = 56.89429
    qwm_doc.MeshX_E_55.Length = 5.143000000000001
    qwm_doc.MeshX_E_55.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_55.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_55.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_55.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_56")
    qwm_doc.MeshX_E_56.Placement = FreeCAD.Placement(FreeCAD.Vector(57.80143, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_56.Orientation = "X"
    qwm_doc.MeshX_E_56.Position = 57.80143
    qwm_doc.MeshX_E_56.Length = 5.143000000000001
    qwm_doc.MeshX_E_56.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_56.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_56.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_56.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_57")
    qwm_doc.MeshX_E_57.Placement = FreeCAD.Placement(FreeCAD.Vector(58.70857, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_57.Orientation = "X"
    qwm_doc.MeshX_E_57.Position = 58.70857
    qwm_doc.MeshX_E_57.Length = 5.143000000000001
    qwm_doc.MeshX_E_57.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_57.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_57.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_57.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_58")
    qwm_doc.MeshX_E_58.Placement = FreeCAD.Placement(FreeCAD.Vector(59.61571, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_58.Orientation = "X"
    qwm_doc.MeshX_E_58.Position = 59.61571
    qwm_doc.MeshX_E_58.Length = 5.143000000000001
    qwm_doc.MeshX_E_58.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_58.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_58.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_58.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_59")
    qwm_doc.MeshX_E_59.Placement = FreeCAD.Placement(FreeCAD.Vector(60.52286, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_59.Orientation = "X"
    qwm_doc.MeshX_E_59.Position = 60.52286
    qwm_doc.MeshX_E_59.Length = 5.143000000000001
    qwm_doc.MeshX_E_59.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_59.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_59.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_59.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_60")
    qwm_doc.MeshX_E_60.Placement = FreeCAD.Placement(FreeCAD.Vector(61.43, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_60.Orientation = "X"
    qwm_doc.MeshX_E_60.Position = 61.43
    qwm_doc.MeshX_E_60.Length = 5.143000000000001
    qwm_doc.MeshX_E_60.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_60.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_60.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_60.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_61")
    qwm_doc.MeshX_E_61.Placement = FreeCAD.Placement(FreeCAD.Vector(62.41208, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_61.Orientation = "X"
    qwm_doc.MeshX_E_61.Position = 62.41208
    qwm_doc.MeshX_E_61.Length = 5.143000000000001
    qwm_doc.MeshX_E_61.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_61.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_61.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_61.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_62")
    qwm_doc.MeshX_E_62.Placement = FreeCAD.Placement(FreeCAD.Vector(63.39417, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_62.Orientation = "X"
    qwm_doc.MeshX_E_62.Position = 63.39417
    qwm_doc.MeshX_E_62.Length = 5.143000000000001
    qwm_doc.MeshX_E_62.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_62.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_62.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_62.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_63")
    qwm_doc.MeshX_E_63.Placement = FreeCAD.Placement(FreeCAD.Vector(64.37625, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_63.Orientation = "X"
    qwm_doc.MeshX_E_63.Position = 64.37625
    qwm_doc.MeshX_E_63.Length = 5.143000000000001
    qwm_doc.MeshX_E_63.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_63.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_63.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_63.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_64")
    qwm_doc.MeshX_E_64.Placement = FreeCAD.Placement(FreeCAD.Vector(65.35833, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_64.Orientation = "X"
    qwm_doc.MeshX_E_64.Position = 65.35833
    qwm_doc.MeshX_E_64.Length = 5.143000000000001
    qwm_doc.MeshX_E_64.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_64.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_64.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_64.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_65")
    qwm_doc.MeshX_E_65.Placement = FreeCAD.Placement(FreeCAD.Vector(66.34042, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_65.Orientation = "X"
    qwm_doc.MeshX_E_65.Position = 66.34042
    qwm_doc.MeshX_E_65.Length = 5.143000000000001
    qwm_doc.MeshX_E_65.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_65.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_65.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_65.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_66")
    qwm_doc.MeshX_E_66.Placement = FreeCAD.Placement(FreeCAD.Vector(67.3225, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_66.Orientation = "X"
    qwm_doc.MeshX_E_66.Position = 67.3225
    qwm_doc.MeshX_E_66.Length = 5.143000000000001
    qwm_doc.MeshX_E_66.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_66.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_66.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_66.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_67")
    qwm_doc.MeshX_E_67.Placement = FreeCAD.Placement(FreeCAD.Vector(68.30458, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_67.Orientation = "X"
    qwm_doc.MeshX_E_67.Position = 68.30458
    qwm_doc.MeshX_E_67.Length = 5.143000000000001
    qwm_doc.MeshX_E_67.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_67.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_67.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_67.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_68")
    qwm_doc.MeshX_E_68.Placement = FreeCAD.Placement(FreeCAD.Vector(69.28667, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_68.Orientation = "X"
    qwm_doc.MeshX_E_68.Position = 69.28667
    qwm_doc.MeshX_E_68.Length = 5.143000000000001
    qwm_doc.MeshX_E_68.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_68.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_68.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_68.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_69")
    qwm_doc.MeshX_E_69.Placement = FreeCAD.Placement(FreeCAD.Vector(70.26875, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_69.Orientation = "X"
    qwm_doc.MeshX_E_69.Position = 70.26875
    qwm_doc.MeshX_E_69.Length = 5.143000000000001
    qwm_doc.MeshX_E_69.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_69.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_69.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_69.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_70")
    qwm_doc.MeshX_E_70.Placement = FreeCAD.Placement(FreeCAD.Vector(71.25083, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_70.Orientation = "X"
    qwm_doc.MeshX_E_70.Position = 71.25083
    qwm_doc.MeshX_E_70.Length = 5.143000000000001
    qwm_doc.MeshX_E_70.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_70.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_70.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_70.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_71")
    qwm_doc.MeshX_E_71.Placement = FreeCAD.Placement(FreeCAD.Vector(72.23292, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_71.Orientation = "X"
    qwm_doc.MeshX_E_71.Position = 72.23292
    qwm_doc.MeshX_E_71.Length = 5.143000000000001
    qwm_doc.MeshX_E_71.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_71.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_71.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_71.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_72")
    qwm_doc.MeshX_E_72.Placement = FreeCAD.Placement(FreeCAD.Vector(73.215, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_72.Orientation = "X"
    qwm_doc.MeshX_E_72.Position = 73.215
    qwm_doc.MeshX_E_72.Length = 5.143000000000001
    qwm_doc.MeshX_E_72.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_72.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_72.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_72.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_73")
    qwm_doc.MeshX_E_73.Placement = FreeCAD.Placement(FreeCAD.Vector(74.19708, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_73.Orientation = "X"
    qwm_doc.MeshX_E_73.Position = 74.19708
    qwm_doc.MeshX_E_73.Length = 5.143000000000001
    qwm_doc.MeshX_E_73.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_73.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_73.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_73.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_74")
    qwm_doc.MeshX_E_74.Placement = FreeCAD.Placement(FreeCAD.Vector(75.17917, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_74.Orientation = "X"
    qwm_doc.MeshX_E_74.Position = 75.17917
    qwm_doc.MeshX_E_74.Length = 5.143000000000001
    qwm_doc.MeshX_E_74.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_74.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_74.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_74.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_75")
    qwm_doc.MeshX_E_75.Placement = FreeCAD.Placement(FreeCAD.Vector(76.16125, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_75.Orientation = "X"
    qwm_doc.MeshX_E_75.Position = 76.16125
    qwm_doc.MeshX_E_75.Length = 5.143000000000001
    qwm_doc.MeshX_E_75.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_75.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_75.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_75.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_76")
    qwm_doc.MeshX_E_76.Placement = FreeCAD.Placement(FreeCAD.Vector(77.14333, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_76.Orientation = "X"
    qwm_doc.MeshX_E_76.Position = 77.14333
    qwm_doc.MeshX_E_76.Length = 5.143000000000001
    qwm_doc.MeshX_E_76.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_76.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_76.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_76.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_77")
    qwm_doc.MeshX_E_77.Placement = FreeCAD.Placement(FreeCAD.Vector(78.12542, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_77.Orientation = "X"
    qwm_doc.MeshX_E_77.Position = 78.12542
    qwm_doc.MeshX_E_77.Length = 5.143000000000001
    qwm_doc.MeshX_E_77.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_77.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_77.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_77.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_78")
    qwm_doc.MeshX_E_78.Placement = FreeCAD.Placement(FreeCAD.Vector(79.1075, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_78.Orientation = "X"
    qwm_doc.MeshX_E_78.Position = 79.1075
    qwm_doc.MeshX_E_78.Length = 5.143000000000001
    qwm_doc.MeshX_E_78.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_78.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_78.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_78.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_79")
    qwm_doc.MeshX_E_79.Placement = FreeCAD.Placement(FreeCAD.Vector(80.08958, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_79.Orientation = "X"
    qwm_doc.MeshX_E_79.Position = 80.08958
    qwm_doc.MeshX_E_79.Length = 5.143000000000001
    qwm_doc.MeshX_E_79.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_79.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_79.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_79.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_80")
    qwm_doc.MeshX_E_80.Placement = FreeCAD.Placement(FreeCAD.Vector(81.07167, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_80.Orientation = "X"
    qwm_doc.MeshX_E_80.Position = 81.07167
    qwm_doc.MeshX_E_80.Length = 5.143000000000001
    qwm_doc.MeshX_E_80.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_80.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_80.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_80.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_81")
    qwm_doc.MeshX_E_81.Placement = FreeCAD.Placement(FreeCAD.Vector(82.05375, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_81.Orientation = "X"
    qwm_doc.MeshX_E_81.Position = 82.05375
    qwm_doc.MeshX_E_81.Length = 5.143000000000001
    qwm_doc.MeshX_E_81.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_81.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_81.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_81.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_82")
    qwm_doc.MeshX_E_82.Placement = FreeCAD.Placement(FreeCAD.Vector(83.03583, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_82.Orientation = "X"
    qwm_doc.MeshX_E_82.Position = 83.03583
    qwm_doc.MeshX_E_82.Length = 5.143000000000001
    qwm_doc.MeshX_E_82.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_82.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_82.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_82.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_83")
    qwm_doc.MeshX_E_83.Placement = FreeCAD.Placement(FreeCAD.Vector(84.01792, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_83.Orientation = "X"
    qwm_doc.MeshX_E_83.Position = 84.01792
    qwm_doc.MeshX_E_83.Length = 5.143000000000001
    qwm_doc.MeshX_E_83.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_83.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_83.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_83.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_84")
    qwm_doc.MeshX_E_84.Placement = FreeCAD.Placement(FreeCAD.Vector(85.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_84.Orientation = "X"
    qwm_doc.MeshX_E_84.Position = 85.0
    qwm_doc.MeshX_E_84.Length = 5.143000000000001
    qwm_doc.MeshX_E_84.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_84.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_84.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_84.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_85")
    qwm_doc.MeshX_E_85.Placement = FreeCAD.Placement(FreeCAD.Vector(86.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_85.Orientation = "X"
    qwm_doc.MeshX_E_85.Position = 86.0
    qwm_doc.MeshX_E_85.Length = 5.143000000000001
    qwm_doc.MeshX_E_85.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_85.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_85.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_85.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_86")
    qwm_doc.MeshX_E_86.Placement = FreeCAD.Placement(FreeCAD.Vector(87.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_86.Orientation = "X"
    qwm_doc.MeshX_E_86.Position = 87.0
    qwm_doc.MeshX_E_86.Length = 5.143000000000001
    qwm_doc.MeshX_E_86.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_86.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_86.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_86.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_87")
    qwm_doc.MeshX_E_87.Placement = FreeCAD.Placement(FreeCAD.Vector(88.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_87.Orientation = "X"
    qwm_doc.MeshX_E_87.Position = 88.0
    qwm_doc.MeshX_E_87.Length = 5.143000000000001
    qwm_doc.MeshX_E_87.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_87.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_87.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_87.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_88")
    qwm_doc.MeshX_E_88.Placement = FreeCAD.Placement(FreeCAD.Vector(89.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_88.Orientation = "X"
    qwm_doc.MeshX_E_88.Position = 89.0
    qwm_doc.MeshX_E_88.Length = 5.143000000000001
    qwm_doc.MeshX_E_88.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_88.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_88.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_88.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_89")
    qwm_doc.MeshX_E_89.Placement = FreeCAD.Placement(FreeCAD.Vector(90.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_89.Orientation = "X"
    qwm_doc.MeshX_E_89.Position = 90.0
    qwm_doc.MeshX_E_89.Length = 5.143000000000001
    qwm_doc.MeshX_E_89.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_89.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_89.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_89.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_90")
    qwm_doc.MeshX_E_90.Placement = FreeCAD.Placement(FreeCAD.Vector(91.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_90.Orientation = "X"
    qwm_doc.MeshX_E_90.Position = 91.0
    qwm_doc.MeshX_E_90.Length = 5.143000000000001
    qwm_doc.MeshX_E_90.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_90.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_90.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_90.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_91")
    qwm_doc.MeshX_E_91.Placement = FreeCAD.Placement(FreeCAD.Vector(92.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_91.Orientation = "X"
    qwm_doc.MeshX_E_91.Position = 92.0
    qwm_doc.MeshX_E_91.Length = 5.143000000000001
    qwm_doc.MeshX_E_91.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_91.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_91.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_91.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_92")
    qwm_doc.MeshX_E_92.Placement = FreeCAD.Placement(FreeCAD.Vector(93.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_92.Orientation = "X"
    qwm_doc.MeshX_E_92.Position = 93.0
    qwm_doc.MeshX_E_92.Length = 5.143000000000001
    qwm_doc.MeshX_E_92.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_92.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_92.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_92.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_93")
    qwm_doc.MeshX_E_93.Placement = FreeCAD.Placement(FreeCAD.Vector(94.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_93.Orientation = "X"
    qwm_doc.MeshX_E_93.Position = 94.0
    qwm_doc.MeshX_E_93.Length = 5.143000000000001
    qwm_doc.MeshX_E_93.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_93.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_93.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_93.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_94")
    qwm_doc.MeshX_E_94.Placement = FreeCAD.Placement(FreeCAD.Vector(95.0, -37.4285, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_94.Orientation = "X"
    qwm_doc.MeshX_E_94.Position = 95.0
    qwm_doc.MeshX_E_94.Length = 5.143000000000001
    qwm_doc.MeshX_E_94.Width = 2.254
    FreeCAD.Gui.ActiveDocument.MeshX_E_94.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_94.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_94.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_1")
    qwm_doc.MeshY_E_1.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -40.0, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_1.Orientation = "Y"
    qwm_doc.MeshY_E_1.Position = -40.0
    qwm_doc.MeshY_E_1.Length = 2.254
    qwm_doc.MeshY_E_1.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_1.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_2")
    qwm_doc.MeshY_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -39.0, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_2.Orientation = "Y"
    qwm_doc.MeshY_E_2.Position = -39.0
    qwm_doc.MeshY_E_2.Length = 2.254
    qwm_doc.MeshY_E_2.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_3")
    qwm_doc.MeshY_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -38.0, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_3.Orientation = "Y"
    qwm_doc.MeshY_E_3.Position = -38.0
    qwm_doc.MeshY_E_3.Length = 2.254
    qwm_doc.MeshY_E_3.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_4")
    qwm_doc.MeshY_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.0, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_4.Orientation = "Y"
    qwm_doc.MeshY_E_4.Position = -37.0
    qwm_doc.MeshY_E_4.Length = 2.254
    qwm_doc.MeshY_E_4.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_5")
    qwm_doc.MeshY_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -36.0, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_5.Orientation = "Y"
    qwm_doc.MeshY_E_5.Position = -36.0
    qwm_doc.MeshY_E_5.Length = 2.254
    qwm_doc.MeshY_E_5.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_6")
    qwm_doc.MeshY_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -35.0, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_6.Orientation = "Y"
    qwm_doc.MeshY_E_6.Position = -35.0
    qwm_doc.MeshY_E_6.Length = 2.254
    qwm_doc.MeshY_E_6.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_7")
    qwm_doc.MeshY_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -34.0, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_7.Orientation = "Y"
    qwm_doc.MeshY_E_7.Position = -34.0
    qwm_doc.MeshY_E_7.Length = 2.254
    qwm_doc.MeshY_E_7.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_8")
    qwm_doc.MeshY_E_8.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -33.0, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_8.Orientation = "Y"
    qwm_doc.MeshY_E_8.Position = -33.0
    qwm_doc.MeshY_E_8.Length = 2.254
    qwm_doc.MeshY_E_8.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_8.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_8.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_8.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_9")
    qwm_doc.MeshY_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -32.0, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_9.Orientation = "Y"
    qwm_doc.MeshY_E_9.Position = -32.0
    qwm_doc.MeshY_E_9.Length = 2.254
    qwm_doc.MeshY_E_9.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_10")
    qwm_doc.MeshY_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -31.0, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_10.Orientation = "Y"
    qwm_doc.MeshY_E_10.Position = -31.0
    qwm_doc.MeshY_E_10.Length = 2.254
    qwm_doc.MeshY_E_10.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_11")
    qwm_doc.MeshY_E_11.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -30.0, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_11.Orientation = "Y"
    qwm_doc.MeshY_E_11.Position = -30.0
    qwm_doc.MeshY_E_11.Length = 2.254
    qwm_doc.MeshY_E_11.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_11.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_11.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_11.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_12")
    qwm_doc.MeshY_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -29.02263, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_12.Orientation = "Y"
    qwm_doc.MeshY_E_12.Position = -29.02263
    qwm_doc.MeshY_E_12.Length = 2.254
    qwm_doc.MeshY_E_12.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_13")
    qwm_doc.MeshY_E_13.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -28.04526, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_13.Orientation = "Y"
    qwm_doc.MeshY_E_13.Position = -28.04526
    qwm_doc.MeshY_E_13.Length = 2.254
    qwm_doc.MeshY_E_13.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_13.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_13.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_13.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_14")
    qwm_doc.MeshY_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -27.06789, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_14.Orientation = "Y"
    qwm_doc.MeshY_E_14.Position = -27.06789
    qwm_doc.MeshY_E_14.Length = 2.254
    qwm_doc.MeshY_E_14.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_15")
    qwm_doc.MeshY_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -26.09053, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_15.Orientation = "Y"
    qwm_doc.MeshY_E_15.Position = -26.09053
    qwm_doc.MeshY_E_15.Length = 2.254
    qwm_doc.MeshY_E_15.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_16")
    qwm_doc.MeshY_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -25.11316, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_16.Orientation = "Y"
    qwm_doc.MeshY_E_16.Position = -25.11316
    qwm_doc.MeshY_E_16.Length = 2.254
    qwm_doc.MeshY_E_16.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_17")
    qwm_doc.MeshY_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -24.13579, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_17.Orientation = "Y"
    qwm_doc.MeshY_E_17.Position = -24.13579
    qwm_doc.MeshY_E_17.Length = 2.254
    qwm_doc.MeshY_E_17.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_18")
    qwm_doc.MeshY_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -23.15842, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_18.Orientation = "Y"
    qwm_doc.MeshY_E_18.Position = -23.15842
    qwm_doc.MeshY_E_18.Length = 2.254
    qwm_doc.MeshY_E_18.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_19")
    qwm_doc.MeshY_E_19.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -22.18105, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_19.Orientation = "Y"
    qwm_doc.MeshY_E_19.Position = -22.18105
    qwm_doc.MeshY_E_19.Length = 2.254
    qwm_doc.MeshY_E_19.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_19.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_19.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_19.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_20")
    qwm_doc.MeshY_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -21.20368, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_20.Orientation = "Y"
    qwm_doc.MeshY_E_20.Position = -21.20368
    qwm_doc.MeshY_E_20.Length = 2.254
    qwm_doc.MeshY_E_20.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_21")
    qwm_doc.MeshY_E_21.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -20.22632, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_21.Orientation = "Y"
    qwm_doc.MeshY_E_21.Position = -20.22632
    qwm_doc.MeshY_E_21.Length = 2.254
    qwm_doc.MeshY_E_21.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_21.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_21.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_21.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_22")
    qwm_doc.MeshY_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -19.24895, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_22.Orientation = "Y"
    qwm_doc.MeshY_E_22.Position = -19.24895
    qwm_doc.MeshY_E_22.Length = 2.254
    qwm_doc.MeshY_E_22.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_23")
    qwm_doc.MeshY_E_23.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -18.27158, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_23.Orientation = "Y"
    qwm_doc.MeshY_E_23.Position = -18.27158
    qwm_doc.MeshY_E_23.Length = 2.254
    qwm_doc.MeshY_E_23.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_23.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_23.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_23.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_24")
    qwm_doc.MeshY_E_24.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -17.29421, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_24.Orientation = "Y"
    qwm_doc.MeshY_E_24.Position = -17.29421
    qwm_doc.MeshY_E_24.Length = 2.254
    qwm_doc.MeshY_E_24.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_24.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_24.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_24.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_25")
    qwm_doc.MeshY_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -16.31684, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_25.Orientation = "Y"
    qwm_doc.MeshY_E_25.Position = -16.31684
    qwm_doc.MeshY_E_25.Length = 2.254
    qwm_doc.MeshY_E_25.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_26")
    qwm_doc.MeshY_E_26.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -15.33947, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_26.Orientation = "Y"
    qwm_doc.MeshY_E_26.Position = -15.33947
    qwm_doc.MeshY_E_26.Length = 2.254
    qwm_doc.MeshY_E_26.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_26.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_26.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_26.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_27")
    qwm_doc.MeshY_E_27.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -14.36211, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_27.Orientation = "Y"
    qwm_doc.MeshY_E_27.Position = -14.36211
    qwm_doc.MeshY_E_27.Length = 2.254
    qwm_doc.MeshY_E_27.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_27.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_27.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_27.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_28")
    qwm_doc.MeshY_E_28.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -13.38474, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_28.Orientation = "Y"
    qwm_doc.MeshY_E_28.Position = -13.38474
    qwm_doc.MeshY_E_28.Length = 2.254
    qwm_doc.MeshY_E_28.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_28.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_28.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_28.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_29")
    qwm_doc.MeshY_E_29.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -12.40737, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_29.Orientation = "Y"
    qwm_doc.MeshY_E_29.Position = -12.40737
    qwm_doc.MeshY_E_29.Length = 2.254
    qwm_doc.MeshY_E_29.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_29.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_29.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_29.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_30")
    qwm_doc.MeshY_E_30.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -11.43, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_30.Orientation = "Y"
    qwm_doc.MeshY_E_30.Position = -11.43
    qwm_doc.MeshY_E_30.Length = 2.254
    qwm_doc.MeshY_E_30.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_30.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_30.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_30.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_31")
    qwm_doc.MeshY_E_31.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -10.43609, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_31.Orientation = "Y"
    qwm_doc.MeshY_E_31.Position = -10.43609
    qwm_doc.MeshY_E_31.Length = 2.254
    qwm_doc.MeshY_E_31.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_31.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_31.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_31.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_32")
    qwm_doc.MeshY_E_32.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -9.44217, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_32.Orientation = "Y"
    qwm_doc.MeshY_E_32.Position = -9.44217
    qwm_doc.MeshY_E_32.Length = 2.254
    qwm_doc.MeshY_E_32.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_32.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_32.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_32.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_33")
    qwm_doc.MeshY_E_33.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -8.44826, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_33.Orientation = "Y"
    qwm_doc.MeshY_E_33.Position = -8.44826
    qwm_doc.MeshY_E_33.Length = 2.254
    qwm_doc.MeshY_E_33.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_33.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_33.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_33.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_34")
    qwm_doc.MeshY_E_34.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -7.45435, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_34.Orientation = "Y"
    qwm_doc.MeshY_E_34.Position = -7.45435
    qwm_doc.MeshY_E_34.Length = 2.254
    qwm_doc.MeshY_E_34.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_34.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_34.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_34.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_35")
    qwm_doc.MeshY_E_35.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -6.46043, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_35.Orientation = "Y"
    qwm_doc.MeshY_E_35.Position = -6.46043
    qwm_doc.MeshY_E_35.Length = 2.254
    qwm_doc.MeshY_E_35.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_35.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_35.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_35.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_36")
    qwm_doc.MeshY_E_36.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -5.46652, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_36.Orientation = "Y"
    qwm_doc.MeshY_E_36.Position = -5.46652
    qwm_doc.MeshY_E_36.Length = 2.254
    qwm_doc.MeshY_E_36.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_36.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_36.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_36.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_37")
    qwm_doc.MeshY_E_37.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -4.47261, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_37.Orientation = "Y"
    qwm_doc.MeshY_E_37.Position = -4.47261
    qwm_doc.MeshY_E_37.Length = 2.254
    qwm_doc.MeshY_E_37.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_37.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_37.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_37.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_38")
    qwm_doc.MeshY_E_38.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -3.4787, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_38.Orientation = "Y"
    qwm_doc.MeshY_E_38.Position = -3.4787
    qwm_doc.MeshY_E_38.Length = 2.254
    qwm_doc.MeshY_E_38.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_38.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_38.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_38.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_39")
    qwm_doc.MeshY_E_39.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -2.48478, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_39.Orientation = "Y"
    qwm_doc.MeshY_E_39.Position = -2.48478
    qwm_doc.MeshY_E_39.Length = 2.254
    qwm_doc.MeshY_E_39.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_39.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_39.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_39.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_40")
    qwm_doc.MeshY_E_40.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -1.49087, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_40.Orientation = "Y"
    qwm_doc.MeshY_E_40.Position = -1.49087
    qwm_doc.MeshY_E_40.Length = 2.254
    qwm_doc.MeshY_E_40.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_40.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_40.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_40.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_41")
    qwm_doc.MeshY_E_41.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -0.49696, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_41.Orientation = "Y"
    qwm_doc.MeshY_E_41.Position = -0.49696
    qwm_doc.MeshY_E_41.Length = 2.254
    qwm_doc.MeshY_E_41.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_41.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_41.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_41.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_42")
    qwm_doc.MeshY_E_42.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 0.49696, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_42.Orientation = "Y"
    qwm_doc.MeshY_E_42.Position = 0.49696
    qwm_doc.MeshY_E_42.Length = 2.254
    qwm_doc.MeshY_E_42.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_42.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_42.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_42.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_43")
    qwm_doc.MeshY_E_43.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 1.49087, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_43.Orientation = "Y"
    qwm_doc.MeshY_E_43.Position = 1.49087
    qwm_doc.MeshY_E_43.Length = 2.254
    qwm_doc.MeshY_E_43.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_43.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_43.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_43.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_44")
    qwm_doc.MeshY_E_44.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 2.48478, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_44.Orientation = "Y"
    qwm_doc.MeshY_E_44.Position = 2.48478
    qwm_doc.MeshY_E_44.Length = 2.254
    qwm_doc.MeshY_E_44.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_44.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_44.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_44.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_45")
    qwm_doc.MeshY_E_45.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 3.4787, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_45.Orientation = "Y"
    qwm_doc.MeshY_E_45.Position = 3.4787
    qwm_doc.MeshY_E_45.Length = 2.254
    qwm_doc.MeshY_E_45.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_45.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_45.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_45.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_46")
    qwm_doc.MeshY_E_46.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 4.47261, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_46.Orientation = "Y"
    qwm_doc.MeshY_E_46.Position = 4.47261
    qwm_doc.MeshY_E_46.Length = 2.254
    qwm_doc.MeshY_E_46.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_46.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_46.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_46.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_47")
    qwm_doc.MeshY_E_47.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 5.46652, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_47.Orientation = "Y"
    qwm_doc.MeshY_E_47.Position = 5.46652
    qwm_doc.MeshY_E_47.Length = 2.254
    qwm_doc.MeshY_E_47.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_47.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_47.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_47.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_48")
    qwm_doc.MeshY_E_48.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 6.46043, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_48.Orientation = "Y"
    qwm_doc.MeshY_E_48.Position = 6.46043
    qwm_doc.MeshY_E_48.Length = 2.254
    qwm_doc.MeshY_E_48.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_48.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_48.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_48.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_49")
    qwm_doc.MeshY_E_49.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 7.45435, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_49.Orientation = "Y"
    qwm_doc.MeshY_E_49.Position = 7.45435
    qwm_doc.MeshY_E_49.Length = 2.254
    qwm_doc.MeshY_E_49.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_49.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_49.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_49.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_50")
    qwm_doc.MeshY_E_50.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 8.44826, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_50.Orientation = "Y"
    qwm_doc.MeshY_E_50.Position = 8.44826
    qwm_doc.MeshY_E_50.Length = 2.254
    qwm_doc.MeshY_E_50.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_50.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_50.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_50.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_51")
    qwm_doc.MeshY_E_51.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 9.44217, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_51.Orientation = "Y"
    qwm_doc.MeshY_E_51.Position = 9.44217
    qwm_doc.MeshY_E_51.Length = 2.254
    qwm_doc.MeshY_E_51.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_51.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_51.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_51.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_52")
    qwm_doc.MeshY_E_52.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 10.43609, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_52.Orientation = "Y"
    qwm_doc.MeshY_E_52.Position = 10.43609
    qwm_doc.MeshY_E_52.Length = 2.254
    qwm_doc.MeshY_E_52.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_52.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_52.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_52.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_53")
    qwm_doc.MeshY_E_53.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, 11.43, -3.9530000000000003),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_53.Orientation = "Y"
    qwm_doc.MeshY_E_53.Position = 11.43
    qwm_doc.MeshY_E_53.Length = 2.254
    qwm_doc.MeshY_E_53.Width = 9.0
    FreeCAD.Gui.ActiveDocument.MeshY_E_53.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_53.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_53.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_1")
    qwm_doc.MeshZ_E_1.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, -5.08),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_1.Orientation = "Z"
    qwm_doc.MeshZ_E_1.Position = -5.08
    qwm_doc.MeshZ_E_1.Length = 9.0
    qwm_doc.MeshZ_E_1.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_1.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_2")
    qwm_doc.MeshZ_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, -4.15636),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_2.Orientation = "Z"
    qwm_doc.MeshZ_E_2.Position = -4.15636
    qwm_doc.MeshZ_E_2.Length = 9.0
    qwm_doc.MeshZ_E_2.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_3")
    qwm_doc.MeshZ_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, -3.23273),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_3.Orientation = "Z"
    qwm_doc.MeshZ_E_3.Position = -3.23273
    qwm_doc.MeshZ_E_3.Length = 9.0
    qwm_doc.MeshZ_E_3.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_4")
    qwm_doc.MeshZ_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, -2.30909),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_4.Orientation = "Z"
    qwm_doc.MeshZ_E_4.Position = -2.30909
    qwm_doc.MeshZ_E_4.Length = 9.0
    qwm_doc.MeshZ_E_4.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_5")
    qwm_doc.MeshZ_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, -1.38545),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_5.Orientation = "Z"
    qwm_doc.MeshZ_E_5.Position = -1.38545
    qwm_doc.MeshZ_E_5.Length = 9.0
    qwm_doc.MeshZ_E_5.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_6")
    qwm_doc.MeshZ_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, -0.46182),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_6.Orientation = "Z"
    qwm_doc.MeshZ_E_6.Position = -0.46182
    qwm_doc.MeshZ_E_6.Length = 9.0
    qwm_doc.MeshZ_E_6.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_7")
    qwm_doc.MeshZ_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 0.46182),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_7.Orientation = "Z"
    qwm_doc.MeshZ_E_7.Position = 0.46182
    qwm_doc.MeshZ_E_7.Length = 9.0
    qwm_doc.MeshZ_E_7.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_8")
    qwm_doc.MeshZ_E_8.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 1.38545),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_8.Orientation = "Z"
    qwm_doc.MeshZ_E_8.Position = 1.38545
    qwm_doc.MeshZ_E_8.Length = 9.0
    qwm_doc.MeshZ_E_8.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_8.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_8.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_8.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_9")
    qwm_doc.MeshZ_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 2.30909),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_9.Orientation = "Z"
    qwm_doc.MeshZ_E_9.Position = 2.30909
    qwm_doc.MeshZ_E_9.Length = 9.0
    qwm_doc.MeshZ_E_9.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_10")
    qwm_doc.MeshZ_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 3.23273),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_10.Orientation = "Z"
    qwm_doc.MeshZ_E_10.Position = 3.23273
    qwm_doc.MeshZ_E_10.Length = 9.0
    qwm_doc.MeshZ_E_10.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_11")
    qwm_doc.MeshZ_E_11.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 4.15636),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_11.Orientation = "Z"
    qwm_doc.MeshZ_E_11.Position = 4.15636
    qwm_doc.MeshZ_E_11.Length = 9.0
    qwm_doc.MeshZ_E_11.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_11.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_11.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_11.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_12")
    qwm_doc.MeshZ_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 5.08),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_12.Orientation = "Z"
    qwm_doc.MeshZ_E_12.Position = 5.08
    qwm_doc.MeshZ_E_12.Length = 9.0
    qwm_doc.MeshZ_E_12.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_13")
    qwm_doc.MeshZ_E_13.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 6.0768),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_13.Orientation = "Z"
    qwm_doc.MeshZ_E_13.Position = 6.0768
    qwm_doc.MeshZ_E_13.Length = 9.0
    qwm_doc.MeshZ_E_13.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_13.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_13.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_13.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_14")
    qwm_doc.MeshZ_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 7.0736),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_14.Orientation = "Z"
    qwm_doc.MeshZ_E_14.Position = 7.0736
    qwm_doc.MeshZ_E_14.Length = 9.0
    qwm_doc.MeshZ_E_14.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_15")
    qwm_doc.MeshZ_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 8.0704),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_15.Orientation = "Z"
    qwm_doc.MeshZ_E_15.Position = 8.0704
    qwm_doc.MeshZ_E_15.Length = 9.0
    qwm_doc.MeshZ_E_15.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_16")
    qwm_doc.MeshZ_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 9.0672),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_16.Orientation = "Z"
    qwm_doc.MeshZ_E_16.Position = 9.0672
    qwm_doc.MeshZ_E_16.Length = 9.0
    qwm_doc.MeshZ_E_16.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_17")
    qwm_doc.MeshZ_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 10.064),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_17.Orientation = "Z"
    qwm_doc.MeshZ_E_17.Position = 10.064
    qwm_doc.MeshZ_E_17.Length = 9.0
    qwm_doc.MeshZ_E_17.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_18")
    qwm_doc.MeshZ_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 11.0608),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_18.Orientation = "Z"
    qwm_doc.MeshZ_E_18.Position = 11.0608
    qwm_doc.MeshZ_E_18.Length = 9.0
    qwm_doc.MeshZ_E_18.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_19")
    qwm_doc.MeshZ_E_19.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 12.0576),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_19.Orientation = "Z"
    qwm_doc.MeshZ_E_19.Position = 12.0576
    qwm_doc.MeshZ_E_19.Length = 9.0
    qwm_doc.MeshZ_E_19.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_19.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_19.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_19.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_20")
    qwm_doc.MeshZ_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 13.0544),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_20.Orientation = "Z"
    qwm_doc.MeshZ_E_20.Position = 13.0544
    qwm_doc.MeshZ_E_20.Length = 9.0
    qwm_doc.MeshZ_E_20.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_21")
    qwm_doc.MeshZ_E_21.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 14.0512),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_21.Orientation = "Z"
    qwm_doc.MeshZ_E_21.Position = 14.0512
    qwm_doc.MeshZ_E_21.Length = 9.0
    qwm_doc.MeshZ_E_21.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_21.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_21.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_21.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_22")
    qwm_doc.MeshZ_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 15.048),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_22.Orientation = "Z"
    qwm_doc.MeshZ_E_22.Position = 15.048
    qwm_doc.MeshZ_E_22.Length = 9.0
    qwm_doc.MeshZ_E_22.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_23")
    qwm_doc.MeshZ_E_23.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 16.0448),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_23.Orientation = "Z"
    qwm_doc.MeshZ_E_23.Position = 16.0448
    qwm_doc.MeshZ_E_23.Length = 9.0
    qwm_doc.MeshZ_E_23.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_23.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_23.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_23.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_24")
    qwm_doc.MeshZ_E_24.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 17.0416),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_24.Orientation = "Z"
    qwm_doc.MeshZ_E_24.Position = 17.0416
    qwm_doc.MeshZ_E_24.Length = 9.0
    qwm_doc.MeshZ_E_24.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_24.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_24.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_24.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_25")
    qwm_doc.MeshZ_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 18.0384),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_25.Orientation = "Z"
    qwm_doc.MeshZ_E_25.Position = 18.0384
    qwm_doc.MeshZ_E_25.Length = 9.0
    qwm_doc.MeshZ_E_25.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_26")
    qwm_doc.MeshZ_E_26.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 19.0352),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_26.Orientation = "Z"
    qwm_doc.MeshZ_E_26.Position = 19.0352
    qwm_doc.MeshZ_E_26.Length = 9.0
    qwm_doc.MeshZ_E_26.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_26.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_26.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_26.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_27")
    qwm_doc.MeshZ_E_27.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 20.032),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_27.Orientation = "Z"
    qwm_doc.MeshZ_E_27.Position = 20.032
    qwm_doc.MeshZ_E_27.Length = 9.0
    qwm_doc.MeshZ_E_27.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_27.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_27.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_27.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_28")
    qwm_doc.MeshZ_E_28.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 21.0288),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_28.Orientation = "Z"
    qwm_doc.MeshZ_E_28.Position = 21.0288
    qwm_doc.MeshZ_E_28.Length = 9.0
    qwm_doc.MeshZ_E_28.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_28.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_28.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_28.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_29")
    qwm_doc.MeshZ_E_29.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 22.0256),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_29.Orientation = "Z"
    qwm_doc.MeshZ_E_29.Position = 22.0256
    qwm_doc.MeshZ_E_29.Length = 9.0
    qwm_doc.MeshZ_E_29.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_29.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_29.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_29.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_30")
    qwm_doc.MeshZ_E_30.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 23.0224),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_30.Orientation = "Z"
    qwm_doc.MeshZ_E_30.Position = 23.0224
    qwm_doc.MeshZ_E_30.Length = 9.0
    qwm_doc.MeshZ_E_30.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_30.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_30.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_30.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_31")
    qwm_doc.MeshZ_E_31.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 24.0192),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_31.Orientation = "Z"
    qwm_doc.MeshZ_E_31.Position = 24.0192
    qwm_doc.MeshZ_E_31.Length = 9.0
    qwm_doc.MeshZ_E_31.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_31.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_31.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_31.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_32")
    qwm_doc.MeshZ_E_32.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 25.016),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_32.Orientation = "Z"
    qwm_doc.MeshZ_E_32.Position = 25.016
    qwm_doc.MeshZ_E_32.Length = 9.0
    qwm_doc.MeshZ_E_32.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_32.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_32.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_32.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_33")
    qwm_doc.MeshZ_E_33.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 26.0128),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_33.Orientation = "Z"
    qwm_doc.MeshZ_E_33.Position = 26.0128
    qwm_doc.MeshZ_E_33.Length = 9.0
    qwm_doc.MeshZ_E_33.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_33.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_33.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_33.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_34")
    qwm_doc.MeshZ_E_34.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 27.0096),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_34.Orientation = "Z"
    qwm_doc.MeshZ_E_34.Position = 27.0096
    qwm_doc.MeshZ_E_34.Length = 9.0
    qwm_doc.MeshZ_E_34.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_34.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_34.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_34.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_35")
    qwm_doc.MeshZ_E_35.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 28.0064),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_35.Orientation = "Z"
    qwm_doc.MeshZ_E_35.Position = 28.0064
    qwm_doc.MeshZ_E_35.Length = 9.0
    qwm_doc.MeshZ_E_35.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_35.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_35.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_35.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_36")
    qwm_doc.MeshZ_E_36.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 29.0032),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_36.Orientation = "Z"
    qwm_doc.MeshZ_E_36.Position = 29.0032
    qwm_doc.MeshZ_E_36.Length = 9.0
    qwm_doc.MeshZ_E_36.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_36.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_36.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_36.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_37")
    qwm_doc.MeshZ_E_37.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 30.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_37.Orientation = "Z"
    qwm_doc.MeshZ_E_37.Position = 30.0
    qwm_doc.MeshZ_E_37.Length = 9.0
    qwm_doc.MeshZ_E_37.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_37.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_37.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_37.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_38")
    qwm_doc.MeshZ_E_38.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 31.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_38.Orientation = "Z"
    qwm_doc.MeshZ_E_38.Position = 31.0
    qwm_doc.MeshZ_E_38.Length = 9.0
    qwm_doc.MeshZ_E_38.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_38.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_38.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_38.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_39")
    qwm_doc.MeshZ_E_39.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 32.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_39.Orientation = "Z"
    qwm_doc.MeshZ_E_39.Position = 32.0
    qwm_doc.MeshZ_E_39.Length = 9.0
    qwm_doc.MeshZ_E_39.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_39.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_39.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_39.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_40")
    qwm_doc.MeshZ_E_40.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 33.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_40.Orientation = "Z"
    qwm_doc.MeshZ_E_40.Position = 33.0
    qwm_doc.MeshZ_E_40.Length = 9.0
    qwm_doc.MeshZ_E_40.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_40.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_40.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_40.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_41")
    qwm_doc.MeshZ_E_41.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 34.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_41.Orientation = "Z"
    qwm_doc.MeshZ_E_41.Position = 34.0
    qwm_doc.MeshZ_E_41.Length = 9.0
    qwm_doc.MeshZ_E_41.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_41.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_41.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_41.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_42")
    qwm_doc.MeshZ_E_42.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 35.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_42.Orientation = "Z"
    qwm_doc.MeshZ_E_42.Position = 35.0
    qwm_doc.MeshZ_E_42.Length = 9.0
    qwm_doc.MeshZ_E_42.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_42.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_42.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_42.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_43")
    qwm_doc.MeshZ_E_43.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 36.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_43.Orientation = "Z"
    qwm_doc.MeshZ_E_43.Position = 36.0
    qwm_doc.MeshZ_E_43.Length = 9.0
    qwm_doc.MeshZ_E_43.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_43.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_43.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_43.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_44")
    qwm_doc.MeshZ_E_44.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 37.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_44.Orientation = "Z"
    qwm_doc.MeshZ_E_44.Position = 37.0
    qwm_doc.MeshZ_E_44.Length = 9.0
    qwm_doc.MeshZ_E_44.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_44.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_44.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_44.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_45")
    qwm_doc.MeshZ_E_45.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 38.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_45.Orientation = "Z"
    qwm_doc.MeshZ_E_45.Position = 38.0
    qwm_doc.MeshZ_E_45.Length = 9.0
    qwm_doc.MeshZ_E_45.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_45.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_45.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_45.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_46")
    qwm_doc.MeshZ_E_46.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 39.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_46.Orientation = "Z"
    qwm_doc.MeshZ_E_46.Position = 39.0
    qwm_doc.MeshZ_E_46.Length = 9.0
    qwm_doc.MeshZ_E_46.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_46.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_46.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_46.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_47")
    qwm_doc.MeshZ_E_47.Placement = FreeCAD.Placement(FreeCAD.Vector(9.5, -37.4285, 40.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_47.Orientation = "Z"
    qwm_doc.MeshZ_E_47.Position = 40.0
    qwm_doc.MeshZ_E_47.Length = 9.0
    qwm_doc.MeshZ_E_47.Width = 5.143000000000001
    FreeCAD.Gui.ActiveDocument.MeshZ_E_47.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_47.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_47.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","Input")
    qwm_doc.Input.Length = 22.86
    qwm_doc.Input.Width = 10.16
    qwm_doc.Input.Placement = FreeCAD.Placement(FreeCAD.Vector(5.0, 0.0, 0.0), FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.Input.Orientation = "X"
    qwm_doc.Input.Position = 5.0
    qwm_doc.Input.Activity = "PLUS"
    qwm_doc.Input.Type = "Source"
    qwm_doc.Input.SymmetryH = False
    qwm_doc.Input.SymmetryV = False
    qwm_doc.Input.PointCoordX = 5.0
    qwm_doc.Input.PointCoordY = 0.0
    qwm_doc.Input.PointCoordZ = 0.0
    qwm_doc.Input.effectivePermitivityMode = "AUTO"
    qwm_doc.Input.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('pulse of spectrum f1<f<f2',5.0,15.0,3.0),1.0,0.0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),0.570039,50,1,0))
    qwm_doc.Input.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.Input.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.Input.ReferenceOffset = abs(qwm_doc.Input.PointCoordX - 10.0)
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","Output")
    qwm_doc.Output.Length = 22.86
    qwm_doc.Output.Width = 10.16
    qwm_doc.Output.Placement = FreeCAD.Placement(FreeCAD.Vector(95.0, 0.0, 0.0), FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.Output.Orientation = "X"
    qwm_doc.Output.Position = 95.0
    qwm_doc.Output.Activity = "MINUS"
    qwm_doc.Output.Type = "Load"
    qwm_doc.Output.SymmetryH = False
    qwm_doc.Output.SymmetryV = False
    qwm_doc.Output.PointCoordX = 95.0
    qwm_doc.Output.PointCoordY = 0.0
    qwm_doc.Output.PointCoordZ = 0.0
    qwm_doc.Output.effectivePermitivityMode = "AUTO"
    qwm_doc.Output.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('pulse of spectrum f1<f<f2',5.0,15.0,3.0),1.0,0.0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),0.570039,50,1,0))
    qwm_doc.Output.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.Output.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.Output.ReferenceOffset = abs(qwm_doc.Output.PointCoordX - 90.0)
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","Arm_H")
    qwm_doc.Arm_H.Length = 10.16
    qwm_doc.Arm_H.Width = 22.86
    qwm_doc.Arm_H.Placement = FreeCAD.Placement(FreeCAD.Vector(50.0, -40.0, 0.0), FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.Arm_H.Orientation = "Y"
    qwm_doc.Arm_H.Position = -40.0
    qwm_doc.Arm_H.Activity = "PLUS"
    qwm_doc.Arm_H.Type = "Load"
    qwm_doc.Arm_H.SymmetryH = False
    qwm_doc.Arm_H.SymmetryV = False
    qwm_doc.Arm_H.PointCoordX = 50.0
    qwm_doc.Arm_H.PointCoordY = -40.0
    qwm_doc.Arm_H.PointCoordZ = 0.0
    qwm_doc.Arm_H.effectivePermitivityMode = "AUTO"
    qwm_doc.Arm_H.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('pulse of spectrum f1<f<f2',5.0,15.0,3.0),1.0,0.0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),0.570039,50,1,0))
    qwm_doc.Arm_H.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.Arm_H.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.Arm_H.ReferenceOffset = abs(qwm_doc.Arm_H.PointCoordY - 0.0)
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","Arm_E")
    qwm_doc.Arm_E.Length = 10.159999999999997
    qwm_doc.Arm_E.Width = 22.86
    qwm_doc.Arm_E.Placement = FreeCAD.Placement(FreeCAD.Vector(50.0, 0.0, 40.0), FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.Arm_E.Orientation = "Z"
    qwm_doc.Arm_E.Position = 40.0
    qwm_doc.Arm_E.Activity = "MINUS"
    qwm_doc.Arm_E.Type = "Load"
    qwm_doc.Arm_E.SymmetryH = False
    qwm_doc.Arm_E.SymmetryV = False
    qwm_doc.Arm_E.PointCoordX = 50.0
    qwm_doc.Arm_E.PointCoordY = 0.0
    qwm_doc.Arm_E.PointCoordZ = 40.0
    qwm_doc.Arm_E.effectivePermitivityMode = "AUTO"
    qwm_doc.Arm_E.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('pulse of spectrum f1<f<f2',5.0,15.0,3.0),1.0,0.0,1,0),'TEM','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(10,0.2),(9,11,0.01),0.570039,50,1,0))
    qwm_doc.Arm_E.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.Arm_E.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.Arm_E.ReferenceOffset = abs(qwm_doc.Arm_E.PointCoordZ - 35.0)
