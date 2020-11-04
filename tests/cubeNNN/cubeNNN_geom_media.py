
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p18')
    qwm_doc.sketch_p18.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p18.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,0.0,0), FreeCAD.Vector(6.0,0.0,0)))
    qwm_doc.sketch_p18.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,0.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p18.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p18.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(4.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p18")
    qwm_doc.p18.Base = qwm_doc.sketch_p18
    qwm_doc.p18.Dir = (0, 0, 2.0)
    qwm_doc.p18.Solid = True
    p18_viewObject = qwm_doc.p18.ViewObject
    p18_viewObject.Transparency = 60
    qwm_doc.p18.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p19')
    qwm_doc.sketch_p19.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p19.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,0.0,0), FreeCAD.Vector(8.0,0.0,0)))
    qwm_doc.sketch_p19.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,0.0,0), FreeCAD.Vector(8.0,2.0,0)))
    qwm_doc.sketch_p19.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,2.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p19.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(6.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p19")
    qwm_doc.p19.Base = qwm_doc.sketch_p19
    qwm_doc.p19.Dir = (0, 0, 2.0)
    qwm_doc.p19.Solid = True
    p19_viewObject = qwm_doc.p19.ViewObject
    p19_viewObject.Transparency = 60
    qwm_doc.p19.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p20')
    qwm_doc.sketch_p20.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p20.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,2.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p20.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p20.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(0.0,4.0,0)))
    qwm_doc.sketch_p20.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,4.0,0), FreeCAD.Vector(0.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p20")
    qwm_doc.p20.Base = qwm_doc.sketch_p20
    qwm_doc.p20.Dir = (0, 0, 2.0)
    qwm_doc.p20.Solid = True
    p20_viewObject = qwm_doc.p20.ViewObject
    p20_viewObject.Transparency = 60
    qwm_doc.p20.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p21')
    qwm_doc.sketch_p21.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p21.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p21.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p21.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p21.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p21")
    qwm_doc.p21.Base = qwm_doc.sketch_p21
    qwm_doc.p21.Dir = (0, 0, 2.0)
    qwm_doc.p21.Solid = True
    p21_viewObject = qwm_doc.p21.ViewObject
    p21_viewObject.Transparency = 60
    qwm_doc.p21.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p22')
    qwm_doc.sketch_p22.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p22.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p22.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p22.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p22.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p22")
    qwm_doc.p22.Base = qwm_doc.sketch_p22
    qwm_doc.p22.Dir = (0, 0, 2.0)
    qwm_doc.p22.Solid = True
    p22_viewObject = qwm_doc.p22.ViewObject
    p22_viewObject.Transparency = 60
    qwm_doc.p22.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p23')
    qwm_doc.sketch_p23.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p23.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(8.0,2.0,0)))
    qwm_doc.sketch_p23.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,2.0,0), FreeCAD.Vector(8.0,4.0,0)))
    qwm_doc.sketch_p23.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,4.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p23.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p23")
    qwm_doc.p23.Base = qwm_doc.sketch_p23
    qwm_doc.p23.Dir = (0, 0, 2.0)
    qwm_doc.p23.Solid = True
    p23_viewObject = qwm_doc.p23.ViewObject
    p23_viewObject.Transparency = 60
    qwm_doc.p23.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p24')
    qwm_doc.sketch_p24.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p24.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,4.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p24.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p24.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(0.0,6.0,0)))
    qwm_doc.sketch_p24.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,6.0,0), FreeCAD.Vector(0.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p24")
    qwm_doc.p24.Base = qwm_doc.sketch_p24
    qwm_doc.p24.Dir = (0, 0, 2.0)
    qwm_doc.p24.Solid = True
    p24_viewObject = qwm_doc.p24.ViewObject
    p24_viewObject.Transparency = 60
    qwm_doc.p24.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p25')
    qwm_doc.sketch_p25.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p25.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p25.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p25.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p25.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p25")
    qwm_doc.p25.Base = qwm_doc.sketch_p25
    qwm_doc.p25.Dir = (0, 0, 2.0)
    qwm_doc.p25.Solid = True
    p25_viewObject = qwm_doc.p25.ViewObject
    p25_viewObject.Transparency = 60
    qwm_doc.p25.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p26')
    qwm_doc.sketch_p26.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p26.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p26.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p26.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p26.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p26")
    qwm_doc.p26.Base = qwm_doc.sketch_p26
    qwm_doc.p26.Dir = (0, 0, 2.0)
    qwm_doc.p26.Solid = True
    p26_viewObject = qwm_doc.p26.ViewObject
    p26_viewObject.Transparency = 60
    qwm_doc.p26.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p27')
    qwm_doc.sketch_p27.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p27.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(8.0,4.0,0)))
    qwm_doc.sketch_p27.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,4.0,0), FreeCAD.Vector(8.0,6.0,0)))
    qwm_doc.sketch_p27.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,6.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p27.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p27")
    qwm_doc.p27.Base = qwm_doc.sketch_p27
    qwm_doc.p27.Dir = (0, 0, 2.0)
    qwm_doc.p27.Solid = True
    p27_viewObject = qwm_doc.p27.ViewObject
    p27_viewObject.Transparency = 60
    qwm_doc.p27.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p28')
    qwm_doc.sketch_p28.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p28.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,6.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p28.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(2.0,8.0,0)))
    qwm_doc.sketch_p28.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,8.0,0), FreeCAD.Vector(0.0,8.0,0)))
    qwm_doc.sketch_p28.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,8.0,0), FreeCAD.Vector(0.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p28")
    qwm_doc.p28.Base = qwm_doc.sketch_p28
    qwm_doc.p28.Dir = (0, 0, 2.0)
    qwm_doc.p28.Solid = True
    p28_viewObject = qwm_doc.p28.ViewObject
    p28_viewObject.Transparency = 60
    qwm_doc.p28.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p29')
    qwm_doc.sketch_p29.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p29.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p29.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(4.0,8.0,0)))
    qwm_doc.sketch_p29.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,8.0,0), FreeCAD.Vector(2.0,8.0,0)))
    qwm_doc.sketch_p29.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,8.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p29")
    qwm_doc.p29.Base = qwm_doc.sketch_p29
    qwm_doc.p29.Dir = (0, 0, 2.0)
    qwm_doc.p29.Solid = True
    p29_viewObject = qwm_doc.p29.ViewObject
    p29_viewObject.Transparency = 60
    qwm_doc.p29.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p30')
    qwm_doc.sketch_p30.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p30.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p30.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(6.0,8.0,0)))
    qwm_doc.sketch_p30.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,8.0,0), FreeCAD.Vector(4.0,8.0,0)))
    qwm_doc.sketch_p30.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,8.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p30")
    qwm_doc.p30.Base = qwm_doc.sketch_p30
    qwm_doc.p30.Dir = (0, 0, 2.0)
    qwm_doc.p30.Solid = True
    p30_viewObject = qwm_doc.p30.ViewObject
    p30_viewObject.Transparency = 60
    qwm_doc.p30.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p31')
    qwm_doc.sketch_p31.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p31.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(8.0,6.0,0)))
    qwm_doc.sketch_p31.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,6.0,0), FreeCAD.Vector(8.0,8.0,0)))
    qwm_doc.sketch_p31.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,8.0,0), FreeCAD.Vector(6.0,8.0,0)))
    qwm_doc.sketch_p31.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,8.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p31")
    qwm_doc.p31.Base = qwm_doc.sketch_p31
    qwm_doc.p31.Dir = (0, 0, 2.0)
    qwm_doc.p31.Solid = True
    p31_viewObject = qwm_doc.p31.ViewObject
    p31_viewObject.Transparency = 60
    qwm_doc.p31.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p32')
    qwm_doc.sketch_p32.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p32.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,0.0,0), FreeCAD.Vector(2.0,0.0,0)))
    qwm_doc.sketch_p32.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,0.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p32.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(0.0,2.0,0)))
    qwm_doc.sketch_p32.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,2.0,0), FreeCAD.Vector(0.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p32")
    qwm_doc.p32.Base = qwm_doc.sketch_p32
    qwm_doc.p32.Dir = (0, 0, 2.0)
    qwm_doc.p32.Solid = True
    p32_viewObject = qwm_doc.p32.ViewObject
    p32_viewObject.Transparency = 60
    qwm_doc.p32.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p33')
    qwm_doc.sketch_p33.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p33.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,0.0,0), FreeCAD.Vector(4.0,0.0,0)))
    qwm_doc.sketch_p33.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,0.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p33.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p33.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(2.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p33")
    qwm_doc.p33.Base = qwm_doc.sketch_p33
    qwm_doc.p33.Dir = (0, 0, 2.0)
    qwm_doc.p33.Solid = True
    p33_viewObject = qwm_doc.p33.ViewObject
    p33_viewObject.Transparency = 60
    qwm_doc.p33.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p34')
    qwm_doc.sketch_p34.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p34.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,0.0,0), FreeCAD.Vector(6.0,0.0,0)))
    qwm_doc.sketch_p34.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,0.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p34.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p34.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(4.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p34")
    qwm_doc.p34.Base = qwm_doc.sketch_p34
    qwm_doc.p34.Dir = (0, 0, 2.0)
    qwm_doc.p34.Solid = True
    p34_viewObject = qwm_doc.p34.ViewObject
    p34_viewObject.Transparency = 60
    qwm_doc.p34.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p35')
    qwm_doc.sketch_p35.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p35.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,0.0,0), FreeCAD.Vector(8.0,0.0,0)))
    qwm_doc.sketch_p35.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,0.0,0), FreeCAD.Vector(8.0,2.0,0)))
    qwm_doc.sketch_p35.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,2.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p35.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(6.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p35")
    qwm_doc.p35.Base = qwm_doc.sketch_p35
    qwm_doc.p35.Dir = (0, 0, 2.0)
    qwm_doc.p35.Solid = True
    p35_viewObject = qwm_doc.p35.ViewObject
    p35_viewObject.Transparency = 60
    qwm_doc.p35.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p36')
    qwm_doc.sketch_p36.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p36.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,2.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p36.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p36.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(0.0,4.0,0)))
    qwm_doc.sketch_p36.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,4.0,0), FreeCAD.Vector(0.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p36")
    qwm_doc.p36.Base = qwm_doc.sketch_p36
    qwm_doc.p36.Dir = (0, 0, 2.0)
    qwm_doc.p36.Solid = True
    p36_viewObject = qwm_doc.p36.ViewObject
    p36_viewObject.Transparency = 60
    qwm_doc.p36.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p37')
    qwm_doc.sketch_p37.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p37.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p37.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p37.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p37.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p37")
    qwm_doc.p37.Base = qwm_doc.sketch_p37
    qwm_doc.p37.Dir = (0, 0, 2.0)
    qwm_doc.p37.Solid = True
    p37_viewObject = qwm_doc.p37.ViewObject
    p37_viewObject.Transparency = 60
    qwm_doc.p37.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p38')
    qwm_doc.sketch_p38.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p38.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p38.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p38.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p38.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p38")
    qwm_doc.p38.Base = qwm_doc.sketch_p38
    qwm_doc.p38.Dir = (0, 0, 2.0)
    qwm_doc.p38.Solid = True
    p38_viewObject = qwm_doc.p38.ViewObject
    p38_viewObject.Transparency = 60
    qwm_doc.p38.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p39')
    qwm_doc.sketch_p39.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p39.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(8.0,2.0,0)))
    qwm_doc.sketch_p39.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,2.0,0), FreeCAD.Vector(8.0,4.0,0)))
    qwm_doc.sketch_p39.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,4.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p39.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p39")
    qwm_doc.p39.Base = qwm_doc.sketch_p39
    qwm_doc.p39.Dir = (0, 0, 2.0)
    qwm_doc.p39.Solid = True
    p39_viewObject = qwm_doc.p39.ViewObject
    p39_viewObject.Transparency = 60
    qwm_doc.p39.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p40')
    qwm_doc.sketch_p40.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p40.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,4.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p40.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p40.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(0.0,6.0,0)))
    qwm_doc.sketch_p40.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,6.0,0), FreeCAD.Vector(0.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p40")
    qwm_doc.p40.Base = qwm_doc.sketch_p40
    qwm_doc.p40.Dir = (0, 0, 2.0)
    qwm_doc.p40.Solid = True
    p40_viewObject = qwm_doc.p40.ViewObject
    p40_viewObject.Transparency = 60
    qwm_doc.p40.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p41')
    qwm_doc.sketch_p41.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p41.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p41.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p41.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p41.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p41")
    qwm_doc.p41.Base = qwm_doc.sketch_p41
    qwm_doc.p41.Dir = (0, 0, 2.0)
    qwm_doc.p41.Solid = True
    p41_viewObject = qwm_doc.p41.ViewObject
    p41_viewObject.Transparency = 60
    qwm_doc.p41.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p42')
    qwm_doc.sketch_p42.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p42.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p42.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p42.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p42.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p42")
    qwm_doc.p42.Base = qwm_doc.sketch_p42
    qwm_doc.p42.Dir = (0, 0, 2.0)
    qwm_doc.p42.Solid = True
    p42_viewObject = qwm_doc.p42.ViewObject
    p42_viewObject.Transparency = 60
    qwm_doc.p42.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p43')
    qwm_doc.sketch_p43.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p43.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(8.0,4.0,0)))
    qwm_doc.sketch_p43.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,4.0,0), FreeCAD.Vector(8.0,6.0,0)))
    qwm_doc.sketch_p43.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,6.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p43.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p43")
    qwm_doc.p43.Base = qwm_doc.sketch_p43
    qwm_doc.p43.Dir = (0, 0, 2.0)
    qwm_doc.p43.Solid = True
    p43_viewObject = qwm_doc.p43.ViewObject
    p43_viewObject.Transparency = 60
    qwm_doc.p43.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p44')
    qwm_doc.sketch_p44.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p44.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,6.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p44.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(2.0,8.0,0)))
    qwm_doc.sketch_p44.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,8.0,0), FreeCAD.Vector(0.0,8.0,0)))
    qwm_doc.sketch_p44.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,8.0,0), FreeCAD.Vector(0.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p44")
    qwm_doc.p44.Base = qwm_doc.sketch_p44
    qwm_doc.p44.Dir = (0, 0, 2.0)
    qwm_doc.p44.Solid = True
    p44_viewObject = qwm_doc.p44.ViewObject
    p44_viewObject.Transparency = 60
    qwm_doc.p44.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p45')
    qwm_doc.sketch_p45.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p45.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p45.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(4.0,8.0,0)))
    qwm_doc.sketch_p45.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,8.0,0), FreeCAD.Vector(2.0,8.0,0)))
    qwm_doc.sketch_p45.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,8.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p45")
    qwm_doc.p45.Base = qwm_doc.sketch_p45
    qwm_doc.p45.Dir = (0, 0, 2.0)
    qwm_doc.p45.Solid = True
    p45_viewObject = qwm_doc.p45.ViewObject
    p45_viewObject.Transparency = 60
    qwm_doc.p45.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p46')
    qwm_doc.sketch_p46.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p46.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p46.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(6.0,8.0,0)))
    qwm_doc.sketch_p46.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,8.0,0), FreeCAD.Vector(4.0,8.0,0)))
    qwm_doc.sketch_p46.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,8.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p46")
    qwm_doc.p46.Base = qwm_doc.sketch_p46
    qwm_doc.p46.Dir = (0, 0, 2.0)
    qwm_doc.p46.Solid = True
    p46_viewObject = qwm_doc.p46.ViewObject
    p46_viewObject.Transparency = 60
    qwm_doc.p46.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p47')
    qwm_doc.sketch_p47.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p47.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(8.0,6.0,0)))
    qwm_doc.sketch_p47.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,6.0,0), FreeCAD.Vector(8.0,8.0,0)))
    qwm_doc.sketch_p47.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,8.0,0), FreeCAD.Vector(6.0,8.0,0)))
    qwm_doc.sketch_p47.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,8.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p47")
    qwm_doc.p47.Base = qwm_doc.sketch_p47
    qwm_doc.p47.Dir = (0, 0, 2.0)
    qwm_doc.p47.Solid = True
    p47_viewObject = qwm_doc.p47.ViewObject
    p47_viewObject.Transparency = 60
    qwm_doc.p47.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p48')
    qwm_doc.sketch_p48.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p48.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,0.0,0), FreeCAD.Vector(2.0,0.0,0)))
    qwm_doc.sketch_p48.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,0.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p48.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(0.0,2.0,0)))
    qwm_doc.sketch_p48.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,2.0,0), FreeCAD.Vector(0.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p48")
    qwm_doc.p48.Base = qwm_doc.sketch_p48
    qwm_doc.p48.Dir = (0, 0, 2.0)
    qwm_doc.p48.Solid = True
    p48_viewObject = qwm_doc.p48.ViewObject
    p48_viewObject.Transparency = 60
    qwm_doc.p48.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p49')
    qwm_doc.sketch_p49.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p49.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,0.0,0), FreeCAD.Vector(4.0,0.0,0)))
    qwm_doc.sketch_p49.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,0.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p49.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p49.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(2.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p49")
    qwm_doc.p49.Base = qwm_doc.sketch_p49
    qwm_doc.p49.Dir = (0, 0, 2.0)
    qwm_doc.p49.Solid = True
    p49_viewObject = qwm_doc.p49.ViewObject
    p49_viewObject.Transparency = 60
    qwm_doc.p49.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p50')
    qwm_doc.sketch_p50.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p50.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,0.0,0), FreeCAD.Vector(6.0,0.0,0)))
    qwm_doc.sketch_p50.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,0.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p50.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p50.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(4.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p50")
    qwm_doc.p50.Base = qwm_doc.sketch_p50
    qwm_doc.p50.Dir = (0, 0, 2.0)
    qwm_doc.p50.Solid = True
    p50_viewObject = qwm_doc.p50.ViewObject
    p50_viewObject.Transparency = 60
    qwm_doc.p50.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p51')
    qwm_doc.sketch_p51.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p51.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,0.0,0), FreeCAD.Vector(8.0,0.0,0)))
    qwm_doc.sketch_p51.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,0.0,0), FreeCAD.Vector(8.0,2.0,0)))
    qwm_doc.sketch_p51.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,2.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p51.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(6.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p51")
    qwm_doc.p51.Base = qwm_doc.sketch_p51
    qwm_doc.p51.Dir = (0, 0, 2.0)
    qwm_doc.p51.Solid = True
    p51_viewObject = qwm_doc.p51.ViewObject
    p51_viewObject.Transparency = 60
    qwm_doc.p51.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p52')
    qwm_doc.sketch_p52.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p52.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,2.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.sketch_p52.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p52.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(0.0,4.0,0)))
    qwm_doc.sketch_p52.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,4.0,0), FreeCAD.Vector(0.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p52")
    qwm_doc.p52.Base = qwm_doc.sketch_p52
    qwm_doc.p52.Dir = (0, 0, 2.0)
    qwm_doc.p52.Solid = True
    p52_viewObject = qwm_doc.p52.ViewObject
    p52_viewObject.Transparency = 60
    qwm_doc.p52.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p53')
    qwm_doc.sketch_p53.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p53.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,2.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.sketch_p53.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p53.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p53.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(2.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p53")
    qwm_doc.p53.Base = qwm_doc.sketch_p53
    qwm_doc.p53.Dir = (0, 0, 2.0)
    qwm_doc.p53.Solid = True
    p53_viewObject = qwm_doc.p53.ViewObject
    p53_viewObject.Transparency = 60
    qwm_doc.p53.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p54')
    qwm_doc.sketch_p54.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p54.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,2.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.sketch_p54.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p54.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p54.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(4.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p54")
    qwm_doc.p54.Base = qwm_doc.sketch_p54
    qwm_doc.p54.Dir = (0, 0, 2.0)
    qwm_doc.p54.Solid = True
    p54_viewObject = qwm_doc.p54.ViewObject
    p54_viewObject.Transparency = 60
    qwm_doc.p54.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p55')
    qwm_doc.sketch_p55.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p55.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,2.0,0), FreeCAD.Vector(8.0,2.0,0)))
    qwm_doc.sketch_p55.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,2.0,0), FreeCAD.Vector(8.0,4.0,0)))
    qwm_doc.sketch_p55.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,4.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p55.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(6.0,2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p55")
    qwm_doc.p55.Base = qwm_doc.sketch_p55
    qwm_doc.p55.Dir = (0, 0, 2.0)
    qwm_doc.p55.Solid = True
    p55_viewObject = qwm_doc.p55.ViewObject
    p55_viewObject.Transparency = 60
    qwm_doc.p55.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p56')
    qwm_doc.sketch_p56.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p56.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,4.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.sketch_p56.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p56.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(0.0,6.0,0)))
    qwm_doc.sketch_p56.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,6.0,0), FreeCAD.Vector(0.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p56")
    qwm_doc.p56.Base = qwm_doc.sketch_p56
    qwm_doc.p56.Dir = (0, 0, 2.0)
    qwm_doc.p56.Solid = True
    p56_viewObject = qwm_doc.p56.ViewObject
    p56_viewObject.Transparency = 60
    qwm_doc.p56.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p57')
    qwm_doc.sketch_p57.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p57.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,4.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.sketch_p57.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p57.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p57.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(2.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p57")
    qwm_doc.p57.Base = qwm_doc.sketch_p57
    qwm_doc.p57.Dir = (0, 0, 2.0)
    qwm_doc.p57.Solid = True
    p57_viewObject = qwm_doc.p57.ViewObject
    p57_viewObject.Transparency = 60
    qwm_doc.p57.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p58')
    qwm_doc.sketch_p58.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p58.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,4.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.sketch_p58.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p58.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p58.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(4.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p58")
    qwm_doc.p58.Base = qwm_doc.sketch_p58
    qwm_doc.p58.Dir = (0, 0, 2.0)
    qwm_doc.p58.Solid = True
    p58_viewObject = qwm_doc.p58.ViewObject
    p58_viewObject.Transparency = 60
    qwm_doc.p58.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p59')
    qwm_doc.sketch_p59.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p59.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,4.0,0), FreeCAD.Vector(8.0,4.0,0)))
    qwm_doc.sketch_p59.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,4.0,0), FreeCAD.Vector(8.0,6.0,0)))
    qwm_doc.sketch_p59.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,6.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p59.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(6.0,4.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p59")
    qwm_doc.p59.Base = qwm_doc.sketch_p59
    qwm_doc.p59.Dir = (0, 0, 2.0)
    qwm_doc.p59.Solid = True
    p59_viewObject = qwm_doc.p59.ViewObject
    p59_viewObject.Transparency = 60
    qwm_doc.p59.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p60')
    qwm_doc.sketch_p60.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p60.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,6.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.sketch_p60.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(2.0,8.0,0)))
    qwm_doc.sketch_p60.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,8.0,0), FreeCAD.Vector(0.0,8.0,0)))
    qwm_doc.sketch_p60.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,8.0,0), FreeCAD.Vector(0.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p60")
    qwm_doc.p60.Base = qwm_doc.sketch_p60
    qwm_doc.p60.Dir = (0, 0, 2.0)
    qwm_doc.p60.Solid = True
    p60_viewObject = qwm_doc.p60.ViewObject
    p60_viewObject.Transparency = 60
    qwm_doc.p60.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p61')
    qwm_doc.sketch_p61.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p61.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,6.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.sketch_p61.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(4.0,8.0,0)))
    qwm_doc.sketch_p61.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,8.0,0), FreeCAD.Vector(2.0,8.0,0)))
    qwm_doc.sketch_p61.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,8.0,0), FreeCAD.Vector(2.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p61")
    qwm_doc.p61.Base = qwm_doc.sketch_p61
    qwm_doc.p61.Dir = (0, 0, 2.0)
    qwm_doc.p61.Solid = True
    p61_viewObject = qwm_doc.p61.ViewObject
    p61_viewObject.Transparency = 60
    qwm_doc.p61.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p62')
    qwm_doc.sketch_p62.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p62.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,6.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.sketch_p62.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(6.0,8.0,0)))
    qwm_doc.sketch_p62.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,8.0,0), FreeCAD.Vector(4.0,8.0,0)))
    qwm_doc.sketch_p62.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,8.0,0), FreeCAD.Vector(4.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p62")
    qwm_doc.p62.Base = qwm_doc.sketch_p62
    qwm_doc.p62.Dir = (0, 0, 2.0)
    qwm_doc.p62.Solid = True
    p62_viewObject = qwm_doc.p62.ViewObject
    p62_viewObject.Transparency = 60
    qwm_doc.p62.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_p63')
    qwm_doc.sketch_p63.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,6.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_p63.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,6.0,0), FreeCAD.Vector(8.0,6.0,0)))
    qwm_doc.sketch_p63.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,6.0,0), FreeCAD.Vector(8.0,8.0,0)))
    qwm_doc.sketch_p63.addGeometry(Part.LineSegment(FreeCAD.Vector(8.0,8.0,0), FreeCAD.Vector(6.0,8.0,0)))
    qwm_doc.sketch_p63.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,8.0,0), FreeCAD.Vector(6.0,6.0,0)))
    qwm_doc.addObject("Part::Extrusion", "p63")
    qwm_doc.p63.Base = qwm_doc.sketch_p63
    qwm_doc.p63.Dir = (0, 0, 2.0)
    qwm_doc.p63.Solid = True
    p63_viewObject = qwm_doc.p63.ViewObject
    p63_viewObject.Transparency = 60
    qwm_doc.p63.Medium = QW_Modeller.getQWMedium("air")
