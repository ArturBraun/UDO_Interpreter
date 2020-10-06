
import QW_Modeller, FreeCADGui
from cylinder_circuit import *
from cylinder_geom_media import *
from cylinder_mesh import *
from cylinder_excit import *
from cylinder_ppost import *
from cylinder_setsimul import *
from cylinder_runsimul import *

class cylinder_Project(QW_Project): # test
    def __init__(self, qwm_doc):
        self.qwm_doc = qwm_doc
        qwm_doc.Company = 'QWED SP. z o.o.'
        qwm_doc.CreatedBy = 'Automatically generated'
        qwm_doc.Comment = 'cylinder'

    def set_Circuit_Parameters(self):
        #most parameters are defaults taken from qw_project
        super(cylinder_Project, self).set_Circuit_Parameters()
        set_Circuit_Parameters(self.qwm_doc)

    def set_GeometryAndMedia(self):
        super(cylinder_Project, self).set_GeometryAndMedia()
        set_GeometryAndMedia(self.qwm_doc)

    def set_Mesh(self):
        #most parameters are defaults taken from qw_project
        super(cylinder_Project, self).set_Mesh()
        set_Mesh(self.qwm_doc)

    def set_Excitation(self):
        super(cylinder_Project, self).set_Excitation()
        set_Excitation(self.qwm_doc)

    def set_Postprocessing(self):
        super(cylinder_Project, self).set_Postprocessing()
        set_Postprocessing(self.qwm_doc)

    def set_Simulation(self):
        super(cylinder_Project, self).set_Simulation()
        set_Simulation(self.qwm_doc)

    def run_Simulation(self):
        super(cylinder_Project, self).run_Simulation()
        run_Simulation(self.qwm_doc)

        