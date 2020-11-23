
from qw_units import *
# Circuit settings
def set_Circuit_Parameters(qwm_doc):
    qwm_doc.QW_Circuit.CircuitType = "3D"
    qwm_doc.QW_Circuit.MetalLossesBandwidth = "Decade"
    qwm_doc.QW_Circuit.SuppressLossesDielectric = False
    qwm_doc.QW_Circuit.SuppressLossesMetal = False
    qwm_doc.QW_Circuit.SuppressLossesMagnetic = False
    qwm_doc.QW_Circuit.SuppressSingularityCorrections = False
    qwm_doc.QW_Circuit.SuppressDensity_SAR = False
    qwm_doc.QW_BHM.AllowBHM = False
    qwm_doc.QW_Circuit.Units = "mm"
    qwm_doc.QW_Circuit.FrequencyUnits = "GHz"
