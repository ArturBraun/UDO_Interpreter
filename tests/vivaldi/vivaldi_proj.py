
import QW_Modeller, FreeCADGui
from vivaldi_circuit import *
from vivaldi_geom_media import *
from vivaldi_mesh import *
from vivaldi_excit import *
from vivaldi_ppost import *
from vivaldi_setsimul import *
from vivaldi_runsimul import *

class vivaldi_Project(QW_Project): # test
    def __init__(self, qwm_doc):
        self.qwm_doc = qwm_doc
        qwm_doc.Company = 'QWED SP. z o.o.'
        qwm_doc.CreatedBy = 'Automatically generated'
        qwm_doc.Comment = 'vivaldi'

    def set_Circuit_Parameters(self):
        #most parameters are defaults taken from qw_project
        super(vivaldi_Project, self).set_Circuit_Parameters()
        set_Circuit_Parameters(self.qwm_doc)

    def set_GeometryAndMedia(self):
        super(vivaldi_Project, self).set_GeometryAndMedia()
        set_GeometryAndMedia(self.qwm_doc)

    def set_Mesh(self):
        #most parameters are defaults taken from qw_project
        super(vivaldi_Project, self).set_Mesh()
        set_Mesh(self.qwm_doc)

    def set_Excitation(self):
        super(vivaldi_Project, self).set_Excitation()
        set_Excitation(self.qwm_doc)

    def set_Postprocessing(self):
        super(vivaldi_Project, self).set_Postprocessing()
        set_Postprocessing(self.qwm_doc)

    def set_Simulation(self):
        super(vivaldi_Project, self).set_Simulation()
        set_Simulation(self.qwm_doc)

    def run_Simulation(self):
        super(vivaldi_Project, self).run_Simulation()
        run_Simulation(self.qwm_doc)

        