
from qw_units import *
from qw_project import *

# S postprocessing set
def set_Postprocessing(qwm_doc):
    qwm_doc.QW_PostprocessingS.From = 15.0
    qwm_doc.QW_PostprocessingS.To = 25.0
    qwm_doc.QW_PostprocessingS.Step = 0.05
    qwm_doc.QW_PostprocessingS.ReciprocalNport = True
    qwm_doc.QW_PostprocessingS.ReciprocalLossless2port = False
    pass
