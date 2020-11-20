
from qw_units import *
from qw_project import *

# S postprocessing set
def set_Postprocessing(qwm_doc):
    qwm_doc.QW_PostprocessingS.From = 15.0
    qwm_doc.QW_PostprocessingS.To = 25.0
    qwm_doc.QW_PostprocessingS.Step = 0.01
    qwm_doc.QW_PostprocessingS.ReciprocalNport = True
    qwm_doc.QW_PostprocessingS.ReciprocalLossless2port = False
    qwm_doc.QW_PostprocessingNTF.Active = True
    qwm_doc.QW_PostprocessingNTF.Frequencies = [20.0]
    qwm_doc.QW_PostprocessingNTF.Eps = 1.0
    qwm_doc.QW_PostprocessingNTF.Mu = 1.0
    qwm_doc.QW_PostprocessingNTF.Sigma = 0.0
    qwm_doc.QW_PostprocessingNTF.SigmaM = 0.0
    pass
