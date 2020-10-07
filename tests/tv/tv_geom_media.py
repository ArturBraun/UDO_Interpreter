
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_tv')
    qwm_doc.sketch_tv.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.5,0.0,0.0,0.0))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,0.0,0), FreeCAD.Vector(3.695518130045147,1.5307337294603591,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(3.695518130045147,1.5307337294603591,0), FreeCAD.Vector(2.8284271247461903,2.8284271247461903,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(2.8284271247461903,2.8284271247461903,0), FreeCAD.Vector(1.5307337294603593,3.695518130045147,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(1.5307337294603593,3.695518130045147,0), FreeCAD.Vector(2.4492935982947064e-16,4.0,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(2.4492935982947064e-16,4.0,0), FreeCAD.Vector(-1.530733729460359,3.695518130045147,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.530733729460359,3.695518130045147,0), FreeCAD.Vector(-2.82842712474619,2.8284271247461903,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(-2.82842712474619,2.8284271247461903,0), FreeCAD.Vector(-3.695518130045147,1.5307337294603596,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(-3.695518130045147,1.5307337294603596,0), FreeCAD.Vector(-4.0,4.898587196589413e-16,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(-4.0,4.898587196589413e-16,0), FreeCAD.Vector(-3.6955181300451474,-1.5307337294603587,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(-3.6955181300451474,-1.5307337294603587,0), FreeCAD.Vector(-2.8284271247461907,-2.82842712474619,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(-2.8284271247461907,-2.82842712474619,0), FreeCAD.Vector(-1.530733729460358,-3.6955181300451474,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.530733729460358,-3.6955181300451474,0), FreeCAD.Vector(-7.347880794884119e-16,-4.0,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(-7.347880794884119e-16,-4.0,0), FreeCAD.Vector(1.53073372946036,-3.6955181300451465,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(1.53073372946036,-3.6955181300451465,0), FreeCAD.Vector(2.8284271247461894,-2.8284271247461907,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(2.8284271247461894,-2.8284271247461907,0), FreeCAD.Vector(3.6955181300451474,-1.5307337294603582,0)))
    qwm_doc.sketch_tv.addGeometry(Part.LineSegment(FreeCAD.Vector(3.6955181300451474,-1.5307337294603582,0), FreeCAD.Vector(4.0,0.0,0)))
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_tv1')
    qwm_doc.sketch_tv1.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.5,0.0,0.0,0.0))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,0.0,0), FreeCAD.Vector(1.8477590650225735,0.7653668647301796,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(1.8477590650225735,0.7653668647301796,0), FreeCAD.Vector(1.4142135623730951,1.4142135623730951,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(1.4142135623730951,1.4142135623730951,0), FreeCAD.Vector(0.7653668647301797,1.8477590650225735,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(0.7653668647301797,1.8477590650225735,0), FreeCAD.Vector(1.2246467991473532e-16,2.0,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(1.2246467991473532e-16,2.0,0), FreeCAD.Vector(-0.7653668647301795,1.8477590650225735,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(-0.7653668647301795,1.8477590650225735,0), FreeCAD.Vector(-1.414213562373095,1.4142135623730951,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.414213562373095,1.4142135623730951,0), FreeCAD.Vector(-1.8477590650225735,0.7653668647301798,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.8477590650225735,0.7653668647301798,0), FreeCAD.Vector(-2.0,2.4492935982947064e-16,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(-2.0,2.4492935982947064e-16,0), FreeCAD.Vector(-1.8477590650225737,-0.7653668647301793,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.8477590650225737,-0.7653668647301793,0), FreeCAD.Vector(-1.4142135623730954,-1.414213562373095,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.4142135623730954,-1.414213562373095,0), FreeCAD.Vector(-0.765366864730179,-1.8477590650225737,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(-0.765366864730179,-1.8477590650225737,0), FreeCAD.Vector(-3.6739403974420594e-16,-2.0,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(-3.6739403974420594e-16,-2.0,0), FreeCAD.Vector(0.76536686473018,-1.8477590650225733,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(0.76536686473018,-1.8477590650225733,0), FreeCAD.Vector(1.4142135623730947,-1.4142135623730954,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(1.4142135623730947,-1.4142135623730954,0), FreeCAD.Vector(1.8477590650225737,-0.7653668647301791,0)))
    qwm_doc.sketch_tv1.addGeometry(Part.LineSegment(FreeCAD.Vector(1.8477590650225737,-0.7653668647301791,0), FreeCAD.Vector(2.0,0.0,0)))
    qwm_doc.addObject("Part::Loft", "tv1")
    qwm_doc.tv1.Sections=[qwm_doc.sketch_tv, qwm_doc.sketch_tv1]
    qwm_doc.tv1.Solid=True
    qwm_doc.tv1.Ruled=False
    qwm_doc.tv1.Closed=False
    tv1_viewObject = qwm_doc.tv1.ViewObject
    tv1_viewObject.Transparency = 60
    qwm_doc.tv1.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.recompute()
    