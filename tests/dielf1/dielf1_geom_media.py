
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_wg')
    qwm_doc.sketch_wg.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,0.0,0), FreeCAD.Vector(0.0,-10.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,-10.0,0), FreeCAD.Vector(20.0,-10.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(20.0,-10.0,0), FreeCAD.Vector(20.0,-6.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(20.0,-6.0,0), FreeCAD.Vector(40.0,-6.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(40.0,-6.0,0), FreeCAD.Vector(40.0,-10.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(40.0,-10.0,0), FreeCAD.Vector(60.0,-10.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(60.0,-10.0,0), FreeCAD.Vector(60.0,10.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(60.0,10.0,0), FreeCAD.Vector(40.0,10.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(40.0,10.0,0), FreeCAD.Vector(40.0,6.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(40.0,6.0,0), FreeCAD.Vector(20.0,6.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(20.0,6.0,0), FreeCAD.Vector(20.0,10.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(20.0,10.0,0), FreeCAD.Vector(0.0,10.0,0)))
    qwm_doc.sketch_wg.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,10.0,0), FreeCAD.Vector(0.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "wg")
    qwm_doc.wg.Base = qwm_doc.sketch_wg
    qwm_doc.wg.Dir = (0, 0, 10.0)
    qwm_doc.wg.Solid = True
    wg_viewObject = qwm_doc.wg.ViewObject
    wg_viewObject.Transparency = 60
    qwm_doc.wg.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_res')
    qwm_doc.sketch_res.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(35.0,0.0,0), FreeCAD.Vector(34.89073800366903,1.0395584540887968,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(34.89073800366903,1.0395584540887968,0), FreeCAD.Vector(34.56772728821301,2.033683215379001,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(34.56772728821301,2.033683215379001,0), FreeCAD.Vector(34.045084971874736,2.938926261462366,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(34.045084971874736,2.938926261462366,0), FreeCAD.Vector(33.34565303179429,3.715724127386971,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(33.34565303179429,3.715724127386971,0), FreeCAD.Vector(32.5,4.330127018922193,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(32.5,4.330127018922193,0), FreeCAD.Vector(31.545084971874736,4.755282581475767,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(31.545084971874736,4.755282581475767,0), FreeCAD.Vector(30.522642316338267,4.972609476841367,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(30.522642316338267,4.972609476841367,0), FreeCAD.Vector(29.477357683661733,4.972609476841367,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(29.477357683661733,4.972609476841367,0), FreeCAD.Vector(28.454915028125264,4.755282581475768,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(28.454915028125264,4.755282581475768,0), FreeCAD.Vector(27.5,4.330127018922194,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(27.5,4.330127018922194,0), FreeCAD.Vector(26.654346968205708,3.715724127386971,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(26.654346968205708,3.715724127386971,0), FreeCAD.Vector(25.954915028125264,2.9389262614623664,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(25.954915028125264,2.9389262614623664,0), FreeCAD.Vector(25.432272711786997,2.033683215379002,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(25.432272711786997,2.033683215379002,0), FreeCAD.Vector(25.10926199633097,1.0395584540887965,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(25.10926199633097,1.0395584540887965,0), FreeCAD.Vector(25.0,6.123233995736766e-16,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(25.0,6.123233995736766e-16,0), FreeCAD.Vector(25.10926199633097,-1.0395584540887977,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(25.10926199633097,-1.0395584540887977,0), FreeCAD.Vector(25.432272711786997,-2.033683215379001,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(25.432272711786997,-2.033683215379001,0), FreeCAD.Vector(25.954915028125264,-2.938926261462365,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(25.954915028125264,-2.938926261462365,0), FreeCAD.Vector(26.654346968205708,-3.715724127386972,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(26.654346968205708,-3.715724127386972,0), FreeCAD.Vector(27.499999999999996,-4.330127018922193,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(27.499999999999996,-4.330127018922193,0), FreeCAD.Vector(28.454915028125264,-4.755282581475767,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(28.454915028125264,-4.755282581475767,0), FreeCAD.Vector(29.477357683661733,-4.972609476841367,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(29.477357683661733,-4.972609476841367,0), FreeCAD.Vector(30.522642316338263,-4.972609476841367,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(30.522642316338263,-4.972609476841367,0), FreeCAD.Vector(31.545084971874736,-4.755282581475768,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(31.545084971874736,-4.755282581475768,0), FreeCAD.Vector(32.5,-4.330127018922193,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(32.5,-4.330127018922193,0), FreeCAD.Vector(33.34565303179429,-3.7157241273869728,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(33.34565303179429,-3.7157241273869728,0), FreeCAD.Vector(34.045084971874736,-2.938926261462367,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(34.045084971874736,-2.938926261462367,0), FreeCAD.Vector(34.56772728821301,-2.0336832153790008,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(34.56772728821301,-2.0336832153790008,0), FreeCAD.Vector(34.89073800366903,-1.0395584540887994,0)))
    qwm_doc.sketch_res.addGeometry(Part.LineSegment(FreeCAD.Vector(34.89073800366903,-1.0395584540887994,0), FreeCAD.Vector(35.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "res")
    qwm_doc.res.Base = qwm_doc.sketch_res
    qwm_doc.res.Dir = (0, 0, 2.0)
    qwm_doc.res.Solid = True
    res_viewObject = qwm_doc.res.ViewObject
    res_viewObject.Transparency = 60
    qwm_doc.res.Medium = QW_Modeller.getQWMedium("metal")
