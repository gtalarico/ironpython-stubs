class ICustomQueryInterface:
 """ Enables developers to provide a custom,managed implementation of the IUnknown::QueryInterface(REFIID riid,void **ppvObject) method. """
 def GetInterface(self,iid,ppv):
  """
  GetInterface(self: ICustomQueryInterface,iid: Guid) -> (CustomQueryInterfaceResult,Guid,IntPtr)

  

   Returns an interface according to a specified interface ID.

  

   iid: The GUID of the requested interface.

   Returns: One of the enumeration values that indicates whether a custom implementation of 

    IUnknown::QueryInterface was used.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
