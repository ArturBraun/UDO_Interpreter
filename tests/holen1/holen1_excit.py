
from FreeCAD import Base
import QW_Modeller
from qw_project import *
from qw_units import *


def set_Excitation(qwm_doc):
    QW_Modeller.addQWObject("QW_Modeller::TemplatePort","Port_1")
    qwm_doc.Port_1.Length = 5.0
    qwm_doc.Port_1.Width = 10.0
    qwm_doc.Port_1.Placement = FreeCAD.Placement(FreeCAD.Vector(-25.0, 0.0, 0.0), FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.Port_1.Orientation = "X"
    qwm_doc.Port_1.Position = -25.0
    qwm_doc.Port_1.Activity = "PLUS"
    qwm_doc.Port_1.Type = "Source"
    qwm_doc.Port_1.SymmetryH = False
    qwm_doc.Port_1.SymmetryV = False
    qwm_doc.Port_1.PointCoordX = -25.0
    qwm_doc.Port_1.PointCoordY = 0.0
    qwm_doc.Port_1.PointCoordZ = 0.0
    qwm_doc.Port_1.effectivePermitivityMode = "AUTO"
    qwm_doc.Port_1.Excitation = QW_Modeller.TemplateExcitation(QW_Modeller.DriveFunction(QW_Modeller.Waveform('pulse of spectrum f1<f<f2',15.0,25.0,3.0),1.0,0.0,1,0),'R_TE01','Ey',1,QW_Modeller.TemplateGenerationConf('Automatic',(20.0,2.0),(17.0,23.0,0.01),0.438278013289489,281,1,0))
    qwm_doc.Port_1.MultiPointExcitation = QW_Modeller.MultiPointPortExcitation(0,"0.1")
    qwm_doc.Port_1.Postprocessing = QW_Modeller.PortPostprocessing(0,0,1)
    qwm_doc.Port_1.ReferenceOffset = abs(qwm_doc.Port_1.PointCoordX - -20.0)
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","AbsorbingBox_1_Z_UP")
    qwm_doc.AbsorbingBox_1_Z_UP.Orientation = "Z"
    qwm_doc.AbsorbingBox_1_Z_UP.Length = 55.060959999999994
    qwm_doc.AbsorbingBox_1_Z_UP.Width = 48.43812
    qwm_doc.AbsorbingBox_1_Z_UP.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 0.0, 24.21906),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.AbsorbingBox_1_Z_UP.Position = 24.21906
    qwm_doc.AbsorbingBox_1_Z_UP.Activity = "MINUS"
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Z_UP.AbsorberDepth = 1.00000
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Z_UP.ShowText = True
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Z_UP.TextSize = 14
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Z_UP.TextPlace = 3
    qwm_doc.AbsorbingBox_1_Z_UP.Type = "MUR"
    qwm_doc.AbsorbingBox_1_Z_UP.EffectivePermittivity = 1.0
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","AbsorbingBox_1_Z_DOWN")
    qwm_doc.AbsorbingBox_1_Z_DOWN.Orientation = "Z"
    qwm_doc.AbsorbingBox_1_Z_DOWN.Length = 55.060959999999994
    qwm_doc.AbsorbingBox_1_Z_DOWN.Width = 48.43812
    qwm_doc.AbsorbingBox_1_Z_DOWN.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 0.0, -24.21906),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.AbsorbingBox_1_Z_DOWN.Position = -24.21906
    qwm_doc.AbsorbingBox_1_Z_DOWN.Activity = "PLUS"
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Z_DOWN.AbsorberDepth = 1.00000
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Z_DOWN.ShowText = True
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Z_DOWN.TextSize = 14
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Z_DOWN.TextPlace = 3
    qwm_doc.AbsorbingBox_1_Z_DOWN.Type = "MUR"
    qwm_doc.AbsorbingBox_1_Z_DOWN.EffectivePermittivity = 1.0
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","AbsorbingBox_1_X_DOWN")
    qwm_doc.AbsorbingBox_1_X_DOWN.Orientation = "X"
    qwm_doc.AbsorbingBox_1_X_DOWN.Length = 48.43812
    qwm_doc.AbsorbingBox_1_X_DOWN.Width = 48.43812
    qwm_doc.AbsorbingBox_1_X_DOWN.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.53048, 0.0, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.AbsorbingBox_1_X_DOWN.Position = -36.53048
    qwm_doc.AbsorbingBox_1_X_DOWN.Activity = "PLUS"
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_X_DOWN.AbsorberDepth = 1.00000
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_X_DOWN.ShowText = True
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_X_DOWN.TextSize = 14
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_X_DOWN.TextPlace = 3
    qwm_doc.AbsorbingBox_1_X_DOWN.Type = "MUR"
    qwm_doc.AbsorbingBox_1_X_DOWN.EffectivePermittivity = 1.0
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","AbsorbingBox_1_X_UP")
    qwm_doc.AbsorbingBox_1_X_UP.Orientation = "X"
    qwm_doc.AbsorbingBox_1_X_UP.Length = 48.43812
    qwm_doc.AbsorbingBox_1_X_UP.Width = 48.43812
    qwm_doc.AbsorbingBox_1_X_UP.Placement = FreeCAD.Placement(FreeCAD.Vector(18.53048, 0.0, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.AbsorbingBox_1_X_UP.Position = 18.53048
    qwm_doc.AbsorbingBox_1_X_UP.Activity = "MINUS"
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_X_UP.AbsorberDepth = 1.00000
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_X_UP.ShowText = True
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_X_UP.TextSize = 14
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_X_UP.TextPlace = 3
    qwm_doc.AbsorbingBox_1_X_UP.Type = "MUR"
    qwm_doc.AbsorbingBox_1_X_UP.EffectivePermittivity = 1.0
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","AbsorbingBox_1_Y_DOWN")
    qwm_doc.AbsorbingBox_1_Y_DOWN.Orientation = "Y"
    qwm_doc.AbsorbingBox_1_Y_DOWN.Length = 48.43812
    qwm_doc.AbsorbingBox_1_Y_DOWN.Width = 55.060959999999994
    qwm_doc.AbsorbingBox_1_Y_DOWN.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, -24.21906, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.AbsorbingBox_1_Y_DOWN.Position = -24.21906
    qwm_doc.AbsorbingBox_1_Y_DOWN.Activity = "PLUS"
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Y_DOWN.AbsorberDepth = 1.00000
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Y_DOWN.ShowText = True
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Y_DOWN.TextSize = 14
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Y_DOWN.TextPlace = 3
    qwm_doc.AbsorbingBox_1_Y_DOWN.Type = "MUR"
    qwm_doc.AbsorbingBox_1_Y_DOWN.EffectivePermittivity = 1.0
    QW_Modeller.addQWObject("QW_Modeller::AbsorbingWall","AbsorbingBox_1_Y_UP")
    qwm_doc.AbsorbingBox_1_Y_UP.Orientation = "Y"
    qwm_doc.AbsorbingBox_1_Y_UP.Length = 48.43812
    qwm_doc.AbsorbingBox_1_Y_UP.Width = 55.060959999999994
    qwm_doc.AbsorbingBox_1_Y_UP.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 24.21906, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.AbsorbingBox_1_Y_UP.Position = 24.21906
    qwm_doc.AbsorbingBox_1_Y_UP.Activity = "MINUS"
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Y_UP.AbsorberDepth = 1.00000
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Y_UP.ShowText = True
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Y_UP.TextSize = 14
    FreeCAD.Gui.ActiveDocument.AbsorbingBox_1_Y_UP.TextPlace = 3
    qwm_doc.AbsorbingBox_1_Y_UP.Type = "MUR"
    qwm_doc.AbsorbingBox_1_Y_UP.EffectivePermittivity = 1.0
    QW_Modeller.addQWObject("QW_Modeller::NTFBox","NTFBox_1")
    qwm_doc.NTFBox_1.Length = 38.0
    qwm_doc.NTFBox_1.Width = 31.37716
    qwm_doc.NTFBox_1.Height = 31.37716
    qwm_doc.NTFBox_1.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 0.0, 0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    FreeCAD.Gui.ActiveDocument.NTFBox_1.ShowText = True
    FreeCAD.Gui.ActiveDocument.NTFBox_1.TextSize = 14
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_106")
    qwm_doc.var_106.Placement = FreeCAD.Placement(FreeCAD.Vector(-25.0, 0.0, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.var_106.Orientation = "X"
    qwm_doc.var_106.Position = -25.0
    qwm_doc.var_106.Length = 48.43812
    qwm_doc.var_106.Width = 48.43812
    FreeCAD.Gui.ActiveDocument.var_106.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_106.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_106.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_107")
    qwm_doc.var_107.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.var_107.Orientation = "X"
    qwm_doc.var_107.Position = 0.0
    qwm_doc.var_107.Length = 48.43812
    qwm_doc.var_107.Width = 48.43812
    FreeCAD.Gui.ActiveDocument.var_107.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_107.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_107.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_108")
    qwm_doc.var_108.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, -4.5, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.var_108.Orientation = "Y"
    qwm_doc.var_108.Position = -4.5
    qwm_doc.var_108.Length = 48.43812
    qwm_doc.var_108.Width = 55.060959999999994
    FreeCAD.Gui.ActiveDocument.var_108.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_108.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_108.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_109")
    qwm_doc.var_109.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, -2.5, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.var_109.Orientation = "Y"
    qwm_doc.var_109.Position = -2.5
    qwm_doc.var_109.Length = 48.43812
    qwm_doc.var_109.Width = 55.060959999999994
    FreeCAD.Gui.ActiveDocument.var_109.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_109.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_109.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_110")
    qwm_doc.var_110.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, -1.5, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.var_110.Orientation = "Y"
    qwm_doc.var_110.Position = -1.5
    qwm_doc.var_110.Length = 48.43812
    qwm_doc.var_110.Width = 55.060959999999994
    FreeCAD.Gui.ActiveDocument.var_110.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_110.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_110.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_111")
    qwm_doc.var_111.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 1.5, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.var_111.Orientation = "Y"
    qwm_doc.var_111.Position = 1.5
    qwm_doc.var_111.Length = 48.43812
    qwm_doc.var_111.Width = 55.060959999999994
    FreeCAD.Gui.ActiveDocument.var_111.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_111.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_111.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_112")
    qwm_doc.var_112.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 2.5, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.var_112.Orientation = "Y"
    qwm_doc.var_112.Position = 2.5
    qwm_doc.var_112.Length = 48.43812
    qwm_doc.var_112.Width = 55.060959999999994
    FreeCAD.Gui.ActiveDocument.var_112.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_112.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_112.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_113")
    qwm_doc.var_113.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 4.5, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.var_113.Orientation = "Y"
    qwm_doc.var_113.Position = 4.5
    qwm_doc.var_113.Length = 48.43812
    qwm_doc.var_113.Width = 55.060959999999994
    FreeCAD.Gui.ActiveDocument.var_113.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_113.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_113.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_114")
    qwm_doc.var_114.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 0.0, -7.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.var_114.Orientation = "Z"
    qwm_doc.var_114.Position = -7.0
    qwm_doc.var_114.Length = 55.060959999999994
    qwm_doc.var_114.Width = 48.43812
    FreeCAD.Gui.ActiveDocument.var_114.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_114.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_114.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_115")
    qwm_doc.var_115.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 0.0, -5.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.var_115.Orientation = "Z"
    qwm_doc.var_115.Position = -5.0
    qwm_doc.var_115.Length = 55.060959999999994
    qwm_doc.var_115.Width = 48.43812
    FreeCAD.Gui.ActiveDocument.var_115.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_115.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_115.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_116")
    qwm_doc.var_116.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 0.0, -0.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.var_116.Orientation = "Z"
    qwm_doc.var_116.Position = -0.5
    qwm_doc.var_116.Length = 55.060959999999994
    qwm_doc.var_116.Width = 48.43812
    FreeCAD.Gui.ActiveDocument.var_116.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_116.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_116.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_117")
    qwm_doc.var_117.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 0.0, 0.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.var_117.Orientation = "Z"
    qwm_doc.var_117.Position = 0.5
    qwm_doc.var_117.Length = 55.060959999999994
    qwm_doc.var_117.Width = 48.43812
    FreeCAD.Gui.ActiveDocument.var_117.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_117.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_117.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_118")
    qwm_doc.var_118.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 0.0, 5.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.var_118.Orientation = "Z"
    qwm_doc.var_118.Position = 5.0
    qwm_doc.var_118.Length = 55.060959999999994
    qwm_doc.var_118.Width = 48.43812
    FreeCAD.Gui.ActiveDocument.var_118.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_118.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_118.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","var_119")
    qwm_doc.var_119.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, 0.0, 7.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.var_119.Orientation = "Z"
    qwm_doc.var_119.Position = 7.0
    qwm_doc.var_119.Length = 55.060959999999994
    qwm_doc.var_119.Width = 48.43812
    FreeCAD.Gui.ActiveDocument.var_119.ShowText = False
    FreeCAD.Gui.ActiveDocument.var_119.TextSize = 14
    FreeCAD.Gui.ActiveDocument.var_119.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_2")
    qwm_doc.specX_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(-35.56961, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_2.Orientation = "X"
    qwm_doc.specX_E_2.Position = -35.56961
    qwm_doc.specX_E_2.Length = 1.0
    qwm_doc.specX_E_2.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_3")
    qwm_doc.specX_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(-34.60873, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_3.Orientation = "X"
    qwm_doc.specX_E_3.Position = -34.60873
    qwm_doc.specX_E_3.Length = 1.0
    qwm_doc.specX_E_3.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_4")
    qwm_doc.specX_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(-33.64786, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_4.Orientation = "X"
    qwm_doc.specX_E_4.Position = -33.64786
    qwm_doc.specX_E_4.Length = 1.0
    qwm_doc.specX_E_4.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_5")
    qwm_doc.specX_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(-32.68699, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_5.Orientation = "X"
    qwm_doc.specX_E_5.Position = -32.68699
    qwm_doc.specX_E_5.Length = 1.0
    qwm_doc.specX_E_5.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_6")
    qwm_doc.specX_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(-31.72611, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_6.Orientation = "X"
    qwm_doc.specX_E_6.Position = -31.72611
    qwm_doc.specX_E_6.Length = 1.0
    qwm_doc.specX_E_6.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_7")
    qwm_doc.specX_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(-30.76524, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_7.Orientation = "X"
    qwm_doc.specX_E_7.Position = -30.76524
    qwm_doc.specX_E_7.Length = 1.0
    qwm_doc.specX_E_7.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_8")
    qwm_doc.specX_E_8.Placement = FreeCAD.Placement(FreeCAD.Vector(-29.80437, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_8.Orientation = "X"
    qwm_doc.specX_E_8.Position = -29.80437
    qwm_doc.specX_E_8.Length = 1.0
    qwm_doc.specX_E_8.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_8.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_8.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_8.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_9")
    qwm_doc.specX_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(-28.84349, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_9.Orientation = "X"
    qwm_doc.specX_E_9.Position = -28.84349
    qwm_doc.specX_E_9.Length = 1.0
    qwm_doc.specX_E_9.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_10")
    qwm_doc.specX_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(-27.88262, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_10.Orientation = "X"
    qwm_doc.specX_E_10.Position = -27.88262
    qwm_doc.specX_E_10.Length = 1.0
    qwm_doc.specX_E_10.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_11")
    qwm_doc.specX_E_11.Placement = FreeCAD.Placement(FreeCAD.Vector(-26.92175, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_11.Orientation = "X"
    qwm_doc.specX_E_11.Position = -26.92175
    qwm_doc.specX_E_11.Length = 1.0
    qwm_doc.specX_E_11.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_11.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_11.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_11.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_12")
    qwm_doc.specX_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(-25.96087, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_12.Orientation = "X"
    qwm_doc.specX_E_12.Position = -25.96087
    qwm_doc.specX_E_12.Length = 1.0
    qwm_doc.specX_E_12.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_14")
    qwm_doc.specX_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(-24.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_14.Orientation = "X"
    qwm_doc.specX_E_14.Position = -24.0
    qwm_doc.specX_E_14.Length = 1.0
    qwm_doc.specX_E_14.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_15")
    qwm_doc.specX_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(-23.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_15.Orientation = "X"
    qwm_doc.specX_E_15.Position = -23.0
    qwm_doc.specX_E_15.Length = 1.0
    qwm_doc.specX_E_15.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_16")
    qwm_doc.specX_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(-22.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_16.Orientation = "X"
    qwm_doc.specX_E_16.Position = -22.0
    qwm_doc.specX_E_16.Length = 1.0
    qwm_doc.specX_E_16.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_17")
    qwm_doc.specX_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(-21.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_17.Orientation = "X"
    qwm_doc.specX_E_17.Position = -21.0
    qwm_doc.specX_E_17.Length = 1.0
    qwm_doc.specX_E_17.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_18")
    qwm_doc.specX_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(-20.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_18.Orientation = "X"
    qwm_doc.specX_E_18.Position = -20.0
    qwm_doc.specX_E_18.Length = 1.0
    qwm_doc.specX_E_18.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_19")
    qwm_doc.specX_E_19.Placement = FreeCAD.Placement(FreeCAD.Vector(-19.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_19.Orientation = "X"
    qwm_doc.specX_E_19.Position = -19.0
    qwm_doc.specX_E_19.Length = 1.0
    qwm_doc.specX_E_19.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_19.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_19.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_19.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_20")
    qwm_doc.specX_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(-18.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_20.Orientation = "X"
    qwm_doc.specX_E_20.Position = -18.0
    qwm_doc.specX_E_20.Length = 1.0
    qwm_doc.specX_E_20.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_21")
    qwm_doc.specX_E_21.Placement = FreeCAD.Placement(FreeCAD.Vector(-17.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_21.Orientation = "X"
    qwm_doc.specX_E_21.Position = -17.0
    qwm_doc.specX_E_21.Length = 1.0
    qwm_doc.specX_E_21.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_21.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_21.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_21.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_22")
    qwm_doc.specX_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(-16.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_22.Orientation = "X"
    qwm_doc.specX_E_22.Position = -16.0
    qwm_doc.specX_E_22.Length = 1.0
    qwm_doc.specX_E_22.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_23")
    qwm_doc.specX_E_23.Placement = FreeCAD.Placement(FreeCAD.Vector(-15.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_23.Orientation = "X"
    qwm_doc.specX_E_23.Position = -15.0
    qwm_doc.specX_E_23.Length = 1.0
    qwm_doc.specX_E_23.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_23.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_23.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_23.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_24")
    qwm_doc.specX_E_24.Placement = FreeCAD.Placement(FreeCAD.Vector(-14.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_24.Orientation = "X"
    qwm_doc.specX_E_24.Position = -14.0
    qwm_doc.specX_E_24.Length = 1.0
    qwm_doc.specX_E_24.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_24.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_24.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_24.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_25")
    qwm_doc.specX_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(-13.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_25.Orientation = "X"
    qwm_doc.specX_E_25.Position = -13.0
    qwm_doc.specX_E_25.Length = 1.0
    qwm_doc.specX_E_25.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_26")
    qwm_doc.specX_E_26.Placement = FreeCAD.Placement(FreeCAD.Vector(-12.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_26.Orientation = "X"
    qwm_doc.specX_E_26.Position = -12.0
    qwm_doc.specX_E_26.Length = 1.0
    qwm_doc.specX_E_26.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_26.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_26.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_26.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_27")
    qwm_doc.specX_E_27.Placement = FreeCAD.Placement(FreeCAD.Vector(-11.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_27.Orientation = "X"
    qwm_doc.specX_E_27.Position = -11.0
    qwm_doc.specX_E_27.Length = 1.0
    qwm_doc.specX_E_27.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_27.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_27.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_27.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_28")
    qwm_doc.specX_E_28.Placement = FreeCAD.Placement(FreeCAD.Vector(-10.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_28.Orientation = "X"
    qwm_doc.specX_E_28.Position = -10.0
    qwm_doc.specX_E_28.Length = 1.0
    qwm_doc.specX_E_28.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_28.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_28.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_28.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_29")
    qwm_doc.specX_E_29.Placement = FreeCAD.Placement(FreeCAD.Vector(-9.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_29.Orientation = "X"
    qwm_doc.specX_E_29.Position = -9.0
    qwm_doc.specX_E_29.Length = 1.0
    qwm_doc.specX_E_29.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_29.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_29.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_29.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_30")
    qwm_doc.specX_E_30.Placement = FreeCAD.Placement(FreeCAD.Vector(-8.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_30.Orientation = "X"
    qwm_doc.specX_E_30.Position = -8.0
    qwm_doc.specX_E_30.Length = 1.0
    qwm_doc.specX_E_30.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_30.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_30.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_30.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_31")
    qwm_doc.specX_E_31.Placement = FreeCAD.Placement(FreeCAD.Vector(-7.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_31.Orientation = "X"
    qwm_doc.specX_E_31.Position = -7.0
    qwm_doc.specX_E_31.Length = 1.0
    qwm_doc.specX_E_31.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_31.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_31.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_31.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_32")
    qwm_doc.specX_E_32.Placement = FreeCAD.Placement(FreeCAD.Vector(-6.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_32.Orientation = "X"
    qwm_doc.specX_E_32.Position = -6.0
    qwm_doc.specX_E_32.Length = 1.0
    qwm_doc.specX_E_32.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_32.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_32.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_32.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_33")
    qwm_doc.specX_E_33.Placement = FreeCAD.Placement(FreeCAD.Vector(-5.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_33.Orientation = "X"
    qwm_doc.specX_E_33.Position = -5.0
    qwm_doc.specX_E_33.Length = 1.0
    qwm_doc.specX_E_33.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_33.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_33.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_33.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_34")
    qwm_doc.specX_E_34.Placement = FreeCAD.Placement(FreeCAD.Vector(-4.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_34.Orientation = "X"
    qwm_doc.specX_E_34.Position = -4.0
    qwm_doc.specX_E_34.Length = 1.0
    qwm_doc.specX_E_34.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_34.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_34.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_34.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_35")
    qwm_doc.specX_E_35.Placement = FreeCAD.Placement(FreeCAD.Vector(-3.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_35.Orientation = "X"
    qwm_doc.specX_E_35.Position = -3.0
    qwm_doc.specX_E_35.Length = 1.0
    qwm_doc.specX_E_35.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_35.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_35.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_35.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_36")
    qwm_doc.specX_E_36.Placement = FreeCAD.Placement(FreeCAD.Vector(-2.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_36.Orientation = "X"
    qwm_doc.specX_E_36.Position = -2.0
    qwm_doc.specX_E_36.Length = 1.0
    qwm_doc.specX_E_36.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_36.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_36.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_36.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_37")
    qwm_doc.specX_E_37.Placement = FreeCAD.Placement(FreeCAD.Vector(-1.0, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_37.Orientation = "X"
    qwm_doc.specX_E_37.Position = -1.0
    qwm_doc.specX_E_37.Length = 1.0
    qwm_doc.specX_E_37.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_37.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_37.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_37.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_39")
    qwm_doc.specX_E_39.Placement = FreeCAD.Placement(FreeCAD.Vector(0.97529, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_39.Orientation = "X"
    qwm_doc.specX_E_39.Position = 0.97529
    qwm_doc.specX_E_39.Length = 1.0
    qwm_doc.specX_E_39.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_39.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_39.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_39.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_40")
    qwm_doc.specX_E_40.Placement = FreeCAD.Placement(FreeCAD.Vector(1.95058, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_40.Orientation = "X"
    qwm_doc.specX_E_40.Position = 1.95058
    qwm_doc.specX_E_40.Length = 1.0
    qwm_doc.specX_E_40.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_40.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_40.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_40.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_41")
    qwm_doc.specX_E_41.Placement = FreeCAD.Placement(FreeCAD.Vector(2.92587, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_41.Orientation = "X"
    qwm_doc.specX_E_41.Position = 2.92587
    qwm_doc.specX_E_41.Length = 1.0
    qwm_doc.specX_E_41.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_41.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_41.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_41.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_42")
    qwm_doc.specX_E_42.Placement = FreeCAD.Placement(FreeCAD.Vector(3.90115, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_42.Orientation = "X"
    qwm_doc.specX_E_42.Position = 3.90115
    qwm_doc.specX_E_42.Length = 1.0
    qwm_doc.specX_E_42.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_42.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_42.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_42.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_43")
    qwm_doc.specX_E_43.Placement = FreeCAD.Placement(FreeCAD.Vector(4.87644, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_43.Orientation = "X"
    qwm_doc.specX_E_43.Position = 4.87644
    qwm_doc.specX_E_43.Length = 1.0
    qwm_doc.specX_E_43.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_43.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_43.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_43.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_44")
    qwm_doc.specX_E_44.Placement = FreeCAD.Placement(FreeCAD.Vector(5.85173, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_44.Orientation = "X"
    qwm_doc.specX_E_44.Position = 5.85173
    qwm_doc.specX_E_44.Length = 1.0
    qwm_doc.specX_E_44.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_44.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_44.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_44.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_45")
    qwm_doc.specX_E_45.Placement = FreeCAD.Placement(FreeCAD.Vector(6.82702, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_45.Orientation = "X"
    qwm_doc.specX_E_45.Position = 6.82702
    qwm_doc.specX_E_45.Length = 1.0
    qwm_doc.specX_E_45.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_45.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_45.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_45.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_46")
    qwm_doc.specX_E_46.Placement = FreeCAD.Placement(FreeCAD.Vector(7.80231, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_46.Orientation = "X"
    qwm_doc.specX_E_46.Position = 7.80231
    qwm_doc.specX_E_46.Length = 1.0
    qwm_doc.specX_E_46.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_46.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_46.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_46.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_47")
    qwm_doc.specX_E_47.Placement = FreeCAD.Placement(FreeCAD.Vector(8.7776, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_47.Orientation = "X"
    qwm_doc.specX_E_47.Position = 8.7776
    qwm_doc.specX_E_47.Length = 1.0
    qwm_doc.specX_E_47.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_47.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_47.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_47.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_48")
    qwm_doc.specX_E_48.Placement = FreeCAD.Placement(FreeCAD.Vector(9.75288, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_48.Orientation = "X"
    qwm_doc.specX_E_48.Position = 9.75288
    qwm_doc.specX_E_48.Length = 1.0
    qwm_doc.specX_E_48.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_48.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_48.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_48.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_49")
    qwm_doc.specX_E_49.Placement = FreeCAD.Placement(FreeCAD.Vector(10.72817, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_49.Orientation = "X"
    qwm_doc.specX_E_49.Position = 10.72817
    qwm_doc.specX_E_49.Length = 1.0
    qwm_doc.specX_E_49.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_49.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_49.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_49.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_50")
    qwm_doc.specX_E_50.Placement = FreeCAD.Placement(FreeCAD.Vector(11.70346, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_50.Orientation = "X"
    qwm_doc.specX_E_50.Position = 11.70346
    qwm_doc.specX_E_50.Length = 1.0
    qwm_doc.specX_E_50.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_50.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_50.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_50.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_51")
    qwm_doc.specX_E_51.Placement = FreeCAD.Placement(FreeCAD.Vector(12.67875, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_51.Orientation = "X"
    qwm_doc.specX_E_51.Position = 12.67875
    qwm_doc.specX_E_51.Length = 1.0
    qwm_doc.specX_E_51.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_51.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_51.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_51.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_52")
    qwm_doc.specX_E_52.Placement = FreeCAD.Placement(FreeCAD.Vector(13.65404, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_52.Orientation = "X"
    qwm_doc.specX_E_52.Position = 13.65404
    qwm_doc.specX_E_52.Length = 1.0
    qwm_doc.specX_E_52.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_52.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_52.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_52.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_53")
    qwm_doc.specX_E_53.Placement = FreeCAD.Placement(FreeCAD.Vector(14.62933, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_53.Orientation = "X"
    qwm_doc.specX_E_53.Position = 14.62933
    qwm_doc.specX_E_53.Length = 1.0
    qwm_doc.specX_E_53.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_53.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_53.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_53.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_54")
    qwm_doc.specX_E_54.Placement = FreeCAD.Placement(FreeCAD.Vector(15.60461, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_54.Orientation = "X"
    qwm_doc.specX_E_54.Position = 15.60461
    qwm_doc.specX_E_54.Length = 1.0
    qwm_doc.specX_E_54.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_54.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_54.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_54.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_55")
    qwm_doc.specX_E_55.Placement = FreeCAD.Placement(FreeCAD.Vector(16.5799, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_55.Orientation = "X"
    qwm_doc.specX_E_55.Position = 16.5799
    qwm_doc.specX_E_55.Length = 1.0
    qwm_doc.specX_E_55.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_55.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_55.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_55.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specX_E_56")
    qwm_doc.specX_E_56.Placement = FreeCAD.Placement(FreeCAD.Vector(17.55519, -23.71906, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.specX_E_56.Orientation = "X"
    qwm_doc.specX_E_56.Position = 17.55519
    qwm_doc.specX_E_56.Length = 1.0
    qwm_doc.specX_E_56.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specX_E_56.ShowText = False
    FreeCAD.Gui.ActiveDocument.specX_E_56.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specX_E_56.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_X_Bottom")
    qwm_doc.Border_X_Bottom.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.53048, -23.71906, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.Border_X_Bottom.Orientation = "X"
    qwm_doc.Border_X_Bottom.Position = -36.53048
    qwm_doc.Border_X_Bottom.Length = 1.0
    qwm_doc.Border_X_Bottom.Width = 48.43812
    FreeCAD.Gui.ActiveDocument.Border_X_Bottom.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_X_Bottom.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_X_Bottom.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_X_Top")
    qwm_doc.Border_X_Top.Placement = FreeCAD.Placement(FreeCAD.Vector(18.53048, -23.71906, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, 0.5))
    qwm_doc.Border_X_Top.Orientation = "X"
    qwm_doc.Border_X_Top.Position = 18.53048
    qwm_doc.Border_X_Top.Length = 1.0
    qwm_doc.Border_X_Top.Width = 48.43812
    FreeCAD.Gui.ActiveDocument.Border_X_Top.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_X_Top.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_X_Top.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_2")
    qwm_doc.specY_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -23.23311, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_2.Orientation = "Y"
    qwm_doc.specY_E_2.Position = -23.23311
    qwm_doc.specY_E_2.Length = 1.0
    qwm_doc.specY_E_2.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_3")
    qwm_doc.specY_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -22.24715, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_3.Orientation = "Y"
    qwm_doc.specY_E_3.Position = -22.24715
    qwm_doc.specY_E_3.Length = 1.0
    qwm_doc.specY_E_3.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_4")
    qwm_doc.specY_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -21.2612, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_4.Orientation = "Y"
    qwm_doc.specY_E_4.Position = -21.2612
    qwm_doc.specY_E_4.Length = 1.0
    qwm_doc.specY_E_4.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_5")
    qwm_doc.specY_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -20.27525, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_5.Orientation = "Y"
    qwm_doc.specY_E_5.Position = -20.27525
    qwm_doc.specY_E_5.Length = 1.0
    qwm_doc.specY_E_5.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_6")
    qwm_doc.specY_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -19.2893, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_6.Orientation = "Y"
    qwm_doc.specY_E_6.Position = -19.2893
    qwm_doc.specY_E_6.Length = 1.0
    qwm_doc.specY_E_6.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_7")
    qwm_doc.specY_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -18.30334, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_7.Orientation = "Y"
    qwm_doc.specY_E_7.Position = -18.30334
    qwm_doc.specY_E_7.Length = 1.0
    qwm_doc.specY_E_7.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_8")
    qwm_doc.specY_E_8.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -17.31739, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_8.Orientation = "Y"
    qwm_doc.specY_E_8.Position = -17.31739
    qwm_doc.specY_E_8.Length = 1.0
    qwm_doc.specY_E_8.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_8.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_8.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_8.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_9")
    qwm_doc.specY_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -16.33144, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_9.Orientation = "Y"
    qwm_doc.specY_E_9.Position = -16.33144
    qwm_doc.specY_E_9.Length = 1.0
    qwm_doc.specY_E_9.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_10")
    qwm_doc.specY_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -15.34548, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_10.Orientation = "Y"
    qwm_doc.specY_E_10.Position = -15.34548
    qwm_doc.specY_E_10.Length = 1.0
    qwm_doc.specY_E_10.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_11")
    qwm_doc.specY_E_11.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -14.35953, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_11.Orientation = "Y"
    qwm_doc.specY_E_11.Position = -14.35953
    qwm_doc.specY_E_11.Length = 1.0
    qwm_doc.specY_E_11.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_11.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_11.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_11.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_12")
    qwm_doc.specY_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -13.37358, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_12.Orientation = "Y"
    qwm_doc.specY_E_12.Position = -13.37358
    qwm_doc.specY_E_12.Length = 1.0
    qwm_doc.specY_E_12.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_13")
    qwm_doc.specY_E_13.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -12.38762, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_13.Orientation = "Y"
    qwm_doc.specY_E_13.Position = -12.38762
    qwm_doc.specY_E_13.Length = 1.0
    qwm_doc.specY_E_13.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_13.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_13.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_13.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_14")
    qwm_doc.specY_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -11.40167, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_14.Orientation = "Y"
    qwm_doc.specY_E_14.Position = -11.40167
    qwm_doc.specY_E_14.Length = 1.0
    qwm_doc.specY_E_14.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_15")
    qwm_doc.specY_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -10.41572, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_15.Orientation = "Y"
    qwm_doc.specY_E_15.Position = -10.41572
    qwm_doc.specY_E_15.Length = 1.0
    qwm_doc.specY_E_15.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_16")
    qwm_doc.specY_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -9.42977, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_16.Orientation = "Y"
    qwm_doc.specY_E_16.Position = -9.42977
    qwm_doc.specY_E_16.Length = 1.0
    qwm_doc.specY_E_16.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_17")
    qwm_doc.specY_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -8.44381, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_17.Orientation = "Y"
    qwm_doc.specY_E_17.Position = -8.44381
    qwm_doc.specY_E_17.Length = 1.0
    qwm_doc.specY_E_17.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_18")
    qwm_doc.specY_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -7.45786, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_18.Orientation = "Y"
    qwm_doc.specY_E_18.Position = -7.45786
    qwm_doc.specY_E_18.Length = 1.0
    qwm_doc.specY_E_18.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_19")
    qwm_doc.specY_E_19.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -6.47191, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_19.Orientation = "Y"
    qwm_doc.specY_E_19.Position = -6.47191
    qwm_doc.specY_E_19.Length = 1.0
    qwm_doc.specY_E_19.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_19.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_19.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_19.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_20")
    qwm_doc.specY_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -5.48595, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_20.Orientation = "Y"
    qwm_doc.specY_E_20.Position = -5.48595
    qwm_doc.specY_E_20.Length = 1.0
    qwm_doc.specY_E_20.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_22")
    qwm_doc.specY_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -3.5, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_22.Orientation = "Y"
    qwm_doc.specY_E_22.Position = -3.5
    qwm_doc.specY_E_22.Length = 1.0
    qwm_doc.specY_E_22.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_25")
    qwm_doc.specY_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -0.5, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_25.Orientation = "Y"
    qwm_doc.specY_E_25.Position = -0.5
    qwm_doc.specY_E_25.Length = 1.0
    qwm_doc.specY_E_25.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_26")
    qwm_doc.specY_E_26.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 0.5, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_26.Orientation = "Y"
    qwm_doc.specY_E_26.Position = 0.5
    qwm_doc.specY_E_26.Length = 1.0
    qwm_doc.specY_E_26.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_26.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_26.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_26.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_29")
    qwm_doc.specY_E_29.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 3.5, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_29.Orientation = "Y"
    qwm_doc.specY_E_29.Position = 3.5
    qwm_doc.specY_E_29.Length = 1.0
    qwm_doc.specY_E_29.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_29.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_29.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_29.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_31")
    qwm_doc.specY_E_31.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 5.48595, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_31.Orientation = "Y"
    qwm_doc.specY_E_31.Position = 5.48595
    qwm_doc.specY_E_31.Length = 1.0
    qwm_doc.specY_E_31.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_31.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_31.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_31.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_32")
    qwm_doc.specY_E_32.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 6.47191, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_32.Orientation = "Y"
    qwm_doc.specY_E_32.Position = 6.47191
    qwm_doc.specY_E_32.Length = 1.0
    qwm_doc.specY_E_32.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_32.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_32.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_32.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_33")
    qwm_doc.specY_E_33.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 7.45786, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_33.Orientation = "Y"
    qwm_doc.specY_E_33.Position = 7.45786
    qwm_doc.specY_E_33.Length = 1.0
    qwm_doc.specY_E_33.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_33.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_33.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_33.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_34")
    qwm_doc.specY_E_34.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 8.44381, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_34.Orientation = "Y"
    qwm_doc.specY_E_34.Position = 8.44381
    qwm_doc.specY_E_34.Length = 1.0
    qwm_doc.specY_E_34.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_34.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_34.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_34.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_35")
    qwm_doc.specY_E_35.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 9.42977, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_35.Orientation = "Y"
    qwm_doc.specY_E_35.Position = 9.42977
    qwm_doc.specY_E_35.Length = 1.0
    qwm_doc.specY_E_35.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_35.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_35.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_35.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_36")
    qwm_doc.specY_E_36.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 10.41572, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_36.Orientation = "Y"
    qwm_doc.specY_E_36.Position = 10.41572
    qwm_doc.specY_E_36.Length = 1.0
    qwm_doc.specY_E_36.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_36.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_36.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_36.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_37")
    qwm_doc.specY_E_37.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 11.40167, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_37.Orientation = "Y"
    qwm_doc.specY_E_37.Position = 11.40167
    qwm_doc.specY_E_37.Length = 1.0
    qwm_doc.specY_E_37.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_37.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_37.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_37.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_38")
    qwm_doc.specY_E_38.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 12.38762, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_38.Orientation = "Y"
    qwm_doc.specY_E_38.Position = 12.38762
    qwm_doc.specY_E_38.Length = 1.0
    qwm_doc.specY_E_38.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_38.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_38.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_38.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_39")
    qwm_doc.specY_E_39.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 13.37358, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_39.Orientation = "Y"
    qwm_doc.specY_E_39.Position = 13.37358
    qwm_doc.specY_E_39.Length = 1.0
    qwm_doc.specY_E_39.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_39.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_39.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_39.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_40")
    qwm_doc.specY_E_40.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 14.35953, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_40.Orientation = "Y"
    qwm_doc.specY_E_40.Position = 14.35953
    qwm_doc.specY_E_40.Length = 1.0
    qwm_doc.specY_E_40.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_40.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_40.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_40.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_41")
    qwm_doc.specY_E_41.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 15.34548, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_41.Orientation = "Y"
    qwm_doc.specY_E_41.Position = 15.34548
    qwm_doc.specY_E_41.Length = 1.0
    qwm_doc.specY_E_41.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_41.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_41.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_41.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_42")
    qwm_doc.specY_E_42.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 16.33144, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_42.Orientation = "Y"
    qwm_doc.specY_E_42.Position = 16.33144
    qwm_doc.specY_E_42.Length = 1.0
    qwm_doc.specY_E_42.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_42.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_42.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_42.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_43")
    qwm_doc.specY_E_43.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 17.31739, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_43.Orientation = "Y"
    qwm_doc.specY_E_43.Position = 17.31739
    qwm_doc.specY_E_43.Length = 1.0
    qwm_doc.specY_E_43.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_43.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_43.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_43.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_44")
    qwm_doc.specY_E_44.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 18.30334, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_44.Orientation = "Y"
    qwm_doc.specY_E_44.Position = 18.30334
    qwm_doc.specY_E_44.Length = 1.0
    qwm_doc.specY_E_44.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_44.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_44.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_44.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_45")
    qwm_doc.specY_E_45.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 19.28929, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_45.Orientation = "Y"
    qwm_doc.specY_E_45.Position = 19.28929
    qwm_doc.specY_E_45.Length = 1.0
    qwm_doc.specY_E_45.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_45.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_45.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_45.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_46")
    qwm_doc.specY_E_46.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 20.27525, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_46.Orientation = "Y"
    qwm_doc.specY_E_46.Position = 20.27525
    qwm_doc.specY_E_46.Length = 1.0
    qwm_doc.specY_E_46.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_46.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_46.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_46.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_47")
    qwm_doc.specY_E_47.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 21.2612, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_47.Orientation = "Y"
    qwm_doc.specY_E_47.Position = 21.2612
    qwm_doc.specY_E_47.Length = 1.0
    qwm_doc.specY_E_47.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_47.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_47.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_47.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_48")
    qwm_doc.specY_E_48.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 22.24715, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_48.Orientation = "Y"
    qwm_doc.specY_E_48.Position = 22.24715
    qwm_doc.specY_E_48.Length = 1.0
    qwm_doc.specY_E_48.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_48.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_48.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_48.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specY_E_49")
    qwm_doc.specY_E_49.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 23.23311, -23.71906),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.specY_E_49.Orientation = "Y"
    qwm_doc.specY_E_49.Position = 23.23311
    qwm_doc.specY_E_49.Length = 1.0
    qwm_doc.specY_E_49.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specY_E_49.ShowText = False
    FreeCAD.Gui.ActiveDocument.specY_E_49.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specY_E_49.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_Y_Bottom")
    qwm_doc.Border_Y_Bottom.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -24.21906, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.Border_Y_Bottom.Orientation = "Y"
    qwm_doc.Border_Y_Bottom.Position = -24.21906
    qwm_doc.Border_Y_Bottom.Length = 48.43812
    qwm_doc.Border_Y_Bottom.Width = 1.0
    FreeCAD.Gui.ActiveDocument.Border_Y_Bottom.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_Y_Bottom.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_Y_Bottom.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_Y_Top")
    qwm_doc.Border_Y_Top.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, 24.21906, 0.0),FreeCAD.Rotation(0.5, 0.5, 0.5, -0.5))
    qwm_doc.Border_Y_Top.Orientation = "Y"
    qwm_doc.Border_Y_Top.Position = 24.21906
    qwm_doc.Border_Y_Top.Length = 48.43812
    qwm_doc.Border_Y_Top.Width = 1.0
    FreeCAD.Gui.ActiveDocument.Border_Y_Top.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_Y_Top.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_Y_Top.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_2")
    qwm_doc.specZ_E_2.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -23.26245),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_2.Orientation = "Z"
    qwm_doc.specZ_E_2.Position = -23.26245
    qwm_doc.specZ_E_2.Length = 1.0
    qwm_doc.specZ_E_2.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_2.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_2.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_2.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_3")
    qwm_doc.specZ_E_3.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -22.30583),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_3.Orientation = "Z"
    qwm_doc.specZ_E_3.Position = -22.30583
    qwm_doc.specZ_E_3.Length = 1.0
    qwm_doc.specZ_E_3.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_3.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_3.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_3.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_4")
    qwm_doc.specZ_E_4.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -21.34922),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_4.Orientation = "Z"
    qwm_doc.specZ_E_4.Position = -21.34922
    qwm_doc.specZ_E_4.Length = 1.0
    qwm_doc.specZ_E_4.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_4.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_4.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_4.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_5")
    qwm_doc.specZ_E_5.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -20.3926),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_5.Orientation = "Z"
    qwm_doc.specZ_E_5.Position = -20.3926
    qwm_doc.specZ_E_5.Length = 1.0
    qwm_doc.specZ_E_5.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_5.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_5.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_5.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_6")
    qwm_doc.specZ_E_6.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -19.43599),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_6.Orientation = "Z"
    qwm_doc.specZ_E_6.Position = -19.43599
    qwm_doc.specZ_E_6.Length = 1.0
    qwm_doc.specZ_E_6.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_6.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_6.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_6.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_7")
    qwm_doc.specZ_E_7.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -18.47937),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_7.Orientation = "Z"
    qwm_doc.specZ_E_7.Position = -18.47937
    qwm_doc.specZ_E_7.Length = 1.0
    qwm_doc.specZ_E_7.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_7.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_7.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_7.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_8")
    qwm_doc.specZ_E_8.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -17.52276),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_8.Orientation = "Z"
    qwm_doc.specZ_E_8.Position = -17.52276
    qwm_doc.specZ_E_8.Length = 1.0
    qwm_doc.specZ_E_8.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_8.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_8.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_8.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_9")
    qwm_doc.specZ_E_9.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -16.56614),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_9.Orientation = "Z"
    qwm_doc.specZ_E_9.Position = -16.56614
    qwm_doc.specZ_E_9.Length = 1.0
    qwm_doc.specZ_E_9.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_9.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_9.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_9.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_10")
    qwm_doc.specZ_E_10.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -15.60953),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_10.Orientation = "Z"
    qwm_doc.specZ_E_10.Position = -15.60953
    qwm_doc.specZ_E_10.Length = 1.0
    qwm_doc.specZ_E_10.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_10.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_10.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_10.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_11")
    qwm_doc.specZ_E_11.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -14.65292),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_11.Orientation = "Z"
    qwm_doc.specZ_E_11.Position = -14.65292
    qwm_doc.specZ_E_11.Length = 1.0
    qwm_doc.specZ_E_11.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_11.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_11.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_11.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_12")
    qwm_doc.specZ_E_12.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -13.6963),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_12.Orientation = "Z"
    qwm_doc.specZ_E_12.Position = -13.6963
    qwm_doc.specZ_E_12.Length = 1.0
    qwm_doc.specZ_E_12.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_12.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_12.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_12.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_13")
    qwm_doc.specZ_E_13.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -12.73969),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_13.Orientation = "Z"
    qwm_doc.specZ_E_13.Position = -12.73969
    qwm_doc.specZ_E_13.Length = 1.0
    qwm_doc.specZ_E_13.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_13.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_13.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_13.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_14")
    qwm_doc.specZ_E_14.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -11.78307),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_14.Orientation = "Z"
    qwm_doc.specZ_E_14.Position = -11.78307
    qwm_doc.specZ_E_14.Length = 1.0
    qwm_doc.specZ_E_14.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_14.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_14.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_14.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_15")
    qwm_doc.specZ_E_15.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -10.82646),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_15.Orientation = "Z"
    qwm_doc.specZ_E_15.Position = -10.82646
    qwm_doc.specZ_E_15.Length = 1.0
    qwm_doc.specZ_E_15.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_15.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_15.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_15.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_16")
    qwm_doc.specZ_E_16.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -9.86984),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_16.Orientation = "Z"
    qwm_doc.specZ_E_16.Position = -9.86984
    qwm_doc.specZ_E_16.Length = 1.0
    qwm_doc.specZ_E_16.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_16.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_16.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_16.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_17")
    qwm_doc.specZ_E_17.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -8.91323),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_17.Orientation = "Z"
    qwm_doc.specZ_E_17.Position = -8.91323
    qwm_doc.specZ_E_17.Length = 1.0
    qwm_doc.specZ_E_17.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_17.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_17.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_17.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_18")
    qwm_doc.specZ_E_18.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -7.95661),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_18.Orientation = "Z"
    qwm_doc.specZ_E_18.Position = -7.95661
    qwm_doc.specZ_E_18.Length = 1.0
    qwm_doc.specZ_E_18.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_18.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_18.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_18.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_20")
    qwm_doc.specZ_E_20.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_20.Orientation = "Z"
    qwm_doc.specZ_E_20.Position = -6.0
    qwm_doc.specZ_E_20.Length = 1.0
    qwm_doc.specZ_E_20.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_20.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_20.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_20.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_22")
    qwm_doc.specZ_E_22.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -4.1),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_22.Orientation = "Z"
    qwm_doc.specZ_E_22.Position = -4.1
    qwm_doc.specZ_E_22.Length = 1.0
    qwm_doc.specZ_E_22.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_22.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_22.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_22.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_23")
    qwm_doc.specZ_E_23.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -3.2),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_23.Orientation = "Z"
    qwm_doc.specZ_E_23.Position = -3.2
    qwm_doc.specZ_E_23.Length = 1.0
    qwm_doc.specZ_E_23.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_23.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_23.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_23.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_24")
    qwm_doc.specZ_E_24.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -2.3),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_24.Orientation = "Z"
    qwm_doc.specZ_E_24.Position = -2.3
    qwm_doc.specZ_E_24.Length = 1.0
    qwm_doc.specZ_E_24.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_24.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_24.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_24.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_25")
    qwm_doc.specZ_E_25.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, -1.4),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_25.Orientation = "Z"
    qwm_doc.specZ_E_25.Position = -1.4
    qwm_doc.specZ_E_25.Length = 1.0
    qwm_doc.specZ_E_25.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_25.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_25.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_25.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_28")
    qwm_doc.specZ_E_28.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 1.4),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_28.Orientation = "Z"
    qwm_doc.specZ_E_28.Position = 1.4
    qwm_doc.specZ_E_28.Length = 1.0
    qwm_doc.specZ_E_28.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_28.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_28.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_28.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_29")
    qwm_doc.specZ_E_29.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 2.3),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_29.Orientation = "Z"
    qwm_doc.specZ_E_29.Position = 2.3
    qwm_doc.specZ_E_29.Length = 1.0
    qwm_doc.specZ_E_29.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_29.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_29.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_29.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_30")
    qwm_doc.specZ_E_30.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 3.2),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_30.Orientation = "Z"
    qwm_doc.specZ_E_30.Position = 3.2
    qwm_doc.specZ_E_30.Length = 1.0
    qwm_doc.specZ_E_30.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_30.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_30.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_30.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_31")
    qwm_doc.specZ_E_31.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 4.1),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_31.Orientation = "Z"
    qwm_doc.specZ_E_31.Position = 4.1
    qwm_doc.specZ_E_31.Length = 1.0
    qwm_doc.specZ_E_31.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_31.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_31.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_31.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_33")
    qwm_doc.specZ_E_33.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_33.Orientation = "Z"
    qwm_doc.specZ_E_33.Position = 6.0
    qwm_doc.specZ_E_33.Length = 1.0
    qwm_doc.specZ_E_33.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_33.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_33.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_33.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_35")
    qwm_doc.specZ_E_35.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 7.95661),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_35.Orientation = "Z"
    qwm_doc.specZ_E_35.Position = 7.95661
    qwm_doc.specZ_E_35.Length = 1.0
    qwm_doc.specZ_E_35.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_35.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_35.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_35.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_36")
    qwm_doc.specZ_E_36.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 8.91323),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_36.Orientation = "Z"
    qwm_doc.specZ_E_36.Position = 8.91323
    qwm_doc.specZ_E_36.Length = 1.0
    qwm_doc.specZ_E_36.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_36.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_36.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_36.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_37")
    qwm_doc.specZ_E_37.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 9.86984),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_37.Orientation = "Z"
    qwm_doc.specZ_E_37.Position = 9.86984
    qwm_doc.specZ_E_37.Length = 1.0
    qwm_doc.specZ_E_37.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_37.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_37.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_37.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_38")
    qwm_doc.specZ_E_38.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 10.82646),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_38.Orientation = "Z"
    qwm_doc.specZ_E_38.Position = 10.82646
    qwm_doc.specZ_E_38.Length = 1.0
    qwm_doc.specZ_E_38.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_38.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_38.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_38.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_39")
    qwm_doc.specZ_E_39.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 11.78307),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_39.Orientation = "Z"
    qwm_doc.specZ_E_39.Position = 11.78307
    qwm_doc.specZ_E_39.Length = 1.0
    qwm_doc.specZ_E_39.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_39.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_39.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_39.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_40")
    qwm_doc.specZ_E_40.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 12.73969),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_40.Orientation = "Z"
    qwm_doc.specZ_E_40.Position = 12.73969
    qwm_doc.specZ_E_40.Length = 1.0
    qwm_doc.specZ_E_40.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_40.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_40.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_40.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_41")
    qwm_doc.specZ_E_41.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 13.6963),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_41.Orientation = "Z"
    qwm_doc.specZ_E_41.Position = 13.6963
    qwm_doc.specZ_E_41.Length = 1.0
    qwm_doc.specZ_E_41.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_41.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_41.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_41.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_42")
    qwm_doc.specZ_E_42.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 14.65292),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_42.Orientation = "Z"
    qwm_doc.specZ_E_42.Position = 14.65292
    qwm_doc.specZ_E_42.Length = 1.0
    qwm_doc.specZ_E_42.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_42.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_42.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_42.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_43")
    qwm_doc.specZ_E_43.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 15.60953),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_43.Orientation = "Z"
    qwm_doc.specZ_E_43.Position = 15.60953
    qwm_doc.specZ_E_43.Length = 1.0
    qwm_doc.specZ_E_43.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_43.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_43.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_43.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_44")
    qwm_doc.specZ_E_44.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 16.56614),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_44.Orientation = "Z"
    qwm_doc.specZ_E_44.Position = 16.56614
    qwm_doc.specZ_E_44.Length = 1.0
    qwm_doc.specZ_E_44.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_44.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_44.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_44.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_45")
    qwm_doc.specZ_E_45.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 17.52276),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_45.Orientation = "Z"
    qwm_doc.specZ_E_45.Position = 17.52276
    qwm_doc.specZ_E_45.Length = 1.0
    qwm_doc.specZ_E_45.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_45.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_45.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_45.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_46")
    qwm_doc.specZ_E_46.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 18.47937),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_46.Orientation = "Z"
    qwm_doc.specZ_E_46.Position = 18.47937
    qwm_doc.specZ_E_46.Length = 1.0
    qwm_doc.specZ_E_46.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_46.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_46.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_46.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_47")
    qwm_doc.specZ_E_47.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 19.43599),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_47.Orientation = "Z"
    qwm_doc.specZ_E_47.Position = 19.43599
    qwm_doc.specZ_E_47.Length = 1.0
    qwm_doc.specZ_E_47.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_47.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_47.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_47.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_48")
    qwm_doc.specZ_E_48.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 20.3926),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_48.Orientation = "Z"
    qwm_doc.specZ_E_48.Position = 20.3926
    qwm_doc.specZ_E_48.Length = 1.0
    qwm_doc.specZ_E_48.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_48.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_48.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_48.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_49")
    qwm_doc.specZ_E_49.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 21.34922),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_49.Orientation = "Z"
    qwm_doc.specZ_E_49.Position = 21.34922
    qwm_doc.specZ_E_49.Length = 1.0
    qwm_doc.specZ_E_49.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_49.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_49.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_49.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_50")
    qwm_doc.specZ_E_50.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 22.30583),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_50.Orientation = "Z"
    qwm_doc.specZ_E_50.Position = 22.30583
    qwm_doc.specZ_E_50.Length = 1.0
    qwm_doc.specZ_E_50.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_50.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_50.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_50.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","specZ_E_51")
    qwm_doc.specZ_E_51.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0, 0.0, 23.26245),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.specZ_E_51.Orientation = "Z"
    qwm_doc.specZ_E_51.Position = 23.26245
    qwm_doc.specZ_E_51.Length = 1.0
    qwm_doc.specZ_E_51.Width = 1.0
    FreeCAD.Gui.ActiveDocument.specZ_E_51.ShowText = False
    FreeCAD.Gui.ActiveDocument.specZ_E_51.TextSize = 14
    FreeCAD.Gui.ActiveDocument.specZ_E_51.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_Z_Bottom")
    qwm_doc.Border_Z_Bottom.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -23.71906, -24.21906),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.Border_Z_Bottom.Orientation = "Z"
    qwm_doc.Border_Z_Bottom.Position = -24.21906
    qwm_doc.Border_Z_Bottom.Length = 1.0
    qwm_doc.Border_Z_Bottom.Width = 1.0
    FreeCAD.Gui.ActiveDocument.Border_Z_Bottom.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_Z_Bottom.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_Z_Bottom.TextPlace = 3
    QW_Modeller.addQWObject("QW_Modeller::SnappingPlane","Border_Z_Top")
    qwm_doc.Border_Z_Top.Placement = FreeCAD.Placement(FreeCAD.Vector(-36.03048, -23.71906, 24.21906),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.Border_Z_Top.Orientation = "Z"
    qwm_doc.Border_Z_Top.Position = 24.21906
    qwm_doc.Border_Z_Top.Length = 1.0
    qwm_doc.Border_Z_Top.Width = 1.0
    FreeCAD.Gui.ActiveDocument.Border_Z_Top.ShowText = False
    FreeCAD.Gui.ActiveDocument.Border_Z_Top.TextSize = 14
    FreeCAD.Gui.ActiveDocument.Border_Z_Top.TextPlace = 3
