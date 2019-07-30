class IWebRequestCreate:
 """ Provides the base interface for creating System.Net.WebRequest instances. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return IWebRequestCreate()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def Create(self,uri):
  """
  Create(self: IWebRequestCreate,uri: Uri) -> WebRequest
  
   Creates a System.Net.WebRequest instance.
  
   uri: The uniform resource identifier (URI) of the Web resource.
   Returns: A System.Net.WebRequest instance.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
