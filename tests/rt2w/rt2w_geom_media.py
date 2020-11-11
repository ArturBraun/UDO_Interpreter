
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_rt2wone')
    qwm_doc.sketch_rt2wone.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,-2.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_rt2wone.addGeometry(Part.LineSegment(FreeCAD.Vector(-10.0,-3.0,0), FreeCAD.Vector(10.0,-3.0,0)))
    qwm_doc.sketch_rt2wone.addGeometry(Part.LineSegment(FreeCAD.Vector(10.0,-3.0,0), FreeCAD.Vector(10.0,3.0,0)))
    qwm_doc.sketch_rt2wone.addGeometry(Part.LineSegment(FreeCAD.Vector(10.0,3.0,0), FreeCAD.Vector(-10.0,3.0,0)))
    qwm_doc.sketch_rt2wone.addGeometry(Part.LineSegment(FreeCAD.Vector(-10.0,3.0,0), FreeCAD.Vector(-10.0,-3.0,0)))
    qwm_doc.addObject("Part::Extrusion", "rt2wone")
    qwm_doc.rt2wone.Base = qwm_doc.sketch_rt2wone
    qwm_doc.rt2wone.Dir = (0, 0, 4.0)
    qwm_doc.rt2wone.Solid = True
    rt2wone_viewObject = qwm_doc.rt2wone.ViewObject
    rt2wone_viewObject.Transparency = 60
    qwm_doc.rt2wone.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_rt2wsec')
    qwm_doc.sketch_rt2wsec.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,-1.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_rt2wsec.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,-2.0,0), FreeCAD.Vector(10.0,-2.0,0)))
    qwm_doc.sketch_rt2wsec.addGeometry(Part.LineSegment(FreeCAD.Vector(10.0,-2.0,0), FreeCAD.Vector(10.0,2.0,0)))
    qwm_doc.sketch_rt2wsec.addGeometry(Part.LineSegment(FreeCAD.Vector(10.0,2.0,0), FreeCAD.Vector(0.0,2.0,0)))
    qwm_doc.sketch_rt2wsec.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,2.0,0), FreeCAD.Vector(0.0,-2.0,0)))
    qwm_doc.addObject("Part::Extrusion", "rt2wsec")
    qwm_doc.rt2wsec.Base = qwm_doc.sketch_rt2wsec
    qwm_doc.rt2wsec.Dir = (0, 0, 3.0)
    qwm_doc.rt2wsec.Solid = True
    rt2wsec_viewObject = qwm_doc.rt2wsec.ViewObject
    rt2wsec_viewObject.Transparency = 60
    qwm_doc.rt2wsec.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.rt2wsec.Placement=FreeCAD.Placement(FreeCAD.Vector(0,0,0), FreeCAD.Rotation(FreeCAD.Vector(0,0,1),90.0), FreeCAD.Vector(0.0,0.0,0))
    qwm_doc.addObject("Part::MultiFuse","Fusion1")
    qwm_doc.Fusion1.Shapes = [qwm_doc.rt2wsec,qwm_doc.rt2wone,]
    qwm_doc.Fusion1.Medium = qwm_doc.rt2wsec.Medium
    FreeCAD.Gui.activeDocument().rt2wsec.Visibility = False
    FreeCAD.Gui.activeDocument().rt2wone.Visibility = False
    qwm_doc.Fusion1.Label = 'rt2w'
