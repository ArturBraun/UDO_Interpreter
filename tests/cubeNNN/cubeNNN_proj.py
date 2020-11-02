
import QW_Modeller, FreeCADGui
from cubeNNN_circuit import *
from cubeNNN_geom_media import *
from cubeNNN_mesh import *
from cubeNNN_excit import *
from cubeNNN_ppost import *
from cubeNNN_setsimul import *
from cubeNNN_runsimul import *

class cubeNNN_Project(QW_Project): # test
    def __init__(self, qwm_doc):
        self.qwm_doc = qwm_doc
        qwm_doc.Company = 'QWED SP. z o.o.'
        qwm_doc.CreatedBy = 'Automatically generated'
        qwm_doc.Comment = 'cubeNNN'

    def set_Circuit_Parameters(self):
        #most parameters are defaults taken from qw_project
        super(cubeNNN_Project, self).set_Circuit_Parameters()
        set_Circuit_Parameters(self.qwm_doc)

    def set_GeometryAndMedia(self):
        super(cubeNNN_Project, self).set_GeometryAndMedia()
        set_GeometryAndMedia(self.qwm_doc)

    def set_Mesh(self):
        #most parameters are defaults taken from qw_project
        super(cubeNNN_Project, self).set_Mesh()
        set_Mesh(self.qwm_doc)

    def set_Excitation(self):
        super(cubeNNN_Project, self).set_Excitation()
        set_Excitation(self.qwm_doc)

    def set_Postprocessing(self):
        super(cubeNNN_Project, self).set_Postprocessing()
        set_Postprocessing(self.qwm_doc)

    def set_Simulation(self):
        super(cubeNNN_Project, self).set_Simulation()
        set_Simulation(self.qwm_doc)

    def run_Simulation(self):
        super(cubeNNN_Project, self).run_Simulation()
        run_Simulation(self.qwm_doc)

        