
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_vtape')
    qwm_doc.sketch_vtape.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.5,0.0,0.0,0.0))
    qwm_doc.sketch_vtape.addGeometry(Part.LineSegment(FreeCAD.Vector(-6.0,-3.0,0), FreeCAD.Vector(6.0,-3.0,0)))
    qwm_doc.sketch_vtape.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,-3.0,0), FreeCAD.Vector(6.0,3.0,0)))
    qwm_doc.sketch_vtape.addGeometry(Part.LineSegment(FreeCAD.Vector(6.0,3.0,0), FreeCAD.Vector(-6.0,3.0,0)))
    qwm_doc.sketch_vtape.addGeometry(Part.LineSegment(FreeCAD.Vector(-6.0,3.0,0), FreeCAD.Vector(-6.0,-3.0,0)))
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_vtape1')
    qwm_doc.sketch_vtape1.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,30.0),FreeCAD.Rotation(0.5,0.0,0.0,0.0))
    qwm_doc.sketch_vtape1.addGeometry(Part.LineSegment(FreeCAD.Vector(-4.0,-1.5,0), FreeCAD.Vector(4.0,-1.5,0)))
    qwm_doc.sketch_vtape1.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,-1.5,0), FreeCAD.Vector(4.0,1.5,0)))
    qwm_doc.sketch_vtape1.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,1.5,0), FreeCAD.Vector(-4.0,1.5,0)))
    qwm_doc.sketch_vtape1.addGeometry(Part.LineSegment(FreeCAD.Vector(-4.0,1.5,0), FreeCAD.Vector(-4.0,-1.5,0)))
    qwm_doc.addObject("Part::Loft", "vtape1")
    qwm_doc.vtape1.Sections=[qwm_doc.sketch_vtape, qwm_doc.sketch_vtape1]
    qwm_doc.vtape1.Solid=True
    qwm_doc.vtape1.Ruled=False
    qwm_doc.vtape1.Closed=False
    vtape1_viewObject = qwm_doc.vtape1.ViewObject
    vtape1_viewObject.Transparency = 60
    qwm_doc.vtape1.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.recompute()
