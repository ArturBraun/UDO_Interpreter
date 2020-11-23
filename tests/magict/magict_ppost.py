
from qw_units import *
from qw_project import *

# S postprocessing set
def set_Postprocessing(qwm_doc):
    qwm_doc.QW_PostprocessingS.From = 8.0
    qwm_doc.QW_PostprocessingS.To = 12.0
    qwm_doc.QW_PostprocessingS.Step = 0.01
    qwm_doc.QW_PostprocessingS.ReciprocalNport = True
    qwm_doc.QW_PostprocessingS.ReciprocalLossless2port = False
    qwm_doc.QW_PostprocessingS.SmnIterationsPerPort = 5000
    qwm_doc.QW_PostprocessingS.SmnType = "Multi simulator"
    pass
