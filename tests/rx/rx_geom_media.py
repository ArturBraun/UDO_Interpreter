
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_rxone')
    qwm_doc.sketch_rxone.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,-2.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_rxone.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,-13.0,0), FreeCAD.Vector(20.0,-13.0,0)))
    qwm_doc.sketch_rxone.addGeometry(Part.LineSegment(FreeCAD.Vector(20.0,-13.0,0), FreeCAD.Vector(20.0,-7.0,0)))
    qwm_doc.sketch_rxone.addGeometry(Part.LineSegment(FreeCAD.Vector(20.0,-7.0,0), FreeCAD.Vector(0.0,-7.0,0)))
    qwm_doc.sketch_rxone.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,-7.0,0), FreeCAD.Vector(0.0,-13.0,0)))
    qwm_doc.addObject("Part::Extrusion", "rxone")
    qwm_doc.rxone.Base = qwm_doc.sketch_rxone
    qwm_doc.rxone.Dir = (0, 0, 5.0)
    qwm_doc.rxone.Solid = True
    rxone_viewObject = qwm_doc.rxone.ViewObject
    rxone_viewObject.Transparency = 60
    qwm_doc.rxone.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.rxone.Placement=FreeCAD.Placement(FreeCAD.Vector(0,0,0), FreeCAD.Rotation(FreeCAD.Vector(0,0,1),90.0), FreeCAD.Vector(0.0,-10.0,0))
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_rxsec')
    qwm_doc.sketch_rxsec.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,-2.5),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_rxsec.addGeometry(Part.LineSegment(FreeCAD.Vector(-10.0,-3.0,0), FreeCAD.Vector(10.0,-3.0,0)))
    qwm_doc.sketch_rxsec.addGeometry(Part.LineSegment(FreeCAD.Vector(10.0,-3.0,0), FreeCAD.Vector(10.0,3.0,0)))
    qwm_doc.sketch_rxsec.addGeometry(Part.LineSegment(FreeCAD.Vector(10.0,3.0,0), FreeCAD.Vector(-10.0,3.0,0)))
    qwm_doc.sketch_rxsec.addGeometry(Part.LineSegment(FreeCAD.Vector(-10.0,3.0,0), FreeCAD.Vector(-10.0,-3.0,0)))
    qwm_doc.addObject("Part::Extrusion", "rxsec")
    qwm_doc.rxsec.Base = qwm_doc.sketch_rxsec
    qwm_doc.rxsec.Dir = (0, 0, 5.0)
    qwm_doc.rxsec.Solid = True
    rxsec_viewObject = qwm_doc.rxsec.ViewObject
    rxsec_viewObject.Transparency = 60
    qwm_doc.rxsec.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject("Part::MultiFuse","Fusion1")
    qwm_doc.Fusion1.Shapes = [qwm_doc.rxsec,qwm_doc.rxone,]
    qwm_doc.Fusion1.Medium = qwm_doc.rxsec.Medium
    FreeCAD.Gui.activeDocument().rxsec.Visibility = False
    FreeCAD.Gui.activeDocument().rxone.Visibility = False
    qwm_doc.Fusion1.Label = 'rxall'
