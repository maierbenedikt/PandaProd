import FWCore.ParameterSet.Config as cms

from subprocess import check_output
import os


#------------------------------------------------------
PandaNtupler = cms.EDAnalyzer("Ntupler",

    info = cms.string("PandaNtupler"),
    cmssw = cms.string( os.environ['CMSSW_VERSION'] ) , # no need to ship it with the grid option

    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    muons = cms.InputTag("slimmedMuons"),
    electrons = cms.InputTag("slimmedElectrons"),
    taus = cms.InputTag("slimmedTaus"),
    photons = cms.InputTag("slimmedPhotons"),

    savePuppiCands = cms.bool(False),
    saveCHSCands = cms.bool(False), 
    doCHSAK4 = cms.bool(True),
    doPuppiAK4 = cms.bool(True),
    doPuppiCA15 = cms.bool(True),
    doCHSCA15 = cms.bool(False),
    doPuppiAK8 = cms.bool(False),
    doCHSAK8 = cms.bool(False),

    chsAK4 = cms.InputTag("slimmedJets"),
    puppiAK4 = cms.InputTag("patJetsPFAK4Puppi"),
    chsAK8 = cms.InputTag("packedPatJetsPFchsAK8"),
    puppiAK8 = cms.InputTag("packedPatJetsPFpuppiAK8"),
    chsCA15 = cms.InputTag("packedPatJetsPFchsCA15"),
    puppiCA15 = cms.InputTag("packedPatJetsPFpuppiCA15"),

    mets = cms.InputTag("slimmedMETs"),
    metsPuppi = cms.InputTag("type1PuppiMET"),
    metsPuppiUncorrected = cms.InputTag("pfMETPuppi"),

    puppiPFCands = cms.InputTag("puppi"),
    chsPFCands = cms.InputTag('packedPFCandidates'),
    #chsPFCands = cms.InputTag('pfCHS'),

    # gen
    generator = cms.InputTag("generator"),
    genjets = cms.InputTag("slimmedGenJets"),
    prunedgen = cms.InputTag("prunedGenParticles"),
    packedgen = cms.InputTag("packedGenParticles"),

    #ak4
    minAK4Pt  = cms.double (15.),
    maxAK4Eta = cms.double (4.7),

    #ak8
    minAK8Pt  = cms.double (180.),
    maxAK8Eta = cms.double (2.5),

    #ca15
    minCA15Pt  = cms.double (180.),
    maxCA15Eta = cms.double (2.5),

    #gen
    minGenParticlePt = cms.double(5.),
    minGenJetPt = cms.double(20.),
                      
)
#------------------------------------------------------


