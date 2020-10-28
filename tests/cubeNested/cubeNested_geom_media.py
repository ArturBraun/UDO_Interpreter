
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_cubic')
    qwm_doc.sketch_cubic.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_cubic.addGeometry(Part.LineSegment(FreeCAD.Vector(-5.0,-5.0,0), FreeCAD.Vector(5.0,-5.0,0)))
    qwm_doc.sketch_cubic.addGeometry(Part.LineSegment(FreeCAD.Vector(5.0,-5.0,0), FreeCAD.Vector(5.0,5.0,0)))
    qwm_doc.sketch_cubic.addGeometry(Part.LineSegment(FreeCAD.Vector(5.0,5.0,0), FreeCAD.Vector(-5.0,5.0,0)))
    qwm_doc.sketch_cubic.addGeometry(Part.LineSegment(FreeCAD.Vector(-5.0,5.0,0), FreeCAD.Vector(-5.0,-5.0,0)))
    qwm_doc.addObject("Part::Extrusion", "cubic")
    qwm_doc.cubic.Base = qwm_doc.sketch_cubic
    qwm_doc.cubic.Dir = (0, 0, 10.0)
    qwm_doc.cubic.Solid = True
    cubic_viewObject = qwm_doc.cubic.ViewObject
    cubic_viewObject.Transparency = 60
    qwm_doc.cubic.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.recompute()
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_cubic1')
    qwm_doc.sketch_cubic1.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,15.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_cubic1.addGeometry(Part.LineSegment(FreeCAD.Vector(10.0,10.0,0), FreeCAD.Vector(20.0,10.0,0)))
    qwm_doc.sketch_cubic1.addGeometry(Part.LineSegment(FreeCAD.Vector(20.0,10.0,0), FreeCAD.Vector(20.0,20.0,0)))
    qwm_doc.sketch_cubic1.addGeometry(Part.LineSegment(FreeCAD.Vector(20.0,20.0,0), FreeCAD.Vector(10.0,20.0,0)))
    qwm_doc.sketch_cubic1.addGeometry(Part.LineSegment(FreeCAD.Vector(10.0,20.0,0), FreeCAD.Vector(10.0,10.0,0)))
    qwm_doc.addObject("Part::Extrusion", "cubic1")
    qwm_doc.cubic1.Base = qwm_doc.sketch_cubic1
    qwm_doc.cubic1.Dir = (0, 0, 10.0)
    qwm_doc.cubic1.Solid = True
    cubic1_viewObject = qwm_doc.cubic1.ViewObject
    cubic1_viewObject.Transparency = 60
    qwm_doc.cubic1.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.recompute()
