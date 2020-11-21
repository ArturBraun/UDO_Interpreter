
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_waveguid')
    qwm_doc.sketch_waveguid.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_waveguid.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,0.0,0), FreeCAD.Vector(30.0,0.0,0)))
    qwm_doc.sketch_waveguid.addGeometry(Part.LineSegment(FreeCAD.Vector(30.0,0.0,0), FreeCAD.Vector(30.0,10.0,0)))
    qwm_doc.sketch_waveguid.addGeometry(Part.LineSegment(FreeCAD.Vector(30.0,10.0,0), FreeCAD.Vector(0.0,10.0,0)))
    qwm_doc.sketch_waveguid.addGeometry(Part.LineSegment(FreeCAD.Vector(0.0,10.0,0), FreeCAD.Vector(0.0,0.0,0)))
    qwm_doc.addObject("Part::Extrusion", "waveguid")
    qwm_doc.waveguid.Base = qwm_doc.sketch_waveguid
    qwm_doc.waveguid.Dir = (0, 0, 5.0)
    qwm_doc.waveguid.Solid = True
    waveguid_viewObject = qwm_doc.waveguid.ViewObject
    waveguid_viewObject.Transparency = 60
    qwm_doc.waveguid.Medium = QW_Modeller.getQWMedium("air")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_antenna')
    qwm_doc.sketch_antenna.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,3.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(20.6,5.0,0), FreeCAD.Vector(20.580785280403234,5.195090322016128,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(20.580785280403234,5.195090322016128,0), FreeCAD.Vector(20.523879532511287,5.38268343236509,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(20.523879532511287,5.38268343236509,0), FreeCAD.Vector(20.431469612302546,5.555570233019602,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(20.431469612302546,5.555570233019602,0), FreeCAD.Vector(20.307106781186548,5.707106781186548,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(20.307106781186548,5.707106781186548,0), FreeCAD.Vector(20.155570233019603,5.831469612302545,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(20.155570233019603,5.831469612302545,0), FreeCAD.Vector(19.982683432365093,5.923879532511287,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.982683432365093,5.923879532511287,0), FreeCAD.Vector(19.79509032201613,5.98078528040323,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.79509032201613,5.98078528040323,0), FreeCAD.Vector(19.6,6.0,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.6,6.0,0), FreeCAD.Vector(19.404909677983873,5.98078528040323,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.404909677983873,5.98078528040323,0), FreeCAD.Vector(19.21731656763491,5.923879532511287,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.21731656763491,5.923879532511287,0), FreeCAD.Vector(19.0444297669804,5.831469612302545,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.0444297669804,5.831469612302545,0), FreeCAD.Vector(18.892893218813455,5.707106781186548,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(18.892893218813455,5.707106781186548,0), FreeCAD.Vector(18.768530387697457,5.555570233019602,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(18.768530387697457,5.555570233019602,0), FreeCAD.Vector(18.676120467488715,5.38268343236509,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(18.676120467488715,5.38268343236509,0), FreeCAD.Vector(18.61921471959677,5.195090322016128,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(18.61921471959677,5.195090322016128,0), FreeCAD.Vector(18.6,5.0,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(18.6,5.0,0), FreeCAD.Vector(18.61921471959677,4.804909677983872,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(18.61921471959677,4.804909677983872,0), FreeCAD.Vector(18.676120467488715,4.61731656763491,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(18.676120467488715,4.61731656763491,0), FreeCAD.Vector(18.768530387697457,4.444429766980398,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(18.768530387697457,4.444429766980398,0), FreeCAD.Vector(18.892893218813455,4.292893218813452,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(18.892893218813455,4.292893218813452,0), FreeCAD.Vector(19.0444297669804,4.168530387697455,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.0444297669804,4.168530387697455,0), FreeCAD.Vector(19.217316567634914,4.076120467488713,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.217316567634914,4.076120467488713,0), FreeCAD.Vector(19.404909677983873,4.01921471959677,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.404909677983873,4.01921471959677,0), FreeCAD.Vector(19.6,4.0,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.6,4.0,0), FreeCAD.Vector(19.79509032201613,4.01921471959677,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.79509032201613,4.01921471959677,0), FreeCAD.Vector(19.982683432365093,4.076120467488713,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(19.982683432365093,4.076120467488713,0), FreeCAD.Vector(20.155570233019603,4.168530387697454,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(20.155570233019603,4.168530387697454,0), FreeCAD.Vector(20.307106781186548,4.292893218813452,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(20.307106781186548,4.292893218813452,0), FreeCAD.Vector(20.431469612302546,4.444429766980398,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(20.431469612302546,4.444429766980398,0), FreeCAD.Vector(20.523879532511287,4.61731656763491,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(20.523879532511287,4.61731656763491,0), FreeCAD.Vector(20.58078528040323,4.804909677983871,0)))
    qwm_doc.sketch_antenna.addGeometry(Part.LineSegment(FreeCAD.Vector(20.58078528040323,4.804909677983871,0), FreeCAD.Vector(20.6,5.0,0)))
    qwm_doc.addObject("Part::Extrusion", "antenna")
    qwm_doc.antenna.Base = qwm_doc.sketch_antenna
    qwm_doc.antenna.Dir = (0, 0, 11.0)
    qwm_doc.antenna.Solid = True
    antenna_viewObject = qwm_doc.antenna.ViewObject
    antenna_viewObject.Transparency = 60
    qwm_doc.antenna.Medium = QW_Modeller.getQWMedium("metal")
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_coaxair')
    qwm_doc.sketch_coaxair.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,5.0),FreeCAD.Rotation(0.0, 0.0, 0.0, 1.0))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(22.1,5.0,0), FreeCAD.Vector(22.05196320100808,5.487725805040321,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(22.05196320100808,5.487725805040321,0), FreeCAD.Vector(21.90969883127822,5.956708580912725,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(21.90969883127822,5.956708580912725,0), FreeCAD.Vector(21.678674030756365,6.388925582549005,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(21.678674030756365,6.388925582549005,0), FreeCAD.Vector(21.36776695296637,6.767766952966369,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(21.36776695296637,6.767766952966369,0), FreeCAD.Vector(20.988925582549008,7.078674030756363,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(20.988925582549008,7.078674030756363,0), FreeCAD.Vector(20.556708580912726,7.309698831278217,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(20.556708580912726,7.309698831278217,0), FreeCAD.Vector(20.08772580504032,7.451963201008076,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(20.08772580504032,7.451963201008076,0), FreeCAD.Vector(19.6,7.5,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(19.6,7.5,0), FreeCAD.Vector(19.11227419495968,7.451963201008076,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(19.11227419495968,7.451963201008076,0), FreeCAD.Vector(18.643291419087276,7.309698831278217,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(18.643291419087276,7.309698831278217,0), FreeCAD.Vector(18.211074417450995,7.078674030756362,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(18.211074417450995,7.078674030756362,0), FreeCAD.Vector(17.832233047033633,6.767766952966369,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(17.832233047033633,6.767766952966369,0), FreeCAD.Vector(17.521325969243637,6.388925582549005,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(17.521325969243637,6.388925582549005,0), FreeCAD.Vector(17.290301168721783,5.956708580912725,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(17.290301168721783,5.956708580912725,0), FreeCAD.Vector(17.148036798991924,5.487725805040321,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(17.148036798991924,5.487725805040321,0), FreeCAD.Vector(17.1,5.0,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(17.1,5.0,0), FreeCAD.Vector(17.148036798991924,4.512274194959679,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(17.148036798991924,4.512274194959679,0), FreeCAD.Vector(17.290301168721783,4.043291419087276,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(17.290301168721783,4.043291419087276,0), FreeCAD.Vector(17.521325969243637,3.611074417450994,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(17.521325969243637,3.611074417450994,0), FreeCAD.Vector(17.832233047033633,3.232233047033631,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(17.832233047033633,3.232233047033631,0), FreeCAD.Vector(18.211074417450995,2.921325969243637,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(18.211074417450995,2.921325969243637,0), FreeCAD.Vector(18.643291419087276,2.690301168721783,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(18.643291419087276,2.690301168721783,0), FreeCAD.Vector(19.11227419495968,2.5480367989919244,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(19.11227419495968,2.5480367989919244,0), FreeCAD.Vector(19.6,2.5,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(19.6,2.5,0), FreeCAD.Vector(20.08772580504032,2.548036798991924,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(20.08772580504032,2.548036798991924,0), FreeCAD.Vector(20.556708580912726,2.6903011687217835,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(20.556708580912726,2.6903011687217835,0), FreeCAD.Vector(20.988925582549005,2.9213259692436364,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(20.988925582549005,2.9213259692436364,0), FreeCAD.Vector(21.36776695296637,3.2322330470336307,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(21.36776695296637,3.2322330470336307,0), FreeCAD.Vector(21.678674030756365,3.6110744174509946,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(21.678674030756365,3.6110744174509946,0), FreeCAD.Vector(21.90969883127822,4.043291419087276,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(21.90969883127822,4.043291419087276,0), FreeCAD.Vector(22.05196320100808,4.512274194959678,0)))
    qwm_doc.sketch_coaxair.addGeometry(Part.LineSegment(FreeCAD.Vector(22.05196320100808,4.512274194959678,0), FreeCAD.Vector(22.1,5.0,0)))
    qwm_doc.addObject("Part::Extrusion", "coaxair")
    qwm_doc.coaxair.Base = qwm_doc.sketch_coaxair
    qwm_doc.coaxair.Dir = (0, 0, 9.0)
    qwm_doc.coaxair.Solid = True
    coaxair_viewObject = qwm_doc.coaxair.ViewObject
    coaxair_viewObject.Transparency = 60
    qwm_doc.coaxair.Medium = QW_Modeller.getQWMedium("air")
