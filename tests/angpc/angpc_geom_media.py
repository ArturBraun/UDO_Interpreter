
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
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_angpc')
    qwm_doc.sketch_angpc.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,0.0),FreeCAD.Rotation(0.5,0.0,0.0,0.0))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0,0.0,0), FreeCAD.Vector(4.0,0.0,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(4.0,0.0,0), FreeCAD.Vector(3.939231012048832,0.6945927106677213,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(3.939231012048832,0.6945927106677213,0), FreeCAD.Vector(3.7587704831436337,1.3680805733026749,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(3.7587704831436337,1.3680805733026749,0), FreeCAD.Vector(3.464101615137755,1.9999999999999998,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(3.464101615137755,1.9999999999999998,0), FreeCAD.Vector(3.064177772475912,2.571150438746157,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(3.064177772475912,2.571150438746157,0), FreeCAD.Vector(2.5711504387461575,3.064177772475912,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(2.5711504387461575,3.064177772475912,0), FreeCAD.Vector(2.0000000000000004,3.4641016151377544,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(2.0000000000000004,3.4641016151377544,0), FreeCAD.Vector(1.3680805733026753,3.7587704831436333,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(1.3680805733026753,3.7587704831436333,0), FreeCAD.Vector(0.6945927106677217,3.939231012048832,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(0.6945927106677217,3.939231012048832,0), FreeCAD.Vector(2.4492935982947064e-16,4.0,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(2.4492935982947064e-16,4.0,0), FreeCAD.Vector(1.2246467991473532e-16,2.0,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(1.2246467991473532e-16,2.0,0), FreeCAD.Vector(0.34729635533386083,1.969615506024416,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(0.34729635533386083,1.969615506024416,0), FreeCAD.Vector(0.6840402866513376,1.8793852415718166,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(0.6840402866513376,1.8793852415718166,0), FreeCAD.Vector(1.0000000000000002,1.7320508075688772,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(1.0000000000000002,1.7320508075688772,0), FreeCAD.Vector(1.2855752193730787,1.532088886237956,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(1.2855752193730787,1.532088886237956,0), FreeCAD.Vector(1.532088886237956,1.2855752193730785,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(1.532088886237956,1.2855752193730785,0), FreeCAD.Vector(1.7320508075688774,0.9999999999999999,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(1.7320508075688774,0.9999999999999999,0), FreeCAD.Vector(1.8793852415718169,0.6840402866513374,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(1.8793852415718169,0.6840402866513374,0), FreeCAD.Vector(1.969615506024416,0.34729635533386066,0)))
    qwm_doc.sketch_angpc.addGeometry(Part.LineSegment(FreeCAD.Vector(1.969615506024416,0.34729635533386066,0), FreeCAD.Vector(2.0,0.0,0)))
    qwm_doc.addObject('Sketcher::SketchObject', 'sketch_angpc1')
    qwm_doc.sketch_angpc1.Placement = FreeCAD.Placement(FreeCAD.Vector(0.0,0.0,4.0),FreeCAD.Rotation(0.5,0.0,0.0,0.0))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(3.0,0.0,0), FreeCAD.Vector(5.0,0.0,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(5.0,0.0,0), FreeCAD.Vector(4.92403876506104,0.8682408883346516,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(4.92403876506104,0.8682408883346516,0), FreeCAD.Vector(4.698463103929543,1.7101007166283435,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(4.698463103929543,1.7101007166283435,0), FreeCAD.Vector(4.330127018922194,2.4999999999999996,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(4.330127018922194,2.4999999999999996,0), FreeCAD.Vector(3.83022221559489,3.2139380484326963,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(3.83022221559489,3.2139380484326963,0), FreeCAD.Vector(3.2139380484326967,3.83022221559489,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(3.2139380484326967,3.83022221559489,0), FreeCAD.Vector(2.5000000000000004,4.330127018922193,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(2.5000000000000004,4.330127018922193,0), FreeCAD.Vector(1.7101007166283442,4.698463103929542,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(1.7101007166283442,4.698463103929542,0), FreeCAD.Vector(0.8682408883346521,4.92403876506104,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(0.8682408883346521,4.92403876506104,0), FreeCAD.Vector(3.061616997868383e-16,5.0,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(3.061616997868383e-16,5.0,0), FreeCAD.Vector(1.8369701987210297e-16,3.0,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(1.8369701987210297e-16,3.0,0), FreeCAD.Vector(0.5209445330007912,2.954423259036624,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(0.5209445330007912,2.954423259036624,0), FreeCAD.Vector(1.0260604299770064,2.819077862357725,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(1.0260604299770064,2.819077862357725,0), FreeCAD.Vector(1.5000000000000004,2.598076211353316,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(1.5000000000000004,2.598076211353316,0), FreeCAD.Vector(1.9283628290596182,2.298133329356934,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(1.9283628290596182,2.298133329356934,0), FreeCAD.Vector(2.298133329356934,1.9283628290596178,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(2.298133329356934,1.9283628290596178,0), FreeCAD.Vector(2.598076211353316,1.4999999999999998,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(2.598076211353316,1.4999999999999998,0), FreeCAD.Vector(2.8190778623577253,1.0260604299770062,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(2.8190778623577253,1.0260604299770062,0), FreeCAD.Vector(2.954423259036624,0.520944533000791,0)))
    qwm_doc.sketch_angpc1.addGeometry(Part.LineSegment(FreeCAD.Vector(2.954423259036624,0.520944533000791,0), FreeCAD.Vector(3.0,0.0,0)))
    qwm_doc.addObject("Part::Loft", "angpc1")
    qwm_doc.angpc1.Sections=[qwm_doc.sketch_angpc, qwm_doc.sketch_angpc1]
    qwm_doc.angpc1.Solid=True
    qwm_doc.angpc1.Ruled=False
    qwm_doc.angpc1.Closed=False
    angpc1_viewObject = qwm_doc.angpc1.ViewObject
    angpc1_viewObject.Transparency = 60
    qwm_doc.angpc1.Medium = QW_Modeller.getQWMedium("metal")
    qwm_doc.recompute()
    