
import FreeCADGui,QW_Modeller,FreeCAD
#from qw_project import *
from qw_units import *

def set_Mesh(qwm_doc):
    MeshBox1 = QW_Modeller.addQWObject("QW_Modeller::MeshBox","MeshBox1")
    MeshBox1.Length = 90.0
    MeshBox1.Width = 51.43
    MeshBox1.Height = 45.08
    MeshBox1.Placement = FreeCAD.Placement(FreeCAD.Vector(50.0,-14.285,17.46),FreeCAD.Rotation(0.0000000,0.0000000,0.0000000,1.0000000))
    MeshBox1.MeshX = True
    MeshBox1.MeshY = True
    MeshBox1.MeshZ = True
    MeshBox1.MeshXCellSize = 1.0
    MeshBox1.MeshYCellSize = 1.0
    MeshBox1.MeshZCellSize = 1.0
    MeshBox1.SnapToXMinus = False
    MeshBox1.SnapToXPlus = False
    MeshBox1.SnapToYMinus = False
    MeshBox1.SnapToYPlus = False
    MeshBox1.SnapToZMinus = False
    MeshBox1.SnapToZPlus = False
