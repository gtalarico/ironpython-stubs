class ICustomAdapter:
 """ Provides a way for clients to access the actual object,rather than the adapter object handed out by a custom marshaler. """
 def GetUnderlyingObject(self):
  """
  GetUnderlyingObject(self: ICustomAdapter) -> object

  

   Provides access to the underlying object wrapped by a custom marshaler.

   Returns: The object contained by the adapter object.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
