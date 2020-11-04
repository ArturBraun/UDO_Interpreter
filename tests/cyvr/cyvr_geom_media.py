
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_cyvr')
    qwm_doc.sketch_cyvr.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,0.0,0), FreeCAD.Vector(1.8477590650225735,0.7653668647301796,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(1.8477590650225735,0.7653668647301796,0), FreeCAD.Vector(1.4142135623730951,1.4142135623730951,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(1.4142135623730951,1.4142135623730951,0), FreeCAD.Vector(0.7653668647301797,1.8477590650225735,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(0.7653668647301797,1.8477590650225735,0), FreeCAD.Vector(1.2246467991473532e-16,2.0,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(1.2246467991473532e-16,2.0,0), FreeCAD.Vector(-0.7653668647301795,1.8477590650225735,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(-0.7653668647301795,1.8477590650225735,0), FreeCAD.Vector(-1.414213562373095,1.4142135623730951,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.414213562373095,1.4142135623730951,0), FreeCAD.Vector(-1.8477590650225735,0.7653668647301798,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.8477590650225735,0.7653668647301798,0), FreeCAD.Vector(-2.0,2.4492935982947064e-16,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(-2.0,2.4492935982947064e-16,0), FreeCAD.Vector(-1.8477590650225737,-0.7653668647301793,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.8477590650225737,-0.7653668647301793,0), FreeCAD.Vector(-1.4142135623730954,-1.414213562373095,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.4142135623730954,-1.414213562373095,0), FreeCAD.Vector(-0.765366864730179,-1.8477590650225737,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(-0.765366864730179,-1.8477590650225737,0), FreeCAD.Vector(-3.6739403974420594e-16,-2.0,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(-3.6739403974420594e-16,-2.0,0), FreeCAD.Vector(0.76536686473018,-1.8477590650225733,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(0.76536686473018,-1.8477590650225733,0), FreeCAD.Vector(1.4142135623730947,-1.4142135623730954,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(1.4142135623730947,-1.4142135623730954,0), FreeCAD.Vector(1.8477590650225737,-0.7653668647301791,0)))
    qwm_doc.sketch_cyvr.addGeometry(Part.LineSegment(FreeCAD.Vector(1.8477590650225737,-0.7653668647301791,0), FreeCAD.Vector(2.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "cyvr")
    qwm_doc.cyvr.Base = qwm_doc.sketch_cyvr
    qwm_doc.cyvr.Dir = (0, 0, 4.0)
    qwm_doc.cyvr.Solid = True
    cyvr_viewObject = qwm_doc.cyvr.ViewObject
    cyvr_viewObject.Transparency = 60
    qwm_doc.cyvr.Medium = QW_Modeller.getQWMedium("air")
