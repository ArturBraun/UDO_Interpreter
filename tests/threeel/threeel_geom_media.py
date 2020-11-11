
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_cubic1')
    qwm_doc.sketch_cubic1.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_cubic1.addGeometry(Part.LineSegment(FreeCAD.Vector(-3.0,-2.5,0), FreeCAD.Vector(3.0,-2.5,0)))
    qwm_doc.sketch_cubic1.addGeometry(Part.LineSegment(FreeCAD.Vector(3.0,-2.5,0), FreeCAD.Vector(3.0,2.5,0)))
    qwm_doc.sketch_cubic1.addGeometry(Part.LineSegment(FreeCAD.Vector(3.0,2.5,0), FreeCAD.Vector(-3.0,2.5,0)))
    qwm_doc.sketch_cubic1.addGeometry(Part.LineSegment(FreeCAD.Vector(-3.0,2.5,0), FreeCAD.Vector(-3.0,-2.5,0)))
    qwm_doc.addObject("Part::Extrusion", "cubic1")
    qwm_doc.cubic1.Base = qwm_doc.sketch_cubic1
    qwm_doc.cubic1.Dir = (0, 0, 5.0)
    qwm_doc.cubic1.Solid = True
    cubic1_viewObject = qwm_doc.cubic1.ViewObject
    cubic1_viewObject.Transparency = 60
    qwm_doc.cubic1.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_prismb')
    qwm_doc.sketch_prismb.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,5.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_prismb.addGeometry(Part.LineSegment(FreeCAD.Vector(-3.0,-2.5,0), FreeCAD.Vector(3.0,-2.5,0)))
    qwm_doc.sketch_prismb.addGeometry(Part.LineSegment(FreeCAD.Vector(3.0,-2.5,0), FreeCAD.Vector(3.0,2.5,0)))
    qwm_doc.sketch_prismb.addGeometry(Part.LineSegment(FreeCAD.Vector(3.0,2.5,0), FreeCAD.Vector(-3.0,2.5,0)))
    qwm_doc.sketch_prismb.addGeometry(Part.LineSegment(FreeCAD.Vector(-3.0,2.5,0), FreeCAD.Vector(-3.0,-2.5,0)))
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_prismt')
    qwm_doc.sketch_prismt.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,12.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_prismt.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.5,-1.25,0), FreeCAD.Vector(1.5,-1.25,0)))
    qwm_doc.sketch_prismt.addGeometry(Part.LineSegment(FreeCAD.Vector(1.5,-1.25,0), FreeCAD.Vector(1.5,1.25,0)))
    qwm_doc.sketch_prismt.addGeometry(Part.LineSegment(FreeCAD.Vector(1.5,1.25,0), FreeCAD.Vector(-1.5,1.25,0)))
    qwm_doc.sketch_prismt.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.5,1.25,0), FreeCAD.Vector(-1.5,-1.25,0)))
    qwm_doc.addObject("Part::Loft", "prismt")
    qwm_doc.prismt.Sections=[qwm_doc.sketch_prismb, qwm_doc.sketch_prismt]
    qwm_doc.prismt.Solid=True
    qwm_doc.prismt.Ruled=False
    qwm_doc.prismt.Closed=False
    prismt_viewObject = qwm_doc.prismt.ViewObject
    prismt_viewObject.Transparency = 60
    qwm_doc.prismt.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_cubic3')
    qwm_doc.sketch_cubic3.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,12.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_cubic3.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.5,-1.25,0), FreeCAD.Vector(1.5,-1.25,0)))
    qwm_doc.sketch_cubic3.addGeometry(Part.LineSegment(FreeCAD.Vector(1.5,-1.25,0), FreeCAD.Vector(1.5,1.25,0)))
    qwm_doc.sketch_cubic3.addGeometry(Part.LineSegment(FreeCAD.Vector(1.5,1.25,0), FreeCAD.Vector(-1.5,1.25,0)))
    qwm_doc.sketch_cubic3.addGeometry(Part.LineSegment(FreeCAD.Vector(-1.5,1.25,0), FreeCAD.Vector(-1.5,-1.25,0)))
    qwm_doc.addObject("Part::Extrusion", "cubic3")
    qwm_doc.cubic3.Base = qwm_doc.sketch_cubic3
    qwm_doc.cubic3.Dir = (0, 0, 3.0)
    qwm_doc.cubic3.Solid = True
    cubic3_viewObject = qwm_doc.cubic3.ViewObject
    cubic3_viewObject.Transparency = 60
    qwm_doc.cubic3.Medium = QW_Modeller.getQWMedium("air")
