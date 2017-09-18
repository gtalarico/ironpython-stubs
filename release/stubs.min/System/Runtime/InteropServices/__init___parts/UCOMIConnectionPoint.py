class UCOMIConnectionPoint:
 """ Use System.Runtime.InteropServices.ComTypes.IConnectionPoint instead. """
 def Advise(self,pUnkSink,pdwCookie):
  """
  Advise(self: UCOMIConnectionPoint,pUnkSink: object) -> int

  

   Establishes an advisory connection between the connection point and the caller's sink object.

  

   pUnkSink: Reference to the sink to receive calls for the outgoing interface managed by this connection 

    point.
  """
  pass
 def EnumConnections(self,ppEnum):
  """
  EnumConnections(self: UCOMIConnectionPoint) -> UCOMIEnumConnections

  

   Creates an enumerator object for iteration through the connections that exist to this connection 

    point.
  """
  pass
 def GetConnectionInterface(self,pIID):
  """
  GetConnectionInterface(self: UCOMIConnectionPoint) -> Guid

  

   Returns the IID of the outgoing interface managed by this connection point.
  """
  pass
 def GetConnectionPointContainer(self,ppCPC):
  """
  GetConnectionPointContainer(self: UCOMIConnectionPoint) -> UCOMIConnectionPointContainer

  

   Retrieves the IConnectionPointContainer interface pointer to the connectable object that 

    conceptually owns this connection point.
  """
  pass
 def Unadvise(self,dwCookie):
  """
  Unadvise(self: UCOMIConnectionPoint,dwCookie: int)

   Terminates an advisory connection previously established through 

    System.Runtime.InteropServices.UCOMIConnectionPoint.Advise(System.Object,System.Int32@).

  

  

   dwCookie: The connection cookie previously returned from 

    System.Runtime.InteropServices.UCOMIConnectionPoint.Advise(System.Object,System.Int32@).
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
