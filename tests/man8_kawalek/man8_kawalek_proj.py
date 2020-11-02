
import QW_Modeller, FreeCADGui
from man8_kawalek_circuit import *
from man8_kawalek_geom_media import *
from man8_kawalek_mesh import *
from man8_kawalek_excit import *
from man8_kawalek_ppost import *
from man8_kawalek_setsimul import *
from man8_kawalek_runsimul import *

class man8_kawalek_Project(QW_Project): # test
    def __init__(self, qwm_doc):
        self.qwm_doc = qwm_doc
        qwm_doc.Company = 'QWED SP. z o.o.'
        qwm_doc.CreatedBy = 'Automatically generated'
        qwm_doc.Comment = 'man8_kawalek'

    def set_Circuit_Parameters(self):
        #most parameters are defaults taken from qw_project
        super(man8_kawalek_Project, self).set_Circuit_Parameters()
        set_Circuit_Parameters(self.qwm_doc)

    def set_GeometryAndMedia(self):
        super(man8_kawalek_Project, self).set_GeometryAndMedia()
        set_GeometryAndMedia(self.qwm_doc)

    def set_Mesh(self):
        #most parameters are defaults taken from qw_project
        super(man8_kawalek_Project, self).set_Mesh()
        set_Mesh(self.qwm_doc)

    def set_Excitation(self):
        super(man8_kawalek_Project, self).set_Excitation()
        set_Excitation(self.qwm_doc)

    def set_Postprocessing(self):
        super(man8_kawalek_Project, self).set_Postprocessing()
        set_Postprocessing(self.qwm_doc)

    def set_Simulation(self):
        super(man8_kawalek_Project, self).set_Simulation()
        set_Simulation(self.qwm_doc)

    def run_Simulation(self):
        super(man8_kawalek_Project, self).run_Simulation()
        run_Simulation(self.qwm_doc)

        