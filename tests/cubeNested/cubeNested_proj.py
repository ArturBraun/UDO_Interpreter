
import QW_Modeller, FreeCADGui
from cubeNested_circuit import *
from cubeNested_geom_media import *
from cubeNested_mesh import *
from cubeNested_excit import *
from cubeNested_ppost import *
from cubeNested_setsimul import *
from cubeNested_runsimul import *

class cubeNested_Project(QW_Project): # test
    def __init__(self, qwm_doc):
        self.qwm_doc = qwm_doc
        qwm_doc.Company = 'QWED SP. z o.o.'
        qwm_doc.CreatedBy = 'Automatically generated'
        qwm_doc.Comment = 'cubeNested'

    def set_Circuit_Parameters(self):
        #most parameters are defaults taken from qw_project
        super(cubeNested_Project, self).set_Circuit_Parameters()
        set_Circuit_Parameters(self.qwm_doc)

    def set_GeometryAndMedia(self):
        super(cubeNested_Project, self).set_GeometryAndMedia()
        set_GeometryAndMedia(self.qwm_doc)

    def set_Mesh(self):
        #most parameters are defaults taken from qw_project
        super(cubeNested_Project, self).set_Mesh()
        set_Mesh(self.qwm_doc)

    def set_Excitation(self):
        super(cubeNested_Project, self).set_Excitation()
        set_Excitation(self.qwm_doc)

    def set_Postprocessing(self):
        super(cubeNested_Project, self).set_Postprocessing()
        set_Postprocessing(self.qwm_doc)

    def set_Simulation(self):
        super(cubeNested_Project, self).set_Simulation()
        set_Simulation(self.qwm_doc)

    def run_Simulation(self):
        super(cubeNested_Project, self).run_Simulation()
        run_Simulation(self.qwm_doc)

        