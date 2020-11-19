
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p')
    qwm_doc.sketch_p.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,0.0,0), FreeCAD.Vector(2.0,0.0,0)))
    qwm_doc.sketch_p.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,0.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(0.0,2.0,0)))
    qwm_doc.sketch_p.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,2.0,0), FreeCAD.Vector(0.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p")
    qwm_doc.p.Base = qwm_doc.sketch_p
    qwm_doc.p.Dir = (0, 0, 2.0)
    qwm_doc.p.Solid = True
    p_viewObject = qwm_doc.p.ViewObject
    p_viewObject.Transparency = 60
    qwm_doc.p.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p1')
    qwm_doc.sketch_p1.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p1.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,0.0,0), FreeCAD.Vector(4.0,0.0,0)))
    qwm_doc.sketch_p1.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,0.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p1.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p1.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(2.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p1")
    qwm_doc.p1.Base = qwm_doc.sketch_p1
    qwm_doc.p1.Dir = (0, 0, 2.0)
    qwm_doc.p1.Solid = True
    p1_viewObject = qwm_doc.p1.ViewObject
    p1_viewObject.Transparency = 60
    qwm_doc.p1.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p2')
    qwm_doc.sketch_p2.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p2.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,0.0,0), FreeCAD.Vector(6.0,0.0,0)))
    qwm_doc.sketch_p2.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,0.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p2.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p2.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(4.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p2")
    qwm_doc.p2.Base = qwm_doc.sketch_p2
    qwm_doc.p2.Dir = (0, 0, 2.0)
    qwm_doc.p2.Solid = True
    p2_viewObject = qwm_doc.p2.ViewObject
    p2_viewObject.Transparency = 60
    qwm_doc.p2.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p3')
    qwm_doc.sketch_p3.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p3.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,0.0,0), FreeCAD.Vector(8.0,0.0,0)))
    qwm_doc.sketch_p3.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,0.0,0), FreeCAD.Vector(8.0,2.0,0)))
    qwm_doc.sketch_p3.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,2.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p3.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(6.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p3")
    qwm_doc.p3.Base = qwm_doc.sketch_p3
    qwm_doc.p3.Dir = (0, 0, 2.0)
    qwm_doc.p3.Solid = True
    p3_viewObject = qwm_doc.p3.ViewObject
    p3_viewObject.Transparency = 60
    qwm_doc.p3.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p4')
    qwm_doc.sketch_p4.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p4.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,2.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p4.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p4.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(0.0,4.0,0)))
    qwm_doc.sketch_p4.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,4.0,0), FreeCAD.Vector(0.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p4")
    qwm_doc.p4.Base = qwm_doc.sketch_p4
    qwm_doc.p4.Dir = (0, 0, 2.0)
    qwm_doc.p4.Solid = True
    p4_viewObject = qwm_doc.p4.ViewObject
    p4_viewObject.Transparency = 60
    qwm_doc.p4.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p5')
    qwm_doc.sketch_p5.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p5.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p5.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p5.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p5.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p5")
    qwm_doc.p5.Base = qwm_doc.sketch_p5
    qwm_doc.p5.Dir = (0, 0, 2.0)
    qwm_doc.p5.Solid = True
    p5_viewObject = qwm_doc.p5.ViewObject
    p5_viewObject.Transparency = 60
    qwm_doc.p5.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p6')
    qwm_doc.sketch_p6.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p6.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p6.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p6.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p6.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p6")
    qwm_doc.p6.Base = qwm_doc.sketch_p6
    qwm_doc.p6.Dir = (0, 0, 2.0)
    qwm_doc.p6.Solid = True
    p6_viewObject = qwm_doc.p6.ViewObject
    p6_viewObject.Transparency = 60
    qwm_doc.p6.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p7')
    qwm_doc.sketch_p7.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p7.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(8.0,2.0,0)))
    qwm_doc.sketch_p7.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,2.0,0), FreeCAD.Vector(8.0,4.0,0)))
    qwm_doc.sketch_p7.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,4.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p7.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p7")
    qwm_doc.p7.Base = qwm_doc.sketch_p7
    qwm_doc.p7.Dir = (0, 0, 2.0)
    qwm_doc.p7.Solid = True
    p7_viewObject = qwm_doc.p7.ViewObject
    p7_viewObject.Transparency = 60
    qwm_doc.p7.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p8')
    qwm_doc.sketch_p8.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p8.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,4.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p8.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p8.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(0.0,6.0,0)))
    qwm_doc.sketch_p8.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,6.0,0), FreeCAD.Vector(0.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p8")
    qwm_doc.p8.Base = qwm_doc.sketch_p8
    qwm_doc.p8.Dir = (0, 0, 2.0)
    qwm_doc.p8.Solid = True
    p8_viewObject = qwm_doc.p8.ViewObject
    p8_viewObject.Transparency = 60
    qwm_doc.p8.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p9')
    qwm_doc.sketch_p9.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p9.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p9.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p9.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p9.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p9")
    qwm_doc.p9.Base = qwm_doc.sketch_p9
    qwm_doc.p9.Dir = (0, 0, 2.0)
    qwm_doc.p9.Solid = True
    p9_viewObject = qwm_doc.p9.ViewObject
    p9_viewObject.Transparency = 60
    qwm_doc.p9.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p10')
    qwm_doc.sketch_p10.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p10.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p10.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p10.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p10.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p10")
    qwm_doc.p10.Base = qwm_doc.sketch_p10
    qwm_doc.p10.Dir = (0, 0, 2.0)
    qwm_doc.p10.Solid = True
    p10_viewObject = qwm_doc.p10.ViewObject
    p10_viewObject.Transparency = 60
    qwm_doc.p10.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p11')
    qwm_doc.sketch_p11.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p11.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(8.0,4.0,0)))
    qwm_doc.sketch_p11.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,4.0,0), FreeCAD.Vector(8.0,6.0,0)))
    qwm_doc.sketch_p11.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,6.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p11.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p11")
    qwm_doc.p11.Base = qwm_doc.sketch_p11
    qwm_doc.p11.Dir = (0, 0, 2.0)
    qwm_doc.p11.Solid = True
    p11_viewObject = qwm_doc.p11.ViewObject
    p11_viewObject.Transparency = 60
    qwm_doc.p11.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p12')
    qwm_doc.sketch_p12.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p12.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,6.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p12.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(2.0,8.0,0)))
    qwm_doc.sketch_p12.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,8.0,0), FreeCAD.Vector(0.0,8.0,0)))
    qwm_doc.sketch_p12.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,8.0,0), FreeCAD.Vector(0.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p12")
    qwm_doc.p12.Base = qwm_doc.sketch_p12
    qwm_doc.p12.Dir = (0, 0, 2.0)
    qwm_doc.p12.Solid = True
    p12_viewObject = qwm_doc.p12.ViewObject
    p12_viewObject.Transparency = 60
    qwm_doc.p12.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p13')
    qwm_doc.sketch_p13.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p13.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p13.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(4.0,8.0,0)))
    qwm_doc.sketch_p13.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,8.0,0), FreeCAD.Vector(2.0,8.0,0)))
    qwm_doc.sketch_p13.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,8.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p13")
    qwm_doc.p13.Base = qwm_doc.sketch_p13
    qwm_doc.p13.Dir = (0, 0, 2.0)
    qwm_doc.p13.Solid = True
    p13_viewObject = qwm_doc.p13.ViewObject
    p13_viewObject.Transparency = 60
    qwm_doc.p13.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p14')
    qwm_doc.sketch_p14.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p14.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p14.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(6.0,8.0,0)))
    qwm_doc.sketch_p14.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,8.0,0), FreeCAD.Vector(4.0,8.0,0)))
    qwm_doc.sketch_p14.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,8.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p14")
    qwm_doc.p14.Base = qwm_doc.sketch_p14
    qwm_doc.p14.Dir = (0, 0, 2.0)
    qwm_doc.p14.Solid = True
    p14_viewObject = qwm_doc.p14.ViewObject
    p14_viewObject.Transparency = 60
    qwm_doc.p14.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p15')
    qwm_doc.sketch_p15.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p15.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(8.0,6.0,0)))
    qwm_doc.sketch_p15.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,6.0,0), FreeCAD.Vector(8.0,8.0,0)))
    qwm_doc.sketch_p15.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,8.0,0), FreeCAD.Vector(6.0,8.0,0)))
    qwm_doc.sketch_p15.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,8.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p15")
    qwm_doc.p15.Base = qwm_doc.sketch_p15
    qwm_doc.p15.Dir = (0, 0, 2.0)
    qwm_doc.p15.Solid = True
    p15_viewObject = qwm_doc.p15.ViewObject
    p15_viewObject.Transparency = 60
    qwm_doc.p15.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p16')
    qwm_doc.sketch_p16.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p16.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,0.0,0), FreeCAD.Vector(2.0,0.0,0)))
    qwm_doc.sketch_p16.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,0.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p16.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(0.0,2.0,0)))
    qwm_doc.sketch_p16.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,2.0,0), FreeCAD.Vector(0.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p16")
    qwm_doc.p16.Base = qwm_doc.sketch_p16
    qwm_doc.p16.Dir = (0, 0, 2.0)
    qwm_doc.p16.Solid = True
    p16_viewObject = qwm_doc.p16.ViewObject
    p16_viewObject.Transparency = 60
    qwm_doc.p16.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p17')
    qwm_doc.sketch_p17.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p17.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,0.0,0), FreeCAD.Vector(4.0,0.0,0)))
    qwm_doc.sketch_p17.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,0.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p17.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p17.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(2.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p17")
    qwm_doc.p17.Base = qwm_doc.sketch_p17
    qwm_doc.p17.Dir = (0, 0, 2.0)
    qwm_doc.p17.Solid = True
    p17_viewObject = qwm_doc.p17.ViewObject
    p17_viewObject.Transparency = 60
    qwm_doc.p17.Medium = QW_Modeller.getQWMedium("air")
