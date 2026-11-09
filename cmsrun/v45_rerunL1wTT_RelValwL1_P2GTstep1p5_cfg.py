# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: l1nanoPhase2 -s L1TrackTrigger,L1,L1P2GT:step1p5_2026,NANO:@Phase2L1DPGwithGen --processName L1TReRun --conditions auto:phase2_realistic --geometry ExtendedRun4D121 --era Phase2C17I13M9 --eventcontent NANOAOD --datatier GEN-SIM-DIGI-RAW-MINIAOD --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring,L1Trigger/Configuration/customisePhase2TTOn110.customisePhase2TTOn110 --procModifiers nano_l1_hlt --filein /store/relval/CMSSW_20_0_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_150X_mcRun4_realistic_v1_STD_D121_RegeneratedGS_PU-v1/2590000/0033230b-a131-453a-95c0-fe14d5027d1f.root --fileout file:output_Phase2_L1T.root --python_filename v45_rerunL1wTT_RelValwL1_P2GTstep1p5_cfg.py --customise_commands 'process.finalGenParticles.src = '"'"'genParticles'"'"'\nprocess.genJetTable.src = '"'"'ak4GenJetsNoNu'"'"'\ndelattr(process.genParticleTable.externalVariables,'"'"'iso'"'"')\ndel process.genIso\ndel process.genJetFlavourTable\ndel process.patJetPartonsNano\nimport FWCore.ParameterSet.Config as cms; from PhysicsTools.NanoAOD.simpleSingletonCandidateFlatTableProducer_cfi import simpleSingletonCandidateFlatTableProducer; from PhysicsTools.NanoAOD.common_cff import PTVars; process.metMCTable = simpleSingletonCandidateFlatTableProducer.clone(src='"'"'genMetTrue'"'"', name='"'"'GenMET'"'"', doc='"'"'Gen MET'"'"', variables=cms.PSet(PTVars)); from PhysicsTools.NanoAOD.jetMC_cff import genJetAK8Table as _ak8; process.genJetAK8Table = _ak8.clone(src='"'"'ak8GenJetsNoNu'"'"', doc='"'"'AK8 gen jets (no nu)'"'"', cut='"'"'pt > 10'"'"'); process.genExtra_step = cms.Path(process.metMCTable + process.genJetAK8Table); process.schedule.append(process.genExtra_step); process.l1tSC8PFL1PuppiEmulator.doMass = cms.bool(True); process.l1tSC8PFL1PuppiCorrectedEmulator.doMass = cms.bool(True)' '--inputCommands=keep *, drop l1tPFJets_*_*_*, drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT' --mc -n 4 --nThreads 4
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Phase2C17I13M9_cff import Phase2C17I13M9
from Configuration.ProcessModifiers.nano_l1_hlt_cff import nano_l1_hlt

process = cms.Process('L1TReRun',Phase2C17I13M9,nano_l1_hlt)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtendedRun4D121Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.SimPhase2L1GlobalTriggerEmulator_cff')
process.load('L1Trigger.Configuration.Phase2GTMenus.SeedDefinitions.v0p0_2026.l1tGTMenu_lepSeeds_cff')
process.load('L1Trigger.Configuration.Phase2GTMenus.SeedDefinitions.v0p0_2026.l1tGTMenu_hadr_metSeeds_cff')
process.load('L1Trigger.Configuration.Phase2GTMenus.SeedDefinitions.v0p0_2026.l1tGTMenu_crossLepSeeds_cff')
process.load('L1Trigger.Configuration.Phase2GTMenus.SeedDefinitions.v0p0_2026.l1tGTMenu_hadr_crossLepSeeds_cff')
process.load('L1Trigger.Configuration.Phase2GTMenus.SeedDefinitions.v0p0_2026.l1tGTMenu_vbfSeeds_cff')
process.load('L1Trigger.Configuration.Phase2GTMenus.SeedDefinitions.v0p0_2026.l1tGTMenu_displacedSeeds_cff')
process.load('DPGAnalysis.Phase2L1TNanoAOD.l1tPh2Nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(4),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('/store/relval/CMSSW_20_0_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_150X_mcRun4_realistic_v1_STD_D121_RegeneratedGS_PU-v1/2590000/0033230b-a131-453a-95c0-fe14d5027d1f.root'),
    inputCommands = cms.untracked.vstring(
        'keep *',
        'drop l1tPFJets_*_*_*',
        'drop l1tTrackerMuons_l1tTkMuonsGmt*_*_HLT'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.obsolete.untracked.bool,
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('l1nanoPhase2 nevts:4'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-MINIAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:output_Phase2_L1T.root'),
    outputCommands = process.NANOAODEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

# Path and EndPath definitions
process.L1TrackTrigger_step = cms.Path(process.L1TrackTrigger)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.Phase2L1GTProducer = cms.Path(process.l1tGTProducerSequence)
process.Phase2L1GTAlgoBlockProducer = cms.Path(process.l1tGTAlgoBlockProducerSequence)
process.pDoubleEGEle = cms.Path(process.DoubleEGEle)
process.pDoubleIsoTau = cms.Path(process.DoubleIsoTau)
process.pDoubleTkEle = cms.Path(process.DoubleTkEle)
process.pDoubleTkEleIso_er1p5 = cms.Path(process.DoubleTkEleIsoer1p5)
process.pDoubleTkEle_er1p2_dR_Max0p6 = cms.Path(process.DoubleTkEleer1p2dRMax0p6)
process.pDoubleTkEle_er1p5_dEta_Max1p5 = cms.Path(process.DoubleTkEleer1p5dEtaMax1p5)
process.pDoubleTkMu = cms.Path(process.DoubleTkMu)
process.pDoubleTkMu0er1p4_SQ_OS_dR_Max1p4 = cms.Path(process.DoubleTkMu0er1p4SQOSdRMax1p4)
process.pDoubleTkMu4er2p0_SQ_OS_dR_Max1p6 = cms.Path(process.DoubleTkMu4er2p0SQOSdRMax1p6)
process.pDoubleTkPhoIso = cms.Path(process.DoubleTkPhoIso)
process.pDoubleTkPhoIso_er1p5 = cms.Path(process.DoubleTkPhoIsoer1p5)
process.pSingleEGEle = cms.Path(process.SingleEGEle)
process.pSingleTkEle = cms.Path(process.SingleTkEle)
process.pSingleTkEleIso = cms.Path(process.SingleTkEleIso)
process.pSingleTkIsoPhoton = cms.Path(process.SingleTkIsoPhoton)
process.pSingleTkMu = cms.Path(process.SingleTkMu)
process.pSingleTkMu_Barrel = cms.Path(process.SingleTkMuBarrel)
process.pTripleTkMu = cms.Path(process.TripleTkMu)
process.pTripleTkMu_4_2p5_0_OS12_Mass_Max12 = cms.Path(process.TripleTkMu42p50OS12MassMax12)
process.pTripleTkMu_4_2p5_0_OS13_Mass_Max12 = cms.Path(process.TripleTkMu42p50OS13MassMax12)
process.pTripleTkMu_4_2p5_0_OS23_Mass_Max12 = cms.Path(process.TripleTkMu42p50OS23MassMax12)
process.pDoubleJet = cms.Path(process.DoubleJet)
process.pDoubleJet_Mass_Min250_dEta_Max1p5 = cms.Path(process.DoubleJetMassMin250dEtaMax1p5)
process.pDoubleJet_dEta_Max1p6 = cms.Path(process.DoubleJetdEtaMax1p6)
process.pHTSum = cms.Path(process.HTSum)
process.pMETSum = cms.Path(process.METSum)
process.pSingleJet = cms.Path(process.SingleJet)
process.pDoubleTkMu_DoubleTkEle = cms.Path(process.DoubleTkMuDoubleTkEle)
process.pDoubleTkMu_TkEle = cms.Path(process.DoubleTkMuTkEle)
process.pTkMu20_TkEle10 = cms.Path(process.TkMu20TkEle10)
process.pTkMu7_TkEle20 = cms.Path(process.TkMu7TkEle20)
process.pTkMu_DoubleTkEle = cms.Path(process.TkMuDoubleTkEle)
process.pDoubleIsoTau_Jet = cms.Path(process.DoubleIsoTauJet)
process.pDoubleTkEle_HTSum = cms.Path(process.DoubleTkEleHTSum)
process.pDoubleTkMu_HTSum = cms.Path(process.DoubleTkMuHTSum)
process.pDoubleTkMu_Jet_Mu1 = cms.Path(process.DoubleTkMuJetMu1)
process.pDoubleTkMu_Jet_Mu2 = cms.Path(process.DoubleTkMuJetMu2)
process.pDoubleTkMu_METSum_HTSum = cms.Path(process.DoubleTkMuMETSumHTSum)
process.pTkEleIso_HTSum = cms.Path(process.TkEleIsoHTSum)
process.pTkEleIso_IsoTau = cms.Path(process.TkEleIsoIsoTau)
process.pTkMu12_HTSum150 = cms.Path(process.TkMu12HTSum150)
process.pTkMu6_HTSum240 = cms.Path(process.TkMu6HTSum240)
process.pTkMu_IsoTau = cms.Path(process.TkMuIsoTau)
process.pTkMu_Jet_METSum = cms.Path(process.TkMuJetMETSum)
process.pDoubleJet_IsoTau = cms.Path(process.DoubleJetIsoTau)
process.pDoubleJet_METSum = cms.Path(process.DoubleJetMETSum)
process.pDoubleJet_Mass_Min1000 = cms.Path(process.DoubleJetMassMin1000)
process.pDoubleJet_TkEleIso = cms.Path(process.DoubleJetTkEleIso)
process.pDoubleJet_TkMu = cms.Path(process.DoubleJetTkMu)
process.pDoubleDispMu = cms.Path(process.DoubleDispMu)
process.pSingleDispMu_BMTF = cms.Path(process.SingleDispMuBMTF)
process.nanoAOD_step = cms.Path(process.l1tPh2NanoSequence)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODoutput_step = cms.EndPath(process.NANOAODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.L1TrackTrigger_step,process.L1simulation_step,process.Phase2L1GTProducer,process.Phase2L1GTAlgoBlockProducer,process.pDoubleDispMu,process.pDoubleEGEle,process.pDoubleIsoTau,process.pDoubleIsoTau_Jet,process.pDoubleJet,process.pDoubleJet_IsoTau,process.pDoubleJet_METSum,process.pDoubleJet_Mass_Min1000,process.pDoubleJet_Mass_Min250_dEta_Max1p5,process.pDoubleJet_TkEleIso,process.pDoubleJet_TkMu,process.pDoubleJet_dEta_Max1p6,process.pDoubleTkEle,process.pDoubleTkEleIso_er1p5,process.pDoubleTkEle_HTSum,process.pDoubleTkEle_er1p2_dR_Max0p6,process.pDoubleTkEle_er1p5_dEta_Max1p5,process.pDoubleTkMu,process.pDoubleTkMu0er1p4_SQ_OS_dR_Max1p4,process.pDoubleTkMu4er2p0_SQ_OS_dR_Max1p6,process.pDoubleTkMu_DoubleTkEle,process.pDoubleTkMu_HTSum,process.pDoubleTkMu_Jet_Mu1,process.pDoubleTkMu_Jet_Mu2,process.pDoubleTkMu_METSum_HTSum,process.pDoubleTkMu_TkEle,process.pDoubleTkPhoIso,process.pDoubleTkPhoIso_er1p5,process.pHTSum,process.pMETSum,process.pSingleDispMu_BMTF,process.pSingleEGEle,process.pSingleJet,process.pSingleTkEle,process.pSingleTkEleIso,process.pSingleTkIsoPhoton,process.pSingleTkMu,process.pSingleTkMu_Barrel,process.pTkEleIso_HTSum,process.pTkEleIso_IsoTau,process.pTkMu12_HTSum150,process.pTkMu20_TkEle10,process.pTkMu6_HTSum240,process.pTkMu7_TkEle20,process.pTkMu_DoubleTkEle,process.pTkMu_IsoTau,process.pTkMu_Jet_METSum,process.pTripleTkMu,process.pTripleTkMu_4_2p5_0_OS12_Mass_Max12,process.pTripleTkMu_4_2p5_0_OS13_Mass_Max12,process.pTripleTkMu_4_2p5_0_OS23_Mass_Max12,process.nanoAOD_step,process.endjob_step,process.NANOAODoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 4
process.options.numberOfStreams = 0

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.aging
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000 

#call to customisation function customise_aging_1000 imported from SLHCUpgradeSimulations.Configuration.aging
process = customise_aging_1000(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customisePhase2TTOn110
from L1Trigger.Configuration.customisePhase2TTOn110 import customisePhase2TTOn110 

#call to customisation function customisePhase2TTOn110 imported from L1Trigger.Configuration.customisePhase2TTOn110
process = customisePhase2TTOn110(process)

# Automatic addition of the customisation function from DPGAnalysis.Phase2L1TNanoAOD.l1tPh2Nano_cff
from DPGAnalysis.Phase2L1TNanoAOD.l1tPh2Nano_cff import addPh2L1Objects,addPh2GTObjects,addGenObjects 

#call to customisation function addPh2L1Objects imported from DPGAnalysis.Phase2L1TNanoAOD.l1tPh2Nano_cff
process = addPh2L1Objects(process)

#call to customisation function addPh2GTObjects imported from DPGAnalysis.Phase2L1TNanoAOD.l1tPh2Nano_cff
process = addPh2GTObjects(process)

#call to customisation function addGenObjects imported from DPGAnalysis.Phase2L1TNanoAOD.l1tPh2Nano_cff
process = addGenObjects(process)

# End of customisation functions


# Customisation from command line

process.finalGenParticles.src = 'genParticles'
process.genJetTable.src = 'ak4GenJetsNoNu'
delattr(process.genParticleTable.externalVariables,'iso')
del process.genIso
del process.genJetFlavourTable
del process.patJetPartonsNano
import FWCore.ParameterSet.Config as cms; from PhysicsTools.NanoAOD.simpleSingletonCandidateFlatTableProducer_cfi import simpleSingletonCandidateFlatTableProducer; from PhysicsTools.NanoAOD.common_cff import PTVars; process.metMCTable = simpleSingletonCandidateFlatTableProducer.clone(src='genMetTrue', name='GenMET', doc='Gen MET', variables=cms.PSet(PTVars)); from PhysicsTools.NanoAOD.jetMC_cff import genJetAK8Table as _ak8; process.genJetAK8Table = _ak8.clone(src='ak8GenJetsNoNu', doc='AK8 gen jets (no nu)', cut='pt > 10'); process.genExtra_step = cms.Path(process.metMCTable + process.genJetAK8Table); process.schedule.append(process.genExtra_step); process.l1tSC8PFL1PuppiEmulator.doMass = cms.bool(True); process.l1tSC8PFL1PuppiCorrectedEmulator.doMass = cms.bool(True)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
