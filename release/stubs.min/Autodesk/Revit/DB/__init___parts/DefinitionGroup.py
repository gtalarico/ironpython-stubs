class DefinitionGroup(APIObject,IDisposable):
 """ The DefinitionGroup is a container that is used to hold shared parameter definitions on disk. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Definitions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Definitions property returns an object that contains all the shared parameter
definitions within the group.

Get: Definitions(self: DefinitionGroup) -> Definitions

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the name of the parameter group.

Get: Name(self: DefinitionGroup) -> str

"""


