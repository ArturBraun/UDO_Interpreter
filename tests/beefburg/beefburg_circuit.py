
from qw_units import *
# Circuit settings
def set_Circuit_Parameters(qwm_doc):
    qwm_doc.QW_Circuit.CircuitType = "3D"
    qwm_doc.QW_Circuit.MetalLossesBandwidth = "Decade"
    qwm_doc.QW_Circuit.SuppressLossesDielectric = False
    qwm_doc.QW_Circuit.SuppressLossesMetal = False
    qwm_doc.QW_Circuit.SuppressLossesMagnetic = False
    qwm_doc.QW_Circuit.Units = "mm"
    qwm_doc.QW_Circuit.FrequencyUnits = "GHz"
    qwm_doc.QW_Circuit.SuppressSingularityCorrections = False
    qwm_doc.QW_Circuit.SuppressDensity_SAR = False
    qwm_doc.QW_BHM.AllowBHM = False
    qwm_doc.QW_Circuit.UseEnergyLevel = False
    qwm_doc.QW_Circuit.EnergyLevelDescentDB = -40.0
    qwm_doc.QW_Circuit.EnergyLevelLogEveryDB = 10.0
    qwm_doc.QW_Circuit.EnergyProbingEvery = 1.0
    qwm_doc.QW_Circuit.SParametrsAccuracy = 0.005
    qwm_doc.QW_Circuit.PulsesNbLimit = 20
    qwm_doc.QW_Circuit.SaveSParametrsWhenFinished = True
    qwm_doc.QW_Circuit.FreezeWhenFinished = True
    qwm_doc.QW_Circuit.SuspendWhenFinished = True
    qwm_doc.QW_Circuit.ContinueAfterPulsesNbLimit = True
    qwm_doc.QW_BHM.AllowHFM = False
    qwm_doc.QW_BHM.AllowMovementAndRotation = False
    qwm_doc.QW_BHM.FirstEmSteadyState = 100
    qwm_doc.QW_BHM.NextEmSteadyState = 10
    qwm_doc.QW_BHM.HeatingPatternConstruction = 3
    qwm_doc.QW_BHM.TotalHeatingTime = 60.0
    qwm_doc.QW_BHM.HeatingTimeStep = 10.0
    qwm_doc.QW_BHM.SuspendAfterEach = False
    qwm_doc.QW_BHM.SuspendAfterStep = False
    qwm_doc.QW_BHM.SuspendStep = 1
    qwm_doc.QW_BHM.FreezeAfterEach = False
    qwm_doc.QW_BHM.FreezeAfterStep = False
    qwm_doc.QW_BHM.FreezeStep = 1
    qwm_doc.QW_BHM.SuspendAfterEach = False
    qwm_doc.QW_BHM.SuspendAfterStep = False
    qwm_doc.QW_BHM.SuspendStep = 1
    qwm_doc.QW_BHM.FreezeAfterEach = False
    qwm_doc.QW_BHM.FreezeAfterStep = False
    qwm_doc.QW_BHM.FreezeStep = 1
    qwm_doc.QW_BHM.ComponentsListFormat = 0
    qwm_doc.QW_BHM.IncludeShapeData = True
    qwm_doc.QW_BHM.IncludeFDTDMesh = False