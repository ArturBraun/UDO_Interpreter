
import QW_Modeller, FreeCADGui
from ant2R_circuit import *
from ant2R_geom_media import *
from ant2R_mesh import *
from ant2R_excit import *
from ant2R_ppost import *
from ant2R_setsimul import *
from ant2R_runsimul import *

class ant2R_Project(QW_Project): # test
    def __init__(self, qwm_doc):
        self.qwm_doc = qwm_doc
        qwm_doc.Company = 'QWED SP. z o.o.'
        qwm_doc.CreatedBy = 'Automatically generated'
        qwm_doc.Comment = 'ant2R'

    def set_Circuit_Parameters(self):
        #most parameters are defaults taken from qw_project
        super(ant2R_Project, self).set_Circuit_Parameters()
        set_Circuit_Parameters(self.qwm_doc)

    def set_GeometryAndMedia(self):
        super(ant2R_Project, self).set_GeometryAndMedia()
        set_GeometryAndMedia(self.qwm_doc)

    def set_Mesh(self):
        #most parameters are defaults taken from qw_project
        super(ant2R_Project, self).set_Mesh()
        set_Mesh(self.qwm_doc)

    def set_Excitation(self):
        super(ant2R_Project, self).set_Excitation()
        set_Excitation(self.qwm_doc)

    def set_Postprocessing(self):
        super(ant2R_Project, self).set_Postprocessing()
        set_Postprocessing(self.qwm_doc)

    def set_Simulation(self):
        super(ant2R_Project, self).set_Simulation()
        set_Simulation(self.qwm_doc)

    def run_Simulation(self):
        super(ant2R_Project, self).run_Simulation()
        run_Simulation(self.qwm_doc)

        