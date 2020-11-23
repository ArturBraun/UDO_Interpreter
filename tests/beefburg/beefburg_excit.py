
from FreeCAD import Base
import QW_Modeller
from qw_project import *
from qw_units import *


def set_Excitation(qwm_doc):
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_1")
    qwm_doc.MeshX_E_1.Placement = FreeCAD.Placement(FreeCAD.Vector(-133.5, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_1.Orientation = "X"
    qwm_doc.MeshX_E_1.Position = -133.5
    qwm_doc.MeshX_E_1.Length = 27.0
    qwm_doc.MeshX_E_1.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_1.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_2")
    qwm_doc.MeshX_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(-131.86364, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_2.Orientation = "X"
    qwm_doc.MeshX_E_2.Position = -131.86364
    qwm_doc.MeshX_E_2.Length = 27.0
    qwm_doc.MeshX_E_2.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_3")
    qwm_doc.MeshX_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(-130.22727, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_3.Orientation = "X"
    qwm_doc.MeshX_E_3.Position = -130.22727
    qwm_doc.MeshX_E_3.Length = 27.0
    qwm_doc.MeshX_E_3.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_4")
    qwm_doc.MeshX_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(-128.59091, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_4.Orientation = "X"
    qwm_doc.MeshX_E_4.Position = -128.59091
    qwm_doc.MeshX_E_4.Length = 27.0
    qwm_doc.MeshX_E_4.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_5")
    qwm_doc.MeshX_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(-126.95455, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_5.Orientation = "X"
    qwm_doc.MeshX_E_5.Position = -126.95455
    qwm_doc.MeshX_E_5.Length = 27.0
    qwm_doc.MeshX_E_5.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_6")
    qwm_doc.MeshX_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(-125.31818, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_6.Orientation = "X"
    qwm_doc.MeshX_E_6.Position = -125.31818
    qwm_doc.MeshX_E_6.Length = 27.0
    qwm_doc.MeshX_E_6.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_7")
    qwm_doc.MeshX_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(-123.68182, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_7.Orientation = "X"
    qwm_doc.MeshX_E_7.Position = -123.68182
    qwm_doc.MeshX_E_7.Length = 27.0
    qwm_doc.MeshX_E_7.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_8")
    qwm_doc.MeshX_E_8.Placement = FreeCAD.Placement(FreeCAD.Vector(-122.04545, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_8.Orientation = "X"
    qwm_doc.MeshX_E_8.Position = -122.04545
    qwm_doc.MeshX_E_8.Length = 27.0
    qwm_doc.MeshX_E_8.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_8.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_8.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_8.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_9")
    qwm_doc.MeshX_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.40909, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_9.Orientation = "X"
    qwm_doc.MeshX_E_9.Position = -120.40909
    qwm_doc.MeshX_E_9.Length = 27.0
    qwm_doc.MeshX_E_9.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_10")
    qwm_doc.MeshX_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(-118.77273, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_10.Orientation = "X"
    qwm_doc.MeshX_E_10.Position = -118.77273
    qwm_doc.MeshX_E_10.Length = 27.0
    qwm_doc.MeshX_E_10.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_11")
    qwm_doc.MeshX_E_11.Placement = FreeCAD.Placement(FreeCAD.Vector(-117.13636, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_11.Orientation = "X"
    qwm_doc.MeshX_E_11.Position = -117.13636
    qwm_doc.MeshX_E_11.Length = 27.0
    qwm_doc.MeshX_E_11.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_11.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_11.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_11.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_12")
    qwm_doc.MeshX_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(-115.5, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_12.Orientation = "X"
    qwm_doc.MeshX_E_12.Position = -115.5
    qwm_doc.MeshX_E_12.Length = 27.0
    qwm_doc.MeshX_E_12.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_13")
    qwm_doc.MeshX_E_13.Placement = FreeCAD.Placement(FreeCAD.Vector(-114.5, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_13.Orientation = "X"
    qwm_doc.MeshX_E_13.Position = -114.5
    qwm_doc.MeshX_E_13.Length = 27.0
    qwm_doc.MeshX_E_13.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_13.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_13.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_13.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_14")
    qwm_doc.MeshX_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(-113.5, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_14.Orientation = "X"
    qwm_doc.MeshX_E_14.Position = -113.5
    qwm_doc.MeshX_E_14.Length = 27.0
    qwm_doc.MeshX_E_14.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_15")
    qwm_doc.MeshX_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(-111.82813, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_15.Orientation = "X"
    qwm_doc.MeshX_E_15.Position = -111.82813
    qwm_doc.MeshX_E_15.Length = 27.0
    qwm_doc.MeshX_E_15.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_16")
    qwm_doc.MeshX_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(-110.15625, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_16.Orientation = "X"
    qwm_doc.MeshX_E_16.Position = -110.15625
    qwm_doc.MeshX_E_16.Length = 27.0
    qwm_doc.MeshX_E_16.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_17")
    qwm_doc.MeshX_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(-108.48438, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_17.Orientation = "X"
    qwm_doc.MeshX_E_17.Position = -108.48438
    qwm_doc.MeshX_E_17.Length = 27.0
    qwm_doc.MeshX_E_17.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_18")
    qwm_doc.MeshX_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(-106.8125, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_18.Orientation = "X"
    qwm_doc.MeshX_E_18.Position = -106.8125
    qwm_doc.MeshX_E_18.Length = 27.0
    qwm_doc.MeshX_E_18.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_19")
    qwm_doc.MeshX_E_19.Placement = FreeCAD.Placement(FreeCAD.Vector(-105.14063, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_19.Orientation = "X"
    qwm_doc.MeshX_E_19.Position = -105.14063
    qwm_doc.MeshX_E_19.Length = 27.0
    qwm_doc.MeshX_E_19.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_19.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_19.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_19.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_20")
    qwm_doc.MeshX_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(-103.46875, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_20.Orientation = "X"
    qwm_doc.MeshX_E_20.Position = -103.46875
    qwm_doc.MeshX_E_20.Length = 27.0
    qwm_doc.MeshX_E_20.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_21")
    qwm_doc.MeshX_E_21.Placement = FreeCAD.Placement(FreeCAD.Vector(-101.79688, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_21.Orientation = "X"
    qwm_doc.MeshX_E_21.Position = -101.79688
    qwm_doc.MeshX_E_21.Length = 27.0
    qwm_doc.MeshX_E_21.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_21.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_21.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_21.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_22")
    qwm_doc.MeshX_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(-100.125, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_22.Orientation = "X"
    qwm_doc.MeshX_E_22.Position = -100.125
    qwm_doc.MeshX_E_22.Length = 27.0
    qwm_doc.MeshX_E_22.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_23")
    qwm_doc.MeshX_E_23.Placement = FreeCAD.Placement(FreeCAD.Vector(-98.45313, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_23.Orientation = "X"
    qwm_doc.MeshX_E_23.Position = -98.45313
    qwm_doc.MeshX_E_23.Length = 27.0
    qwm_doc.MeshX_E_23.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_23.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_23.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_23.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_24")
    qwm_doc.MeshX_E_24.Placement = FreeCAD.Placement(FreeCAD.Vector(-96.78125, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_24.Orientation = "X"
    qwm_doc.MeshX_E_24.Position = -96.78125
    qwm_doc.MeshX_E_24.Length = 27.0
    qwm_doc.MeshX_E_24.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_24.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_24.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_24.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_25")
    qwm_doc.MeshX_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(-95.10938, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_25.Orientation = "X"
    qwm_doc.MeshX_E_25.Position = -95.10938
    qwm_doc.MeshX_E_25.Length = 27.0
    qwm_doc.MeshX_E_25.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_26")
    qwm_doc.MeshX_E_26.Placement = FreeCAD.Placement(FreeCAD.Vector(-93.4375, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_26.Orientation = "X"
    qwm_doc.MeshX_E_26.Position = -93.4375
    qwm_doc.MeshX_E_26.Length = 27.0
    qwm_doc.MeshX_E_26.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_26.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_26.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_26.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_27")
    qwm_doc.MeshX_E_27.Placement = FreeCAD.Placement(FreeCAD.Vector(-91.76563, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_27.Orientation = "X"
    qwm_doc.MeshX_E_27.Position = -91.76563
    qwm_doc.MeshX_E_27.Length = 27.0
    qwm_doc.MeshX_E_27.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_27.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_27.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_27.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_28")
    qwm_doc.MeshX_E_28.Placement = FreeCAD.Placement(FreeCAD.Vector(-90.09375, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_28.Orientation = "X"
    qwm_doc.MeshX_E_28.Position = -90.09375
    qwm_doc.MeshX_E_28.Length = 27.0
    qwm_doc.MeshX_E_28.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_28.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_28.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_28.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_29")
    qwm_doc.MeshX_E_29.Placement = FreeCAD.Placement(FreeCAD.Vector(-88.42188, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_29.Orientation = "X"
    qwm_doc.MeshX_E_29.Position = -88.42188
    qwm_doc.MeshX_E_29.Length = 27.0
    qwm_doc.MeshX_E_29.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_29.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_29.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_29.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_30")
    qwm_doc.MeshX_E_30.Placement = FreeCAD.Placement(FreeCAD.Vector(-86.75, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_30.Orientation = "X"
    qwm_doc.MeshX_E_30.Position = -86.75
    qwm_doc.MeshX_E_30.Length = 27.0
    qwm_doc.MeshX_E_30.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_30.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_30.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_30.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_31")
    qwm_doc.MeshX_E_31.Placement = FreeCAD.Placement(FreeCAD.Vector(-85.07813, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_31.Orientation = "X"
    qwm_doc.MeshX_E_31.Position = -85.07813
    qwm_doc.MeshX_E_31.Length = 27.0
    qwm_doc.MeshX_E_31.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_31.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_31.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_31.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_32")
    qwm_doc.MeshX_E_32.Placement = FreeCAD.Placement(FreeCAD.Vector(-83.40625, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_32.Orientation = "X"
    qwm_doc.MeshX_E_32.Position = -83.40625
    qwm_doc.MeshX_E_32.Length = 27.0
    qwm_doc.MeshX_E_32.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_32.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_32.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_32.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_33")
    qwm_doc.MeshX_E_33.Placement = FreeCAD.Placement(FreeCAD.Vector(-81.73437, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_33.Orientation = "X"
    qwm_doc.MeshX_E_33.Position = -81.73437
    qwm_doc.MeshX_E_33.Length = 27.0
    qwm_doc.MeshX_E_33.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_33.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_33.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_33.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_34")
    qwm_doc.MeshX_E_34.Placement = FreeCAD.Placement(FreeCAD.Vector(-80.0625, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_34.Orientation = "X"
    qwm_doc.MeshX_E_34.Position = -80.0625
    qwm_doc.MeshX_E_34.Length = 27.0
    qwm_doc.MeshX_E_34.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_34.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_34.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_34.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_35")
    qwm_doc.MeshX_E_35.Placement = FreeCAD.Placement(FreeCAD.Vector(-78.39062, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_35.Orientation = "X"
    qwm_doc.MeshX_E_35.Position = -78.39062
    qwm_doc.MeshX_E_35.Length = 27.0
    qwm_doc.MeshX_E_35.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_35.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_35.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_35.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_36")
    qwm_doc.MeshX_E_36.Placement = FreeCAD.Placement(FreeCAD.Vector(-76.71875, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_36.Orientation = "X"
    qwm_doc.MeshX_E_36.Position = -76.71875
    qwm_doc.MeshX_E_36.Length = 27.0
    qwm_doc.MeshX_E_36.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_36.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_36.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_36.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_37")
    qwm_doc.MeshX_E_37.Placement = FreeCAD.Placement(FreeCAD.Vector(-75.04687, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_37.Orientation = "X"
    qwm_doc.MeshX_E_37.Position = -75.04687
    qwm_doc.MeshX_E_37.Length = 27.0
    qwm_doc.MeshX_E_37.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_37.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_37.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_37.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_38")
    qwm_doc.MeshX_E_38.Placement = FreeCAD.Placement(FreeCAD.Vector(-73.375, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_38.Orientation = "X"
    qwm_doc.MeshX_E_38.Position = -73.375
    qwm_doc.MeshX_E_38.Length = 27.0
    qwm_doc.MeshX_E_38.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_38.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_38.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_38.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_39")
    qwm_doc.MeshX_E_39.Placement = FreeCAD.Placement(FreeCAD.Vector(-71.70312, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_39.Orientation = "X"
    qwm_doc.MeshX_E_39.Position = -71.70312
    qwm_doc.MeshX_E_39.Length = 27.0
    qwm_doc.MeshX_E_39.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_39.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_39.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_39.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_40")
    qwm_doc.MeshX_E_40.Placement = FreeCAD.Placement(FreeCAD.Vector(-70.03125, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_40.Orientation = "X"
    qwm_doc.MeshX_E_40.Position = -70.03125
    qwm_doc.MeshX_E_40.Length = 27.0
    qwm_doc.MeshX_E_40.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_40.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_40.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_40.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_41")
    qwm_doc.MeshX_E_41.Placement = FreeCAD.Placement(FreeCAD.Vector(-68.35937, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_41.Orientation = "X"
    qwm_doc.MeshX_E_41.Position = -68.35937
    qwm_doc.MeshX_E_41.Length = 27.0
    qwm_doc.MeshX_E_41.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_41.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_41.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_41.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_42")
    qwm_doc.MeshX_E_42.Placement = FreeCAD.Placement(FreeCAD.Vector(-66.6875, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_42.Orientation = "X"
    qwm_doc.MeshX_E_42.Position = -66.6875
    qwm_doc.MeshX_E_42.Length = 27.0
    qwm_doc.MeshX_E_42.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_42.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_42.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_42.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_43")
    qwm_doc.MeshX_E_43.Placement = FreeCAD.Placement(FreeCAD.Vector(-65.01562, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_43.Orientation = "X"
    qwm_doc.MeshX_E_43.Position = -65.01562
    qwm_doc.MeshX_E_43.Length = 27.0
    qwm_doc.MeshX_E_43.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_43.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_43.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_43.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_44")
    qwm_doc.MeshX_E_44.Placement = FreeCAD.Placement(FreeCAD.Vector(-63.34375, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_44.Orientation = "X"
    qwm_doc.MeshX_E_44.Position = -63.34375
    qwm_doc.MeshX_E_44.Length = 27.0
    qwm_doc.MeshX_E_44.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_44.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_44.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_44.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_45")
    qwm_doc.MeshX_E_45.Placement = FreeCAD.Placement(FreeCAD.Vector(-61.67187, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_45.Orientation = "X"
    qwm_doc.MeshX_E_45.Position = -61.67187
    qwm_doc.MeshX_E_45.Length = 27.0
    qwm_doc.MeshX_E_45.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_45.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_45.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_45.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_46")
    qwm_doc.MeshX_E_46.Placement = FreeCAD.Placement(FreeCAD.Vector(-60.0, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_46.Orientation = "X"
    qwm_doc.MeshX_E_46.Position = -60.0
    qwm_doc.MeshX_E_46.Length = 27.0
    qwm_doc.MeshX_E_46.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_46.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_46.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_46.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_47")
    qwm_doc.MeshX_E_47.Placement = FreeCAD.Placement(FreeCAD.Vector(-58.30986, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_47.Orientation = "X"
    qwm_doc.MeshX_E_47.Position = -58.30986
    qwm_doc.MeshX_E_47.Length = 27.0
    qwm_doc.MeshX_E_47.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_47.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_47.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_47.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_48")
    qwm_doc.MeshX_E_48.Placement = FreeCAD.Placement(FreeCAD.Vector(-56.61972, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_48.Orientation = "X"
    qwm_doc.MeshX_E_48.Position = -56.61972
    qwm_doc.MeshX_E_48.Length = 27.0
    qwm_doc.MeshX_E_48.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_48.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_48.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_48.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_49")
    qwm_doc.MeshX_E_49.Placement = FreeCAD.Placement(FreeCAD.Vector(-54.92958, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_49.Orientation = "X"
    qwm_doc.MeshX_E_49.Position = -54.92958
    qwm_doc.MeshX_E_49.Length = 27.0
    qwm_doc.MeshX_E_49.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_49.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_49.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_49.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_50")
    qwm_doc.MeshX_E_50.Placement = FreeCAD.Placement(FreeCAD.Vector(-53.23944, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_50.Orientation = "X"
    qwm_doc.MeshX_E_50.Position = -53.23944
    qwm_doc.MeshX_E_50.Length = 27.0
    qwm_doc.MeshX_E_50.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_50.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_50.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_50.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_51")
    qwm_doc.MeshX_E_51.Placement = FreeCAD.Placement(FreeCAD.Vector(-51.5493, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_51.Orientation = "X"
    qwm_doc.MeshX_E_51.Position = -51.5493
    qwm_doc.MeshX_E_51.Length = 27.0
    qwm_doc.MeshX_E_51.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_51.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_51.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_51.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_52")
    qwm_doc.MeshX_E_52.Placement = FreeCAD.Placement(FreeCAD.Vector(-49.85915, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_52.Orientation = "X"
    qwm_doc.MeshX_E_52.Position = -49.85915
    qwm_doc.MeshX_E_52.Length = 27.0
    qwm_doc.MeshX_E_52.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_52.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_52.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_52.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_53")
    qwm_doc.MeshX_E_53.Placement = FreeCAD.Placement(FreeCAD.Vector(-48.16901, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_53.Orientation = "X"
    qwm_doc.MeshX_E_53.Position = -48.16901
    qwm_doc.MeshX_E_53.Length = 27.0
    qwm_doc.MeshX_E_53.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_53.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_53.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_53.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_54")
    qwm_doc.MeshX_E_54.Placement = FreeCAD.Placement(FreeCAD.Vector(-46.47887, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_54.Orientation = "X"
    qwm_doc.MeshX_E_54.Position = -46.47887
    qwm_doc.MeshX_E_54.Length = 27.0
    qwm_doc.MeshX_E_54.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_54.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_54.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_54.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_55")
    qwm_doc.MeshX_E_55.Placement = FreeCAD.Placement(FreeCAD.Vector(-44.78873, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_55.Orientation = "X"
    qwm_doc.MeshX_E_55.Position = -44.78873
    qwm_doc.MeshX_E_55.Length = 27.0
    qwm_doc.MeshX_E_55.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_55.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_55.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_55.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_56")
    qwm_doc.MeshX_E_56.Placement = FreeCAD.Placement(FreeCAD.Vector(-43.09859, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_56.Orientation = "X"
    qwm_doc.MeshX_E_56.Position = -43.09859
    qwm_doc.MeshX_E_56.Length = 27.0
    qwm_doc.MeshX_E_56.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_56.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_56.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_56.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_57")
    qwm_doc.MeshX_E_57.Placement = FreeCAD.Placement(FreeCAD.Vector(-41.40845, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_57.Orientation = "X"
    qwm_doc.MeshX_E_57.Position = -41.40845
    qwm_doc.MeshX_E_57.Length = 27.0
    qwm_doc.MeshX_E_57.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_57.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_57.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_57.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_58")
    qwm_doc.MeshX_E_58.Placement = FreeCAD.Placement(FreeCAD.Vector(-39.71831, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_58.Orientation = "X"
    qwm_doc.MeshX_E_58.Position = -39.71831
    qwm_doc.MeshX_E_58.Length = 27.0
    qwm_doc.MeshX_E_58.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_58.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_58.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_58.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_59")
    qwm_doc.MeshX_E_59.Placement = FreeCAD.Placement(FreeCAD.Vector(-38.02817, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_59.Orientation = "X"
    qwm_doc.MeshX_E_59.Position = -38.02817
    qwm_doc.MeshX_E_59.Length = 27.0
    qwm_doc.MeshX_E_59.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_59.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_59.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_59.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_60")
    qwm_doc.MeshX_E_60.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.33803, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_60.Orientation = "X"
    qwm_doc.MeshX_E_60.Position = -36.33803
    qwm_doc.MeshX_E_60.Length = 27.0
    qwm_doc.MeshX_E_60.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_60.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_60.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_60.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_61")
    qwm_doc.MeshX_E_61.Placement = FreeCAD.Placement(FreeCAD.Vector(-34.64789, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_61.Orientation = "X"
    qwm_doc.MeshX_E_61.Position = -34.64789
    qwm_doc.MeshX_E_61.Length = 27.0
    qwm_doc.MeshX_E_61.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_61.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_61.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_61.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_62")
    qwm_doc.MeshX_E_62.Placement = FreeCAD.Placement(FreeCAD.Vector(-32.95775, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_62.Orientation = "X"
    qwm_doc.MeshX_E_62.Position = -32.95775
    qwm_doc.MeshX_E_62.Length = 27.0
    qwm_doc.MeshX_E_62.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_62.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_62.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_62.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_63")
    qwm_doc.MeshX_E_63.Placement = FreeCAD.Placement(FreeCAD.Vector(-31.26761, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_63.Orientation = "X"
    qwm_doc.MeshX_E_63.Position = -31.26761
    qwm_doc.MeshX_E_63.Length = 27.0
    qwm_doc.MeshX_E_63.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_63.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_63.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_63.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_64")
    qwm_doc.MeshX_E_64.Placement = FreeCAD.Placement(FreeCAD.Vector(-29.57746, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_64.Orientation = "X"
    qwm_doc.MeshX_E_64.Position = -29.57746
    qwm_doc.MeshX_E_64.Length = 27.0
    qwm_doc.MeshX_E_64.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_64.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_64.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_64.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_65")
    qwm_doc.MeshX_E_65.Placement = FreeCAD.Placement(FreeCAD.Vector(-27.88732, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_65.Orientation = "X"
    qwm_doc.MeshX_E_65.Position = -27.88732
    qwm_doc.MeshX_E_65.Length = 27.0
    qwm_doc.MeshX_E_65.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_65.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_65.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_65.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_66")
    qwm_doc.MeshX_E_66.Placement = FreeCAD.Placement(FreeCAD.Vector(-26.19718, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_66.Orientation = "X"
    qwm_doc.MeshX_E_66.Position = -26.19718
    qwm_doc.MeshX_E_66.Length = 27.0
    qwm_doc.MeshX_E_66.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_66.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_66.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_66.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_67")
    qwm_doc.MeshX_E_67.Placement = FreeCAD.Placement(FreeCAD.Vector(-24.50704, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_67.Orientation = "X"
    qwm_doc.MeshX_E_67.Position = -24.50704
    qwm_doc.MeshX_E_67.Length = 27.0
    qwm_doc.MeshX_E_67.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_67.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_67.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_67.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_68")
    qwm_doc.MeshX_E_68.Placement = FreeCAD.Placement(FreeCAD.Vector(-22.8169, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_68.Orientation = "X"
    qwm_doc.MeshX_E_68.Position = -22.8169
    qwm_doc.MeshX_E_68.Length = 27.0
    qwm_doc.MeshX_E_68.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_68.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_68.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_68.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_69")
    qwm_doc.MeshX_E_69.Placement = FreeCAD.Placement(FreeCAD.Vector(-21.12676, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_69.Orientation = "X"
    qwm_doc.MeshX_E_69.Position = -21.12676
    qwm_doc.MeshX_E_69.Length = 27.0
    qwm_doc.MeshX_E_69.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_69.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_69.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_69.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_70")
    qwm_doc.MeshX_E_70.Placement = FreeCAD.Placement(FreeCAD.Vector(-19.43662, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_70.Orientation = "X"
    qwm_doc.MeshX_E_70.Position = -19.43662
    qwm_doc.MeshX_E_70.Length = 27.0
    qwm_doc.MeshX_E_70.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_70.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_70.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_70.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_71")
    qwm_doc.MeshX_E_71.Placement = FreeCAD.Placement(FreeCAD.Vector(-17.74648, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_71.Orientation = "X"
    qwm_doc.MeshX_E_71.Position = -17.74648
    qwm_doc.MeshX_E_71.Length = 27.0
    qwm_doc.MeshX_E_71.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_71.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_71.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_71.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_72")
    qwm_doc.MeshX_E_72.Placement = FreeCAD.Placement(FreeCAD.Vector(-16.05634, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_72.Orientation = "X"
    qwm_doc.MeshX_E_72.Position = -16.05634
    qwm_doc.MeshX_E_72.Length = 27.0
    qwm_doc.MeshX_E_72.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_72.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_72.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_72.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_73")
    qwm_doc.MeshX_E_73.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.3662, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_73.Orientation = "X"
    qwm_doc.MeshX_E_73.Position = -14.3662
    qwm_doc.MeshX_E_73.Length = 27.0
    qwm_doc.MeshX_E_73.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_73.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_73.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_73.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_74")
    qwm_doc.MeshX_E_74.Placement = FreeCAD.Placement(FreeCAD.Vector(-12.67606, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_74.Orientation = "X"
    qwm_doc.MeshX_E_74.Position = -12.67606
    qwm_doc.MeshX_E_74.Length = 27.0
    qwm_doc.MeshX_E_74.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_74.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_74.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_74.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_75")
    qwm_doc.MeshX_E_75.Placement = FreeCAD.Placement(FreeCAD.Vector(-10.98592, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_75.Orientation = "X"
    qwm_doc.MeshX_E_75.Position = -10.98592
    qwm_doc.MeshX_E_75.Length = 27.0
    qwm_doc.MeshX_E_75.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_75.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_75.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_75.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_76")
    qwm_doc.MeshX_E_76.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.29577, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_76.Orientation = "X"
    qwm_doc.MeshX_E_76.Position = -9.29577
    qwm_doc.MeshX_E_76.Length = 27.0
    qwm_doc.MeshX_E_76.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_76.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_76.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_76.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_77")
    qwm_doc.MeshX_E_77.Placement = FreeCAD.Placement(FreeCAD.Vector(-7.60563, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_77.Orientation = "X"
    qwm_doc.MeshX_E_77.Position = -7.60563
    qwm_doc.MeshX_E_77.Length = 27.0
    qwm_doc.MeshX_E_77.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_77.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_77.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_77.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_78")
    qwm_doc.MeshX_E_78.Placement = FreeCAD.Placement(FreeCAD.Vector(-5.91549, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_78.Orientation = "X"
    qwm_doc.MeshX_E_78.Position = -5.91549
    qwm_doc.MeshX_E_78.Length = 27.0
    qwm_doc.MeshX_E_78.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_78.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_78.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_78.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_79")
    qwm_doc.MeshX_E_79.Placement = FreeCAD.Placement(FreeCAD.Vector(-4.22535, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_79.Orientation = "X"
    qwm_doc.MeshX_E_79.Position = -4.22535
    qwm_doc.MeshX_E_79.Length = 27.0
    qwm_doc.MeshX_E_79.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_79.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_79.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_79.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_80")
    qwm_doc.MeshX_E_80.Placement = FreeCAD.Placement(FreeCAD.Vector(-2.53521, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_80.Orientation = "X"
    qwm_doc.MeshX_E_80.Position = -2.53521
    qwm_doc.MeshX_E_80.Length = 27.0
    qwm_doc.MeshX_E_80.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_80.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_80.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_80.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_81")
    qwm_doc.MeshX_E_81.Placement = FreeCAD.Placement(FreeCAD.Vector(-0.84507, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_81.Orientation = "X"
    qwm_doc.MeshX_E_81.Position = -0.84507
    qwm_doc.MeshX_E_81.Length = 27.0
    qwm_doc.MeshX_E_81.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_81.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_81.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_81.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_82")
    qwm_doc.MeshX_E_82.Placement = FreeCAD.Placement(FreeCAD.Vector(0.84507, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_82.Orientation = "X"
    qwm_doc.MeshX_E_82.Position = 0.84507
    qwm_doc.MeshX_E_82.Length = 27.0
    qwm_doc.MeshX_E_82.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_82.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_82.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_82.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_83")
    qwm_doc.MeshX_E_83.Placement = FreeCAD.Placement(FreeCAD.Vector(2.53521, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_83.Orientation = "X"
    qwm_doc.MeshX_E_83.Position = 2.53521
    qwm_doc.MeshX_E_83.Length = 27.0
    qwm_doc.MeshX_E_83.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_83.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_83.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_83.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_84")
    qwm_doc.MeshX_E_84.Placement = FreeCAD.Placement(FreeCAD.Vector(4.22535, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_84.Orientation = "X"
    qwm_doc.MeshX_E_84.Position = 4.22535
    qwm_doc.MeshX_E_84.Length = 27.0
    qwm_doc.MeshX_E_84.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_84.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_84.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_84.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_85")
    qwm_doc.MeshX_E_85.Placement = FreeCAD.Placement(FreeCAD.Vector(5.91549, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_85.Orientation = "X"
    qwm_doc.MeshX_E_85.Position = 5.91549
    qwm_doc.MeshX_E_85.Length = 27.0
    qwm_doc.MeshX_E_85.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_85.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_85.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_85.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_86")
    qwm_doc.MeshX_E_86.Placement = FreeCAD.Placement(FreeCAD.Vector(7.60563, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_86.Orientation = "X"
    qwm_doc.MeshX_E_86.Position = 7.60563
    qwm_doc.MeshX_E_86.Length = 27.0
    qwm_doc.MeshX_E_86.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_86.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_86.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_86.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_87")
    qwm_doc.MeshX_E_87.Placement = FreeCAD.Placement(FreeCAD.Vector(9.29577, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_87.Orientation = "X"
    qwm_doc.MeshX_E_87.Position = 9.29577
    qwm_doc.MeshX_E_87.Length = 27.0
    qwm_doc.MeshX_E_87.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_87.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_87.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_87.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_88")
    qwm_doc.MeshX_E_88.Placement = FreeCAD.Placement(FreeCAD.Vector(10.98592, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_88.Orientation = "X"
    qwm_doc.MeshX_E_88.Position = 10.98592
    qwm_doc.MeshX_E_88.Length = 27.0
    qwm_doc.MeshX_E_88.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_88.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_88.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_88.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_89")
    qwm_doc.MeshX_E_89.Placement = FreeCAD.Placement(FreeCAD.Vector(12.67606, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_89.Orientation = "X"
    qwm_doc.MeshX_E_89.Position = 12.67606
    qwm_doc.MeshX_E_89.Length = 27.0
    qwm_doc.MeshX_E_89.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_89.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_89.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_89.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_90")
    qwm_doc.MeshX_E_90.Placement = FreeCAD.Placement(FreeCAD.Vector(14.3662, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_90.Orientation = "X"
    qwm_doc.MeshX_E_90.Position = 14.3662
    qwm_doc.MeshX_E_90.Length = 27.0
    qwm_doc.MeshX_E_90.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_90.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_90.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_90.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_91")
    qwm_doc.MeshX_E_91.Placement = FreeCAD.Placement(FreeCAD.Vector(16.05634, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_91.Orientation = "X"
    qwm_doc.MeshX_E_91.Position = 16.05634
    qwm_doc.MeshX_E_91.Length = 27.0
    qwm_doc.MeshX_E_91.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_91.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_91.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_91.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_92")
    qwm_doc.MeshX_E_92.Placement = FreeCAD.Placement(FreeCAD.Vector(17.74648, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_92.Orientation = "X"
    qwm_doc.MeshX_E_92.Position = 17.74648
    qwm_doc.MeshX_E_92.Length = 27.0
    qwm_doc.MeshX_E_92.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_92.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_92.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_92.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_93")
    qwm_doc.MeshX_E_93.Placement = FreeCAD.Placement(FreeCAD.Vector(19.43662, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_93.Orientation = "X"
    qwm_doc.MeshX_E_93.Position = 19.43662
    qwm_doc.MeshX_E_93.Length = 27.0
    qwm_doc.MeshX_E_93.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_93.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_93.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_93.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_94")
    qwm_doc.MeshX_E_94.Placement = FreeCAD.Placement(FreeCAD.Vector(21.12676, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_94.Orientation = "X"
    qwm_doc.MeshX_E_94.Position = 21.12676
    qwm_doc.MeshX_E_94.Length = 27.0
    qwm_doc.MeshX_E_94.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_94.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_94.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_94.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_95")
    qwm_doc.MeshX_E_95.Placement = FreeCAD.Placement(FreeCAD.Vector(22.8169, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_95.Orientation = "X"
    qwm_doc.MeshX_E_95.Position = 22.8169
    qwm_doc.MeshX_E_95.Length = 27.0
    qwm_doc.MeshX_E_95.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_95.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_95.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_95.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_96")
    qwm_doc.MeshX_E_96.Placement = FreeCAD.Placement(FreeCAD.Vector(24.50704, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_96.Orientation = "X"
    qwm_doc.MeshX_E_96.Position = 24.50704
    qwm_doc.MeshX_E_96.Length = 27.0
    qwm_doc.MeshX_E_96.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_96.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_96.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_96.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_97")
    qwm_doc.MeshX_E_97.Placement = FreeCAD.Placement(FreeCAD.Vector(26.19718, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_97.Orientation = "X"
    qwm_doc.MeshX_E_97.Position = 26.19718
    qwm_doc.MeshX_E_97.Length = 27.0
    qwm_doc.MeshX_E_97.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_97.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_97.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_97.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_98")
    qwm_doc.MeshX_E_98.Placement = FreeCAD.Placement(FreeCAD.Vector(27.88732, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_98.Orientation = "X"
    qwm_doc.MeshX_E_98.Position = 27.88732
    qwm_doc.MeshX_E_98.Length = 27.0
    qwm_doc.MeshX_E_98.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_98.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_98.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_98.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_99")
    qwm_doc.MeshX_E_99.Placement = FreeCAD.Placement(FreeCAD.Vector(29.57746, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_99.Orientation = "X"
    qwm_doc.MeshX_E_99.Position = 29.57746
    qwm_doc.MeshX_E_99.Length = 27.0
    qwm_doc.MeshX_E_99.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_99.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_99.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_99.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_100")
    qwm_doc.MeshX_E_100.Placement = FreeCAD.Placement(FreeCAD.Vector(31.26761, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_100.Orientation = "X"
    qwm_doc.MeshX_E_100.Position = 31.26761
    qwm_doc.MeshX_E_100.Length = 27.0
    qwm_doc.MeshX_E_100.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_100.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_100.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_100.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_101")
    qwm_doc.MeshX_E_101.Placement = FreeCAD.Placement(FreeCAD.Vector(32.95775, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_101.Orientation = "X"
    qwm_doc.MeshX_E_101.Position = 32.95775
    qwm_doc.MeshX_E_101.Length = 27.0
    qwm_doc.MeshX_E_101.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_101.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_101.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_101.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_102")
    qwm_doc.MeshX_E_102.Placement = FreeCAD.Placement(FreeCAD.Vector(34.64789, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_102.Orientation = "X"
    qwm_doc.MeshX_E_102.Position = 34.64789
    qwm_doc.MeshX_E_102.Length = 27.0
    qwm_doc.MeshX_E_102.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_102.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_102.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_102.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_103")
    qwm_doc.MeshX_E_103.Placement = FreeCAD.Placement(FreeCAD.Vector(36.33803, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_103.Orientation = "X"
    qwm_doc.MeshX_E_103.Position = 36.33803
    qwm_doc.MeshX_E_103.Length = 27.0
    qwm_doc.MeshX_E_103.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_103.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_103.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_103.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_104")
    qwm_doc.MeshX_E_104.Placement = FreeCAD.Placement(FreeCAD.Vector(38.02817, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_104.Orientation = "X"
    qwm_doc.MeshX_E_104.Position = 38.02817
    qwm_doc.MeshX_E_104.Length = 27.0
    qwm_doc.MeshX_E_104.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_104.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_104.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_104.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_105")
    qwm_doc.MeshX_E_105.Placement = FreeCAD.Placement(FreeCAD.Vector(39.71831, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_105.Orientation = "X"
    qwm_doc.MeshX_E_105.Position = 39.71831
    qwm_doc.MeshX_E_105.Length = 27.0
    qwm_doc.MeshX_E_105.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_105.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_105.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_105.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_106")
    qwm_doc.MeshX_E_106.Placement = FreeCAD.Placement(FreeCAD.Vector(41.40845, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_106.Orientation = "X"
    qwm_doc.MeshX_E_106.Position = 41.40845
    qwm_doc.MeshX_E_106.Length = 27.0
    qwm_doc.MeshX_E_106.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_106.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_106.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_106.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_107")
    qwm_doc.MeshX_E_107.Placement = FreeCAD.Placement(FreeCAD.Vector(43.09859, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_107.Orientation = "X"
    qwm_doc.MeshX_E_107.Position = 43.09859
    qwm_doc.MeshX_E_107.Length = 27.0
    qwm_doc.MeshX_E_107.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_107.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_107.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_107.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_108")
    qwm_doc.MeshX_E_108.Placement = FreeCAD.Placement(FreeCAD.Vector(44.78873, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_108.Orientation = "X"
    qwm_doc.MeshX_E_108.Position = 44.78873
    qwm_doc.MeshX_E_108.Length = 27.0
    qwm_doc.MeshX_E_108.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_108.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_108.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_108.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_109")
    qwm_doc.MeshX_E_109.Placement = FreeCAD.Placement(FreeCAD.Vector(46.47887, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_109.Orientation = "X"
    qwm_doc.MeshX_E_109.Position = 46.47887
    qwm_doc.MeshX_E_109.Length = 27.0
    qwm_doc.MeshX_E_109.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_109.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_109.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_109.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_110")
    qwm_doc.MeshX_E_110.Placement = FreeCAD.Placement(FreeCAD.Vector(48.16901, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_110.Orientation = "X"
    qwm_doc.MeshX_E_110.Position = 48.16901
    qwm_doc.MeshX_E_110.Length = 27.0
    qwm_doc.MeshX_E_110.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_110.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_110.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_110.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_111")
    qwm_doc.MeshX_E_111.Placement = FreeCAD.Placement(FreeCAD.Vector(49.85915, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_111.Orientation = "X"
    qwm_doc.MeshX_E_111.Position = 49.85915
    qwm_doc.MeshX_E_111.Length = 27.0
    qwm_doc.MeshX_E_111.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_111.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_111.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_111.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_112")
    qwm_doc.MeshX_E_112.Placement = FreeCAD.Placement(FreeCAD.Vector(51.5493, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_112.Orientation = "X"
    qwm_doc.MeshX_E_112.Position = 51.5493
    qwm_doc.MeshX_E_112.Length = 27.0
    qwm_doc.MeshX_E_112.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_112.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_112.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_112.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_113")
    qwm_doc.MeshX_E_113.Placement = FreeCAD.Placement(FreeCAD.Vector(53.23944, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_113.Orientation = "X"
    qwm_doc.MeshX_E_113.Position = 53.23944
    qwm_doc.MeshX_E_113.Length = 27.0
    qwm_doc.MeshX_E_113.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_113.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_113.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_113.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_114")
    qwm_doc.MeshX_E_114.Placement = FreeCAD.Placement(FreeCAD.Vector(54.92958, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_114.Orientation = "X"
    qwm_doc.MeshX_E_114.Position = 54.92958
    qwm_doc.MeshX_E_114.Length = 27.0
    qwm_doc.MeshX_E_114.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_114.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_114.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_114.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_115")
    qwm_doc.MeshX_E_115.Placement = FreeCAD.Placement(FreeCAD.Vector(56.61972, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_115.Orientation = "X"
    qwm_doc.MeshX_E_115.Position = 56.61972
    qwm_doc.MeshX_E_115.Length = 27.0
    qwm_doc.MeshX_E_115.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_115.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_115.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_115.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_116")
    qwm_doc.MeshX_E_116.Placement = FreeCAD.Placement(FreeCAD.Vector(58.30986, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_116.Orientation = "X"
    qwm_doc.MeshX_E_116.Position = 58.30986
    qwm_doc.MeshX_E_116.Length = 27.0
    qwm_doc.MeshX_E_116.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_116.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_116.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_116.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_117")
    qwm_doc.MeshX_E_117.Placement = FreeCAD.Placement(FreeCAD.Vector(60.0, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_117.Orientation = "X"
    qwm_doc.MeshX_E_117.Position = 60.0
    qwm_doc.MeshX_E_117.Length = 27.0
    qwm_doc.MeshX_E_117.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_117.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_117.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_117.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_118")
    qwm_doc.MeshX_E_118.Placement = FreeCAD.Placement(FreeCAD.Vector(61.67187, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_118.Orientation = "X"
    qwm_doc.MeshX_E_118.Position = 61.67187
    qwm_doc.MeshX_E_118.Length = 27.0
    qwm_doc.MeshX_E_118.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_118.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_118.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_118.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_119")
    qwm_doc.MeshX_E_119.Placement = FreeCAD.Placement(FreeCAD.Vector(63.34375, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_119.Orientation = "X"
    qwm_doc.MeshX_E_119.Position = 63.34375
    qwm_doc.MeshX_E_119.Length = 27.0
    qwm_doc.MeshX_E_119.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_119.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_119.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_119.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_120")
    qwm_doc.MeshX_E_120.Placement = FreeCAD.Placement(FreeCAD.Vector(65.01562, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_120.Orientation = "X"
    qwm_doc.MeshX_E_120.Position = 65.01562
    qwm_doc.MeshX_E_120.Length = 27.0
    qwm_doc.MeshX_E_120.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_120.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_120.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_120.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_121")
    qwm_doc.MeshX_E_121.Placement = FreeCAD.Placement(FreeCAD.Vector(66.6875, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_121.Orientation = "X"
    qwm_doc.MeshX_E_121.Position = 66.6875
    qwm_doc.MeshX_E_121.Length = 27.0
    qwm_doc.MeshX_E_121.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_121.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_121.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_121.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_122")
    qwm_doc.MeshX_E_122.Placement = FreeCAD.Placement(FreeCAD.Vector(68.35937, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_122.Orientation = "X"
    qwm_doc.MeshX_E_122.Position = 68.35937
    qwm_doc.MeshX_E_122.Length = 27.0
    qwm_doc.MeshX_E_122.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_122.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_122.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_122.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_123")
    qwm_doc.MeshX_E_123.Placement = FreeCAD.Placement(FreeCAD.Vector(70.03125, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_123.Orientation = "X"
    qwm_doc.MeshX_E_123.Position = 70.03125
    qwm_doc.MeshX_E_123.Length = 27.0
    qwm_doc.MeshX_E_123.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_123.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_123.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_123.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_124")
    qwm_doc.MeshX_E_124.Placement = FreeCAD.Placement(FreeCAD.Vector(71.70312, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_124.Orientation = "X"
    qwm_doc.MeshX_E_124.Position = 71.70312
    qwm_doc.MeshX_E_124.Length = 27.0
    qwm_doc.MeshX_E_124.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_124.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_124.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_124.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_125")
    qwm_doc.MeshX_E_125.Placement = FreeCAD.Placement(FreeCAD.Vector(73.375, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_125.Orientation = "X"
    qwm_doc.MeshX_E_125.Position = 73.375
    qwm_doc.MeshX_E_125.Length = 27.0
    qwm_doc.MeshX_E_125.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_125.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_125.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_125.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_126")
    qwm_doc.MeshX_E_126.Placement = FreeCAD.Placement(FreeCAD.Vector(75.04687, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_126.Orientation = "X"
    qwm_doc.MeshX_E_126.Position = 75.04687
    qwm_doc.MeshX_E_126.Length = 27.0
    qwm_doc.MeshX_E_126.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_126.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_126.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_126.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_127")
    qwm_doc.MeshX_E_127.Placement = FreeCAD.Placement(FreeCAD.Vector(76.71875, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_127.Orientation = "X"
    qwm_doc.MeshX_E_127.Position = 76.71875
    qwm_doc.MeshX_E_127.Length = 27.0
    qwm_doc.MeshX_E_127.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_127.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_127.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_127.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_128")
    qwm_doc.MeshX_E_128.Placement = FreeCAD.Placement(FreeCAD.Vector(78.39062, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_128.Orientation = "X"
    qwm_doc.MeshX_E_128.Position = 78.39062
    qwm_doc.MeshX_E_128.Length = 27.0
    qwm_doc.MeshX_E_128.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_128.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_128.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_128.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_129")
    qwm_doc.MeshX_E_129.Placement = FreeCAD.Placement(FreeCAD.Vector(80.0625, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_129.Orientation = "X"
    qwm_doc.MeshX_E_129.Position = 80.0625
    qwm_doc.MeshX_E_129.Length = 27.0
    qwm_doc.MeshX_E_129.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_129.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_129.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_129.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_130")
    qwm_doc.MeshX_E_130.Placement = FreeCAD.Placement(FreeCAD.Vector(81.73437, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_130.Orientation = "X"
    qwm_doc.MeshX_E_130.Position = 81.73437
    qwm_doc.MeshX_E_130.Length = 27.0
    qwm_doc.MeshX_E_130.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_130.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_130.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_130.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_131")
    qwm_doc.MeshX_E_131.Placement = FreeCAD.Placement(FreeCAD.Vector(83.40625, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_131.Orientation = "X"
    qwm_doc.MeshX_E_131.Position = 83.40625
    qwm_doc.MeshX_E_131.Length = 27.0
    qwm_doc.MeshX_E_131.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_131.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_131.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_131.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_132")
    qwm_doc.MeshX_E_132.Placement = FreeCAD.Placement(FreeCAD.Vector(85.07813, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_132.Orientation = "X"
    qwm_doc.MeshX_E_132.Position = 85.07813
    qwm_doc.MeshX_E_132.Length = 27.0
    qwm_doc.MeshX_E_132.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_132.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_132.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_132.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_133")
    qwm_doc.MeshX_E_133.Placement = FreeCAD.Placement(FreeCAD.Vector(86.75, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_133.Orientation = "X"
    qwm_doc.MeshX_E_133.Position = 86.75
    qwm_doc.MeshX_E_133.Length = 27.0
    qwm_doc.MeshX_E_133.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_133.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_133.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_133.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_134")
    qwm_doc.MeshX_E_134.Placement = FreeCAD.Placement(FreeCAD.Vector(88.42188, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_134.Orientation = "X"
    qwm_doc.MeshX_E_134.Position = 88.42188
    qwm_doc.MeshX_E_134.Length = 27.0
    qwm_doc.MeshX_E_134.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_134.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_134.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_134.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_135")
    qwm_doc.MeshX_E_135.Placement = FreeCAD.Placement(FreeCAD.Vector(90.09375, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_135.Orientation = "X"
    qwm_doc.MeshX_E_135.Position = 90.09375
    qwm_doc.MeshX_E_135.Length = 27.0
    qwm_doc.MeshX_E_135.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_135.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_135.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_135.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_136")
    qwm_doc.MeshX_E_136.Placement = FreeCAD.Placement(FreeCAD.Vector(91.76563, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_136.Orientation = "X"
    qwm_doc.MeshX_E_136.Position = 91.76563
    qwm_doc.MeshX_E_136.Length = 27.0
    qwm_doc.MeshX_E_136.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_136.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_136.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_136.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_137")
    qwm_doc.MeshX_E_137.Placement = FreeCAD.Placement(FreeCAD.Vector(93.4375, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_137.Orientation = "X"
    qwm_doc.MeshX_E_137.Position = 93.4375
    qwm_doc.MeshX_E_137.Length = 27.0
    qwm_doc.MeshX_E_137.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_137.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_137.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_137.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_138")
    qwm_doc.MeshX_E_138.Placement = FreeCAD.Placement(FreeCAD.Vector(95.10938, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_138.Orientation = "X"
    qwm_doc.MeshX_E_138.Position = 95.10938
    qwm_doc.MeshX_E_138.Length = 27.0
    qwm_doc.MeshX_E_138.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_138.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_138.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_138.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_139")
    qwm_doc.MeshX_E_139.Placement = FreeCAD.Placement(FreeCAD.Vector(96.78125, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_139.Orientation = "X"
    qwm_doc.MeshX_E_139.Position = 96.78125
    qwm_doc.MeshX_E_139.Length = 27.0
    qwm_doc.MeshX_E_139.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_139.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_139.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_139.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_140")
    qwm_doc.MeshX_E_140.Placement = FreeCAD.Placement(FreeCAD.Vector(98.45313, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_140.Orientation = "X"
    qwm_doc.MeshX_E_140.Position = 98.45313
    qwm_doc.MeshX_E_140.Length = 27.0
    qwm_doc.MeshX_E_140.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_140.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_140.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_140.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_141")
    qwm_doc.MeshX_E_141.Placement = FreeCAD.Placement(FreeCAD.Vector(100.125, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_141.Orientation = "X"
    qwm_doc.MeshX_E_141.Position = 100.125
    qwm_doc.MeshX_E_141.Length = 27.0
    qwm_doc.MeshX_E_141.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_141.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_141.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_141.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_142")
    qwm_doc.MeshX_E_142.Placement = FreeCAD.Placement(FreeCAD.Vector(101.79688, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_142.Orientation = "X"
    qwm_doc.MeshX_E_142.Position = 101.79688
    qwm_doc.MeshX_E_142.Length = 27.0
    qwm_doc.MeshX_E_142.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_142.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_142.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_142.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_143")
    qwm_doc.MeshX_E_143.Placement = FreeCAD.Placement(FreeCAD.Vector(103.46875, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_143.Orientation = "X"
    qwm_doc.MeshX_E_143.Position = 103.46875
    qwm_doc.MeshX_E_143.Length = 27.0
    qwm_doc.MeshX_E_143.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_143.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_143.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_143.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_144")
    qwm_doc.MeshX_E_144.Placement = FreeCAD.Placement(FreeCAD.Vector(105.14063, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_144.Orientation = "X"
    qwm_doc.MeshX_E_144.Position = 105.14063
    qwm_doc.MeshX_E_144.Length = 27.0
    qwm_doc.MeshX_E_144.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_144.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_144.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_144.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_145")
    qwm_doc.MeshX_E_145.Placement = FreeCAD.Placement(FreeCAD.Vector(106.8125, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_145.Orientation = "X"
    qwm_doc.MeshX_E_145.Position = 106.8125
    qwm_doc.MeshX_E_145.Length = 27.0
    qwm_doc.MeshX_E_145.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_145.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_145.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_145.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_146")
    qwm_doc.MeshX_E_146.Placement = FreeCAD.Placement(FreeCAD.Vector(108.48438, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_146.Orientation = "X"
    qwm_doc.MeshX_E_146.Position = 108.48438
    qwm_doc.MeshX_E_146.Length = 27.0
    qwm_doc.MeshX_E_146.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_146.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_146.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_146.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_147")
    qwm_doc.MeshX_E_147.Placement = FreeCAD.Placement(FreeCAD.Vector(110.15625, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_147.Orientation = "X"
    qwm_doc.MeshX_E_147.Position = 110.15625
    qwm_doc.MeshX_E_147.Length = 27.0
    qwm_doc.MeshX_E_147.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_147.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_147.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_147.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_148")
    qwm_doc.MeshX_E_148.Placement = FreeCAD.Placement(FreeCAD.Vector(111.82813, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_148.Orientation = "X"
    qwm_doc.MeshX_E_148.Position = 111.82813
    qwm_doc.MeshX_E_148.Length = 27.0
    qwm_doc.MeshX_E_148.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_148.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_148.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_148.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_149")
    qwm_doc.MeshX_E_149.Placement = FreeCAD.Placement(FreeCAD.Vector(113.5, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_149.Orientation = "X"
    qwm_doc.MeshX_E_149.Position = 113.5
    qwm_doc.MeshX_E_149.Length = 27.0
    qwm_doc.MeshX_E_149.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_149.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_149.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_149.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_150")
    qwm_doc.MeshX_E_150.Placement = FreeCAD.Placement(FreeCAD.Vector(115.16667, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_150.Orientation = "X"
    qwm_doc.MeshX_E_150.Position = 115.16667
    qwm_doc.MeshX_E_150.Length = 27.0
    qwm_doc.MeshX_E_150.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_150.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_150.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_150.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_151")
    qwm_doc.MeshX_E_151.Placement = FreeCAD.Placement(FreeCAD.Vector(116.83333, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_151.Orientation = "X"
    qwm_doc.MeshX_E_151.Position = 116.83333
    qwm_doc.MeshX_E_151.Length = 27.0
    qwm_doc.MeshX_E_151.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_151.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_151.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_151.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_152")
    qwm_doc.MeshX_E_152.Placement = FreeCAD.Placement(FreeCAD.Vector(118.5, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_152.Orientation = "X"
    qwm_doc.MeshX_E_152.Position = 118.5
    qwm_doc.MeshX_E_152.Length = 27.0
    qwm_doc.MeshX_E_152.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_152.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_152.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_152.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_153")
    qwm_doc.MeshX_E_153.Placement = FreeCAD.Placement(FreeCAD.Vector(120.16667, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_153.Orientation = "X"
    qwm_doc.MeshX_E_153.Position = 120.16667
    qwm_doc.MeshX_E_153.Length = 27.0
    qwm_doc.MeshX_E_153.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_153.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_153.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_153.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_154")
    qwm_doc.MeshX_E_154.Placement = FreeCAD.Placement(FreeCAD.Vector(121.83333, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_154.Orientation = "X"
    qwm_doc.MeshX_E_154.Position = 121.83333
    qwm_doc.MeshX_E_154.Length = 27.0
    qwm_doc.MeshX_E_154.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_154.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_154.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_154.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_155")
    qwm_doc.MeshX_E_155.Placement = FreeCAD.Placement(FreeCAD.Vector(123.5, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_155.Orientation = "X"
    qwm_doc.MeshX_E_155.Position = 123.5
    qwm_doc.MeshX_E_155.Length = 27.0
    qwm_doc.MeshX_E_155.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_155.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_155.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_155.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_156")
    qwm_doc.MeshX_E_156.Placement = FreeCAD.Placement(FreeCAD.Vector(125.16667, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_156.Orientation = "X"
    qwm_doc.MeshX_E_156.Position = 125.16667
    qwm_doc.MeshX_E_156.Length = 27.0
    qwm_doc.MeshX_E_156.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_156.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_156.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_156.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_157")
    qwm_doc.MeshX_E_157.Placement = FreeCAD.Placement(FreeCAD.Vector(126.83333, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_157.Orientation = "X"
    qwm_doc.MeshX_E_157.Position = 126.83333
    qwm_doc.MeshX_E_157.Length = 27.0
    qwm_doc.MeshX_E_157.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_157.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_157.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_157.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_158")
    qwm_doc.MeshX_E_158.Placement = FreeCAD.Placement(FreeCAD.Vector(128.5, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_158.Orientation = "X"
    qwm_doc.MeshX_E_158.Position = 128.5
    qwm_doc.MeshX_E_158.Length = 27.0
    qwm_doc.MeshX_E_158.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_158.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_158.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_158.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_159")
    qwm_doc.MeshX_E_159.Placement = FreeCAD.Placement(FreeCAD.Vector(130.16667, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_159.Orientation = "X"
    qwm_doc.MeshX_E_159.Position = 130.16667
    qwm_doc.MeshX_E_159.Length = 27.0
    qwm_doc.MeshX_E_159.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_159.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_159.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_159.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_160")
    qwm_doc.MeshX_E_160.Placement = FreeCAD.Placement(FreeCAD.Vector(131.83333, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_160.Orientation = "X"
    qwm_doc.MeshX_E_160.Position = 131.83333
    qwm_doc.MeshX_E_160.Length = 27.0
    qwm_doc.MeshX_E_160.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_160.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_160.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_160.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshX_E_161")
    qwm_doc.MeshX_E_161.Placement = FreeCAD.Placement(FreeCAD.Vector(133.5, -121.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.MeshX_E_161.Orientation = "X"
    qwm_doc.MeshX_E_161.Position = 133.5
    qwm_doc.MeshX_E_161.Length = 27.0
    qwm_doc.MeshX_E_161.Width = 13.4
    FreeCAD.Gui.ActiveDocument.MeshX_E_161.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshX_E_161.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshX_E_161.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_1")
    qwm_doc.MeshY_E_1.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -135.0, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_1.Orientation = "Y"
    qwm_doc.MeshY_E_1.Position = -135.0
    qwm_doc.MeshY_E_1.Length = 13.4
    qwm_doc.MeshY_E_1.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_1.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_2")
    qwm_doc.MeshY_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -133.34615, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_2.Orientation = "Y"
    qwm_doc.MeshY_E_2.Position = -133.34615
    qwm_doc.MeshY_E_2.Length = 13.4
    qwm_doc.MeshY_E_2.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_3")
    qwm_doc.MeshY_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -131.69231, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_3.Orientation = "Y"
    qwm_doc.MeshY_E_3.Position = -131.69231
    qwm_doc.MeshY_E_3.Length = 13.4
    qwm_doc.MeshY_E_3.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_4")
    qwm_doc.MeshY_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -130.03846, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_4.Orientation = "Y"
    qwm_doc.MeshY_E_4.Position = -130.03846
    qwm_doc.MeshY_E_4.Length = 13.4
    qwm_doc.MeshY_E_4.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_5")
    qwm_doc.MeshY_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -128.38462, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_5.Orientation = "Y"
    qwm_doc.MeshY_E_5.Position = -128.38462
    qwm_doc.MeshY_E_5.Length = 13.4
    qwm_doc.MeshY_E_5.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_6")
    qwm_doc.MeshY_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -126.73077, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_6.Orientation = "Y"
    qwm_doc.MeshY_E_6.Position = -126.73077
    qwm_doc.MeshY_E_6.Length = 13.4
    qwm_doc.MeshY_E_6.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_7")
    qwm_doc.MeshY_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -125.07692, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_7.Orientation = "Y"
    qwm_doc.MeshY_E_7.Position = -125.07692
    qwm_doc.MeshY_E_7.Length = 13.4
    qwm_doc.MeshY_E_7.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_8")
    qwm_doc.MeshY_E_8.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -123.42308, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_8.Orientation = "Y"
    qwm_doc.MeshY_E_8.Position = -123.42308
    qwm_doc.MeshY_E_8.Length = 13.4
    qwm_doc.MeshY_E_8.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_8.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_8.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_8.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_9")
    qwm_doc.MeshY_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.76923, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_9.Orientation = "Y"
    qwm_doc.MeshY_E_9.Position = -121.76923
    qwm_doc.MeshY_E_9.Length = 13.4
    qwm_doc.MeshY_E_9.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_10")
    qwm_doc.MeshY_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -120.11538, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_10.Orientation = "Y"
    qwm_doc.MeshY_E_10.Position = -120.11538
    qwm_doc.MeshY_E_10.Length = 13.4
    qwm_doc.MeshY_E_10.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_11")
    qwm_doc.MeshY_E_11.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -118.46154, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_11.Orientation = "Y"
    qwm_doc.MeshY_E_11.Position = -118.46154
    qwm_doc.MeshY_E_11.Length = 13.4
    qwm_doc.MeshY_E_11.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_11.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_11.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_11.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_12")
    qwm_doc.MeshY_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -116.80769, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_12.Orientation = "Y"
    qwm_doc.MeshY_E_12.Position = -116.80769
    qwm_doc.MeshY_E_12.Length = 13.4
    qwm_doc.MeshY_E_12.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_13")
    qwm_doc.MeshY_E_13.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -115.15385, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_13.Orientation = "Y"
    qwm_doc.MeshY_E_13.Position = -115.15385
    qwm_doc.MeshY_E_13.Length = 13.4
    qwm_doc.MeshY_E_13.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_13.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_13.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_13.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_14")
    qwm_doc.MeshY_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -113.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_14.Orientation = "Y"
    qwm_doc.MeshY_E_14.Position = -113.5
    qwm_doc.MeshY_E_14.Length = 13.4
    qwm_doc.MeshY_E_14.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_15")
    qwm_doc.MeshY_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -111.82741, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_15.Orientation = "Y"
    qwm_doc.MeshY_E_15.Position = -111.82741
    qwm_doc.MeshY_E_15.Length = 13.4
    qwm_doc.MeshY_E_15.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_16")
    qwm_doc.MeshY_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -110.15483, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_16.Orientation = "Y"
    qwm_doc.MeshY_E_16.Position = -110.15483
    qwm_doc.MeshY_E_16.Length = 13.4
    qwm_doc.MeshY_E_16.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_17")
    qwm_doc.MeshY_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -108.48224, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_17.Orientation = "Y"
    qwm_doc.MeshY_E_17.Position = -108.48224
    qwm_doc.MeshY_E_17.Length = 13.4
    qwm_doc.MeshY_E_17.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_18")
    qwm_doc.MeshY_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -106.80965, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_18.Orientation = "Y"
    qwm_doc.MeshY_E_18.Position = -106.80965
    qwm_doc.MeshY_E_18.Length = 13.4
    qwm_doc.MeshY_E_18.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_19")
    qwm_doc.MeshY_E_19.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -105.13707, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_19.Orientation = "Y"
    qwm_doc.MeshY_E_19.Position = -105.13707
    qwm_doc.MeshY_E_19.Length = 13.4
    qwm_doc.MeshY_E_19.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_19.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_19.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_19.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_20")
    qwm_doc.MeshY_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -103.46448, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_20.Orientation = "Y"
    qwm_doc.MeshY_E_20.Position = -103.46448
    qwm_doc.MeshY_E_20.Length = 13.4
    qwm_doc.MeshY_E_20.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_21")
    qwm_doc.MeshY_E_21.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -101.79189, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_21.Orientation = "Y"
    qwm_doc.MeshY_E_21.Position = -101.79189
    qwm_doc.MeshY_E_21.Length = 13.4
    qwm_doc.MeshY_E_21.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_21.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_21.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_21.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_22")
    qwm_doc.MeshY_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -100.1193, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_22.Orientation = "Y"
    qwm_doc.MeshY_E_22.Position = -100.1193
    qwm_doc.MeshY_E_22.Length = 13.4
    qwm_doc.MeshY_E_22.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_23")
    qwm_doc.MeshY_E_23.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -98.44672, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_23.Orientation = "Y"
    qwm_doc.MeshY_E_23.Position = -98.44672
    qwm_doc.MeshY_E_23.Length = 13.4
    qwm_doc.MeshY_E_23.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_23.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_23.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_23.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_24")
    qwm_doc.MeshY_E_24.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -96.77413, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_24.Orientation = "Y"
    qwm_doc.MeshY_E_24.Position = -96.77413
    qwm_doc.MeshY_E_24.Length = 13.4
    qwm_doc.MeshY_E_24.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_24.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_24.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_24.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_25")
    qwm_doc.MeshY_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -95.10154, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_25.Orientation = "Y"
    qwm_doc.MeshY_E_25.Position = -95.10154
    qwm_doc.MeshY_E_25.Length = 13.4
    qwm_doc.MeshY_E_25.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_26")
    qwm_doc.MeshY_E_26.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -93.42896, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_26.Orientation = "Y"
    qwm_doc.MeshY_E_26.Position = -93.42896
    qwm_doc.MeshY_E_26.Length = 13.4
    qwm_doc.MeshY_E_26.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_26.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_26.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_26.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_27")
    qwm_doc.MeshY_E_27.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -91.75637, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_27.Orientation = "Y"
    qwm_doc.MeshY_E_27.Position = -91.75637
    qwm_doc.MeshY_E_27.Length = 13.4
    qwm_doc.MeshY_E_27.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_27.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_27.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_27.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_28")
    qwm_doc.MeshY_E_28.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -90.08378, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_28.Orientation = "Y"
    qwm_doc.MeshY_E_28.Position = -90.08378
    qwm_doc.MeshY_E_28.Length = 13.4
    qwm_doc.MeshY_E_28.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_28.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_28.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_28.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_29")
    qwm_doc.MeshY_E_29.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -88.4112, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_29.Orientation = "Y"
    qwm_doc.MeshY_E_29.Position = -88.4112
    qwm_doc.MeshY_E_29.Length = 13.4
    qwm_doc.MeshY_E_29.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_29.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_29.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_29.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_30")
    qwm_doc.MeshY_E_30.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -86.73861, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_30.Orientation = "Y"
    qwm_doc.MeshY_E_30.Position = -86.73861
    qwm_doc.MeshY_E_30.Length = 13.4
    qwm_doc.MeshY_E_30.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_30.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_30.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_30.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_31")
    qwm_doc.MeshY_E_31.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -85.06602, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_31.Orientation = "Y"
    qwm_doc.MeshY_E_31.Position = -85.06602
    qwm_doc.MeshY_E_31.Length = 13.4
    qwm_doc.MeshY_E_31.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_31.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_31.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_31.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_32")
    qwm_doc.MeshY_E_32.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -83.39344, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_32.Orientation = "Y"
    qwm_doc.MeshY_E_32.Position = -83.39344
    qwm_doc.MeshY_E_32.Length = 13.4
    qwm_doc.MeshY_E_32.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_32.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_32.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_32.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_33")
    qwm_doc.MeshY_E_33.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -81.72085, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_33.Orientation = "Y"
    qwm_doc.MeshY_E_33.Position = -81.72085
    qwm_doc.MeshY_E_33.Length = 13.4
    qwm_doc.MeshY_E_33.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_33.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_33.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_33.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_34")
    qwm_doc.MeshY_E_34.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -80.04826, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_34.Orientation = "Y"
    qwm_doc.MeshY_E_34.Position = -80.04826
    qwm_doc.MeshY_E_34.Length = 13.4
    qwm_doc.MeshY_E_34.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_34.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_34.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_34.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_35")
    qwm_doc.MeshY_E_35.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -78.37568, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_35.Orientation = "Y"
    qwm_doc.MeshY_E_35.Position = -78.37568
    qwm_doc.MeshY_E_35.Length = 13.4
    qwm_doc.MeshY_E_35.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_35.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_35.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_35.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_36")
    qwm_doc.MeshY_E_36.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -76.70309, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_36.Orientation = "Y"
    qwm_doc.MeshY_E_36.Position = -76.70309
    qwm_doc.MeshY_E_36.Length = 13.4
    qwm_doc.MeshY_E_36.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_36.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_36.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_36.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_37")
    qwm_doc.MeshY_E_37.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -75.0305, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_37.Orientation = "Y"
    qwm_doc.MeshY_E_37.Position = -75.0305
    qwm_doc.MeshY_E_37.Length = 13.4
    qwm_doc.MeshY_E_37.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_37.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_37.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_37.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_38")
    qwm_doc.MeshY_E_38.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -73.35792, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_38.Orientation = "Y"
    qwm_doc.MeshY_E_38.Position = -73.35792
    qwm_doc.MeshY_E_38.Length = 13.4
    qwm_doc.MeshY_E_38.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_38.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_38.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_38.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_39")
    qwm_doc.MeshY_E_39.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -71.68533, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_39.Orientation = "Y"
    qwm_doc.MeshY_E_39.Position = -71.68533
    qwm_doc.MeshY_E_39.Length = 13.4
    qwm_doc.MeshY_E_39.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_39.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_39.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_39.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_40")
    qwm_doc.MeshY_E_40.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -70.01274, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_40.Orientation = "Y"
    qwm_doc.MeshY_E_40.Position = -70.01274
    qwm_doc.MeshY_E_40.Length = 13.4
    qwm_doc.MeshY_E_40.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_40.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_40.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_40.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_41")
    qwm_doc.MeshY_E_41.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -68.34015, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_41.Orientation = "Y"
    qwm_doc.MeshY_E_41.Position = -68.34015
    qwm_doc.MeshY_E_41.Length = 13.4
    qwm_doc.MeshY_E_41.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_41.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_41.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_41.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_42")
    qwm_doc.MeshY_E_42.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -66.66757, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_42.Orientation = "Y"
    qwm_doc.MeshY_E_42.Position = -66.66757
    qwm_doc.MeshY_E_42.Length = 13.4
    qwm_doc.MeshY_E_42.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_42.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_42.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_42.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_43")
    qwm_doc.MeshY_E_43.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -64.99498, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_43.Orientation = "Y"
    qwm_doc.MeshY_E_43.Position = -64.99498
    qwm_doc.MeshY_E_43.Length = 13.4
    qwm_doc.MeshY_E_43.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_43.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_43.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_43.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_44")
    qwm_doc.MeshY_E_44.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -63.32239, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_44.Orientation = "Y"
    qwm_doc.MeshY_E_44.Position = -63.32239
    qwm_doc.MeshY_E_44.Length = 13.4
    qwm_doc.MeshY_E_44.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_44.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_44.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_44.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_45")
    qwm_doc.MeshY_E_45.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -61.64981, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_45.Orientation = "Y"
    qwm_doc.MeshY_E_45.Position = -61.64981
    qwm_doc.MeshY_E_45.Length = 13.4
    qwm_doc.MeshY_E_45.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_45.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_45.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_45.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_46")
    qwm_doc.MeshY_E_46.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -59.97722, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_46.Orientation = "Y"
    qwm_doc.MeshY_E_46.Position = -59.97722
    qwm_doc.MeshY_E_46.Length = 13.4
    qwm_doc.MeshY_E_46.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_46.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_46.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_46.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_47")
    qwm_doc.MeshY_E_47.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -58.36359, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_47.Orientation = "Y"
    qwm_doc.MeshY_E_47.Position = -58.36359
    qwm_doc.MeshY_E_47.Length = 13.4
    qwm_doc.MeshY_E_47.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_47.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_47.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_47.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_48")
    qwm_doc.MeshY_E_48.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -56.74996, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_48.Orientation = "Y"
    qwm_doc.MeshY_E_48.Position = -56.74996
    qwm_doc.MeshY_E_48.Length = 13.4
    qwm_doc.MeshY_E_48.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_48.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_48.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_48.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_49")
    qwm_doc.MeshY_E_49.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -55.13632, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_49.Orientation = "Y"
    qwm_doc.MeshY_E_49.Position = -55.13632
    qwm_doc.MeshY_E_49.Length = 13.4
    qwm_doc.MeshY_E_49.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_49.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_49.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_49.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_50")
    qwm_doc.MeshY_E_50.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -53.52269, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_50.Orientation = "Y"
    qwm_doc.MeshY_E_50.Position = -53.52269
    qwm_doc.MeshY_E_50.Length = 13.4
    qwm_doc.MeshY_E_50.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_50.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_50.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_50.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_51")
    qwm_doc.MeshY_E_51.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -51.90906, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_51.Orientation = "Y"
    qwm_doc.MeshY_E_51.Position = -51.90906
    qwm_doc.MeshY_E_51.Length = 13.4
    qwm_doc.MeshY_E_51.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_51.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_51.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_51.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_52")
    qwm_doc.MeshY_E_52.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -50.29543, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_52.Orientation = "Y"
    qwm_doc.MeshY_E_52.Position = -50.29543
    qwm_doc.MeshY_E_52.Length = 13.4
    qwm_doc.MeshY_E_52.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_52.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_52.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_52.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_53")
    qwm_doc.MeshY_E_53.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -48.68179, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_53.Orientation = "Y"
    qwm_doc.MeshY_E_53.Position = -48.68179
    qwm_doc.MeshY_E_53.Length = 13.4
    qwm_doc.MeshY_E_53.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_53.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_53.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_53.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_54")
    qwm_doc.MeshY_E_54.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -47.06816, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_54.Orientation = "Y"
    qwm_doc.MeshY_E_54.Position = -47.06816
    qwm_doc.MeshY_E_54.Length = 13.4
    qwm_doc.MeshY_E_54.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_54.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_54.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_54.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_55")
    qwm_doc.MeshY_E_55.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -45.45453, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_55.Orientation = "Y"
    qwm_doc.MeshY_E_55.Position = -45.45453
    qwm_doc.MeshY_E_55.Length = 13.4
    qwm_doc.MeshY_E_55.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_55.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_55.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_55.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_56")
    qwm_doc.MeshY_E_56.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -43.8409, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_56.Orientation = "Y"
    qwm_doc.MeshY_E_56.Position = -43.8409
    qwm_doc.MeshY_E_56.Length = 13.4
    qwm_doc.MeshY_E_56.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_56.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_56.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_56.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_57")
    qwm_doc.MeshY_E_57.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -42.22726, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_57.Orientation = "Y"
    qwm_doc.MeshY_E_57.Position = -42.22726
    qwm_doc.MeshY_E_57.Length = 13.4
    qwm_doc.MeshY_E_57.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_57.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_57.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_57.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_58")
    qwm_doc.MeshY_E_58.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -40.61363, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_58.Orientation = "Y"
    qwm_doc.MeshY_E_58.Position = -40.61363
    qwm_doc.MeshY_E_58.Length = 13.4
    qwm_doc.MeshY_E_58.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_58.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_58.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_58.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_59")
    qwm_doc.MeshY_E_59.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -39.0, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_59.Orientation = "Y"
    qwm_doc.MeshY_E_59.Position = -39.0
    qwm_doc.MeshY_E_59.Length = 13.4
    qwm_doc.MeshY_E_59.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_59.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_59.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_59.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_60")
    qwm_doc.MeshY_E_60.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -37.30435, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_60.Orientation = "Y"
    qwm_doc.MeshY_E_60.Position = -37.30435
    qwm_doc.MeshY_E_60.Length = 13.4
    qwm_doc.MeshY_E_60.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_60.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_60.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_60.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_61")
    qwm_doc.MeshY_E_61.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -35.6087, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_61.Orientation = "Y"
    qwm_doc.MeshY_E_61.Position = -35.6087
    qwm_doc.MeshY_E_61.Length = 13.4
    qwm_doc.MeshY_E_61.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_61.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_61.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_61.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_62")
    qwm_doc.MeshY_E_62.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -33.91304, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_62.Orientation = "Y"
    qwm_doc.MeshY_E_62.Position = -33.91304
    qwm_doc.MeshY_E_62.Length = 13.4
    qwm_doc.MeshY_E_62.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_62.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_62.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_62.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_63")
    qwm_doc.MeshY_E_63.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -32.21739, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_63.Orientation = "Y"
    qwm_doc.MeshY_E_63.Position = -32.21739
    qwm_doc.MeshY_E_63.Length = 13.4
    qwm_doc.MeshY_E_63.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_63.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_63.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_63.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_64")
    qwm_doc.MeshY_E_64.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -30.52174, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_64.Orientation = "Y"
    qwm_doc.MeshY_E_64.Position = -30.52174
    qwm_doc.MeshY_E_64.Length = 13.4
    qwm_doc.MeshY_E_64.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_64.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_64.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_64.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_65")
    qwm_doc.MeshY_E_65.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -28.82609, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_65.Orientation = "Y"
    qwm_doc.MeshY_E_65.Position = -28.82609
    qwm_doc.MeshY_E_65.Length = 13.4
    qwm_doc.MeshY_E_65.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_65.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_65.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_65.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_66")
    qwm_doc.MeshY_E_66.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -27.13043, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_66.Orientation = "Y"
    qwm_doc.MeshY_E_66.Position = -27.13043
    qwm_doc.MeshY_E_66.Length = 13.4
    qwm_doc.MeshY_E_66.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_66.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_66.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_66.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_67")
    qwm_doc.MeshY_E_67.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -25.43478, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_67.Orientation = "Y"
    qwm_doc.MeshY_E_67.Position = -25.43478
    qwm_doc.MeshY_E_67.Length = 13.4
    qwm_doc.MeshY_E_67.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_67.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_67.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_67.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_68")
    qwm_doc.MeshY_E_68.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -23.73913, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_68.Orientation = "Y"
    qwm_doc.MeshY_E_68.Position = -23.73913
    qwm_doc.MeshY_E_68.Length = 13.4
    qwm_doc.MeshY_E_68.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_68.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_68.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_68.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_69")
    qwm_doc.MeshY_E_69.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -22.04348, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_69.Orientation = "Y"
    qwm_doc.MeshY_E_69.Position = -22.04348
    qwm_doc.MeshY_E_69.Length = 13.4
    qwm_doc.MeshY_E_69.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_69.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_69.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_69.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_70")
    qwm_doc.MeshY_E_70.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -20.34783, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_70.Orientation = "Y"
    qwm_doc.MeshY_E_70.Position = -20.34783
    qwm_doc.MeshY_E_70.Length = 13.4
    qwm_doc.MeshY_E_70.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_70.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_70.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_70.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_71")
    qwm_doc.MeshY_E_71.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -18.65217, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_71.Orientation = "Y"
    qwm_doc.MeshY_E_71.Position = -18.65217
    qwm_doc.MeshY_E_71.Length = 13.4
    qwm_doc.MeshY_E_71.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_71.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_71.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_71.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_72")
    qwm_doc.MeshY_E_72.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -16.95652, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_72.Orientation = "Y"
    qwm_doc.MeshY_E_72.Position = -16.95652
    qwm_doc.MeshY_E_72.Length = 13.4
    qwm_doc.MeshY_E_72.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_72.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_72.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_72.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_73")
    qwm_doc.MeshY_E_73.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -15.26087, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_73.Orientation = "Y"
    qwm_doc.MeshY_E_73.Position = -15.26087
    qwm_doc.MeshY_E_73.Length = 13.4
    qwm_doc.MeshY_E_73.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_73.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_73.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_73.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_74")
    qwm_doc.MeshY_E_74.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -13.56522, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_74.Orientation = "Y"
    qwm_doc.MeshY_E_74.Position = -13.56522
    qwm_doc.MeshY_E_74.Length = 13.4
    qwm_doc.MeshY_E_74.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_74.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_74.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_74.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_75")
    qwm_doc.MeshY_E_75.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -11.86957, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_75.Orientation = "Y"
    qwm_doc.MeshY_E_75.Position = -11.86957
    qwm_doc.MeshY_E_75.Length = 13.4
    qwm_doc.MeshY_E_75.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_75.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_75.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_75.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_76")
    qwm_doc.MeshY_E_76.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -10.17391, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_76.Orientation = "Y"
    qwm_doc.MeshY_E_76.Position = -10.17391
    qwm_doc.MeshY_E_76.Length = 13.4
    qwm_doc.MeshY_E_76.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_76.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_76.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_76.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_77")
    qwm_doc.MeshY_E_77.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -8.47826, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_77.Orientation = "Y"
    qwm_doc.MeshY_E_77.Position = -8.47826
    qwm_doc.MeshY_E_77.Length = 13.4
    qwm_doc.MeshY_E_77.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_77.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_77.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_77.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_78")
    qwm_doc.MeshY_E_78.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -6.78261, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_78.Orientation = "Y"
    qwm_doc.MeshY_E_78.Position = -6.78261
    qwm_doc.MeshY_E_78.Length = 13.4
    qwm_doc.MeshY_E_78.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_78.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_78.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_78.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_79")
    qwm_doc.MeshY_E_79.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -5.08696, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_79.Orientation = "Y"
    qwm_doc.MeshY_E_79.Position = -5.08696
    qwm_doc.MeshY_E_79.Length = 13.4
    qwm_doc.MeshY_E_79.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_79.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_79.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_79.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_80")
    qwm_doc.MeshY_E_80.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -3.3913, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_80.Orientation = "Y"
    qwm_doc.MeshY_E_80.Position = -3.3913
    qwm_doc.MeshY_E_80.Length = 13.4
    qwm_doc.MeshY_E_80.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_80.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_80.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_80.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_81")
    qwm_doc.MeshY_E_81.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -1.69565, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_81.Orientation = "Y"
    qwm_doc.MeshY_E_81.Position = -1.69565
    qwm_doc.MeshY_E_81.Length = 13.4
    qwm_doc.MeshY_E_81.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_81.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_81.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_81.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_82")
    qwm_doc.MeshY_E_82.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 0.0, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_82.Orientation = "Y"
    qwm_doc.MeshY_E_82.Position = 0.0
    qwm_doc.MeshY_E_82.Length = 13.4
    qwm_doc.MeshY_E_82.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_82.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_82.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_82.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_83")
    qwm_doc.MeshY_E_83.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 1.69565, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_83.Orientation = "Y"
    qwm_doc.MeshY_E_83.Position = 1.69565
    qwm_doc.MeshY_E_83.Length = 13.4
    qwm_doc.MeshY_E_83.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_83.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_83.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_83.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_84")
    qwm_doc.MeshY_E_84.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 3.3913, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_84.Orientation = "Y"
    qwm_doc.MeshY_E_84.Position = 3.3913
    qwm_doc.MeshY_E_84.Length = 13.4
    qwm_doc.MeshY_E_84.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_84.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_84.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_84.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_85")
    qwm_doc.MeshY_E_85.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 5.08696, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_85.Orientation = "Y"
    qwm_doc.MeshY_E_85.Position = 5.08696
    qwm_doc.MeshY_E_85.Length = 13.4
    qwm_doc.MeshY_E_85.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_85.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_85.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_85.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_86")
    qwm_doc.MeshY_E_86.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 6.78261, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_86.Orientation = "Y"
    qwm_doc.MeshY_E_86.Position = 6.78261
    qwm_doc.MeshY_E_86.Length = 13.4
    qwm_doc.MeshY_E_86.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_86.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_86.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_86.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_87")
    qwm_doc.MeshY_E_87.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 8.47826, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_87.Orientation = "Y"
    qwm_doc.MeshY_E_87.Position = 8.47826
    qwm_doc.MeshY_E_87.Length = 13.4
    qwm_doc.MeshY_E_87.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_87.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_87.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_87.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_88")
    qwm_doc.MeshY_E_88.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 10.17391, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_88.Orientation = "Y"
    qwm_doc.MeshY_E_88.Position = 10.17391
    qwm_doc.MeshY_E_88.Length = 13.4
    qwm_doc.MeshY_E_88.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_88.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_88.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_88.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_89")
    qwm_doc.MeshY_E_89.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 11.86957, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_89.Orientation = "Y"
    qwm_doc.MeshY_E_89.Position = 11.86957
    qwm_doc.MeshY_E_89.Length = 13.4
    qwm_doc.MeshY_E_89.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_89.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_89.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_89.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_90")
    qwm_doc.MeshY_E_90.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 13.56522, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_90.Orientation = "Y"
    qwm_doc.MeshY_E_90.Position = 13.56522
    qwm_doc.MeshY_E_90.Length = 13.4
    qwm_doc.MeshY_E_90.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_90.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_90.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_90.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_91")
    qwm_doc.MeshY_E_91.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 15.26087, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_91.Orientation = "Y"
    qwm_doc.MeshY_E_91.Position = 15.26087
    qwm_doc.MeshY_E_91.Length = 13.4
    qwm_doc.MeshY_E_91.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_91.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_91.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_91.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_92")
    qwm_doc.MeshY_E_92.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 16.95652, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_92.Orientation = "Y"
    qwm_doc.MeshY_E_92.Position = 16.95652
    qwm_doc.MeshY_E_92.Length = 13.4
    qwm_doc.MeshY_E_92.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_92.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_92.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_92.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_93")
    qwm_doc.MeshY_E_93.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 18.65217, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_93.Orientation = "Y"
    qwm_doc.MeshY_E_93.Position = 18.65217
    qwm_doc.MeshY_E_93.Length = 13.4
    qwm_doc.MeshY_E_93.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_93.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_93.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_93.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_94")
    qwm_doc.MeshY_E_94.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 20.34783, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_94.Orientation = "Y"
    qwm_doc.MeshY_E_94.Position = 20.34783
    qwm_doc.MeshY_E_94.Length = 13.4
    qwm_doc.MeshY_E_94.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_94.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_94.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_94.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_95")
    qwm_doc.MeshY_E_95.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 22.04348, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_95.Orientation = "Y"
    qwm_doc.MeshY_E_95.Position = 22.04348
    qwm_doc.MeshY_E_95.Length = 13.4
    qwm_doc.MeshY_E_95.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_95.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_95.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_95.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_96")
    qwm_doc.MeshY_E_96.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 23.73913, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_96.Orientation = "Y"
    qwm_doc.MeshY_E_96.Position = 23.73913
    qwm_doc.MeshY_E_96.Length = 13.4
    qwm_doc.MeshY_E_96.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_96.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_96.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_96.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_97")
    qwm_doc.MeshY_E_97.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 25.43478, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_97.Orientation = "Y"
    qwm_doc.MeshY_E_97.Position = 25.43478
    qwm_doc.MeshY_E_97.Length = 13.4
    qwm_doc.MeshY_E_97.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_97.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_97.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_97.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_98")
    qwm_doc.MeshY_E_98.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 27.13043, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_98.Orientation = "Y"
    qwm_doc.MeshY_E_98.Position = 27.13043
    qwm_doc.MeshY_E_98.Length = 13.4
    qwm_doc.MeshY_E_98.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_98.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_98.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_98.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_99")
    qwm_doc.MeshY_E_99.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 28.82609, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_99.Orientation = "Y"
    qwm_doc.MeshY_E_99.Position = 28.82609
    qwm_doc.MeshY_E_99.Length = 13.4
    qwm_doc.MeshY_E_99.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_99.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_99.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_99.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_100")
    qwm_doc.MeshY_E_100.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 30.52174, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_100.Orientation = "Y"
    qwm_doc.MeshY_E_100.Position = 30.52174
    qwm_doc.MeshY_E_100.Length = 13.4
    qwm_doc.MeshY_E_100.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_100.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_100.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_100.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_101")
    qwm_doc.MeshY_E_101.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 32.21739, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_101.Orientation = "Y"
    qwm_doc.MeshY_E_101.Position = 32.21739
    qwm_doc.MeshY_E_101.Length = 13.4
    qwm_doc.MeshY_E_101.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_101.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_101.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_101.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_102")
    qwm_doc.MeshY_E_102.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 33.91304, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_102.Orientation = "Y"
    qwm_doc.MeshY_E_102.Position = 33.91304
    qwm_doc.MeshY_E_102.Length = 13.4
    qwm_doc.MeshY_E_102.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_102.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_102.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_102.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_103")
    qwm_doc.MeshY_E_103.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 35.6087, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_103.Orientation = "Y"
    qwm_doc.MeshY_E_103.Position = 35.6087
    qwm_doc.MeshY_E_103.Length = 13.4
    qwm_doc.MeshY_E_103.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_103.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_103.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_103.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_104")
    qwm_doc.MeshY_E_104.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 37.30435, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_104.Orientation = "Y"
    qwm_doc.MeshY_E_104.Position = 37.30435
    qwm_doc.MeshY_E_104.Length = 13.4
    qwm_doc.MeshY_E_104.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_104.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_104.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_104.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_105")
    qwm_doc.MeshY_E_105.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 39.0, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_105.Orientation = "Y"
    qwm_doc.MeshY_E_105.Position = 39.0
    qwm_doc.MeshY_E_105.Length = 13.4
    qwm_doc.MeshY_E_105.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_105.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_105.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_105.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_106")
    qwm_doc.MeshY_E_106.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 40.61363, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_106.Orientation = "Y"
    qwm_doc.MeshY_E_106.Position = 40.61363
    qwm_doc.MeshY_E_106.Length = 13.4
    qwm_doc.MeshY_E_106.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_106.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_106.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_106.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_107")
    qwm_doc.MeshY_E_107.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 42.22726, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_107.Orientation = "Y"
    qwm_doc.MeshY_E_107.Position = 42.22726
    qwm_doc.MeshY_E_107.Length = 13.4
    qwm_doc.MeshY_E_107.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_107.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_107.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_107.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_108")
    qwm_doc.MeshY_E_108.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 43.8409, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_108.Orientation = "Y"
    qwm_doc.MeshY_E_108.Position = 43.8409
    qwm_doc.MeshY_E_108.Length = 13.4
    qwm_doc.MeshY_E_108.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_108.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_108.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_108.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_109")
    qwm_doc.MeshY_E_109.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 45.45453, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_109.Orientation = "Y"
    qwm_doc.MeshY_E_109.Position = 45.45453
    qwm_doc.MeshY_E_109.Length = 13.4
    qwm_doc.MeshY_E_109.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_109.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_109.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_109.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_110")
    qwm_doc.MeshY_E_110.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 47.06816, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_110.Orientation = "Y"
    qwm_doc.MeshY_E_110.Position = 47.06816
    qwm_doc.MeshY_E_110.Length = 13.4
    qwm_doc.MeshY_E_110.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_110.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_110.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_110.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_111")
    qwm_doc.MeshY_E_111.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 48.68179, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_111.Orientation = "Y"
    qwm_doc.MeshY_E_111.Position = 48.68179
    qwm_doc.MeshY_E_111.Length = 13.4
    qwm_doc.MeshY_E_111.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_111.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_111.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_111.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_112")
    qwm_doc.MeshY_E_112.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 50.29543, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_112.Orientation = "Y"
    qwm_doc.MeshY_E_112.Position = 50.29543
    qwm_doc.MeshY_E_112.Length = 13.4
    qwm_doc.MeshY_E_112.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_112.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_112.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_112.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_113")
    qwm_doc.MeshY_E_113.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 51.90906, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_113.Orientation = "Y"
    qwm_doc.MeshY_E_113.Position = 51.90906
    qwm_doc.MeshY_E_113.Length = 13.4
    qwm_doc.MeshY_E_113.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_113.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_113.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_113.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_114")
    qwm_doc.MeshY_E_114.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 53.52269, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_114.Orientation = "Y"
    qwm_doc.MeshY_E_114.Position = 53.52269
    qwm_doc.MeshY_E_114.Length = 13.4
    qwm_doc.MeshY_E_114.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_114.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_114.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_114.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_115")
    qwm_doc.MeshY_E_115.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 55.13632, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_115.Orientation = "Y"
    qwm_doc.MeshY_E_115.Position = 55.13632
    qwm_doc.MeshY_E_115.Length = 13.4
    qwm_doc.MeshY_E_115.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_115.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_115.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_115.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_116")
    qwm_doc.MeshY_E_116.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 56.74996, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_116.Orientation = "Y"
    qwm_doc.MeshY_E_116.Position = 56.74996
    qwm_doc.MeshY_E_116.Length = 13.4
    qwm_doc.MeshY_E_116.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_116.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_116.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_116.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_117")
    qwm_doc.MeshY_E_117.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 58.36359, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_117.Orientation = "Y"
    qwm_doc.MeshY_E_117.Position = 58.36359
    qwm_doc.MeshY_E_117.Length = 13.4
    qwm_doc.MeshY_E_117.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_117.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_117.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_117.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_118")
    qwm_doc.MeshY_E_118.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 59.97722, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_118.Orientation = "Y"
    qwm_doc.MeshY_E_118.Position = 59.97722
    qwm_doc.MeshY_E_118.Length = 13.4
    qwm_doc.MeshY_E_118.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_118.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_118.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_118.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_119")
    qwm_doc.MeshY_E_119.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 61.64981, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_119.Orientation = "Y"
    qwm_doc.MeshY_E_119.Position = 61.64981
    qwm_doc.MeshY_E_119.Length = 13.4
    qwm_doc.MeshY_E_119.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_119.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_119.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_119.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_120")
    qwm_doc.MeshY_E_120.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 63.32239, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_120.Orientation = "Y"
    qwm_doc.MeshY_E_120.Position = 63.32239
    qwm_doc.MeshY_E_120.Length = 13.4
    qwm_doc.MeshY_E_120.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_120.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_120.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_120.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_121")
    qwm_doc.MeshY_E_121.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 64.99498, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_121.Orientation = "Y"
    qwm_doc.MeshY_E_121.Position = 64.99498
    qwm_doc.MeshY_E_121.Length = 13.4
    qwm_doc.MeshY_E_121.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_121.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_121.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_121.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_122")
    qwm_doc.MeshY_E_122.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 66.66757, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_122.Orientation = "Y"
    qwm_doc.MeshY_E_122.Position = 66.66757
    qwm_doc.MeshY_E_122.Length = 13.4
    qwm_doc.MeshY_E_122.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_122.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_122.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_122.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_123")
    qwm_doc.MeshY_E_123.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 68.34015, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_123.Orientation = "Y"
    qwm_doc.MeshY_E_123.Position = 68.34015
    qwm_doc.MeshY_E_123.Length = 13.4
    qwm_doc.MeshY_E_123.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_123.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_123.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_123.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_124")
    qwm_doc.MeshY_E_124.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 70.01274, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_124.Orientation = "Y"
    qwm_doc.MeshY_E_124.Position = 70.01274
    qwm_doc.MeshY_E_124.Length = 13.4
    qwm_doc.MeshY_E_124.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_124.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_124.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_124.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_125")
    qwm_doc.MeshY_E_125.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 71.68533, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_125.Orientation = "Y"
    qwm_doc.MeshY_E_125.Position = 71.68533
    qwm_doc.MeshY_E_125.Length = 13.4
    qwm_doc.MeshY_E_125.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_125.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_125.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_125.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_126")
    qwm_doc.MeshY_E_126.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 73.35792, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_126.Orientation = "Y"
    qwm_doc.MeshY_E_126.Position = 73.35792
    qwm_doc.MeshY_E_126.Length = 13.4
    qwm_doc.MeshY_E_126.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_126.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_126.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_126.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_127")
    qwm_doc.MeshY_E_127.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 75.0305, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_127.Orientation = "Y"
    qwm_doc.MeshY_E_127.Position = 75.0305
    qwm_doc.MeshY_E_127.Length = 13.4
    qwm_doc.MeshY_E_127.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_127.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_127.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_127.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_128")
    qwm_doc.MeshY_E_128.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 76.70309, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_128.Orientation = "Y"
    qwm_doc.MeshY_E_128.Position = 76.70309
    qwm_doc.MeshY_E_128.Length = 13.4
    qwm_doc.MeshY_E_128.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_128.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_128.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_128.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_129")
    qwm_doc.MeshY_E_129.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 78.37568, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_129.Orientation = "Y"
    qwm_doc.MeshY_E_129.Position = 78.37568
    qwm_doc.MeshY_E_129.Length = 13.4
    qwm_doc.MeshY_E_129.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_129.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_129.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_129.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_130")
    qwm_doc.MeshY_E_130.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 80.04826, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_130.Orientation = "Y"
    qwm_doc.MeshY_E_130.Position = 80.04826
    qwm_doc.MeshY_E_130.Length = 13.4
    qwm_doc.MeshY_E_130.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_130.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_130.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_130.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_131")
    qwm_doc.MeshY_E_131.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 81.72085, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_131.Orientation = "Y"
    qwm_doc.MeshY_E_131.Position = 81.72085
    qwm_doc.MeshY_E_131.Length = 13.4
    qwm_doc.MeshY_E_131.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_131.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_131.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_131.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_132")
    qwm_doc.MeshY_E_132.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 83.39344, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_132.Orientation = "Y"
    qwm_doc.MeshY_E_132.Position = 83.39344
    qwm_doc.MeshY_E_132.Length = 13.4
    qwm_doc.MeshY_E_132.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_132.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_132.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_132.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_133")
    qwm_doc.MeshY_E_133.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 85.06602, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_133.Orientation = "Y"
    qwm_doc.MeshY_E_133.Position = 85.06602
    qwm_doc.MeshY_E_133.Length = 13.4
    qwm_doc.MeshY_E_133.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_133.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_133.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_133.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_134")
    qwm_doc.MeshY_E_134.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 86.73861, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_134.Orientation = "Y"
    qwm_doc.MeshY_E_134.Position = 86.73861
    qwm_doc.MeshY_E_134.Length = 13.4
    qwm_doc.MeshY_E_134.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_134.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_134.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_134.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_135")
    qwm_doc.MeshY_E_135.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 88.4112, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_135.Orientation = "Y"
    qwm_doc.MeshY_E_135.Position = 88.4112
    qwm_doc.MeshY_E_135.Length = 13.4
    qwm_doc.MeshY_E_135.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_135.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_135.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_135.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_136")
    qwm_doc.MeshY_E_136.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 90.08378, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_136.Orientation = "Y"
    qwm_doc.MeshY_E_136.Position = 90.08378
    qwm_doc.MeshY_E_136.Length = 13.4
    qwm_doc.MeshY_E_136.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_136.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_136.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_136.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_137")
    qwm_doc.MeshY_E_137.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 91.75637, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_137.Orientation = "Y"
    qwm_doc.MeshY_E_137.Position = 91.75637
    qwm_doc.MeshY_E_137.Length = 13.4
    qwm_doc.MeshY_E_137.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_137.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_137.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_137.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_138")
    qwm_doc.MeshY_E_138.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 93.42896, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_138.Orientation = "Y"
    qwm_doc.MeshY_E_138.Position = 93.42896
    qwm_doc.MeshY_E_138.Length = 13.4
    qwm_doc.MeshY_E_138.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_138.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_138.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_138.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_139")
    qwm_doc.MeshY_E_139.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 95.10154, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_139.Orientation = "Y"
    qwm_doc.MeshY_E_139.Position = 95.10154
    qwm_doc.MeshY_E_139.Length = 13.4
    qwm_doc.MeshY_E_139.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_139.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_139.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_139.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_140")
    qwm_doc.MeshY_E_140.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 96.77413, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_140.Orientation = "Y"
    qwm_doc.MeshY_E_140.Position = 96.77413
    qwm_doc.MeshY_E_140.Length = 13.4
    qwm_doc.MeshY_E_140.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_140.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_140.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_140.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_141")
    qwm_doc.MeshY_E_141.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 98.44672, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_141.Orientation = "Y"
    qwm_doc.MeshY_E_141.Position = 98.44672
    qwm_doc.MeshY_E_141.Length = 13.4
    qwm_doc.MeshY_E_141.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_141.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_141.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_141.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_142")
    qwm_doc.MeshY_E_142.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 100.1193, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_142.Orientation = "Y"
    qwm_doc.MeshY_E_142.Position = 100.1193
    qwm_doc.MeshY_E_142.Length = 13.4
    qwm_doc.MeshY_E_142.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_142.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_142.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_142.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_143")
    qwm_doc.MeshY_E_143.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 101.79189, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_143.Orientation = "Y"
    qwm_doc.MeshY_E_143.Position = 101.79189
    qwm_doc.MeshY_E_143.Length = 13.4
    qwm_doc.MeshY_E_143.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_143.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_143.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_143.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_144")
    qwm_doc.MeshY_E_144.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 103.46448, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_144.Orientation = "Y"
    qwm_doc.MeshY_E_144.Position = 103.46448
    qwm_doc.MeshY_E_144.Length = 13.4
    qwm_doc.MeshY_E_144.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_144.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_144.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_144.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_145")
    qwm_doc.MeshY_E_145.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 105.13707, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_145.Orientation = "Y"
    qwm_doc.MeshY_E_145.Position = 105.13707
    qwm_doc.MeshY_E_145.Length = 13.4
    qwm_doc.MeshY_E_145.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_145.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_145.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_145.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_146")
    qwm_doc.MeshY_E_146.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 106.80965, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_146.Orientation = "Y"
    qwm_doc.MeshY_E_146.Position = 106.80965
    qwm_doc.MeshY_E_146.Length = 13.4
    qwm_doc.MeshY_E_146.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_146.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_146.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_146.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_147")
    qwm_doc.MeshY_E_147.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 108.48224, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_147.Orientation = "Y"
    qwm_doc.MeshY_E_147.Position = 108.48224
    qwm_doc.MeshY_E_147.Length = 13.4
    qwm_doc.MeshY_E_147.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_147.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_147.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_147.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_148")
    qwm_doc.MeshY_E_148.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 110.15483, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_148.Orientation = "Y"
    qwm_doc.MeshY_E_148.Position = 110.15483
    qwm_doc.MeshY_E_148.Length = 13.4
    qwm_doc.MeshY_E_148.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_148.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_148.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_148.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_149")
    qwm_doc.MeshY_E_149.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 111.82741, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_149.Orientation = "Y"
    qwm_doc.MeshY_E_149.Position = 111.82741
    qwm_doc.MeshY_E_149.Length = 13.4
    qwm_doc.MeshY_E_149.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_149.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_149.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_149.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_150")
    qwm_doc.MeshY_E_150.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 113.5, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_150.Orientation = "Y"
    qwm_doc.MeshY_E_150.Position = 113.5
    qwm_doc.MeshY_E_150.Length = 13.4
    qwm_doc.MeshY_E_150.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_150.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_150.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_150.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_151")
    qwm_doc.MeshY_E_151.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 115.15385, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_151.Orientation = "Y"
    qwm_doc.MeshY_E_151.Position = 115.15385
    qwm_doc.MeshY_E_151.Length = 13.4
    qwm_doc.MeshY_E_151.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_151.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_151.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_151.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_152")
    qwm_doc.MeshY_E_152.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 116.80769, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_152.Orientation = "Y"
    qwm_doc.MeshY_E_152.Position = 116.80769
    qwm_doc.MeshY_E_152.Length = 13.4
    qwm_doc.MeshY_E_152.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_152.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_152.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_152.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_153")
    qwm_doc.MeshY_E_153.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 118.46154, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_153.Orientation = "Y"
    qwm_doc.MeshY_E_153.Position = 118.46154
    qwm_doc.MeshY_E_153.Length = 13.4
    qwm_doc.MeshY_E_153.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_153.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_153.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_153.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_154")
    qwm_doc.MeshY_E_154.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 120.11538, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_154.Orientation = "Y"
    qwm_doc.MeshY_E_154.Position = 120.11538
    qwm_doc.MeshY_E_154.Length = 13.4
    qwm_doc.MeshY_E_154.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_154.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_154.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_154.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_155")
    qwm_doc.MeshY_E_155.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 121.76923, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_155.Orientation = "Y"
    qwm_doc.MeshY_E_155.Position = 121.76923
    qwm_doc.MeshY_E_155.Length = 13.4
    qwm_doc.MeshY_E_155.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_155.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_155.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_155.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_156")
    qwm_doc.MeshY_E_156.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 123.42308, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_156.Orientation = "Y"
    qwm_doc.MeshY_E_156.Position = 123.42308
    qwm_doc.MeshY_E_156.Length = 13.4
    qwm_doc.MeshY_E_156.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_156.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_156.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_156.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_157")
    qwm_doc.MeshY_E_157.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 125.07692, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_157.Orientation = "Y"
    qwm_doc.MeshY_E_157.Position = 125.07692
    qwm_doc.MeshY_E_157.Length = 13.4
    qwm_doc.MeshY_E_157.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_157.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_157.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_157.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_158")
    qwm_doc.MeshY_E_158.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 126.73077, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_158.Orientation = "Y"
    qwm_doc.MeshY_E_158.Position = 126.73077
    qwm_doc.MeshY_E_158.Length = 13.4
    qwm_doc.MeshY_E_158.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_158.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_158.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_158.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_159")
    qwm_doc.MeshY_E_159.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 128.38462, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_159.Orientation = "Y"
    qwm_doc.MeshY_E_159.Position = 128.38462
    qwm_doc.MeshY_E_159.Length = 13.4
    qwm_doc.MeshY_E_159.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_159.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_159.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_159.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_160")
    qwm_doc.MeshY_E_160.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 130.03846, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_160.Orientation = "Y"
    qwm_doc.MeshY_E_160.Position = 130.03846
    qwm_doc.MeshY_E_160.Length = 13.4
    qwm_doc.MeshY_E_160.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_160.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_160.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_160.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_161")
    qwm_doc.MeshY_E_161.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 131.69231, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_161.Orientation = "Y"
    qwm_doc.MeshY_E_161.Position = 131.69231
    qwm_doc.MeshY_E_161.Length = 13.4
    qwm_doc.MeshY_E_161.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_161.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_161.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_161.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_162")
    qwm_doc.MeshY_E_162.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 133.34615, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_162.Orientation = "Y"
    qwm_doc.MeshY_E_162.Position = 133.34615
    qwm_doc.MeshY_E_162.Length = 13.4
    qwm_doc.MeshY_E_162.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_162.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_162.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_162.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshY_E_163")
    qwm_doc.MeshY_E_163.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, 135.0, 6.7),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.MeshY_E_163.Orientation = "Y"
    qwm_doc.MeshY_E_163.Position = 135.0
    qwm_doc.MeshY_E_163.Length = 13.4
    qwm_doc.MeshY_E_163.Width = 26.700000000000003
    FreeCAD.Gui.ActiveDocument.MeshY_E_163.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshY_E_163.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshY_E_163.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_1")
    qwm_doc.MeshZ_E_1.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_1.Orientation = "Z"
    qwm_doc.MeshZ_E_1.Position = 0.0
    qwm_doc.MeshZ_E_1.Length = 26.700000000000003
    qwm_doc.MeshZ_E_1.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_1.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_1.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_1.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_2")
    qwm_doc.MeshZ_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 7.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_2.Orientation = "Z"
    qwm_doc.MeshZ_E_2.Position = 7.5
    qwm_doc.MeshZ_E_2.Length = 26.700000000000003
    qwm_doc.MeshZ_E_2.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_3")
    qwm_doc.MeshZ_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 15.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_3.Orientation = "Z"
    qwm_doc.MeshZ_E_3.Position = 15.0
    qwm_doc.MeshZ_E_3.Length = 26.700000000000003
    qwm_doc.MeshZ_E_3.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_4")
    qwm_doc.MeshZ_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 16.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_4.Orientation = "Z"
    qwm_doc.MeshZ_E_4.Position = 16.5
    qwm_doc.MeshZ_E_4.Length = 26.700000000000003
    qwm_doc.MeshZ_E_4.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_5")
    qwm_doc.MeshZ_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 18.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_5.Orientation = "Z"
    qwm_doc.MeshZ_E_5.Position = 18.0
    qwm_doc.MeshZ_E_5.Length = 26.700000000000003
    qwm_doc.MeshZ_E_5.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_6")
    qwm_doc.MeshZ_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 19.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_6.Orientation = "Z"
    qwm_doc.MeshZ_E_6.Position = 19.5
    qwm_doc.MeshZ_E_6.Length = 26.700000000000003
    qwm_doc.MeshZ_E_6.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_7")
    qwm_doc.MeshZ_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 21.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_7.Orientation = "Z"
    qwm_doc.MeshZ_E_7.Position = 21.0
    qwm_doc.MeshZ_E_7.Length = 26.700000000000003
    qwm_doc.MeshZ_E_7.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_8")
    qwm_doc.MeshZ_E_8.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 22.66667),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_8.Orientation = "Z"
    qwm_doc.MeshZ_E_8.Position = 22.66667
    qwm_doc.MeshZ_E_8.Length = 26.700000000000003
    qwm_doc.MeshZ_E_8.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_8.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_8.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_8.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_9")
    qwm_doc.MeshZ_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 24.33333),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_9.Orientation = "Z"
    qwm_doc.MeshZ_E_9.Position = 24.33333
    qwm_doc.MeshZ_E_9.Length = 26.700000000000003
    qwm_doc.MeshZ_E_9.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_10")
    qwm_doc.MeshZ_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 26.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_10.Orientation = "Z"
    qwm_doc.MeshZ_E_10.Position = 26.0
    qwm_doc.MeshZ_E_10.Length = 26.700000000000003
    qwm_doc.MeshZ_E_10.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_11")
    qwm_doc.MeshZ_E_11.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 27.66667),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_11.Orientation = "Z"
    qwm_doc.MeshZ_E_11.Position = 27.66667
    qwm_doc.MeshZ_E_11.Length = 26.700000000000003
    qwm_doc.MeshZ_E_11.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_11.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_11.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_11.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_12")
    qwm_doc.MeshZ_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 29.33333),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_12.Orientation = "Z"
    qwm_doc.MeshZ_E_12.Position = 29.33333
    qwm_doc.MeshZ_E_12.Length = 26.700000000000003
    qwm_doc.MeshZ_E_12.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_13")
    qwm_doc.MeshZ_E_13.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 31.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_13.Orientation = "Z"
    qwm_doc.MeshZ_E_13.Position = 31.0
    qwm_doc.MeshZ_E_13.Length = 26.700000000000003
    qwm_doc.MeshZ_E_13.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_13.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_13.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_13.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_14")
    qwm_doc.MeshZ_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 32.66667),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_14.Orientation = "Z"
    qwm_doc.MeshZ_E_14.Position = 32.66667
    qwm_doc.MeshZ_E_14.Length = 26.700000000000003
    qwm_doc.MeshZ_E_14.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_15")
    qwm_doc.MeshZ_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 34.33333),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_15.Orientation = "Z"
    qwm_doc.MeshZ_E_15.Position = 34.33333
    qwm_doc.MeshZ_E_15.Length = 26.700000000000003
    qwm_doc.MeshZ_E_15.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_16")
    qwm_doc.MeshZ_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 36.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_16.Orientation = "Z"
    qwm_doc.MeshZ_E_16.Position = 36.0
    qwm_doc.MeshZ_E_16.Length = 26.700000000000003
    qwm_doc.MeshZ_E_16.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_17")
    qwm_doc.MeshZ_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 37.66667),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_17.Orientation = "Z"
    qwm_doc.MeshZ_E_17.Position = 37.66667
    qwm_doc.MeshZ_E_17.Length = 26.700000000000003
    qwm_doc.MeshZ_E_17.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_18")
    qwm_doc.MeshZ_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 39.33333),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_18.Orientation = "Z"
    qwm_doc.MeshZ_E_18.Position = 39.33333
    qwm_doc.MeshZ_E_18.Length = 26.700000000000003
    qwm_doc.MeshZ_E_18.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_19")
    qwm_doc.MeshZ_E_19.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 41.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_19.Orientation = "Z"
    qwm_doc.MeshZ_E_19.Position = 41.0
    qwm_doc.MeshZ_E_19.Length = 26.700000000000003
    qwm_doc.MeshZ_E_19.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_19.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_19.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_19.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_20")
    qwm_doc.MeshZ_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 42.66667),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_20.Orientation = "Z"
    qwm_doc.MeshZ_E_20.Position = 42.66667
    qwm_doc.MeshZ_E_20.Length = 26.700000000000003
    qwm_doc.MeshZ_E_20.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_21")
    qwm_doc.MeshZ_E_21.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 44.33333),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_21.Orientation = "Z"
    qwm_doc.MeshZ_E_21.Position = 44.33333
    qwm_doc.MeshZ_E_21.Length = 26.700000000000003
    qwm_doc.MeshZ_E_21.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_21.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_21.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_21.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_22")
    qwm_doc.MeshZ_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 46.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_22.Orientation = "Z"
    qwm_doc.MeshZ_E_22.Position = 46.0
    qwm_doc.MeshZ_E_22.Length = 26.700000000000003
    qwm_doc.MeshZ_E_22.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_23")
    qwm_doc.MeshZ_E_23.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 47.66667),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_23.Orientation = "Z"
    qwm_doc.MeshZ_E_23.Position = 47.66667
    qwm_doc.MeshZ_E_23.Length = 26.700000000000003
    qwm_doc.MeshZ_E_23.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_23.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_23.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_23.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_24")
    qwm_doc.MeshZ_E_24.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 49.33333),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_24.Orientation = "Z"
    qwm_doc.MeshZ_E_24.Position = 49.33333
    qwm_doc.MeshZ_E_24.Length = 26.700000000000003
    qwm_doc.MeshZ_E_24.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_24.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_24.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_24.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_25")
    qwm_doc.MeshZ_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 51.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_25.Orientation = "Z"
    qwm_doc.MeshZ_E_25.Position = 51.0
    qwm_doc.MeshZ_E_25.Length = 26.700000000000003
    qwm_doc.MeshZ_E_25.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_26")
    qwm_doc.MeshZ_E_26.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 52.66667),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_26.Orientation = "Z"
    qwm_doc.MeshZ_E_26.Position = 52.66667
    qwm_doc.MeshZ_E_26.Length = 26.700000000000003
    qwm_doc.MeshZ_E_26.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_26.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_26.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_26.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_27")
    qwm_doc.MeshZ_E_27.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 54.33333),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_27.Orientation = "Z"
    qwm_doc.MeshZ_E_27.Position = 54.33333
    qwm_doc.MeshZ_E_27.Length = 26.700000000000003
    qwm_doc.MeshZ_E_27.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_27.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_27.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_27.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_28")
    qwm_doc.MeshZ_E_28.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 56.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_28.Orientation = "Z"
    qwm_doc.MeshZ_E_28.Position = 56.0
    qwm_doc.MeshZ_E_28.Length = 26.700000000000003
    qwm_doc.MeshZ_E_28.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_28.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_28.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_28.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_29")
    qwm_doc.MeshZ_E_29.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 57.7),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_29.Orientation = "Z"
    qwm_doc.MeshZ_E_29.Position = 57.7
    qwm_doc.MeshZ_E_29.Length = 26.700000000000003
    qwm_doc.MeshZ_E_29.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_29.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_29.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_29.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_30")
    qwm_doc.MeshZ_E_30.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 59.4),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_30.Orientation = "Z"
    qwm_doc.MeshZ_E_30.Position = 59.4
    qwm_doc.MeshZ_E_30.Length = 26.700000000000003
    qwm_doc.MeshZ_E_30.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_30.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_30.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_30.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_31")
    qwm_doc.MeshZ_E_31.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 61.1),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_31.Orientation = "Z"
    qwm_doc.MeshZ_E_31.Position = 61.1
    qwm_doc.MeshZ_E_31.Length = 26.700000000000003
    qwm_doc.MeshZ_E_31.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_31.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_31.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_31.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_32")
    qwm_doc.MeshZ_E_32.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 72.63636),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_32.Orientation = "Z"
    qwm_doc.MeshZ_E_32.Position = 72.63636
    qwm_doc.MeshZ_E_32.Length = 26.700000000000003
    qwm_doc.MeshZ_E_32.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_32.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_32.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_32.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_33")
    qwm_doc.MeshZ_E_33.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 84.17273),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_33.Orientation = "Z"
    qwm_doc.MeshZ_E_33.Position = 84.17273
    qwm_doc.MeshZ_E_33.Length = 26.700000000000003
    qwm_doc.MeshZ_E_33.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_33.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_33.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_33.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_34")
    qwm_doc.MeshZ_E_34.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 95.70909),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_34.Orientation = "Z"
    qwm_doc.MeshZ_E_34.Position = 95.70909
    qwm_doc.MeshZ_E_34.Length = 26.700000000000003
    qwm_doc.MeshZ_E_34.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_34.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_34.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_34.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_35")
    qwm_doc.MeshZ_E_35.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 107.24545),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_35.Orientation = "Z"
    qwm_doc.MeshZ_E_35.Position = 107.24545
    qwm_doc.MeshZ_E_35.Length = 26.700000000000003
    qwm_doc.MeshZ_E_35.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_35.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_35.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_35.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_36")
    qwm_doc.MeshZ_E_36.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 118.78182),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_36.Orientation = "Z"
    qwm_doc.MeshZ_E_36.Position = 118.78182
    qwm_doc.MeshZ_E_36.Length = 26.700000000000003
    qwm_doc.MeshZ_E_36.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_36.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_36.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_36.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_37")
    qwm_doc.MeshZ_E_37.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 130.31818),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_37.Orientation = "Z"
    qwm_doc.MeshZ_E_37.Position = 130.31818
    qwm_doc.MeshZ_E_37.Length = 26.700000000000003
    qwm_doc.MeshZ_E_37.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_37.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_37.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_37.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_38")
    qwm_doc.MeshZ_E_38.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 141.85455),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_38.Orientation = "Z"
    qwm_doc.MeshZ_E_38.Position = 141.85455
    qwm_doc.MeshZ_E_38.Length = 26.700000000000003
    qwm_doc.MeshZ_E_38.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_38.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_38.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_38.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_39")
    qwm_doc.MeshZ_E_39.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 153.39091),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_39.Orientation = "Z"
    qwm_doc.MeshZ_E_39.Position = 153.39091
    qwm_doc.MeshZ_E_39.Length = 26.700000000000003
    qwm_doc.MeshZ_E_39.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_39.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_39.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_39.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_40")
    qwm_doc.MeshZ_E_40.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 164.92727),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_40.Orientation = "Z"
    qwm_doc.MeshZ_E_40.Position = 164.92727
    qwm_doc.MeshZ_E_40.Length = 26.700000000000003
    qwm_doc.MeshZ_E_40.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_40.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_40.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_40.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_41")
    qwm_doc.MeshZ_E_41.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 176.46364),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_41.Orientation = "Z"
    qwm_doc.MeshZ_E_41.Position = 176.46364
    qwm_doc.MeshZ_E_41.Length = 26.700000000000003
    qwm_doc.MeshZ_E_41.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_41.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_41.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_41.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_42")
    qwm_doc.MeshZ_E_42.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 188.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_42.Orientation = "Z"
    qwm_doc.MeshZ_E_42.Position = 188.0
    qwm_doc.MeshZ_E_42.Length = 26.700000000000003
    qwm_doc.MeshZ_E_42.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_42.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_42.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_42.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_43")
    qwm_doc.MeshZ_E_43.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 199.42857),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_43.Orientation = "Z"
    qwm_doc.MeshZ_E_43.Position = 199.42857
    qwm_doc.MeshZ_E_43.Length = 26.700000000000003
    qwm_doc.MeshZ_E_43.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_43.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_43.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_43.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_44")
    qwm_doc.MeshZ_E_44.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 210.85714),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_44.Orientation = "Z"
    qwm_doc.MeshZ_E_44.Position = 210.85714
    qwm_doc.MeshZ_E_44.Length = 26.700000000000003
    qwm_doc.MeshZ_E_44.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_44.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_44.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_44.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_45")
    qwm_doc.MeshZ_E_45.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 222.28571),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_45.Orientation = "Z"
    qwm_doc.MeshZ_E_45.Position = 222.28571
    qwm_doc.MeshZ_E_45.Length = 26.700000000000003
    qwm_doc.MeshZ_E_45.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_45.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_45.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_45.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_46")
    qwm_doc.MeshZ_E_46.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 233.71429),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_46.Orientation = "Z"
    qwm_doc.MeshZ_E_46.Position = 233.71429
    qwm_doc.MeshZ_E_46.Length = 26.700000000000003
    qwm_doc.MeshZ_E_46.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_46.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_46.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_46.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_47")
    qwm_doc.MeshZ_E_47.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 245.14286),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_47.Orientation = "Z"
    qwm_doc.MeshZ_E_47.Position = 245.14286
    qwm_doc.MeshZ_E_47.Length = 26.700000000000003
    qwm_doc.MeshZ_E_47.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_47.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_47.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_47.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_48")
    qwm_doc.MeshZ_E_48.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 256.57143),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_48.Orientation = "Z"
    qwm_doc.MeshZ_E_48.Position = 256.57143
    qwm_doc.MeshZ_E_48.Length = 26.700000000000003
    qwm_doc.MeshZ_E_48.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_48.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_48.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_48.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","MeshZ_E_49")
    qwm_doc.MeshZ_E_49.Placement = FreeCAD.Placement(FreeCAD.Vector(-120.15, -121.5, 268.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.MeshZ_E_49.Orientation = "Z"
    qwm_doc.MeshZ_E_49.Position = 268.0
    qwm_doc.MeshZ_E_49.Length = 26.700000000000003
    qwm_doc.MeshZ_E_49.Width = 27.0
    FreeCAD.Gui.ActiveDocument.MeshZ_E_49.ShowText = False
    FreeCAD.Gui.ActiveDocument.MeshZ_E_49.TextSize = 14
    FreeCAD.Gui.ActiveDocument.MeshZ_E_49.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","SourcePort")
    qwm_doc.SourcePort.Length = 18.0
    qwm_doc.SourcePort.Width = 78.0
    qwm_doc.SourcePort.Placement = FreeCAD.Placement(FreeCAD.Vector(-124.5, 0.0, 268.0), FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.SourcePort.Orientation = "Z"
    qwm_doc.SourcePort.Position = 268.0
    qwm_doc.SourcePort.Activity = "MINUS"
    qwm_doc.SourcePort.Type = "Source"
    qwm_doc.SourcePort.SymmetryH = False
    qwm_doc.SourcePort.SymmetryV = False
    qwm_doc.SourcePort.PointCoordX = -124.5
    qwm_doc.SourcePort.PointCoordY = 0.0
    qwm_doc.SourcePort.PointCoordZ = 268.0
    qwm_doc.SourcePort.effectivePermitivityMode = "AUTO"
    qwm_doc.SourcePort.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('pulse of spectrum f1<f<f2',2.0,4.0,3.0),1.0,0.0,1,0),'R_TE01','Ex',1,QW_Modeller.TemplateGenerationConf('Automatic',(2.45,0.1),(2.0,3.0,0.01),0.38474,67,1,0))
    qwm_doc.SourcePort.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.SourcePort.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.SourcePort.ReferenceOffset = abs(qwm_doc.SourcePort.PointCoordZ - 228.0)
