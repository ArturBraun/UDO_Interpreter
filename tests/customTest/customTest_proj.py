
import QW_Modeller, FreeCADGui
from customTest_circuit import *
from customTest_geom_media import *
from customTest_mesh import *
from customTest_excit import *
from customTest_ppost import *
from customTest_setsimul import *
from customTest_runsimul import *

class customTest_Project(QW_Project): # test
    def __init__(self, qwm_doc):
        self.qwm_doc = qwm_doc
        qwm_doc.Company = 'QWED SP. z o.o.'
        qwm_doc.CreatedBy = 'Automatically generated'
        qwm_doc.Comment = 'customTest'

    def set_Circuit_Parameters(self):
        #most parameters are defaults taken from qw_project
        super(customTest_Project, self).set_Circuit_Parameters()
        set_Circuit_Parameters(self.qwm_doc)

    def set_GeometryAndMedia(self):
        super(customTest_Project, self).set_GeometryAndMedia()
        set_GeometryAndMedia(self.qwm_doc)

    def set_Mesh(self):
        #most parameters are defaults taken from qw_project
        super(customTest_Project, self).set_Mesh()
        set_Mesh(self.qwm_doc)

    def set_Excitation(self):
        super(customTest_Project, self).set_Excitation()
        set_Excitation(self.qwm_doc)

    def set_Postprocessing(self):
        super(customTest_Project, self).set_Postprocessing()
        set_Postprocessing(self.qwm_doc)

    def set_Simulation(self):
        super(customTest_Project, self).set_Simulation()
        set_Simulation(self.qwm_doc)

    def run_Simulation(self):
        super(customTest_Project, self).run_Simulation()
        run_Simulation(self.qwm_doc)

        