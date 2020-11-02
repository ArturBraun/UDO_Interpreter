
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_wgu')
    qwm_doc.sketch_wgu.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,-20.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_wgu.addGeometry(Part.LineSegment(FreeCAD.Vector(-7.0,-4.5,0), FreeCAD.Vector(7.0,-4.5,0)))
    qwm_doc.sketch_wgu.addGeometry(Part.LineSegment(FreeCAD.Vector(7.0,-4.5,0), FreeCAD.Vector(7.0,4.5,0)))
    qwm_doc.sketch_wgu.addGeometry(Part.LineSegment(FreeCAD.Vector(7.0,4.5,0), FreeCAD.Vector(-7.0,4.5,0)))
    qwm_doc.sketch_wgu.addGeometry(Part.LineSegment(FreeCAD.Vector(-7.0,4.5,0), FreeCAD.Vector(-7.0,-4.5,0)))
    qwm_doc.sketch_wgu.addGeometry(Part.LineSegment(FreeCAD.Vector(-7.0,-4.5,0), FreeCAD.Vector(-5.0,-2.5,0)))
    qwm_doc.sketch_wgu.addGeometry(Part.LineSegment(FreeCAD.Vector(-5.0,-2.5,0), FreeCAD.Vector(-5.0,2.5,0)))
    qwm_doc.sketch_wgu.addGeometry(Part.LineSegment(FreeCAD.Vector(-5.0,2.5,0), FreeCAD.Vector(5.0,2.5,0)))
    qwm_doc.sketch_wgu.addGeometry(Part.LineSegment(FreeCAD.Vector(5.0,2.5,0), FreeCAD.Vector(5.0,-2.5,0)))
    qwm_doc.sketch_wgu.addGeometry(Part.LineSegment(FreeCAD.Vector(5.0,-2.5,0), FreeCAD.Vector(-5.0,-2.5,0)))
    qwm_doc.sketch_wgu.addGeometry(Part.LineSegment(FreeCAD.Vector(-5.0,-2.5,0), FreeCAD.Vector(-7.0,-4.5,0)))
    qwm_doc.addObject("Part::Extrusion", "wgu")
    qwm_doc.wgu.Base = qwm_doc.sketch_wgu
    qwm_doc.wgu.Dir = (0, 0, 20.0)
    qwm_doc.wgu.Solid = True
    wgu_viewObject = qwm_doc.wgu.ViewObject
    wgu_viewObject.Transparency = 60
    qwm_doc.wgu.Medium = QW_Modeller.getQWMedium("metal")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_horn')
    qwm_doc.sketch_horn.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_horn.addGeometry(Part.LineSegment(FreeCAD.Vector(-7.0,-4.5,0), FreeCAD.Vector(7.0,-4.5,0)))
    qwm_doc.sketch_horn.addGeometry(Part.LineSegment(FreeCAD.Vector(7.0,-4.5,0), FreeCAD.Vector(7.0,4.5,0)))
    qwm_doc.sketch_horn.addGeometry(Part.LineSegment(FreeCAD.Vector(7.0,4.5,0), FreeCAD.Vector(-7.0,4.5,0)))
    qwm_doc.sketch_horn.addGeometry(Part.LineSegment(FreeCAD.Vector(-7.0,4.5,0), FreeCAD.Vector(-7.0,-4.5,0)))
    qwm_doc.sketch_horn.addGeometry(Part.LineSegment(FreeCAD.Vector(-7.0,-4.5,0), FreeCAD.Vector(-5.0,-2.5,0)))
    qwm_doc.sketch_horn.addGeometry(Part.LineSegment(FreeCAD.Vector(-5.0,-2.5,0), FreeCAD.Vector(-5.0,2.5,0)))
    qwm_doc.sketch_horn.addGeometry(Part.LineSegment(FreeCAD.Vector(-5.0,2.5,0), FreeCAD.Vector(5.0,2.5,0)))
    qwm_doc.sketch_horn.addGeometry(Part.LineSegment(FreeCAD.Vector(5.0,2.5,0), FreeCAD.Vector(5.0,-2.5,0)))
    qwm_doc.sketch_horn.addGeometry(Part.LineSegment(FreeCAD.Vector(5.0,-2.5,0), FreeCAD.Vector(-5.0,-2.5,0)))
    qwm_doc.sketch_horn.addGeometry(Part.LineSegment(FreeCAD.Vector(-5.0,-2.5,0), FreeCAD.Vector(-7.0,-4.5,0)))
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_horn1')
    qwm_doc.sketch_horn1.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,30.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_horn1.addGeometry(Part.LineSegment(FreeCAD.Vector(-12.0,-9.5,0), FreeCAD.Vector(12.0,-9.5,0)))
    qwm_doc.sketch_horn1.addGeometry(Part.LineSegment(FreeCAD.Vector(12.0,-9.5,0), FreeCAD.Vector(12.0,9.5,0)))
    qwm_doc.sketch_horn1.addGeometry(Part.LineSegment(FreeCAD.Vector(12.0,9.5,0), FreeCAD.Vector(-12.0,9.5,0)))
    qwm_doc.sketch_horn1.addGeometry(Part.LineSegment(FreeCAD.Vector(-12.0,9.5,0), FreeCAD.Vector(-12.0,-9.5,0)))
    qwm_doc.sketch_horn1.addGeometry(Part.LineSegment(FreeCAD.Vector(-12.0,-9.5,0), FreeCAD.Vector(-10.0,-7.5,0)))
    qwm_doc.sketch_horn1.addGeometry(Part.LineSegment(FreeCAD.Vector(-10.0,-7.5,0), FreeCAD.Vector(-10.0,7.5,0)))
    qwm_doc.sketch_horn1.addGeometry(Part.LineSegment(FreeCAD.Vector(-10.0,7.5,0), FreeCAD.Vector(10.0,7.5,0)))
    qwm_doc.sketch_horn1.addGeometry(Part.LineSegment(FreeCAD.Vector(10.0,7.5,0), FreeCAD.Vector(10.0,-7.5,0)))
    qwm_doc.sketch_horn1.addGeometry(Part.LineSegment(FreeCAD.Vector(10.0,-7.5,0), FreeCAD.Vector(-10.0,-7.5,0)))
    qwm_doc.sketch_horn1.addGeometry(Part.LineSegment(FreeCAD.Vector(-10.0,-7.5,0), FreeCAD.Vector(-12.0,-9.5,0)))
    qwm_doc.addObject("Part::Loft", "horn1")
    qwm_doc.horn1.Sections=[qwm_doc.sketch_horn, qwm_doc.sketch_horn1]
    qwm_doc.horn1.Solid=True
    qwm_doc.horn1.Ruled=False
    qwm_doc.horn1.Closed=False
    horn1_viewObject = qwm_doc.horn1.ViewObject
    horn1_viewObject.Transparency = 60
    qwm_doc.horn1.Medium = QW_Modeller.getQWMedium("metal")
    qwm_doc.recompute()
    