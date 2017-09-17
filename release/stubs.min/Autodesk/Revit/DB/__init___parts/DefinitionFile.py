class DefinitionFile(APIObject,IDisposable):
 """ The DefinitionFile object represents a shared parameters file on disk. """
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
 Filename=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """This property returns the physical filename of the shared parameters file on disk.

Get: Filename(self: DefinitionFile) -> str

"""

 Groups=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Return a map of shared parameter definition groups contained within the file.

Get: Groups(self: DefinitionFile) -> DefinitionGroups

"""


