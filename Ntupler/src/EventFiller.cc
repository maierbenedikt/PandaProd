#include "PandaProd/Ntupler/interface/EventFiller.h"
#include "PandaProd/Ntupler/interface/Ntupler.h"

using namespace panda;

EventFiller::EventFiller(TString n):
    BaseFiller()
{
  data = new PEvent();
  treename = n;
}

EventFiller::~EventFiller(){
  delete data;
}

void EventFiller::init(TTree *t) {
//  PEvent::Class()->IgnoreTObjectStreamer();
  t->Branch(treename.Data(),&data,99);
}

int EventFiller::analyze(const edm::Event& iEvent){
    if (skipEvent!=0 && *skipEvent) {
      return 0;
    }

    data->runNumber     = iEvent.id().run();
    data->lumiNumber    = iEvent.luminosityBlock();
    data->eventNumber   = iEvent.id().event();
    data->isData        = iEvent.isRealData();

    if (!(data->isData)) {
      iEvent.getByToken(gen_token,gen_handle); 
      data->mcWeight = gen_handle->weight();
    }

    iEvent.getByToken(vtx_token,vtx_handle);
    data->npv = vtx_handle->size();

    return 0;
}

