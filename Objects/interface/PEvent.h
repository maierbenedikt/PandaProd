#ifndef PANDA_PEVENTINFO
#define PANDA_PEVENTINFO

#include <TObject.h>
#include <TClonesArray.h>


namespace panda
{
  class PEvent : public TObject
  {
    public:
      PEvent():
        runNumber(0),
        lumiNumber(0),
        eventNumber(0),
        isData(false),
        npv(0),
        mcWeight(-1),
        metFilters(0)
        {}
    ~PEvent(){}
    
    int runNumber, lumiNumber;
    ULong64_t eventNumber;
    bool isData;
    int npv;
    float mcWeight;
    int metFilters;
    ClassDef(PEvent,1)
  };
}
#endif
