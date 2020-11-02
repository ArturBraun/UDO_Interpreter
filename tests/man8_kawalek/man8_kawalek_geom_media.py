
import FreeCAD
import FreeCADGui
from FreeCAD import Base
import QW_Modeller
from qw_project import *
import Part
import Sketcher
from qw_units import *
from qw_paths import *

setGHzBaseFreqUnit()
setmmBaseGeomUnit()

def set_GeometryAndMedia(qwm_doc):
    Fat = QW_Modeller.addQWMedium("Fat")
    Fat.materialtype = "Isotropic"
    Fat.Eps = [5.462, 5.462, 5.462]
    Fat.Mu = [1.0, 1.0, 1.0]
    Fat.Sigma = [0.051, 0.051, 0.051]
    Fat.SigmaM = [0.0, 0.0, 0.0]
    Fat.density = 0.0
    Fat.mcolor_PENPARAMS = (0.6235294117647059,1.0,0.37254901960784315,0.0)
    Fat.mstyle_PENPARAMS = 0
    Fat.mwidth_PENPARAMS = 1
    Fat.mpencolor_BRUSHPARAMS = (0.6235294117647059,1.0,0.37254901960784315,0.0)
    Fat.mbkcolor_BRUSHPARAMS = (0.23529411764705882,0.8509803921568627,0.5176470588235295,0.0)
    Fat.mstyle_BRUSHPARAMS = 99
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_1')
    qwm_doc.sketch_e_1.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,552.0,0), FreeCAD.Vector(192.0,544.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,544.0,0), FreeCAD.Vector(184.0,544.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(184.0,544.0,0), FreeCAD.Vector(184.0,536.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(184.0,536.0,0), FreeCAD.Vector(192.0,536.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,536.0,0), FreeCAD.Vector(192.0,520.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,520.0,0), FreeCAD.Vector(200.0,520.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,520.0,0), FreeCAD.Vector(200.0,512.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,512.0,0), FreeCAD.Vector(208.0,512.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,512.0,0), FreeCAD.Vector(208.0,504.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,504.0,0), FreeCAD.Vector(224.0,504.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,504.0,0), FreeCAD.Vector(224.0,496.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,496.0,0), FreeCAD.Vector(232.0,496.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,496.0,0), FreeCAD.Vector(232.0,488.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,488.0,0), FreeCAD.Vector(248.0,488.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,488.0,0), FreeCAD.Vector(248.0,512.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,512.0,0), FreeCAD.Vector(264.0,512.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,512.0,0), FreeCAD.Vector(264.0,520.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,520.0,0), FreeCAD.Vector(240.0,520.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,520.0,0), FreeCAD.Vector(240.0,528.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,528.0,0), FreeCAD.Vector(248.0,528.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,528.0,0), FreeCAD.Vector(248.0,536.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,536.0,0), FreeCAD.Vector(224.0,536.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,536.0,0), FreeCAD.Vector(224.0,544.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,544.0,0), FreeCAD.Vector(232.0,544.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,544.0,0), FreeCAD.Vector(232.0,552.0,0)))
    qwm_doc.sketch_e_1.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,552.0,0), FreeCAD.Vector(192.0,552.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_1")
    qwm_doc.e_1.Base = qwm_doc.sketch_e_1
    qwm_doc.e_1.Dir = (0, 0, 8.0)
    qwm_doc.e_1.Solid = True
    e_1_viewObject = qwm_doc.e_1.ViewObject
    e_1_viewObject.Transparency = 60
    qwm_doc.e_1.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    BoneCortical = QW_Modeller.addQWMedium("BoneCortical")
    BoneCortical.materialtype = "Isotropic"
    BoneCortical.Eps = [12.45, 12.45, 12.45]
    BoneCortical.Mu = [1.0, 1.0, 1.0]
    BoneCortical.Sigma = [0.1433, 0.1433, 0.1433]
    BoneCortical.SigmaM = [0.0, 0.0, 0.0]
    BoneCortical.density = 0.0
    BoneCortical.mcolor_PENPARAMS = (0.8980392156862745,0.8980392156862745,0.6980392156862745,0.0)
    BoneCortical.mstyle_PENPARAMS = 0
    BoneCortical.mwidth_PENPARAMS = 1
    BoneCortical.mpencolor_BRUSHPARAMS = (0.8980392156862745,0.8980392156862745,0.6980392156862745,0.0)
    BoneCortical.mbkcolor_BRUSHPARAMS = (0.8941176470588236,0.9529411764705882,0.5725490196078431,0.0)
    BoneCortical.mstyle_BRUSHPARAMS = 99
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_2')
    qwm_doc.sketch_e_2.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_2.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,552.0,0), FreeCAD.Vector(232.0,544.0,0)))
    qwm_doc.sketch_e_2.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,544.0,0), FreeCAD.Vector(240.0,544.0,0)))
    qwm_doc.sketch_e_2.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,544.0,0), FreeCAD.Vector(240.0,552.0,0)))
    qwm_doc.sketch_e_2.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,552.0,0), FreeCAD.Vector(232.0,552.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_2")
    qwm_doc.e_2.Base = qwm_doc.sketch_e_2
    qwm_doc.e_2.Dir = (0, 0, 8.0)
    qwm_doc.e_2.Solid = True
    e_2_viewObject = qwm_doc.e_2.ViewObject
    e_2_viewObject.Transparency = 60
    qwm_doc.e_2.Medium = QW_Modeller.getQWMedium("BoneCortical")
    qwm_doc.recompute()
    SkinDry = QW_Modeller.addQWMedium("SkinDry")
    SkinDry.materialtype = "Isotropic"
    SkinDry.Eps = [41.41, 41.41, 41.41]
    SkinDry.Mu = [1.0, 1.0, 1.0]
    SkinDry.Sigma = [0.8667, 0.8667, 0.8667]
    SkinDry.SigmaM = [0.0, 0.0, 0.0]
    SkinDry.density = 0.0
    SkinDry.mcolor_PENPARAMS = (1.0,0.9490196078431372,0.4980392156862745,0.0)
    SkinDry.mstyle_PENPARAMS = 0
    SkinDry.mwidth_PENPARAMS = 1
    SkinDry.mpencolor_BRUSHPARAMS = (1.0,0.9490196078431372,0.4980392156862745,0.0)
    SkinDry.mbkcolor_BRUSHPARAMS = (0.11372549019607843,0.9058823529411765,0.5803921568627451,0.0)
    SkinDry.mstyle_BRUSHPARAMS = 99
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_3')
    qwm_doc.sketch_e_3.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_3.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,552.0,0), FreeCAD.Vector(240.0,536.0,0)))
    qwm_doc.sketch_e_3.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,536.0,0), FreeCAD.Vector(248.0,536.0,0)))
    qwm_doc.sketch_e_3.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,536.0,0), FreeCAD.Vector(248.0,552.0,0)))
    qwm_doc.sketch_e_3.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,552.0,0), FreeCAD.Vector(240.0,552.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_3")
    qwm_doc.e_3.Base = qwm_doc.sketch_e_3
    qwm_doc.e_3.Dir = (0, 0, 8.0)
    qwm_doc.e_3.Solid = True
    e_3_viewObject = qwm_doc.e_3.ViewObject
    e_3_viewObject.Transparency = 60
    qwm_doc.e_3.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_4')
    qwm_doc.sketch_e_4.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_4.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,544.0,0), FreeCAD.Vector(224.0,536.0,0)))
    qwm_doc.sketch_e_4.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,536.0,0), FreeCAD.Vector(232.0,536.0,0)))
    qwm_doc.sketch_e_4.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,536.0,0), FreeCAD.Vector(232.0,544.0,0)))
    qwm_doc.sketch_e_4.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,544.0,0), FreeCAD.Vector(224.0,544.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_4")
    qwm_doc.e_4.Base = qwm_doc.sketch_e_4
    qwm_doc.e_4.Dir = (0, 0, 8.0)
    qwm_doc.e_4.Solid = True
    e_4_viewObject = qwm_doc.e_4.ViewObject
    e_4_viewObject.Transparency = 60
    qwm_doc.e_4.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_5')
    qwm_doc.sketch_e_5.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_5.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,544.0,0), FreeCAD.Vector(232.0,536.0,0)))
    qwm_doc.sketch_e_5.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,536.0,0), FreeCAD.Vector(240.0,536.0,0)))
    qwm_doc.sketch_e_5.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,536.0,0), FreeCAD.Vector(240.0,544.0,0)))
    qwm_doc.sketch_e_5.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,544.0,0), FreeCAD.Vector(232.0,544.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_5")
    qwm_doc.e_5.Base = qwm_doc.sketch_e_5
    qwm_doc.e_5.Dir = (0, 0, 8.0)
    qwm_doc.e_5.Solid = True
    e_5_viewObject = qwm_doc.e_5.ViewObject
    e_5_viewObject.Transparency = 60
    qwm_doc.e_5.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_6')
    qwm_doc.sketch_e_6.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_6.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,536.0,0), FreeCAD.Vector(248.0,528.0,0)))
    qwm_doc.sketch_e_6.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,528.0,0), FreeCAD.Vector(256.0,528.0,0)))
    qwm_doc.sketch_e_6.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,528.0,0), FreeCAD.Vector(256.0,536.0,0)))
    qwm_doc.sketch_e_6.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,536.0,0), FreeCAD.Vector(248.0,536.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_6")
    qwm_doc.e_6.Base = qwm_doc.sketch_e_6
    qwm_doc.e_6.Dir = (0, 0, 8.0)
    qwm_doc.e_6.Solid = True
    e_6_viewObject = qwm_doc.e_6.ViewObject
    e_6_viewObject.Transparency = 60
    qwm_doc.e_6.Medium = QW_Modeller.getQWMedium("BoneCortical")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_7')
    qwm_doc.sketch_e_7.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_7.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,528.0,0), FreeCAD.Vector(240.0,520.0,0)))
    qwm_doc.sketch_e_7.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,520.0,0), FreeCAD.Vector(264.0,520.0,0)))
    qwm_doc.sketch_e_7.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,520.0,0), FreeCAD.Vector(264.0,528.0,0)))
    qwm_doc.sketch_e_7.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,528.0,0), FreeCAD.Vector(240.0,528.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_7")
    qwm_doc.e_7.Base = qwm_doc.sketch_e_7
    qwm_doc.e_7.Dir = (0, 0, 8.0)
    qwm_doc.e_7.Solid = True
    e_7_viewObject = qwm_doc.e_7.ViewObject
    e_7_viewObject.Transparency = 60
    qwm_doc.e_7.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_8')
    qwm_doc.sketch_e_8.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_8.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,520.0,0), FreeCAD.Vector(264.0,512.0,0)))
    qwm_doc.sketch_e_8.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,512.0,0), FreeCAD.Vector(272.0,512.0,0)))
    qwm_doc.sketch_e_8.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,512.0,0), FreeCAD.Vector(272.0,520.0,0)))
    qwm_doc.sketch_e_8.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,520.0,0), FreeCAD.Vector(264.0,520.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_8")
    qwm_doc.e_8.Base = qwm_doc.sketch_e_8
    qwm_doc.e_8.Dir = (0, 0, 8.0)
    qwm_doc.e_8.Solid = True
    e_8_viewObject = qwm_doc.e_8.ViewObject
    e_8_viewObject.Transparency = 60
    qwm_doc.e_8.Medium = QW_Modeller.getQWMedium("BoneCortical")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_9')
    qwm_doc.sketch_e_9.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_9.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,512.0,0), FreeCAD.Vector(256.0,504.0,0)))
    qwm_doc.sketch_e_9.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,504.0,0), FreeCAD.Vector(272.0,504.0,0)))
    qwm_doc.sketch_e_9.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,504.0,0), FreeCAD.Vector(272.0,512.0,0)))
    qwm_doc.sketch_e_9.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,512.0,0), FreeCAD.Vector(256.0,512.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_9")
    qwm_doc.e_9.Base = qwm_doc.sketch_e_9
    qwm_doc.e_9.Dir = (0, 0, 8.0)
    qwm_doc.e_9.Solid = True
    e_9_viewObject = qwm_doc.e_9.ViewObject
    e_9_viewObject.Transparency = 60
    qwm_doc.e_9.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_10')
    qwm_doc.sketch_e_10.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_10.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,512.0,0), FreeCAD.Vector(272.0,504.0,0)))
    qwm_doc.sketch_e_10.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,504.0,0), FreeCAD.Vector(280.0,504.0,0)))
    qwm_doc.sketch_e_10.addGeometry(Part.LineSegment(FreeCAD.Vector(280.0,504.0,0), FreeCAD.Vector(280.0,512.0,0)))
    qwm_doc.sketch_e_10.addGeometry(Part.LineSegment(FreeCAD.Vector(280.0,512.0,0), FreeCAD.Vector(272.0,512.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_10")
    qwm_doc.e_10.Base = qwm_doc.sketch_e_10
    qwm_doc.e_10.Dir = (0, 0, 8.0)
    qwm_doc.e_10.Solid = True
    e_10_viewObject = qwm_doc.e_10.ViewObject
    e_10_viewObject.Transparency = 60
    qwm_doc.e_10.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_11')
    qwm_doc.sketch_e_11.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_11.addGeometry(Part.LineSegment(FreeCAD.Vector(280.0,512.0,0), FreeCAD.Vector(280.0,504.0,0)))
    qwm_doc.sketch_e_11.addGeometry(Part.LineSegment(FreeCAD.Vector(280.0,504.0,0), FreeCAD.Vector(288.0,504.0,0)))
    qwm_doc.sketch_e_11.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,504.0,0), FreeCAD.Vector(288.0,512.0,0)))
    qwm_doc.sketch_e_11.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,512.0,0), FreeCAD.Vector(280.0,512.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_11")
    qwm_doc.e_11.Base = qwm_doc.sketch_e_11
    qwm_doc.e_11.Dir = (0, 0, 8.0)
    qwm_doc.e_11.Solid = True
    e_11_viewObject = qwm_doc.e_11.ViewObject
    e_11_viewObject.Transparency = 60
    qwm_doc.e_11.Medium = QW_Modeller.getQWMedium("BoneCortical")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_12')
    qwm_doc.sketch_e_12.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_12.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,504.0,0), FreeCAD.Vector(272.0,496.0,0)))
    qwm_doc.sketch_e_12.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,496.0,0), FreeCAD.Vector(288.0,496.0,0)))
    qwm_doc.sketch_e_12.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,496.0,0), FreeCAD.Vector(288.0,504.0,0)))
    qwm_doc.sketch_e_12.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,504.0,0), FreeCAD.Vector(272.0,504.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_12")
    qwm_doc.e_12.Base = qwm_doc.sketch_e_12
    qwm_doc.e_12.Dir = (0, 0, 8.0)
    qwm_doc.e_12.Solid = True
    e_12_viewObject = qwm_doc.e_12.ViewObject
    e_12_viewObject.Transparency = 60
    qwm_doc.e_12.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_13')
    qwm_doc.sketch_e_13.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,16.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_13.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,496.0,0), FreeCAD.Vector(272.0,480.0,0)))
    qwm_doc.sketch_e_13.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,480.0,0), FreeCAD.Vector(288.0,480.0,0)))
    qwm_doc.sketch_e_13.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,480.0,0), FreeCAD.Vector(288.0,488.0,0)))
    qwm_doc.sketch_e_13.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,488.0,0), FreeCAD.Vector(296.0,488.0,0)))
    qwm_doc.sketch_e_13.addGeometry(Part.LineSegment(FreeCAD.Vector(296.0,488.0,0), FreeCAD.Vector(296.0,496.0,0)))
    qwm_doc.sketch_e_13.addGeometry(Part.LineSegment(FreeCAD.Vector(296.0,496.0,0), FreeCAD.Vector(272.0,496.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_13")
    qwm_doc.e_13.Base = qwm_doc.sketch_e_13
    qwm_doc.e_13.Dir = (0, 0, 8.0)
    qwm_doc.e_13.Solid = True
    e_13_viewObject = qwm_doc.e_13.ViewObject
    e_13_viewObject.Transparency = 60
    qwm_doc.e_13.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_14')
    qwm_doc.sketch_e_14.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(176.0,552.0,0), FreeCAD.Vector(176.0,520.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(176.0,520.0,0), FreeCAD.Vector(192.0,520.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,520.0,0), FreeCAD.Vector(192.0,512.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,512.0,0), FreeCAD.Vector(200.0,512.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,512.0,0), FreeCAD.Vector(200.0,504.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,504.0,0), FreeCAD.Vector(208.0,504.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,504.0,0), FreeCAD.Vector(208.0,496.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,496.0,0), FreeCAD.Vector(216.0,496.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,496.0,0), FreeCAD.Vector(216.0,480.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,480.0,0), FreeCAD.Vector(224.0,480.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,480.0,0), FreeCAD.Vector(224.0,472.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,472.0,0), FreeCAD.Vector(248.0,472.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,472.0,0), FreeCAD.Vector(248.0,480.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,480.0,0), FreeCAD.Vector(296.0,480.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(296.0,480.0,0), FreeCAD.Vector(296.0,488.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(296.0,488.0,0), FreeCAD.Vector(256.0,488.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,488.0,0), FreeCAD.Vector(256.0,496.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,496.0,0), FreeCAD.Vector(272.0,496.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,496.0,0), FreeCAD.Vector(272.0,504.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,504.0,0), FreeCAD.Vector(216.0,504.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,504.0,0), FreeCAD.Vector(216.0,520.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,520.0,0), FreeCAD.Vector(208.0,520.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,520.0,0), FreeCAD.Vector(208.0,528.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,528.0,0), FreeCAD.Vector(216.0,528.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,528.0,0), FreeCAD.Vector(216.0,536.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,536.0,0), FreeCAD.Vector(192.0,536.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,536.0,0), FreeCAD.Vector(192.0,544.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,544.0,0), FreeCAD.Vector(232.0,544.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,544.0,0), FreeCAD.Vector(232.0,552.0,0)))
    qwm_doc.sketch_e_14.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,552.0,0), FreeCAD.Vector(176.0,552.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_14")
    qwm_doc.e_14.Base = qwm_doc.sketch_e_14
    qwm_doc.e_14.Dir = (0, 0, 8.0)
    qwm_doc.e_14.Solid = True
    e_14_viewObject = qwm_doc.e_14.ViewObject
    e_14_viewObject.Transparency = 60
    qwm_doc.e_14.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_15')
    qwm_doc.sketch_e_15.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_15.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,552.0,0), FreeCAD.Vector(232.0,544.0,0)))
    qwm_doc.sketch_e_15.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,544.0,0), FreeCAD.Vector(224.0,544.0,0)))
    qwm_doc.sketch_e_15.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,544.0,0), FreeCAD.Vector(224.0,536.0,0)))
    qwm_doc.sketch_e_15.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,536.0,0), FreeCAD.Vector(240.0,536.0,0)))
    qwm_doc.sketch_e_15.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,536.0,0), FreeCAD.Vector(240.0,552.0,0)))
    qwm_doc.sketch_e_15.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,552.0,0), FreeCAD.Vector(232.0,552.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_15")
    qwm_doc.e_15.Base = qwm_doc.sketch_e_15
    qwm_doc.e_15.Dir = (0, 0, 8.0)
    qwm_doc.e_15.Solid = True
    e_15_viewObject = qwm_doc.e_15.ViewObject
    e_15_viewObject.Transparency = 60
    qwm_doc.e_15.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    Muscle = QW_Modeller.addQWMedium("Muscle")
    Muscle.materialtype = "Isotropic"
    Muscle.Eps = [55.03, 55.03, 55.03]
    Muscle.Mu = [1.0, 1.0, 1.0]
    Muscle.Sigma = [0.9429, 0.9429, 0.9429]
    Muscle.SigmaM = [0.0, 0.0, 0.0]
    Muscle.density = 0.0
    Muscle.mcolor_PENPARAMS = (1.0,0.37254901960784315,0.0,0.0)
    Muscle.mstyle_PENPARAMS = 0
    Muscle.mwidth_PENPARAMS = 1
    Muscle.mpencolor_BRUSHPARAMS = (1.0,0.37254901960784315,0.0,0.0)
    Muscle.mbkcolor_BRUSHPARAMS = (0.8627450980392157,0.41568627450980394,0.592156862745098,0.0)
    Muscle.mstyle_BRUSHPARAMS = 99
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_16')
    qwm_doc.sketch_e_16.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_16.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,544.0,0), FreeCAD.Vector(192.0,536.0,0)))
    qwm_doc.sketch_e_16.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,536.0,0), FreeCAD.Vector(200.0,536.0,0)))
    qwm_doc.sketch_e_16.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,536.0,0), FreeCAD.Vector(200.0,544.0,0)))
    qwm_doc.sketch_e_16.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,544.0,0), FreeCAD.Vector(192.0,544.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_16")
    qwm_doc.e_16.Base = qwm_doc.sketch_e_16
    qwm_doc.e_16.Dir = (0, 0, 8.0)
    qwm_doc.e_16.Solid = True
    e_16_viewObject = qwm_doc.e_16.ViewObject
    e_16_viewObject.Transparency = 60
    qwm_doc.e_16.Medium = QW_Modeller.getQWMedium("Muscle")
    qwm_doc.recompute()
    BoneMarrow = QW_Modeller.addQWMedium("BoneMarrow")
    BoneMarrow.materialtype = "Isotropic"
    BoneMarrow.Eps = [5.504, 5.504, 5.504]
    BoneMarrow.Mu = [1.0, 1.0, 1.0]
    BoneMarrow.Sigma = [0.0402, 0.0402, 0.0402]
    BoneMarrow.SigmaM = [0.0, 0.0, 0.0]
    BoneMarrow.density = 0.0
    BoneMarrow.mcolor_PENPARAMS = (0.8980392156862745,0.8980392156862745,0.6980392156862745,0.0)
    BoneMarrow.mstyle_PENPARAMS = 0
    BoneMarrow.mwidth_PENPARAMS = 1
    BoneMarrow.mpencolor_BRUSHPARAMS = (0.8980392156862745,0.8980392156862745,0.6980392156862745,0.0)
    BoneMarrow.mbkcolor_BRUSHPARAMS = (0.06666666666666667,0.9058823529411765,0.6274509803921569,0.0)
    BoneMarrow.mstyle_BRUSHPARAMS = 99
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_17')
    qwm_doc.sketch_e_17.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_17.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,544.0,0), FreeCAD.Vector(200.0,536.0,0)))
    qwm_doc.sketch_e_17.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,536.0,0), FreeCAD.Vector(208.0,536.0,0)))
    qwm_doc.sketch_e_17.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,536.0,0), FreeCAD.Vector(208.0,544.0,0)))
    qwm_doc.sketch_e_17.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,544.0,0), FreeCAD.Vector(200.0,544.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_17")
    qwm_doc.e_17.Base = qwm_doc.sketch_e_17
    qwm_doc.e_17.Dir = (0, 0, 8.0)
    qwm_doc.e_17.Solid = True
    e_17_viewObject = qwm_doc.e_17.ViewObject
    e_17_viewObject.Transparency = 60
    qwm_doc.e_17.Medium = QW_Modeller.getQWMedium("BoneMarrow")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_18')
    qwm_doc.sketch_e_18.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_18.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,544.0,0), FreeCAD.Vector(208.0,536.0,0)))
    qwm_doc.sketch_e_18.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,536.0,0), FreeCAD.Vector(216.0,536.0,0)))
    qwm_doc.sketch_e_18.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,536.0,0), FreeCAD.Vector(216.0,544.0,0)))
    qwm_doc.sketch_e_18.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,544.0,0), FreeCAD.Vector(208.0,544.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_18")
    qwm_doc.e_18.Base = qwm_doc.sketch_e_18
    qwm_doc.e_18.Dir = (0, 0, 8.0)
    qwm_doc.e_18.Solid = True
    e_18_viewObject = qwm_doc.e_18.ViewObject
    e_18_viewObject.Transparency = 60
    qwm_doc.e_18.Medium = QW_Modeller.getQWMedium("BoneCortical")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_19')
    qwm_doc.sketch_e_19.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_19.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,544.0,0), FreeCAD.Vector(216.0,536.0,0)))
    qwm_doc.sketch_e_19.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,536.0,0), FreeCAD.Vector(224.0,536.0,0)))
    qwm_doc.sketch_e_19.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,536.0,0), FreeCAD.Vector(224.0,544.0,0)))
    qwm_doc.sketch_e_19.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,544.0,0), FreeCAD.Vector(216.0,544.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_19")
    qwm_doc.e_19.Base = qwm_doc.sketch_e_19
    qwm_doc.e_19.Dir = (0, 0, 8.0)
    qwm_doc.e_19.Solid = True
    e_19_viewObject = qwm_doc.e_19.ViewObject
    e_19_viewObject.Transparency = 60
    qwm_doc.e_19.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    Tendon = QW_Modeller.addQWMedium("Tendon")
    Tendon.materialtype = "Isotropic"
    Tendon.Eps = [45.83, 45.83, 45.83]
    Tendon.Mu = [1.0, 1.0, 1.0]
    Tendon.Sigma = [0.7184, 0.7184, 0.7184]
    Tendon.SigmaM = [0.0, 0.0, 0.0]
    Tendon.density = 0.0
    Tendon.mcolor_PENPARAMS = (0.7764705882352941,0.7764705882352941,0.33725490196078434,0.0)
    Tendon.mstyle_PENPARAMS = 0
    Tendon.mwidth_PENPARAMS = 1
    Tendon.mpencolor_BRUSHPARAMS = (0.7764705882352941,0.7764705882352941,0.33725490196078434,0.0)
    Tendon.mbkcolor_BRUSHPARAMS = (0.10196078431372549,0.6862745098039216,0.3843137254901961,0.0)
    Tendon.mstyle_BRUSHPARAMS = 99
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_20')
    qwm_doc.sketch_e_20.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_20.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,536.0,0), FreeCAD.Vector(216.0,528.0,0)))
    qwm_doc.sketch_e_20.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,528.0,0), FreeCAD.Vector(224.0,528.0,0)))
    qwm_doc.sketch_e_20.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,528.0,0), FreeCAD.Vector(224.0,536.0,0)))
    qwm_doc.sketch_e_20.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,536.0,0), FreeCAD.Vector(216.0,536.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_20")
    qwm_doc.e_20.Base = qwm_doc.sketch_e_20
    qwm_doc.e_20.Dir = (0, 0, 8.0)
    qwm_doc.e_20.Solid = True
    e_20_viewObject = qwm_doc.e_20.ViewObject
    e_20_viewObject.Transparency = 60
    qwm_doc.e_20.Medium = QW_Modeller.getQWMedium("Tendon")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_21')
    qwm_doc.sketch_e_21.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_21.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,536.0,0), FreeCAD.Vector(224.0,528.0,0)))
    qwm_doc.sketch_e_21.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,528.0,0), FreeCAD.Vector(232.0,528.0,0)))
    qwm_doc.sketch_e_21.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,528.0,0), FreeCAD.Vector(232.0,536.0,0)))
    qwm_doc.sketch_e_21.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,536.0,0), FreeCAD.Vector(224.0,536.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_21")
    qwm_doc.e_21.Base = qwm_doc.sketch_e_21
    qwm_doc.e_21.Dir = (0, 0, 8.0)
    qwm_doc.e_21.Solid = True
    e_21_viewObject = qwm_doc.e_21.ViewObject
    e_21_viewObject.Transparency = 60
    qwm_doc.e_21.Medium = QW_Modeller.getQWMedium("BoneCortical")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_22')
    qwm_doc.sketch_e_22.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,536.0,0), FreeCAD.Vector(232.0,520.0,0)))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,520.0,0), FreeCAD.Vector(240.0,520.0,0)))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,520.0,0), FreeCAD.Vector(240.0,504.0,0)))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,504.0,0), FreeCAD.Vector(264.0,504.0,0)))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,504.0,0), FreeCAD.Vector(264.0,512.0,0)))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,512.0,0), FreeCAD.Vector(256.0,512.0,0)))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,512.0,0), FreeCAD.Vector(256.0,520.0,0)))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,520.0,0), FreeCAD.Vector(248.0,520.0,0)))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,520.0,0), FreeCAD.Vector(248.0,528.0,0)))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,528.0,0), FreeCAD.Vector(240.0,528.0,0)))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,528.0,0), FreeCAD.Vector(240.0,536.0,0)))
    qwm_doc.sketch_e_22.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,536.0,0), FreeCAD.Vector(232.0,536.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_22")
    qwm_doc.e_22.Base = qwm_doc.sketch_e_22
    qwm_doc.e_22.Dir = (0, 0, 8.0)
    qwm_doc.e_22.Solid = True
    e_22_viewObject = qwm_doc.e_22.ViewObject
    e_22_viewObject.Transparency = 60
    qwm_doc.e_22.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_23')
    qwm_doc.sketch_e_23.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_23.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,536.0,0), FreeCAD.Vector(240.0,528.0,0)))
    qwm_doc.sketch_e_23.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,528.0,0), FreeCAD.Vector(248.0,528.0,0)))
    qwm_doc.sketch_e_23.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,528.0,0), FreeCAD.Vector(248.0,536.0,0)))
    qwm_doc.sketch_e_23.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,536.0,0), FreeCAD.Vector(240.0,536.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_23")
    qwm_doc.e_23.Base = qwm_doc.sketch_e_23
    qwm_doc.e_23.Dir = (0, 0, 8.0)
    qwm_doc.e_23.Solid = True
    e_23_viewObject = qwm_doc.e_23.ViewObject
    e_23_viewObject.Transparency = 60
    qwm_doc.e_23.Medium = QW_Modeller.getQWMedium("BoneCortical")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_24')
    qwm_doc.sketch_e_24.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_24.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,536.0,0), FreeCAD.Vector(248.0,520.0,0)))
    qwm_doc.sketch_e_24.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,520.0,0), FreeCAD.Vector(256.0,520.0,0)))
    qwm_doc.sketch_e_24.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,520.0,0), FreeCAD.Vector(256.0,536.0,0)))
    qwm_doc.sketch_e_24.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,536.0,0), FreeCAD.Vector(248.0,536.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_24")
    qwm_doc.e_24.Base = qwm_doc.sketch_e_24
    qwm_doc.e_24.Dir = (0, 0, 8.0)
    qwm_doc.e_24.Solid = True
    e_24_viewObject = qwm_doc.e_24.ViewObject
    e_24_viewObject.Transparency = 60
    qwm_doc.e_24.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_25')
    qwm_doc.sketch_e_25.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_25.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,528.0,0), FreeCAD.Vector(208.0,520.0,0)))
    qwm_doc.sketch_e_25.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,520.0,0), FreeCAD.Vector(216.0,520.0,0)))
    qwm_doc.sketch_e_25.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,520.0,0), FreeCAD.Vector(216.0,528.0,0)))
    qwm_doc.sketch_e_25.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,528.0,0), FreeCAD.Vector(208.0,528.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_25")
    qwm_doc.e_25.Base = qwm_doc.sketch_e_25
    qwm_doc.e_25.Dir = (0, 0, 8.0)
    qwm_doc.e_25.Solid = True
    e_25_viewObject = qwm_doc.e_25.ViewObject
    e_25_viewObject.Transparency = 60
    qwm_doc.e_25.Medium = QW_Modeller.getQWMedium("Tendon")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_26')
    qwm_doc.sketch_e_26.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_26.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,528.0,0), FreeCAD.Vector(216.0,520.0,0)))
    qwm_doc.sketch_e_26.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,520.0,0), FreeCAD.Vector(224.0,520.0,0)))
    qwm_doc.sketch_e_26.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,520.0,0), FreeCAD.Vector(224.0,528.0,0)))
    qwm_doc.sketch_e_26.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,528.0,0), FreeCAD.Vector(216.0,528.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_26")
    qwm_doc.e_26.Base = qwm_doc.sketch_e_26
    qwm_doc.e_26.Dir = (0, 0, 8.0)
    qwm_doc.e_26.Solid = True
    e_26_viewObject = qwm_doc.e_26.ViewObject
    e_26_viewObject.Transparency = 60
    qwm_doc.e_26.Medium = QW_Modeller.getQWMedium("BoneMarrow")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_27')
    qwm_doc.sketch_e_27.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_27.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,528.0,0), FreeCAD.Vector(224.0,520.0,0)))
    qwm_doc.sketch_e_27.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,520.0,0), FreeCAD.Vector(216.0,520.0,0)))
    qwm_doc.sketch_e_27.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,520.0,0), FreeCAD.Vector(216.0,504.0,0)))
    qwm_doc.sketch_e_27.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,504.0,0), FreeCAD.Vector(240.0,504.0,0)))
    qwm_doc.sketch_e_27.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,504.0,0), FreeCAD.Vector(240.0,512.0,0)))
    qwm_doc.sketch_e_27.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,512.0,0), FreeCAD.Vector(232.0,512.0,0)))
    qwm_doc.sketch_e_27.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,512.0,0), FreeCAD.Vector(232.0,528.0,0)))
    qwm_doc.sketch_e_27.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,528.0,0), FreeCAD.Vector(224.0,528.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_27")
    qwm_doc.e_27.Base = qwm_doc.sketch_e_27
    qwm_doc.e_27.Dir = (0, 0, 8.0)
    qwm_doc.e_27.Solid = True
    e_27_viewObject = qwm_doc.e_27.ViewObject
    e_27_viewObject.Transparency = 60
    qwm_doc.e_27.Medium = QW_Modeller.getQWMedium("Tendon")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_28')
    qwm_doc.sketch_e_28.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_28.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,520.0,0), FreeCAD.Vector(232.0,512.0,0)))
    qwm_doc.sketch_e_28.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,512.0,0), FreeCAD.Vector(240.0,512.0,0)))
    qwm_doc.sketch_e_28.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,512.0,0), FreeCAD.Vector(240.0,520.0,0)))
    qwm_doc.sketch_e_28.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,520.0,0), FreeCAD.Vector(232.0,520.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_28")
    qwm_doc.e_28.Base = qwm_doc.sketch_e_28
    qwm_doc.e_28.Dir = (0, 0, 8.0)
    qwm_doc.e_28.Solid = True
    e_28_viewObject = qwm_doc.e_28.ViewObject
    e_28_viewObject.Transparency = 60
    qwm_doc.e_28.Medium = QW_Modeller.getQWMedium("BoneCortical")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_29')
    qwm_doc.sketch_e_29.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_29.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,520.0,0), FreeCAD.Vector(256.0,512.0,0)))
    qwm_doc.sketch_e_29.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,512.0,0), FreeCAD.Vector(264.0,512.0,0)))
    qwm_doc.sketch_e_29.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,512.0,0), FreeCAD.Vector(264.0,520.0,0)))
    qwm_doc.sketch_e_29.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,520.0,0), FreeCAD.Vector(256.0,520.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_29")
    qwm_doc.e_29.Base = qwm_doc.sketch_e_29
    qwm_doc.e_29.Dir = (0, 0, 8.0)
    qwm_doc.e_29.Solid = True
    e_29_viewObject = qwm_doc.e_29.ViewObject
    e_29_viewObject.Transparency = 60
    qwm_doc.e_29.Medium = QW_Modeller.getQWMedium("BoneCortical")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_30')
    qwm_doc.sketch_e_30.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_30.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,520.0,0), FreeCAD.Vector(264.0,512.0,0)))
    qwm_doc.sketch_e_30.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,512.0,0), FreeCAD.Vector(272.0,512.0,0)))
    qwm_doc.sketch_e_30.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,512.0,0), FreeCAD.Vector(272.0,520.0,0)))
    qwm_doc.sketch_e_30.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,520.0,0), FreeCAD.Vector(264.0,520.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_30")
    qwm_doc.e_30.Base = qwm_doc.sketch_e_30
    qwm_doc.e_30.Dir = (0, 0, 8.0)
    qwm_doc.e_30.Solid = True
    e_30_viewObject = qwm_doc.e_30.ViewObject
    e_30_viewObject.Transparency = 60
    qwm_doc.e_30.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_31')
    qwm_doc.sketch_e_31.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_31.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,512.0,0), FreeCAD.Vector(264.0,504.0,0)))
    qwm_doc.sketch_e_31.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,504.0,0), FreeCAD.Vector(272.0,504.0,0)))
    qwm_doc.sketch_e_31.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,504.0,0), FreeCAD.Vector(272.0,512.0,0)))
    qwm_doc.sketch_e_31.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,512.0,0), FreeCAD.Vector(264.0,512.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_31")
    qwm_doc.e_31.Base = qwm_doc.sketch_e_31
    qwm_doc.e_31.Dir = (0, 0, 8.0)
    qwm_doc.e_31.Solid = True
    e_31_viewObject = qwm_doc.e_31.ViewObject
    e_31_viewObject.Transparency = 60
    qwm_doc.e_31.Medium = QW_Modeller.getQWMedium("BoneCortical")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_32')
    qwm_doc.sketch_e_32.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_32.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,512.0,0), FreeCAD.Vector(272.0,496.0,0)))
    qwm_doc.sketch_e_32.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,496.0,0), FreeCAD.Vector(288.0,496.0,0)))
    qwm_doc.sketch_e_32.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,496.0,0), FreeCAD.Vector(288.0,504.0,0)))
    qwm_doc.sketch_e_32.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,504.0,0), FreeCAD.Vector(280.0,504.0,0)))
    qwm_doc.sketch_e_32.addGeometry(Part.LineSegment(FreeCAD.Vector(280.0,504.0,0), FreeCAD.Vector(280.0,512.0,0)))
    qwm_doc.sketch_e_32.addGeometry(Part.LineSegment(FreeCAD.Vector(280.0,512.0,0), FreeCAD.Vector(272.0,512.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_32")
    qwm_doc.e_32.Base = qwm_doc.sketch_e_32
    qwm_doc.e_32.Dir = (0, 0, 8.0)
    qwm_doc.e_32.Solid = True
    e_32_viewObject = qwm_doc.e_32.ViewObject
    e_32_viewObject.Transparency = 60
    qwm_doc.e_32.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    ZeroAir = QW_Modeller.addQWMedium("ZeroAir")
    ZeroAir.materialtype = "Isotropic"
    ZeroAir.Eps = [1.0, 1.0, 1.0]
    ZeroAir.Mu = [1.0, 1.0, 1.0]
    ZeroAir.Sigma = [0.0, 0.0, 0.0]
    ZeroAir.SigmaM = [0.0, 0.0, 0.0]
    ZeroAir.density = 0.0
    ZeroAir.mcolor_PENPARAMS = (0.0,1.0,1.0,0.0)
    ZeroAir.mstyle_PENPARAMS = 0
    ZeroAir.mwidth_PENPARAMS = 1
    ZeroAir.mpencolor_BRUSHPARAMS = (0.0,1.0,1.0,0.0)
    ZeroAir.mbkcolor_BRUSHPARAMS = (0.08235294117647059,0.20784313725490197,0.24313725490196078,0.0)
    ZeroAir.mstyle_BRUSHPARAMS = 99
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_33')
    qwm_doc.sketch_e_33.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_33.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,496.0,0), FreeCAD.Vector(256.0,488.0,0)))
    qwm_doc.sketch_e_33.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,488.0,0), FreeCAD.Vector(264.0,488.0,0)))
    qwm_doc.sketch_e_33.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,488.0,0), FreeCAD.Vector(264.0,496.0,0)))
    qwm_doc.sketch_e_33.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,496.0,0), FreeCAD.Vector(256.0,496.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_33")
    qwm_doc.e_33.Base = qwm_doc.sketch_e_33
    qwm_doc.e_33.Dir = (0, 0, 8.0)
    qwm_doc.e_33.Solid = True
    e_33_viewObject = qwm_doc.e_33.ViewObject
    e_33_viewObject.Transparency = 60
    qwm_doc.e_33.Medium = QW_Modeller.getQWMedium("ZeroAir")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_34')
    qwm_doc.sketch_e_34.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_34.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,496.0,0), FreeCAD.Vector(264.0,488.0,0)))
    qwm_doc.sketch_e_34.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,488.0,0), FreeCAD.Vector(296.0,488.0,0)))
    qwm_doc.sketch_e_34.addGeometry(Part.LineSegment(FreeCAD.Vector(296.0,488.0,0), FreeCAD.Vector(296.0,496.0,0)))
    qwm_doc.sketch_e_34.addGeometry(Part.LineSegment(FreeCAD.Vector(296.0,496.0,0), FreeCAD.Vector(264.0,496.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_34")
    qwm_doc.e_34.Base = qwm_doc.sketch_e_34
    qwm_doc.e_34.Dir = (0, 0, 8.0)
    qwm_doc.e_34.Solid = True
    e_34_viewObject = qwm_doc.e_34.ViewObject
    e_34_viewObject.Transparency = 60
    qwm_doc.e_34.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_35')
    qwm_doc.sketch_e_35.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_35.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,480.0,0), FreeCAD.Vector(248.0,472.0,0)))
    qwm_doc.sketch_e_35.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,472.0,0), FreeCAD.Vector(256.0,472.0,0)))
    qwm_doc.sketch_e_35.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,472.0,0), FreeCAD.Vector(256.0,480.0,0)))
    qwm_doc.sketch_e_35.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,480.0,0), FreeCAD.Vector(248.0,480.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_35")
    qwm_doc.e_35.Base = qwm_doc.sketch_e_35
    qwm_doc.e_35.Dir = (0, 0, 8.0)
    qwm_doc.e_35.Solid = True
    e_35_viewObject = qwm_doc.e_35.ViewObject
    e_35_viewObject.Transparency = 60
    qwm_doc.e_35.Medium = QW_Modeller.getQWMedium("ZeroAir")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_36')
    qwm_doc.sketch_e_36.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_36.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,480.0,0), FreeCAD.Vector(256.0,472.0,0)))
    qwm_doc.sketch_e_36.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,472.0,0), FreeCAD.Vector(288.0,472.0,0)))
    qwm_doc.sketch_e_36.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,472.0,0), FreeCAD.Vector(288.0,480.0,0)))
    qwm_doc.sketch_e_36.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,480.0,0), FreeCAD.Vector(256.0,480.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_36")
    qwm_doc.e_36.Base = qwm_doc.sketch_e_36
    qwm_doc.e_36.Dir = (0, 0, 8.0)
    qwm_doc.e_36.Solid = True
    e_36_viewObject = qwm_doc.e_36.ViewObject
    e_36_viewObject.Transparency = 60
    qwm_doc.e_36.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_37')
    qwm_doc.sketch_e_37.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,192.0,0), FreeCAD.Vector(248.0,184.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,184.0,0), FreeCAD.Vector(232.0,184.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,184.0,0), FreeCAD.Vector(232.0,176.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,176.0,0), FreeCAD.Vector(216.0,176.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,176.0,0), FreeCAD.Vector(216.0,168.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,168.0,0), FreeCAD.Vector(208.0,168.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,168.0,0), FreeCAD.Vector(208.0,160.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,160.0,0), FreeCAD.Vector(200.0,160.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,160.0,0), FreeCAD.Vector(200.0,136.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,136.0,0), FreeCAD.Vector(232.0,136.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,136.0,0), FreeCAD.Vector(232.0,144.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,144.0,0), FreeCAD.Vector(240.0,144.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,144.0,0), FreeCAD.Vector(240.0,152.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,152.0,0), FreeCAD.Vector(256.0,152.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,152.0,0), FreeCAD.Vector(256.0,160.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,160.0,0), FreeCAD.Vector(264.0,160.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,160.0,0), FreeCAD.Vector(264.0,184.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,184.0,0), FreeCAD.Vector(256.0,184.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,184.0,0), FreeCAD.Vector(256.0,192.0,0)))
    qwm_doc.sketch_e_37.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,192.0,0), FreeCAD.Vector(248.0,192.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_37")
    qwm_doc.e_37.Base = qwm_doc.sketch_e_37
    qwm_doc.e_37.Dir = (0, 0, 8.0)
    qwm_doc.e_37.Solid = True
    e_37_viewObject = qwm_doc.e_37.ViewObject
    e_37_viewObject.Transparency = 60
    qwm_doc.e_37.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_38')
    qwm_doc.sketch_e_38.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_38.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,168.0,0), FreeCAD.Vector(264.0,160.0,0)))
    qwm_doc.sketch_e_38.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,160.0,0), FreeCAD.Vector(272.0,160.0,0)))
    qwm_doc.sketch_e_38.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,160.0,0), FreeCAD.Vector(272.0,168.0,0)))
    qwm_doc.sketch_e_38.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,168.0,0), FreeCAD.Vector(264.0,168.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_38")
    qwm_doc.e_38.Base = qwm_doc.sketch_e_38
    qwm_doc.e_38.Dir = (0, 0, 8.0)
    qwm_doc.e_38.Solid = True
    e_38_viewObject = qwm_doc.e_38.ViewObject
    e_38_viewObject.Transparency = 60
    qwm_doc.e_38.Medium = QW_Modeller.getQWMedium("ZeroAir")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_39')
    qwm_doc.sketch_e_39.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_39.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,168.0,0), FreeCAD.Vector(272.0,160.0,0)))
    qwm_doc.sketch_e_39.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,160.0,0), FreeCAD.Vector(288.0,160.0,0)))
    qwm_doc.sketch_e_39.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,160.0,0), FreeCAD.Vector(288.0,168.0,0)))
    qwm_doc.sketch_e_39.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,168.0,0), FreeCAD.Vector(272.0,168.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_39")
    qwm_doc.e_39.Base = qwm_doc.sketch_e_39
    qwm_doc.e_39.Dir = (0, 0, 8.0)
    qwm_doc.e_39.Solid = True
    e_39_viewObject = qwm_doc.e_39.ViewObject
    e_39_viewObject.Transparency = 60
    qwm_doc.e_39.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_40')
    qwm_doc.sketch_e_40.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_40.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,160.0,0), FreeCAD.Vector(256.0,152.0,0)))
    qwm_doc.sketch_e_40.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,152.0,0), FreeCAD.Vector(264.0,152.0,0)))
    qwm_doc.sketch_e_40.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,152.0,0), FreeCAD.Vector(264.0,160.0,0)))
    qwm_doc.sketch_e_40.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,160.0,0), FreeCAD.Vector(256.0,160.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_40")
    qwm_doc.e_40.Base = qwm_doc.sketch_e_40
    qwm_doc.e_40.Dir = (0, 0, 8.0)
    qwm_doc.e_40.Solid = True
    e_40_viewObject = qwm_doc.e_40.ViewObject
    e_40_viewObject.Transparency = 60
    qwm_doc.e_40.Medium = QW_Modeller.getQWMedium("ZeroAir")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_41')
    qwm_doc.sketch_e_41.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_41.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,160.0,0), FreeCAD.Vector(264.0,152.0,0)))
    qwm_doc.sketch_e_41.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,152.0,0), FreeCAD.Vector(272.0,152.0,0)))
    qwm_doc.sketch_e_41.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,152.0,0), FreeCAD.Vector(272.0,144.0,0)))
    qwm_doc.sketch_e_41.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,144.0,0), FreeCAD.Vector(280.0,144.0,0)))
    qwm_doc.sketch_e_41.addGeometry(Part.LineSegment(FreeCAD.Vector(280.0,144.0,0), FreeCAD.Vector(280.0,152.0,0)))
    qwm_doc.sketch_e_41.addGeometry(Part.LineSegment(FreeCAD.Vector(280.0,152.0,0), FreeCAD.Vector(288.0,152.0,0)))
    qwm_doc.sketch_e_41.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,152.0,0), FreeCAD.Vector(288.0,160.0,0)))
    qwm_doc.sketch_e_41.addGeometry(Part.LineSegment(FreeCAD.Vector(288.0,160.0,0), FreeCAD.Vector(264.0,160.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_41")
    qwm_doc.e_41.Base = qwm_doc.sketch_e_41
    qwm_doc.e_41.Dir = (0, 0, 8.0)
    qwm_doc.e_41.Solid = True
    e_41_viewObject = qwm_doc.e_41.ViewObject
    e_41_viewObject.Transparency = 60
    qwm_doc.e_41.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_42')
    qwm_doc.sketch_e_42.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_42.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,152.0,0), FreeCAD.Vector(240.0,144.0,0)))
    qwm_doc.sketch_e_42.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,144.0,0), FreeCAD.Vector(248.0,144.0,0)))
    qwm_doc.sketch_e_42.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,144.0,0), FreeCAD.Vector(248.0,152.0,0)))
    qwm_doc.sketch_e_42.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,152.0,0), FreeCAD.Vector(240.0,152.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_42")
    qwm_doc.e_42.Base = qwm_doc.sketch_e_42
    qwm_doc.e_42.Dir = (0, 0, 8.0)
    qwm_doc.e_42.Solid = True
    e_42_viewObject = qwm_doc.e_42.ViewObject
    e_42_viewObject.Transparency = 60
    qwm_doc.e_42.Medium = QW_Modeller.getQWMedium("ZeroAir")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_43')
    qwm_doc.sketch_e_43.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_43.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,152.0,0), FreeCAD.Vector(248.0,144.0,0)))
    qwm_doc.sketch_e_43.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,144.0,0), FreeCAD.Vector(256.0,144.0,0)))
    qwm_doc.sketch_e_43.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,144.0,0), FreeCAD.Vector(256.0,136.0,0)))
    qwm_doc.sketch_e_43.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,136.0,0), FreeCAD.Vector(264.0,136.0,0)))
    qwm_doc.sketch_e_43.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,136.0,0), FreeCAD.Vector(264.0,152.0,0)))
    qwm_doc.sketch_e_43.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,152.0,0), FreeCAD.Vector(248.0,152.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_43")
    qwm_doc.e_43.Base = qwm_doc.sketch_e_43
    qwm_doc.e_43.Dir = (0, 0, 8.0)
    qwm_doc.e_43.Solid = True
    e_43_viewObject = qwm_doc.e_43.ViewObject
    e_43_viewObject.Transparency = 60
    qwm_doc.e_43.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_44')
    qwm_doc.sketch_e_44.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_44.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,152.0,0), FreeCAD.Vector(264.0,144.0,0)))
    qwm_doc.sketch_e_44.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,144.0,0), FreeCAD.Vector(272.0,144.0,0)))
    qwm_doc.sketch_e_44.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,144.0,0), FreeCAD.Vector(272.0,152.0,0)))
    qwm_doc.sketch_e_44.addGeometry(Part.LineSegment(FreeCAD.Vector(272.0,152.0,0), FreeCAD.Vector(264.0,152.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_44")
    qwm_doc.e_44.Base = qwm_doc.sketch_e_44
    qwm_doc.e_44.Dir = (0, 0, 8.0)
    qwm_doc.e_44.Solid = True
    e_44_viewObject = qwm_doc.e_44.ViewObject
    e_44_viewObject.Transparency = 60
    qwm_doc.e_44.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_45')
    qwm_doc.sketch_e_45.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_45.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,144.0,0), FreeCAD.Vector(232.0,136.0,0)))
    qwm_doc.sketch_e_45.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,136.0,0), FreeCAD.Vector(240.0,136.0,0)))
    qwm_doc.sketch_e_45.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,136.0,0), FreeCAD.Vector(240.0,144.0,0)))
    qwm_doc.sketch_e_45.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,144.0,0), FreeCAD.Vector(232.0,144.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_45")
    qwm_doc.e_45.Base = qwm_doc.sketch_e_45
    qwm_doc.e_45.Dir = (0, 0, 8.0)
    qwm_doc.e_45.Solid = True
    e_45_viewObject = qwm_doc.e_45.ViewObject
    e_45_viewObject.Transparency = 60
    qwm_doc.e_45.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_46')
    qwm_doc.sketch_e_46.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_46.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,144.0,0), FreeCAD.Vector(240.0,136.0,0)))
    qwm_doc.sketch_e_46.addGeometry(Part.LineSegment(FreeCAD.Vector(240.0,136.0,0), FreeCAD.Vector(256.0,136.0,0)))
    qwm_doc.sketch_e_46.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,136.0,0), FreeCAD.Vector(256.0,144.0,0)))
    qwm_doc.sketch_e_46.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,144.0,0), FreeCAD.Vector(240.0,144.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_46")
    qwm_doc.e_46.Base = qwm_doc.sketch_e_46
    qwm_doc.e_46.Dir = (0, 0, 8.0)
    qwm_doc.e_46.Solid = True
    e_46_viewObject = qwm_doc.e_46.ViewObject
    e_46_viewObject.Transparency = 60
    qwm_doc.e_46.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_47')
    qwm_doc.sketch_e_47.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,24.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_47.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,136.0,0), FreeCAD.Vector(248.0,128.0,0)))
    qwm_doc.sketch_e_47.addGeometry(Part.LineSegment(FreeCAD.Vector(248.0,128.0,0), FreeCAD.Vector(256.0,128.0,0)))
    qwm_doc.sketch_e_47.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,128.0,0), FreeCAD.Vector(256.0,136.0,0)))
    qwm_doc.sketch_e_47.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,136.0,0), FreeCAD.Vector(248.0,136.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_47")
    qwm_doc.e_47.Base = qwm_doc.sketch_e_47
    qwm_doc.e_47.Dir = (0, 0, 8.0)
    qwm_doc.e_47.Solid = True
    e_47_viewObject = qwm_doc.e_47.ViewObject
    e_47_viewObject.Transparency = 60
    qwm_doc.e_47.Medium = QW_Modeller.getQWMedium("SkinDry")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_48')
    qwm_doc.sketch_e_48.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,32.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(168.0,552.0,0), FreeCAD.Vector(168.0,544.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(168.0,544.0,0), FreeCAD.Vector(160.0,544.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(160.0,544.0,0), FreeCAD.Vector(160.0,528.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(160.0,528.0,0), FreeCAD.Vector(168.0,528.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(168.0,528.0,0), FreeCAD.Vector(168.0,520.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(168.0,520.0,0), FreeCAD.Vector(176.0,520.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(176.0,520.0,0), FreeCAD.Vector(176.0,512.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(176.0,512.0,0), FreeCAD.Vector(184.0,512.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(184.0,512.0,0), FreeCAD.Vector(184.0,504.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(184.0,504.0,0), FreeCAD.Vector(192.0,504.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,504.0,0), FreeCAD.Vector(192.0,496.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,496.0,0), FreeCAD.Vector(200.0,496.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,496.0,0), FreeCAD.Vector(200.0,488.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,488.0,0), FreeCAD.Vector(208.0,488.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,488.0,0), FreeCAD.Vector(208.0,480.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,480.0,0), FreeCAD.Vector(216.0,480.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,480.0,0), FreeCAD.Vector(216.0,472.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,472.0,0), FreeCAD.Vector(224.0,472.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,472.0,0), FreeCAD.Vector(224.0,464.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,464.0,0), FreeCAD.Vector(256.0,464.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,464.0,0), FreeCAD.Vector(256.0,472.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(256.0,472.0,0), FreeCAD.Vector(280.0,472.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(280.0,472.0,0), FreeCAD.Vector(280.0,480.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(280.0,480.0,0), FreeCAD.Vector(264.0,480.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,480.0,0), FreeCAD.Vector(264.0,488.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(264.0,488.0,0), FreeCAD.Vector(232.0,488.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,488.0,0), FreeCAD.Vector(232.0,496.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(232.0,496.0,0), FreeCAD.Vector(216.0,496.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,496.0,0), FreeCAD.Vector(216.0,504.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,504.0,0), FreeCAD.Vector(208.0,504.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,504.0,0), FreeCAD.Vector(208.0,512.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,512.0,0), FreeCAD.Vector(192.0,512.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,512.0,0), FreeCAD.Vector(192.0,528.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,528.0,0), FreeCAD.Vector(176.0,528.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(176.0,528.0,0), FreeCAD.Vector(176.0,552.0,0)))
    qwm_doc.sketch_e_48.addGeometry(Part.LineSegment(FreeCAD.Vector(176.0,552.0,0), FreeCAD.Vector(168.0,552.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_48")
    qwm_doc.e_48.Base = qwm_doc.sketch_e_48
    qwm_doc.e_48.Dir = (0, 0, 8.0)
    qwm_doc.e_48.Solid = True
    e_48_viewObject = qwm_doc.e_48.ViewObject
    e_48_viewObject.Transparency = 60
    qwm_doc.e_48.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_49')
    qwm_doc.sketch_e_49.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,32.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(176.0,552.0,0), FreeCAD.Vector(176.0,528.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(176.0,528.0,0), FreeCAD.Vector(192.0,528.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,528.0,0), FreeCAD.Vector(192.0,512.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,512.0,0), FreeCAD.Vector(208.0,512.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,512.0,0), FreeCAD.Vector(208.0,504.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,504.0,0), FreeCAD.Vector(216.0,504.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,504.0,0), FreeCAD.Vector(216.0,496.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,496.0,0), FreeCAD.Vector(224.0,496.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,496.0,0), FreeCAD.Vector(224.0,528.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(224.0,528.0,0), FreeCAD.Vector(216.0,528.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,528.0,0), FreeCAD.Vector(216.0,536.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(216.0,536.0,0), FreeCAD.Vector(200.0,536.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,536.0,0), FreeCAD.Vector(200.0,544.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(200.0,544.0,0), FreeCAD.Vector(192.0,544.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,544.0,0), FreeCAD.Vector(192.0,552.0,0)))
    qwm_doc.sketch_e_49.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,552.0,0), FreeCAD.Vector(176.0,552.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_49")
    qwm_doc.e_49.Base = qwm_doc.sketch_e_49
    qwm_doc.e_49.Dir = (0, 0, 8.0)
    qwm_doc.e_49.Solid = True
    e_49_viewObject = qwm_doc.e_49.ViewObject
    e_49_viewObject.Transparency = 60
    qwm_doc.e_49.Medium = QW_Modeller.getQWMedium("Muscle")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_e_50')
    qwm_doc.sketch_e_50.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,32.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_e_50.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,552.0,0), FreeCAD.Vector(192.0,544.0,0)))
    qwm_doc.sketch_e_50.addGeometry(Part.LineSegment(FreeCAD.Vector(192.0,544.0,0), FreeCAD.Vector(208.0,544.0,0)))
    qwm_doc.sketch_e_50.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,544.0,0), FreeCAD.Vector(208.0,552.0,0)))
    qwm_doc.sketch_e_50.addGeometry(Part.LineSegment(FreeCAD.Vector(208.0,552.0,0), FreeCAD.Vector(192.0,552.0,0)))
    qwm_doc.addObject("Part::Extrusion", "e_50")
    qwm_doc.e_50.Base = qwm_doc.sketch_e_50
    qwm_doc.e_50.Dir = (0, 0, 8.0)
    qwm_doc.e_50.Solid = True
    e_50_viewObject = qwm_doc.e_50.ViewObject
    e_50_viewObject.Transparency = 60
    qwm_doc.e_50.Medium = QW_Modeller.getQWMedium("Fat")
    qwm_doc.recompute()
