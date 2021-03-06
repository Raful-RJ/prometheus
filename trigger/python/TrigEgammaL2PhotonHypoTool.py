
__all__ = ['TrigEgammaL2PhotonHypoTool']


from Gaugi.messenger.macros import *
from Gaugi import Algorithm
from Gaugi import StatusCode
from Gaugi import GeV
from EventAtlas import Accept


#
# Hypo tool
#
class TrigEgammaL2PhotonHypoTool( Algorithm ):

  __property = [
                "EtCut",
                ]

  #
  # Constructor
  #
  def __init__(self, name, **kw):

    Algorithm.__init__(self, name)

    # Set all properties
    for key, value in kw.items():
      if key in self.__property:
        self.declareProperty( key, value )
      else:
        MSG_FATAL( self, "Property with name %s is not allow for %s object", key, self.__class__.__name__)


  #
  # Initialize method
  #
  def initialize(self):
    self.init_lock()
    return StatusCode.SUCCESS


  #
  # Finalize method
  #
  def finalize(self):
    self.fina_lock()
    return StatusCode.SUCCESS


  #
  # Accept method
  #
  def accept( self, context ):

    phCont = context.getHandler( "HLT__PhotonContainer" ) # beware, this should be review!
    current = phCont.getPos()

    bitAccept = [False for _ in range(phCont.size())]
    etThr =  self.getProperty('EtCut')
    for ph in phCont:
      # Retrieve all quantities
      # pTcalo      = ph.pt();
      bitAccept[ph.getPos()] = True
      MSG_DEBUG( self,  "Event accepted !" )

    phCont.setPos( current )
    passed = any( bitAccept )
    return Accept( self.name(), [("Pass", passed)] )

#
# Configure hypo tool from trigger name
#
def configure( trigger ):

  from TrigEgammaEmulationTool import TriggerInfo
  info = TriggerInfo( trigger )
  etthr = info.etthr()

  from Gaugi import ToolSvc
  emulator = ToolSvc.retrieve("Emulator")

  name = 'Hypo__L2Photon__' + info.signature()[0]+str(int(etthr)) + '_' + info.pidname()

  if not emulator.isValid(name):

    hypo = TrigEgammaL2PhotonHypoTool(name, EtCut = (etthr - 3)*GeV)
    emulator+=hypo

  return name
