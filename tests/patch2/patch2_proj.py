
import QW_Modeller, FreeCADGui
from patch2_circuit import *
from patch2_geom_media import *
from patch2_mesh import *
from patch2_excit import *
from patch2_ppost import *
from patch2_setsimul import *
from patch2_runsimul import *

class patch2_Project(QW_Project): # test
    def __init__(self, qwm_doc):
        self.qwm_doc = qwm_doc
        qwm_doc.Company = 'QWED SP. z o.o.'
        qwm_doc.CreatedBy = 'Automatically generated'
        qwm_doc.Comment = 'patch2'

    def set_Circuit_Parameters(self):
        #most parameters are defaults taken from qw_project
        super(patch2_Project, self).set_Circuit_Parameters()
        set_Circuit_Parameters(self.qwm_doc)

    def set_GeometryAndMedia(self):
        super(patch2_Project, self).set_GeometryAndMedia()
        set_GeometryAndMedia(self.qwm_doc)

    def set_Mesh(self):
        #most parameters are defaults taken from qw_project
        super(patch2_Project, self).set_Mesh()
        set_Mesh(self.qwm_doc)

    def set_Excitation(self):
        super(patch2_Project, self).set_Excitation()
        set_Excitation(self.qwm_doc)

    def set_Postprocessing(self):
        super(patch2_Project, self).set_Postprocessing()
        set_Postprocessing(self.qwm_doc)

    def set_Simulation(self):
        super(patch2_Project, self).set_Simulation()
        set_Simulation(self.qwm_doc)

    def run_Simulation(self):
        super(patch2_Project, self).run_Simulation()
        run_Simulation(self.qwm_doc)

        