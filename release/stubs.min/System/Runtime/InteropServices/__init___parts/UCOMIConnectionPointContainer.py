class UCOMIConnectionPointContainer:
 """ Use System.Runtime.InteropServices.ComTypes.IConnectionPointContainer instead. """
 def EnumConnectionPoints(self,ppEnum):
  """
  EnumConnectionPoints(self: UCOMIConnectionPointContainer) -> UCOMIEnumConnectionPoints

  

   Creates an enumerator of all the connection points supported in the connectable object,one 

    connection point per IID.
  """
  pass
 def FindConnectionPoint(self,riid,ppCP):
  """
  FindConnectionPoint(self: UCOMIConnectionPointContainer,riid: Guid) -> (Guid,UCOMIConnectionPoint)

  

   Asks the connectable object if it has a connection point for a particular IID,and if so,

    returns the IConnectionPoint interface pointer to that connection point.

  

  

   riid: A reference to the outgoing interface IID whose connection point is being requested.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
